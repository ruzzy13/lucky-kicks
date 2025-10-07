Zhafira Uzma || 2406495451 || PBP C  

link pws : https://zhafira-uzma41-luckykicks.pbp.cs.ui.ac.id/  

# **Tugas Individu 6**  

## **1. Apa perbedaan antara synchronous request dan asynchronous request?**  
### a. Synchronous Request  
Dalam synchronous request, ketika sebuah program mengirim permintaan (misalnya, mengambil data dari server), program tersebut akan berhenti dan menunggu hingga respons diterima sepenuhnya sebelum melanjutkan ke baris kode berikutnya. Cara kerja dari synchronous request adalah klien mengirim permintaan ke server. Lalu, klien berhenti dan menunggu respons. Seluruh antarmuka pengguna (UI) bisa menjadi tidak responsif atau "freeze". Kemudian, server memproses permintaan dan mengirimkan respons. Terakhir, klien menerima respons dan melanjutkan eksekusi kode selanjutnya.  
### b. Asynchronous Request  
Dalam asynchronous request, ketika program mengirim permintaan, ia tidak perlu menunggu respons. Program bisa langsung melanjutkan eksekusi baris kode berikutnya. Respons akan diproses nanti jika sudah tiba, biasanya menggunakan mekanisme seperti callback, Promise, atau async/await. Cara kerja dari asynchronous request adalah klien mengirim permintaan ke server. Lalu, klien tidak berhenti dan langsung melanjutkan eksekusi tugas lain. Ketika respons tiba, sebuah fungsi yang telah ditentukan (callback) akan dijalankan untuk memproses data dari respons tersebut.

## **2. Bagaimana AJAX bekerja di Django (alur request–response)?**  
=  AJAX pada Django memungkinkan platfoem web berkomunikasi dengan server Django tanpa perlu me-reload web. Berikut ini adalah jalan kerja AJAX pada Django:  
1. User memberikan aksi pada web yang memicu fungsi JavaScript,  
2. Program mengeksekusi JavaScript & membuat request HTTP dengan Fetch API.  
3. Program mengirimkan asynchronous request ke sever Django.
4. Program akan menunggu dan memproses request tersebut. Setelah mendapat respon, program akan memparsing data yang diterima dan menggunakan data tersebut untuk memanipulasi DOM.  
5. Server Django menerima request dari browser. Url sedolver Django akan mencocokan url dari request dengan yang ada pada file.  
6. Program mengeksekusi logika pada views.py.
7. Setelah mengeksekusi logika selesai, program menyiapkan dan mengirim response balik kepada user.  

## **3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?**  
= Terdapat beberapa keuntungan rendering dengan AJAX dibanding rendering biasa pada Django. Rendering menggunakan AJAX membuat interaksi user dengan platform lebih baik karena bekerja secara instan dan responsif. Ajax juga mengurangi jumlah data yang ditransfer antara user dan server secara signifikan.  Ajax juga membantu Django untuk mengurangi beban servernya dengan membuat Django tidak perlu me-render seluruh template untuk setiap interaksi. Terakhir, AJAX juga bisa menjaga state platform jika tidak di-reload. 

## **4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?**  
= Untuk memastikan keamanan saat menggunakan AJAX untuk fitur login dan register pada Django, kita perlu menggabungkan fitur keamanan bawaan dari Django dan keamanan dari client dan server. Caranya dengan menggunakan HTTPS sehingga semua data yang dikirim, termasuk data AJAX akan dienkripsi. Kita juga mengimplementasikan CSRF Protection untuk menghindari serangan siber. Server juga perlu melakukan validasi input dari user. Selain itu, perlu juga menggunakan hashing untuk password dan menerapkan rate limiting. 

## **5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?**  
= Sebelum menggunakan AJAX, proses rendering lebih lama karena program akan merender semua data yang membuat perforrma interaksi antara user dengan platform berkurang. Dengan menggunakan AJAX, performa interaksi dapat ditingkatkan karena hanya perlu mentransfer data kecil untuk dirender yang membuat waktu rendering lebih cepat. Hal ini membuat feedback yang lebih baik dan lebih terasa real-time. AJAX juga membuat user tidak perlu reload paltform web sehingga bisa mengurangi beban kognitif user. Oleh karena itu, AJAX sangat mempengaruhi user experience pada web.   