---
# Toko Touhou ᗜˬᗜ
An E-Commerce Web for the Touhou Series fandom  

### This E-Commerce Web is made by  
- Favian Zhafif Rizqullah Permana  
- 2306274996  
- PBP-D  

# Live version here : [Toko Touhou ᗜˬᗜ](http://favian-zhafif-tokotouhou.pbp.cs.ui.ac.id/) 
---
## Tugas 2 PBP 2024/2025
### Cara Pengimplementasian Step-by-Step
1. Membuat Proyek Django Baru
Step pertama adalah membuat sebuah proyek baru Django dengan command `django-admin startproject Toko-Touhou`. Step ini dilakukan untuk direktori awal untuk proyek Django yang akan kita buat.

2. Membuat Aplikasi Main
Step kedua adalah membuat sebuah aplikasi bernama `main` dengan menggunakan command `python manage.py startapp main`. Aplikasi main berfungsi sebagai tempat logika dan fitur yang ada pada proyek.

3. Mengkonfigurasi Routing terhadap Aplikasi Main
Step Ketiga adalah konfigurasi routing supaya aplikasi main bisa disertakan. Dalam file urls.py, saya menambahkan kode agar URL dapat dikelola oleh aplikasi:
```python
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

4. Membuat Model "Product" pada Main
Step keempat adalah membuat sebuah model Product dalam file models.py. Atribut yang tercakup seperti name, price, description, dan quantity (punya saya). Step ini bertujuan untuk menyimpan data product.
```python
from django.db import models

class TokoEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
```

5. Membuat View pada Main
Step kelima adalah membuat sebuah view dalam file views.py. Step ini untuk rendering template dari file main.html.
```python
from django.shortcuts import render

def show_main(request):
    context = {
        'products': [
            {
                'nama': 'Fumo Cirno Touhou Plushie',
                'harga': 'Harga: Rp500.000',
                'deskripsi': 'Dijual plushie Fumo Cirno dari series Touhou dengan harga terjangkau (size: 23x14cm)',
                'image': 'https://imgur.com/NmB6s4k.jpeg',
                'stok': 'Stok: 3'
            },
            {
                'nama': 'Fumo Reimu Hakurei Touhou Plushie',
                'harga': 'Harga: Rp500.000',
                'deskripsi': 'Dijual plushie Fumo Reimu Hakurei dari series Touhou dengan harga terjangkau (size: 23x14cm)',
                'image': 'https://imgur.com/T08ac3K.jpeg',
                'stok': 'Stok: 3'
            },
            {
                'nama': 'Fumo Koishi Komeji Touhou Plushie',
                'harga': 'Harga: Rp500.000',
                'deskripsi': 'Dijual plushie Fumo Koishi Komeji dari series Touhou dengan harga terjangkau (size: 23x14cm)',
                'image': 'https://i.imgur.com/eNe8RTJ.jpeg',
                'stok': 'Stok: 3'
            },
            {
                'nama': 'Fumo Marisa Kirisame Touhou Plushie',
                'harga': 'Harga: Rp500.000',
                'deskripsi': 'Dijual plushie Fumo Marisa Kirisame dari series Touhou dengan harga terjangkau (size: 23x14cm)',
                'image': 'https://imgur.com/5Mg568I.jpeg',
                'stok': 'Stok: 3'
            },
            {
                'nama': 'Fumo Youmu Konpaku Touhou Plushie',
                'harga': 'Harga: Rp500.000',
                'deskripsi': 'Dijual plushie Fumo Youmu Konpaku dari series Touhou dengan harga terjangkau (size: 23x14cm)',
                'image': 'https://imgur.com/5MeXVZm.jpeg',
                'stok': 'Stok: 3'
            },
            {
                'nama': 'Fumo Tenshi Hinanawi Touhou Plushie',
                'harga': 'Harga: Rp500.000',
                'deskripsi': 'Dijual plushie Fumo Tenshi Hananawi dari series Touhou dengan harga terjangkau (size: 23x14cm)',
                'image': 'https://imgur.com/akw6Amw.jpeg',
                'stok': 'Stok: 3'
            },
            {
                'nama': 'Fumo Flandre Scarlet Touhou Plushie',
                'harga': 'Harga: Rp500.000',
                'deskripsi': 'Dijual plushie Fumo Flandre Scarlet dari series Touhou dengan harga terjangkau (size: 23x14cm)',
                'image': 'https://imgur.com/k9roVO7.jpeg',
                'stok': 'Stok: 3'
            },
            {
                'nama': 'Fumo Yuuka Kazami Touhou Plushie',
                'harga': 'Harga: Rp500.000',
                'deskripsi': 'Dijual plushie Yuuka Kazami dari series Touhou dengan harga terjangkau (size: 23x14cm)',
                'image': 'https://imgur.com/osr3NDB.jpeg',
                'stok': 'Stok: 3'
            },
            {
                'nama': 'Fumo Patchouli Knowledge Touhou Plushie',
                'harga': 'Harga: Rp500.000',
                'deskripsi': 'Dijual plushie Fumo Patchouli Knowledge dari series Touhou dengan harga terjangkau (size: 23x14cm)',
                'image': 'https://imgur.com/T3H3Kah.jpeg',
                'stok': 'Stok: 3'
            },
            {
                'nama': 'Fumo Reisen Udongein Touhou Plushie',
                'harga': 'Harga: Rp500.000',
                'deskripsi': 'Dijual plushie Fumo Reisen Udongein dari series Touhou dengan harga terjangkau (size: 23x14cm)',
                'image': 'https://imgur.com/hE4c2aK.jpeg',
                'stok': 'Stok: 3'
            }
        ]
    }

    return render(request, "main.html", context)
