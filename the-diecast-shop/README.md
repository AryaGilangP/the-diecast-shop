Nama : Arya Gilang P

NPM : 2306221970

Kelas : PBP F

link : https://arya-gilang-thediecastshop.pbp.cs.ui.ac.id/

## README UNTUK TUGAS 2

<details>
  <summary></summary>

## Proses Pembuatan Projek Django

**Membuat project django baru**
1. membuat repository Github baru bernama 'the-diecast-shop'
2. clone repository kosong ke komputer lokal dengan perintah **git clone https://github.com/AryaGilangP/the-diecast-shop**
3. menghubungkan penyimpanan lokal dengan Github **git remote add origin https://github.com/AryaGilangP/the-diecast-shop**
4. membuat virtual enviroment dan mengaktifkannya
5. membuat file bernama `requirements.txt` lalu menginstall dependensi yang ada di file tersebut
6. buat project django baru 
7. menjalankan server dengan mengubah isi dari allowed hosts, lalu memeriksanya di **http://localhost:8000**

**Membuat aplikasi dengan nama `main` pada project tersebut
lalu mendaftarkannya ke dalam `INSTALLED_APPS`**

**Melakukan routing pada 'main' agar dapat menjalankan aplikasi**
hal ini dilakukan agar web yang kita buat dapat diakses melalui web

**Membuat model pada `models.py` dengan nama produk dan atribut atribut tertentu** 
didalam 'models.py' aku menambahkan beberapa atribut seperti, `name` ,`price` , `description` , `models` , `customer_review`
 
**Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat**
NOTE : disini saya melakukan deployment saat PWS masih sedang error dan itu sudah H-1 deadline jadi sampai sekarang sebenarnya juga masih failed sih

## Request Client ke Web Aplikasi Berbasis Django

![Flow Diagram](diagram/diagram.jpg)
https://www.canva.com/design/DAGQaVKWqVw/UOididZ0zkWlrKeqb3VXSQ/edit?utm_content=DAGQaVKWqVw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Fungsi Git pada Pengembangan Perangkat Lunak

Git adalah sistem kontrol versi terdistribusi yang berfungsi untuk melacak perubahan dalam kode sumber selama pengembangan perangkat lunak. Dalam pengembangan perangkat lunak, Git memiliki beberapa fungsi penting, antara lain:

Pelacakan Perubahan (Version Control) Kolaborasi Tim Pengembangan Paralel (Branching) Audit dan Pemantauan Manajemen Repositori Terdistribusi

Alasan Framework Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak Struktur yang Jelas dan Terorganisir: Django adalah framework yang memiliki struktur proyek yang sangat jelas dan terorganisir, sehingga memudahkan pemula untuk memahami bagaimana aplikasi web diorganisir. Django menggunakan pola arsitektur Model-View-Template (MVT) yang serupa dengan pola Model-View-Controller (MVC) yang umum digunakan di banyak framework.

Username: arya.gilang
Password: 1JGdfEwT7KUiGHaJOvMWtGj0IrsEYnSA

</details>

## README UNTUK TUGAS 3

<details>
  <summary></summary>

**Membuat input form untuk menambahkan objek model pada app sebelumnya.**  

dimulai dengan membuat `forms.py` pada untuk membuat forms yang bisa menerima data baru. Form menggunakan model `CarItems` yang mencakup field yang relevan. Setelah itu kita perbarui kode `views.py` dengan menambahkan fungsi `create_car_items`yang dapat menerima data, memvalidasi input, serta menyimpan data tersebut. Lalu ketika berhasil aka aka di redirect ke halaman utama, dan `views.py` dan `main.html` dimodifikasi untuk menampilkan semua item mobil yang sudah dibuat.

**Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.**

1. Format XML
menambahkan fungsi `show_xml` yang mengambil seluruh data dari entry `CarItems` menggunakan `CarItems.objects.all()` yang akan return hasil dengan type XML.

        ```
        def show_xml(request):
            data = CarItems.objects.all()
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
            ```

