from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import requests
import json

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)
    

    context = {
        'npm': '2406495451',
        'name': request.user.username,
        'class': 'PBP C',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html",context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product 
    }

    return render(request, "show_product.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [{
            'id': str(products.id),
            'title': products.name,
            'content': products.description,
            'category': products.category,
            'thumbnail': products.thumbnail,
            'views': products.views,
            'price': products.price,
            'stock': products.stock,
            'is_featured': products.is_featured,
            'user_id': products.user_id,
    }
            for products in product_list
              ]
    return JsonResponse(data, safe=False)



def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)
   
def show_json_by_id(request, product_id):
   try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'title': product.name,
            'content': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'views': product.views,
            'price': product.price,
            'stock': product.stock,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
   except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    
    messages.success(request, "You have been successfully logged out.") 
    
    response = redirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_ajax(request):
    
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    stock = request.POST.get("stock")
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'
    user = request.user

    new_product = Product(
        name=name,
        price=price,
        stock=stock,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def delete_product_ajax(request, id):
    if request.method == 'DELETE':
        try:
            product = Product.objects.get(pk=id)
            if product.user == request.user:
                product.delete()
                return JsonResponse({"status": "success", "message": "Product deleted successfully"}, status=200)
            else:
                return JsonResponse({"status": "error", "message": "You are not authorized to delete this product."}, status=403)
        except Product.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Product not found."}, status=404)
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=400)

def get_product_json(request, id):
    product = get_object_or_404(Product, pk=id)
    data = {
        "name": product.name,
        "price": product.price,
        "stock": product.stock,
        "description": product.description,
        "category": product.category,
        "thumbnail": product.thumbnail,
        "is_featured": product.is_featured,
    }
    return JsonResponse(data)

@csrf_exempt
def edit_product_ajax(request, id):
    if request.method == 'POST':
        try:
            product = get_object_or_404(Product, pk=id)
            name = request.POST.get("name")
            price_str = request.POST.get("price")
            stock_str = request.POST.get("stock")
            description = request.POST.get("description")
            category = request.POST.get("category")
            thumbnail = request.POST.get("thumbnail")
            is_featured = request.POST.get("is_featured") == 'on'
            if not price_str or not price_str.isdigit():
                return JsonResponse({"status": "error", "message": "Price must be a valid number."}, status=400)
            
            if not stock_str or not stock_str.isdigit():
                return JsonResponse({"status": "error", "message": "Stock must be a valid number."}, status=400)
            
            product.name = name
            product.price = int(price_str)
            product.stock = int(stock_str)
            product.description = description
            product.category = category
            product.thumbnail = thumbnail
            product.is_featured = is_featured
            
            product.save()
            
            return JsonResponse({"status": "success", "message": "Product updated successfully!"}, status=200)

        except Product.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Product not found."}, status=404)
        
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"An unexpected error occurred: {str(e)}"}, status=500)
    
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=400)

def register_ajax(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            redirect_url = reverse('main:login')
            return JsonResponse({
                'status': 'success', 
                'message': 'Your account has been successfully created! redirecting...',
                'redirect_url': redirect_url
            })
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def login_ajax(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                redirect_url = reverse('main:show_main') 
                return JsonResponse({
                    'status': 'success', 
                    'message': 'Login successful ! redirecting...',
                    'redirect_url': redirect_url
                })
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        # Ambil data dari JSON, sesuaikan dengan yang dikirim Flutter
        title = strip_tags(data.get("title", ""))
        content = strip_tags(data.get("content", ""))
        category = data.get("category", "apparel") # Default jika kosong
        thumbnail = data.get("thumbnail", "")
        is_featured = data.get("is_featured", False)
        user = request.user
        
        # Ambil 'price' dan 'stock', konversi dari string ke integer
        try:
            price = int(data.get("price", 0))
            stock = int(data.get("stock", 0))
        except (ValueError, TypeError):
            # Tangani jika data yang dikirim bukan angka
            return JsonResponse({"status": "error", "message": "Price and Stock must be valid numbers."}, status=400)
        
        # Periksa nilai non-negatif
        if price <= 0 or stock < 0:
            return JsonResponse({"status": "error", "message": "Price must be greater than zero and Stock cannot be negative."}, status=400)

        # Buat objek Product baru
        new_product = Product(
            title=title,
            price=price,       # <-- Field baru
            stock=stock,       # <-- Field baru
            content=content,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            user=user
            # Tambahkan field lain jika ada (misal: views=0)
        )
        new_product.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=401)