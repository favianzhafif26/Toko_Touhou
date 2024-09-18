---
# Toko Touhou ᗜˬᗜ
An E-Commerce Web for the Touhou Series fandom  

### This E-Commerce Web is made by:
Name: Favian Zhafif Rizqullah Permana  
Student ID: 2306274996  
Class: PBP-D  

# Live version here : [Toko Touhou ᗜˬᗜ](http://favian-zhafif-tokotouhou.pbp.cs.ui.ac.id/) 
---
## Tugas 2 PBP 2024/2025
## Cara Pengimplementasian Step-by-Step
1. Membuat Proyek Django Baru
Step pertama adalah membuat sebuah proyek baru Django dengan command `django-admin startproject Toko-Touhou`. Step ini dilakukan untuk direktori awal untuk proyek Django yang akan kita buat.

2. Membuat Aplikasi Main
Step kedua adalah membuat sebuah aplikasi bernama `main` dengan menggunakan command `python manage.py startapp main`. Aplikasi main berfungsi sebagai tempat logika dan fitur yang ada pada proyek.

3. Mengkonfigurasi Routing terhadap Aplikasi Main
Step Ketiga adalah konfigurasi routing supaya aplikasi `main` bisa disertakan. Dalam file `urls.py`, saya menambahkan kode agar URL dapat dikelola oleh aplikasi:
```python
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

4. Membuat Model "Product" pada `Main`
Step keempat adalah membuat sebuah model Product dalam file `models.py`. Atribut yang tercakup seperti `name`, `price`, `description`, dan `quantity` (punya saya). Step ini bertujuan untuk menyimpan data product.
```python
from django.db import models

class TokoEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
```

5. Membuat `View` pada `Main`
Step kelima adalah membuat sebuah `view` dalam file `views.py`. Step ini untuk rendering template dari file `main.html`.
```python
from django.shortcuts import render

def show_main(request):
    item_entries = ItemEntry.objects.all()
    context = {
        'identity':{
                'nama': 'Nama: Favian Zhafif Rizqullah Permana',
                'npm': 'NPM: 2306274996',
                'kelas': 'Kelas: PBP-D',
        },
        'products':     
                {
                'item_entries': item_entries
            }
    }

    return render(request, "main.html", context)
```

6. Menambahkan Routing di `urls.py` pada `Main`
Step keenam adalah menambahkan routing `urls.py` di aplikasi `main`. Step ini bertujuan untuk memastikan `view` dapat diakses di URL.
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

7. Mendeploy ke `Pacil Web Service (PWS)`
Step ketuju adalah mendeploy proyek tadi ke `PWS`. Step ini dilakukan supaya proyek tadi bisa diakses lewat internet

8. Membuat `README.md` di GitHub
Step kedelapan adalah membuat `README.md` yang berisi tugas-tugas dan link PWS dari proyek yang saya buat.

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

## Fungsi method `is_valid()` pada form Django        
Method `is_valid()` adalah sebuah method pada Django yang berfungsi sebagai validitator sebuah data sesuai dengan aturan yang berlaku pada form. Method ini juga memastikan bahwa data yang masuk aman dan layak untuk disimpan dan diproses.

## Fungsi `csrf_token` pada form Django
`csrf_token` adalah mekanisme untuk melindungi aplikasi web dari serangan CSRF (Cross-Site Request Forgery) yaitu serangan berupa permintaan berbahaya ke server dari pengguna valid. Oleh karena itu `csrf_token` dangat dibutuhkan untuk memastikan serangan CSRF ini tidak terjadi. Tanpa token ini, tentunya server tidak dapat memverifikasi apakah penggunanya valid atau tidak. Dampaknya, dapat terjadi pengubahan data atau permintaan yang tidak diinginkan.

## Cara Pengimplementasian Step-by-Step
### 1. Membuat form input untuk menambahkan objek model
a. Buat form baru `ItemEntryForm` di Django dengan menggunakan `ModelForm` di file `forms.py` dalam `main`
```python
from django.forms import ModelForm
from main.models import ItemEntry

class ItemEntryForm(ModelForm):
    class Meta:
        model = ItemEntry
        fields = ["name", "price", "description", "quantity", "image"]
```
b. Import `redirect` dan  `ItemEntryForm` buat fungsi `create_item_entry` di file `views.py` dalam `main` untuk menampilkan form secara automatis ketika data di submit
```python
from django.shortcuts import render, redirect
from main.forms import ItemEntryForm

def create_item_entry(request):
    form = ItemEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_item_entry.html", context)
```
c. Import `create_item_entry` dan tambahkan URL ke `urls.py` dalam `main` untuk mengakses fungsi tadi yang sudah dibuat
```python
from main.views import show_main, create_item_entry
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item-entry', create_item_entry, name='create_item_entry'),
]
```
d. Buat template HTML untuk menampilkan form `ItemEntryForm` tadi
```html
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Item Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Item Entry" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```
e. Buat tampilan di `main.html` dengan implementasi form yang tadi
```html
<body>
    {% extends 'base.html' %}
    {% block content %}
    <div class="header">
        <h1>Toko Touhou ᗜˬᗜ</h1>
        <h2>Toko ini dikembangkan oleh:</h2>
    </div>

    <div class="card">
        <h3>{{ identity.nama }}</h3>
        <h3>{{ identity.npm }}</h3>
        <h3>{{ identity.kelas }}</h3>
        <img src="https://i.imgur.com/j6W2Ko4.jpeg"> 
    </div>

    {% if not products.item_entries %}
    <p>Belum ada data item pada toko touhou.</p>
    {% else %}
    <table>
        <tr>
            <th>Item Name</th>
            <th>Price</th>
            <th>Desciption</th>
            <th>Item Quantity</th>
            <th>Item Image</th>
        </tr>

        {% comment %} Berikut cara memperlihatkan data toko di bawah baris ini 
        {% endcomment %} 
        {% for item_entry in products.item_entries %}
        <tr>    
            <td>{{ item_entry.name }}</td>
            <td>{{ item_entry.price }}</td>
            <td>{{ item_entry.description }}</td>
            <td>{{ item_entry.quantity }}</td>
            <td><img src="{{ item_entry.image }}" style="max-width: 200; max-height: 300px;"></td>
        </tr>
        {% endfor %}
    </table>
    {% endif %}

    <br />

    <a href="{% url 'main:create_item_entry' %}">
    <button>Add New item Entry</button>
    </a>
    {% endblock content %}
</body>
```
### 2. Tambahkan 4 Fungsi views baru untuk mengembalikan data dalam format XML, JSON, XML by ID, dan JSON by ID
a. Buat fungsi view untuk masing-masing format pada `views.py` dalam `main`
```python
from django.http import HttpResponse
from django.core import serializers

def show_xml(request):
    data = ItemEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ItemEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ItemEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ItemEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
b. Membuat routing URL ke `urls.py` dalam main untuk setiap fungsi view
```python
from django.urls import path
from main.views import show_main, create_item_entry, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item-entry', create_item_entry, name='create_item_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```

## Pengaksesan semua contoh formal URL di Postman
## XML
![XML](https://i.imgur.com/1ikdUZq.png)
## JSON
![JSON](https://i.imgur.com/xS3zc7s.png)
## XML by ID
![XML by ID](https://i.imgur.com/v7bnusw.png)
## JSON by ID
![JSON by ID](https://i.imgur.com/rgEkwah.png)