2.  Format JSON
     `show_json` serupa dengan `show_xml`, yang akan mengembalikan hasil dengan tipe JSON.  
         
       ```
       def show_json(request):
            data = CarItems.objects.all()
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
       ```
       
3. XML by ID dan JSON by ID
    `show_xml_by_id` dan `show_json_by_id` digunakan untuk mengambil data `CarItems` menggunakan ID. Query dilakukan menggunakan `data = MoodEntry.objects.filter(pk=id)` untuk mengambil data sesuai ID, lalu diubah menjadi format XML atau JSON sesuai yang dipanggil. Untuk memanggilnya kita bisa menambahkan ID di belakang URL.  
        
      ```
      def show_xml_by_id(request, id):
            data = CarItems.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
      ```  
  
      ```
      def show_json_by_id(request, id):
            data = CarItems.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
      ``` 

**Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.**  

URL ditambahkan pada file `urls.py` spaya fungsi pada `views.py` bisa diakses.

```
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-car-item', create_car_item, name='create_car_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```

## Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Karena menghubungkan pengguna dengan server untuk memberikan informasi, layanan, dan konten secara efisien. Tanpa data delivery, pengguna tidak bisa mendapatkan akses real-time terhadap data yang dibutuhkan seperti konten dinamis, transaksi, atau interaksi antar pengguna.

## Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON dianggap lebih populer karena sintaks simpel dan ringan karena menggunakan struktur key-value yang lebih ringkas dibandingkan dengan tag yang lebih berat di XML. Struktur data yang alami, sehingga JSON sangat cocok untuk merepresentasikan objek data dalam bahasa pemrograman, seperti array dan objek. JSON menjadi lebih populer karena kesederhanaannya, kinerjanya yang efisien, dan dukungan luas di lingkungan pemrograman modern seperti JavaScript, Python, dan lainnya. JSON juga lebih mudah dipahami oleh manusia dan mesin dibandingkan dengan XML.

## Fungsi dari Method `is_valid()` pada Form Django dan Mengapa Kita Membutuhkannya?
Memeriksa validitas data yang diinput ke dalam form, apakah sesuai dengan aturan yang ditetapkan (misalnya, panjang teks, format email, atau tipe data).
Mengidentifikasi error dalam input form, jika ada kesalahan, method ini memungkinkan kita untuk mendapatkan informasi tentang kesalahan tersebut melalui atribut `form.errors`.

## Mengapa Kita Membutuhkan `csrf_token` saat Membuat Form di Django? Apa yang Dapat Terjadi Jika Kita Tidak Menambahkannya? Bagaimana Hal Tersebut Dapat Dimanfaatkan oleh Penyerang?
`csrf_token` memastikan bahwa setiap permintaan POST yang dilakukan melalui form di Django benar-benar berasal dari sumber yang sah (yaitu pengguna yang sebenarnya), bukan dari situs eksternal yang berbahaya.
Tanpa `csrf_token`, form menjadi rentan terhadap serangan CSRF, di mana penyerang bisa mengarahkan pengguna ke sebuah halaman web atau email berbahaya yang mengirimkan permintaan tak sah atas nama pengguna tersebut, seperti transfer dana, pengubahan pengaturan akun, atau tindakan lainnya. Penyerang dapat membuat pengguna yang sudah login ke aplikasi melakukan aksi yang tidak disengaja, seperti mengirim data ke server tanpa sepengetahuan pengguna.

## POSTMAN
**XML**
![XML](postman/PostmanXML.jpg)

**JSON**
![JSON](postman/PostmanJSON.jpg)

**XML by ID**
![XML by ID](postman/PostmanXMLbyID.jpg)

**JSON by ID**
![JSON by ID](postman/PostmanJSONbyID.jpg)

</details>