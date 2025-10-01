Zhafira Uzma || 2406495451 || PBP C  

link pws : https://zhafira-uzma41-luckykicks.pbp.cs.ui.ac.id/  

# **Tugas Individu 5**  

## **1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**  
= Urutan prioritas pengambilan CSS selector ditentukan oleh 3 faktor utama, diurutkan dari yang paling penting yaitu importance, specificity, dan source order.  
- Importance atau disebutjuga sebagai "aturan". Jika !important ditambahkan ke sebuah properti css aturan tersebut akan mengalahkan semua aturan lainnya  
- Specificity : Jika tidak ada !important, browser akan menghitung specificity score untuk setiap selector. Selector dengan skor tertinggi akan menang. Hierarki specificity dari yang tertinggi adalah inline styles, id selectors, Class, Attribute, dan Pseudo-class Selectors, dan Element dan Pseudo-element Selectors.  
- Source Order : Jika dua selector memiliki skor kekhususan yang sama persis, maka aturan yang didefinisikan paling akhir di dalam file CSS (atau yang diimpor terakhir) yang akan diterapkan.  

## **2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!**  
=   Responsive design merupakan konsep yang sangat penting dalam pengembangan aplikasi web karena dapat mengingkatkan kepuasan pengguna dan memudahkan pengembangan aplikasi karena lebih efisien dalam pengembangannya (tidak perlu membuat dua aplikasi berbeda untuk tipe perangkat yang berbeda). Contoh aplikasi web yang sudah menerapkan responsive design adalah e-commerce seperti Tokopedia dan Shopee. Ketika membuka aplikasi tersebut pada web komputer, tampilan grid product lebih banyak dari yang ditampilkan pada handphone. Ada pula web yang beum menerapkan responsive design yaitu website arsip ppdb karena ketika website dibuka pada laptop, tampilannya cukup rapih. Berbeda ketika dibuka melalui handphone, banyak elemen yang berantakan dan ukuran sudah ditentukan sehingga ukuran web tidak sesuai dengan ukuran layar handphone.  

## **3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**  
= - Margin :  ruang transparan di bagian luar elemen, setelah border. Fungsinya adalah untuk menciptakan jarak atau spasi antara elemen tersebut dengan elemen lain di sekitarnya.  
- Border : garis yang berada di antara padding dan margin. Border dapat diatur ketebalan, gaya, dan warna.  
- Padding : ruang transparan di bagian dalam elemen yang memisahkan konten (teks dan gambar) dari border. Menambah padding akan membuat ukuran elemen terlihat lebih besar karena ruang di dalamnya bertambah.   
cara mengimplementasikan ketiga hal tersebut adalah dengan membuat class selector. Lalu, didalamnya baru menambahkan ketiga elemen tersebut seperti margin: 30px; border: 5px blue; dan padding: 20px;. Jangan lupa untuk menutup class selector tersebut.

## **4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!**  
= Konsep flex box adalah model layout yang memungkinkan item di dalam sebuah kontainer diatur secara fleksibel di sepanjang satu sumbu, baik secara horizontal maupun vertikal. Kegunaan dari konsep flex box ini adalah membuat navigation bar, centering, card component, dan distribusi ruang. Konsep grid layout adalah  sistem layout berbasis grid dua dimensi yang memungkinkan Anda mengatur konten dalam baris dan kolom secara bersamaan. Ini memberikan kontrol yang jauh lebih besar untuk tata letak halaman web secara keseluruhan. kegunaan dari konsep grid layout adalah membuat layout Home Page, galeri gambar, Dashboard, dan layout asimetris

## **5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**  
=  Pertama-tama, saya menambahkan tailwind pada base.html untuk styling pada website. Kemudian, saya menambahkan function edit product dan delete product user ingin mengubah detail dari suatu produk atau menghapus produk tersebut di file views.py dan membuat path baru di urls.py. Kemudiam saya menambahkan fitur navigation bar untuk tampilan pada main page. Selanjutnya saya melakukan konfigurasi static files dengan meengubah list middleware dan penambahan conditional debug setelah variabel static_url. Terakhir saya melakukan styling pada semua file template sehingga tampilannya menarik. tampilan yang saya bedakan dari tutorial adalah tampilan produk pada main page dan tampilan produk pada detail produk page. 