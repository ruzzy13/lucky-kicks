Zhafira Uzma || 2406495451 || PBP C

link pws : https://zhafira-uzma41-luckykicks.pbp.cs.ui.ac.id/

#**Tugas Individu 3** 

##**1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**  
###= data delivery sangat penting dalam pengimplementasian sebuah platform karena membantu sistem untuk berjalan dengan baik. Melalui alit=ran data yang cepat dan aman, platform mampu mendukung operasional inti. Data Delivery juga memastikan integrasi antarkomponen agar saling terhubung dan sinkron satu sama lain. Selain itu, data delivery juga menjaga reliabilitas dan skalabilitas sistem untuk menjaga performa platform ketika platform sedang digunakan dengan oleh banyak pengguna   

##**2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**  
###=Menurutku, JSON lebih baik dari XML karena JSON lebih mudah diurai daripada XML. JSON dapat diurai menjadi objek JavaScript yang siap pakai. JSON lebih populer dibandingkan XML  karena JSON lebih ringkas, cepat diproses, mudah dibaca, dan integrasi dengan JavaScript  

##**3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**  
###= Method is_valid() pada form Django berfungsi untuk memvalidasi data yang dikirim ke form. Hasil dari method is_valid() adalah nilai boolean yang bernilai True jika semua field valid dan bernilai False jika terdapat error ketika validasi field. Method is_valid() ini sangat penting untuk proyek yang dibuat oleh kita karena method tersebut mencegah data yang tidak valid masuk ke database, memastikan data aman sebelum dilanjutkan ke proses selanjutnya, dan apabila tidak ada validasi, platform dapat menerima input berbahaya yang menyebabkan error.

##**4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**  
###= csrf_token memiliki tujuan untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery). Dengan memiliki csrf_token, setiap request POST akan dicek apakah token valid dan akan diproses jika tokennya valid. Jika kita tidak menambahkan csrf_token pada form Django, maka form akan mudah terkena CSRF yang mengakibatkan server tidak dapat membedakan apakah request dikirm dari web resmi request yang dipalsukan oleh penyerang. Penyerang dapat memanfaatkan keadaan tersebut dengan membuat web palsu yang mengirim request POST ke aplikasi milik korban. Hal ini dapat menyebabkan hal serius seperti mengganti password korban atau memanipulasi data korban tanpa izin.

##**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**  
###= Pertama saya menambahkan 4 fungsi pada views.py untuk melihat objek yang sudah ditambahkan dalam format XML, XML by ID, JSON, dan Json by ID. Saya menambahkan atribut baru pada models.py yaitu id dengan UUID Field agar dapat digunakan pada fungsi pemabnggil by ID oleh XML atau JSON. Kemudian, saya melakukan routing URL untuk masing-masing fungsi sebelumnya.
Tampilan website saya tambahkan dengan button Add yang akan redirect ke halaman form, tampilan list objek yang telah ditambahkan dengan sedikit keterangan mengenai objek tersebut, dan button detail yang akan menampilkan halaman berisi detail objek. Halaman Form berisikan request penambahan objek yang meminta sesuai atribut yang ada pada models.py. Halaman detail akan menampilkan info sesuai atribut pada modela.py dari suatu objek. 

##**6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?**  
###= Tidak ada. Namun untuk modul tutorial, mungkin bisa diberikan foto tambahan sebagai acuan apakah hasil tampilan web yang telah dikerjakan sudah sesuai atau belum dengan yang diajarkan.   