from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406495451',
        'name': 'Zhafira Uzma',
        'class': 'PBP C',
        'nama_aplikasi' : "lucky_kicks"
    }

    return render(request, "main.html", context)