```

6. Menambahkan Routing di urls.py pada Main
Step keenam adalah menambahkan routing urls.py di aplikasi main. Step ini bertujuan untuk memastikan view dapat diakses di URL.
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

7. Mendeploy ke Pacil Web Service (PWS)
Step ketuju adalah mendeploy proyek tadi ke PWS. Step ini dilakukan supaya proyek tadi bisa diakses lewat internet

8. Membuat README.md di GitHub
Step kedelapan adalah membuat README.md yang berisi tugas-tugas dan link PWS dari proyek yang saya buat.

## Bagan Alur Django
```
Django Side                                                                                        Client Side
                                                                      URL <--(Send HTTP Request)-- Client
                                                                       |                             |
                                                    (Directing to Preferred route and view)          |
                                                                       |                             |
Database --(Query /Alter Database) -> Models <--(Read/Write Data)--> Views ---------------------------
                                                                       |
                                                      (Return HTML Template of the View)
                                                                       |
                                                                     Templates

```

## Fungsi Git dalam Pengembangan Perangkat Lunak
Git berfungsi sebagai Version Control System yang memungkinkan pengembang perangkat lunak untuk melacak setiap perubahan kode. Tim pengembang dapat bekerja secara kolaboratif pada proyek yang sama, mengelola branch yang berbeda untuk fitur baru, memperbaiki bug, dan merge dengan aman. Git juga memungkinkan rollback ke versi sebelumnya jika terjadi kesalahan, sehingga meminimalisir risiko dalam pengembangan perangkat lunak. Dengan kata lain, Git membantu menjaga integritas kode dan memastikan tim dapat bekerja secara efisien dalam proyek yang kompleks.

## Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django menyediakan struktur yang jelas dan mengikuti prinsip "konvensi di atas konfigurasi", yang membantu pemula memahami arsitektur aplikasi web. Django juga memiliki dokumentasi yang sangat baik dan komunitas yang besar, sehingga memudahkan pemula untuk menemukan bantuan dan solusi. Django juga dilengkapi dengan banyak fitur bawaan seperti autentikasi pengguna, panel admin, dan ORM, yang mempercepat pengembangan aplikasi tanpa harus membangun fitur-fitur dasar dari nol. Django juga secara default mengikuti praktik keamanan yang baik, mengurangi risiko kerentanan yang umum dalam pengembangan aplikasi web.

## Mengapa model pada Django disebut sebagai ORM?
Model dalam Django disebut sebagai ORM (Object-Relational Mapping) karena Django menggunakan pendekatan ORM untuk memetakan objek Python ke tabel-tabel dalam database relasional. Dengan ORM, kode Python dapat digunakan untuk berinteraksi dengan database tanpa menulis SQL secara langsung. ORM memudahkan operasi database seperti penyimpanan, pengambilan, pembaruan, dan penghapusan data melalui objek Python, sehingga meningkatkan produktivitas dan meminimalkan kemungkinan kesalahan.

---

## Tugas 3 PBP 2024/2025

## Kenapa kita memerlukan data delivery untuk platform
Data delivery adalah proses server menyampaikan data kepada client. Data delivery ini tentu sangat penting, karena dengan data delivery, kita dapat mengirimkan data secara langsung sesuai dengan keinginan client. Data delivery juga membuat proses pengiriman data kepada client jauh lebih cepat dan efisien yang pasti akan berpengaruh dengan kenikmatan pengalaman client.

## Lebih baik menggunakan JSON atau XML? Mengapa JSON lebih populer dipakai dibandingkan dengan XML
- JSON menghasilkan file yang lebih kecil dari XML karena tidak diperlukannya tag pernutup.
- JSON mempunyai sintaks yang biasanya lebih mudah untuk dibaca pengguna dan mesin.
- JSON terintegrasi dengan JavaScript, oleh karena itu JSON lebih mudah untuk diimplementasikan saat pembuatan web.

## Fungsi method '''is_valid()''' pada form Django  

---
