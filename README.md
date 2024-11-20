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

---

## Tugas 4 PBP 2024/2025
### Perbedaan `HttpResponseRedirect()` dan `redirect()`
- `HttpResponseRedirect()` memerlukan URL yang lengkap, sedangkan `redirect()` dapat menerima URL, nama view, nama objek, dan URL lengkap setelah itu di redirect kepada URL yang benar.
- `HttpResponseRedirect()` merupakan fungsi tingkat rendah, sedangkan `redirect()` merupakan fungsi tingkat tinggi, bahkan bisa memanggil `HttpResponseRedirect()`.
- `redirect()` cenderung lebih mudah digunakan.

### Cara Penghubungan model `Product` dengan `User`
Model `Product` atau `ItemEntry` dihubungkan ke model `User` dengan menggunakan ForeignKey sebagai berikut:
```python
from django.db import models
import uuid
from django.contrib.auth.models import User

class ItemEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```
Saat pengguna membuat entry baru, entry tersebut dikaitkan `user` dimana `user` tersebut dapat memiliki banyak entry, dan jika `user` tersebut dihapus, entry-entry -nya juga akan terhapus.

### Perbedaan authentication dan authorization, apa yang dilakukan saat login, dan bagaimana Django mengimplementasikan kedua konsep tersebut
- Authentication
  Merupakan konsep identifikasi dan verifikasi pengguna untuk menentukan siapa `user` yang sedang login.
  contoh: Saat ingin login ditanya username dan password
  implementasi dari Django adalah model `User` bawaan, view login, logout, password change, dan lain-lain.

- Authorization
  Merupakan konsep pemberian izin terhadap `user` untuk hak akses apa yang dimiliki, authorization dilakukan setelah authentication.
  contoh: Hak akses ke beberapa page yang dibatasi sesuai dengan siapa `user` yang login.
  implementasi dari Django adalah sistem permission dan login_required.

### Bagaimana Django Mengingat Pengguna, kegunaan cookies, dan keamanan cookies
Django membuat session di server yang mana session tersebut menyimpan informasi `User`, setelah itu membuat session ID yang unik untuk setiap sessions. Sessions ID yang telah dibuat oleh sessions, disimpan pada cookie. Setiap `User` membuat request, cookie akan dikirim ke server. Saat proses autentikasi, server menerima cookie session id dan mengambil data session dari server. Kegunaan dari cookies adalah untuk menyimpan pengaturan tampilan, menganalisis perilaku User, menyimpan token autentikasi, dan lain-lain. Tidak semua cookies aman digunakan, untuk membuat cookies lebih aman, Django menawarkan beberapa opsi seperti
`HttpOnly` yang mencegah cookie diakses melalui JavaScript dan `Secure` yang mengirim cookie hanya melalui HTTPS.

### Pengimplementasian Checklist secara Step-by-Step
a. Implementasi Fungsi Registrasi, Login, dan Logout
- Tambahkan fungsi `register` ke dalam `views.py` dalam `main` yang membuat form registrasi dan menghasilkan akun
  ```python
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
  ```
- Buat file `register.html` untuk menampilkan form registrasi
  ```html
    {% extends 'base.html' %}
    
    {% block meta %}
    <title>Register</title>
        {% endblock meta %}
        
    {% block content %}
    
    <div class="login">
      <h1>Register</h1>
    
      <form method="POST">
        {% csrf_token %}
        <table>
          {{ form.as_table }}
          <tr>
            <td></td>
            <td><input type="submit" name="submit" value="Daftar" /></td>
          </tr>
        </table>
      </form>
    
      {% if messages %}
      <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
      </ul>
      {% endif %}
    </div>
    
    {% endblock content %}
  ```
- Tambahkan URL di `urls.py` pada `main`
  ```python
     urlpatterns = [
     ...
     path('register/', register, name='register'),
     ]
  ```
- Tambahkan fungsi `login_user` pada `views.py` untuk autentifikasi pengguna saat login
  ```python
    def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
  ```
- Buat `login.html` untuk menampilkan tampilan form login
  ```html
    {% extends 'base.html' %}

    {% block meta %}
    <title>Login</title>
    {% endblock meta %}
    
    {% block content %}
    <div class="login">
      <h1>Login</h1>
    
      <form method="POST" action="">
        {% csrf_token %}
        <table>
          {{ form.as_table }}
          <tr>
            <td></td>
            <td><input class="btn login_btn" type="submit" value="Login" /></td>
          </tr>
        </table>
      </form>
    
      {% if messages %}
      <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
      </ul>
      {% endif %} Don't have an account yet?
      <a href="{% url 'main:register' %}">Register Now</a>
    </div>
    
    {% endblock content %}
  ```
- Tambahkan URL ke `urls.py` pada `main`
  ```python
    urlpatterns = [
   ...
   path('login/', login_user, name='login'),
    ]
  ```
- Buat Fungsi `logout_user` pada `views.py` untuk membuat mekanisme logout
  ```python
    def logout_user(request):
    logout(request)
    return redirect('main:login')
  ```
- Pada `main.html` buat tombol untuk implementasi fungsi logout tersebut ketika dipencet
  ```html
    <a href="{% url 'main:logout' %}">
  <button>Logout</button>
    </a>
  ```
- Tambahkan URL pada `urls.py` pada `main`
  ```python
    urlpatterns = [
   ...
   path('logout/', logout_user, name='logout'),
    ]
  ```
b. Membuat dua akun pengguna dengan masing-masing tiga dummy data untuk setiap akun lokal
- Jalankan proyek Django secara lokal pada `http://localhost:8000/`
- Registrasi dua akun berbeda
- Login pada masin-masing akun dan buat 3 dummy data per akun

c. Mengubungkan `Product` dengan `User`
- Tambahkan ForeignKey pada `ItemEntry` dalam `models.py`
  ```python
    from django.db import models
    import uuid
    from django.contrib.auth.models import User
    
    class ItemEntry(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
  ```
- Ubah `create_item_entry` pada `views.py`
  ```python
    def create_item_entry(request):
    form = ItemEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        ItemEntry = form.save(commit=False)
        ItemEntry.user = request.user
        ItemEntry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_item_entry.html", context)
  ```
- Membuat field baru pada `show_main` yaitu `user_name` sebagai penanda username yang masuk
- Lakukan migrasi untuk menerapkan perubahan
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```
- import os dan ganti variabel `DEBUG` pada `settings.py` pada direktori root
  ```python
    import os

    PRODUCTION = os.getenv("PRODUCTION", False)
    DEBUG = not PRODUCTION
  ```
d. Menampilkan detail informasi dan menerapkan cookies pada last login
- import datetime from django.http , import HttpResponseRedirect from django.urls , import reverse pada `views.py`
  ```python
    import datetime
    from django.http import HttpResponseRedirect
    from django.urls import reverse
  ```
- Pada fungsi `login_user`, tambahkan cookie bernama `last_login` untuk melihat kapan `User` terakhir login
  ```python
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
  ```
- Pada fungsi `show_main`, field `last_login` dalam variabel context
  ```python
    'last_login': request.COOKIES['last_login'],
  ```
- Ubah fungsi `logout_user`
  ```python
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
  ```
- Buka `main.html` dan tambahkan potongan kode berikut di setelah tombol logout untuk menampilkan data last login.
    ```html
        <h5>Sesi terakhir login: {{ last_login }}</h5>
    ```
---

## Tugas 5 PBP 2024/2025

### Urutan Prioritas CSS Selector 
Jika ada beberapa CSS selector yang diterapkan pada satu elemen HTML, prioritasnya ditentukan sebagai berikut:
1. inline styles memiliki prioritas tertinggi `(contoh: style="color: blue;")`.
2. ID selector (#id) memiliki prioritas lebih tinggi dibandingkan class selector atau tag selector.
3. Class selector, attribute selector, dan pseudo-class.
4. Tag selector (elemen) memiliki prioritas paling rendah.
Namun, penggunaan !important dapat mengabaikan urutan prioritas ini dan menjadikan style tersebut paling diutamakan.

### Mengapa responsive design penting dalam pengembangan aplikasi web?
Desain responsif memungkinkan halaman web menyesuaikan tampilannya dengan berbagai ukuran layar. Hal ini penting karena:
Peningkatan Pengguna Mobile, SEO (Search Engine Optimization) situs yang mobile-friendly mendapat peringkat lebih tinggi di mesin pencari, desain responsif meningkatkan kenyamanan pengguna, satu kode HTML dapat digunakan untuk semua perangkat, sehingga lebih efisien dalam pengembangan dan pemeliharaan.
Contoh aplikasi yang sudah responsif adalah Google yang sudah responsif di berbagai perangkat.

### Perbedaan Margin, Border, dan Padding 
Margin: Ruang di luar elemen yang memisahkannya dari elemen lain.
Border: Garis yang mengelilingi elemen, berada di antara padding dan margin.
Padding: Ruang di dalam elemen, antara konten dan border.

cara implementasi:
```css
div {
    margin: 20px; 
    border: 2px solid black;
    padding: 10px;
}
```

###  Konsep flex box dan grid layout beserta kegunaannya
- Flexbox adalah model layout satu dimensi yang memungkinkan penataan elemen secara fleksibel dalam baris atau kolom, ideal untuk layout yang responsif.
- Grid Layout adalah model layout dua dimensi yang memungkinkan penataan elemen dalam baris dan kolom, cocok untuk tata letak yang lebih kompleks.

### Implementasi Checklist Step-by-Step
- Fitur Edit dan Delete Produk
  Menambahkan tombol untuk mengedit dan menghapus produk, serta memanggil fungsi yang sesuai di backend.
  ```python
    def edit_item(request, id):
    item = ItemEntry.objects.get(pk = id)

    form = ItemEntryForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

    def delete_item(request, id):
        item = ItemEntry.objects.get(pk = id)
        item.delete()
        return HttpResponseRedirect(reverse('main:show_main'))
  ```   
  
- Kustomisasi Halaman Login, Register, dan Tambah Produk: Menggunakan Tailwind CSS untuk membuat tampilan yang clean dan modern.
- Kustomisasi Halaman Daftar Produk: Membuat layout card untuk setiap produk yang ditampilkan.
- Responsive Navbar: Mengimplementasikan navbar yang responsif dengan perubahan ke hamburger menu pada versi mobile.

### Hasil Implementasi
![image](https://github.com/user-attachments/assets/7d5d08b6-95be-4c3f-8d46-d3d05fab7231)
![image](https://github.com/user-attachments/assets/2e17b456-0668-42b5-ba39-bed90fc83cdd)
![image](https://github.com/user-attachments/assets/19754cf9-eb3d-4edc-b6b5-cd83d4a1b57d)
![image](https://github.com/user-attachments/assets/f24b1694-5c59-47e5-8311-7e87248fa255)
![image](https://github.com/user-attachments/assets/674093e1-2b72-484d-9c89-5eabe64b69fa)
![image](https://github.com/user-attachments/assets/76c8a039-c711-4630-8886-d4418ba80344)
---

## Tugas 6 PBP 2024/2025
### Manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web
Interaktivitas dinamis, dengan JavaScript, halaman web bisa menjadi lebih interaktif, memungkinkan animasi, tombol responsif, dan manipulasi elemen HTML tanpa perlu memuat ulang seluruh halaman. Selain itu, JavaScript kompatibel dengan berbagai platform, berjalan di semua browser modern, didukung oleh framework dan libray yang dapat mempermudah pengembangan aplikasi web yang lebih kompleks.

### Fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`, dan apa yang akan terjadi jika kita tidak menggunakan `await`
`await` digunakan dalam pemrograman asinkron untuk menunggu hasil dari promise yang dikembalikan oleh `fetch()`, sehingga memudahkan eksekusi kode menjadi lebih terstruktur dan mudah dipahami. Dengan `await`, eksekusi kode akan menunggu hingga promise selesai dan data tersedia sebelum melanjutkan. Tanpa `await`, `fetch()` hanya akan mengembalikan promise, dan kode akan tetap berjalan tanpa menunggu respons, yang dapat menyebabkan kesalahan ketika mencoba mengakses data yang belum diterima.

###  Fungsi decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX `POST`
`CSRF` (Cross-Site Request Forgery) adalah perlindungan di Django untuk memastikan permintaan `POST` berasal dari sumber yang sah. AJAX `POST` sering kali tidak membawa token `CSRF`, yang dapat menyebabkan kegagalan validasi. Decorator `@csrf_exempt` menonaktifkan pengecekan `CSRF` pada view tertentu, berguna dalam situasi seperti Permintaan dari sumber terpercaya, misalnya, AJAX request dari bagian aplikasi yang hanya bisa diakses oleh pengguna terverifikasi dan mencegah kegagalan permintaan, AJAX `POST` tanpa token `CSRF` akan ditolak tanpa decorator ini. Namun, penggunaannya harus hati-hati karena menonaktifkan mekanisme keamanan penting. Pastikan hanya permintaan yang aman yang diizinkan.

### Alasan mengapa membersihan data input pengguna dilakukan di belakang (backend) juga, dan mengapa hal tersebut tidak dilakukan di frontend saja
Pembersihan data di backend sangat penting untuk keamanan, konsistensi data, dan pengelolaan logika bisnis. Data dari frontend bisa dimanipulasi, jadi validasi di backend memastikan bahwa data yang diproses dan disimpan telah diverifikasi dan aman dari ancaman seperti injeksi SQL dan XSS. Selain itu, backend menjaga konsistensi data sesuai aturan bisnis dan dapat mengelola logika pembersihan yang lebih rumit. Ini memastikan pemisahan tanggung jawab antara frontend dan backend, membuat kode lebih terstruktur dan mudah dikelola.

### Implementasi checklist step-by-step
1. Mengubah kode cards data item agar dapat mendukung AJAX `GET`
   - Tambahkan view `add_item_entry_ajax` pada `views.py`
     ```python
         @csrf_exempt
        @require_POST
        def add_item_entry_ajax(request):
            name = strip_tags(request.POST.get("name"))
            price = strip_tags(request.POST.get("price"))
            description = strip_tags(request.POST.get("description"))
            quantity = strip_tags(request.POST.get("quantity"))
            image = strip_tags(request.POST.get("image"))
        
            user = request.user
        
            new_item = ItemEntry(
                name=name, price=price,
                description=description,
                quantity=quantity,
                image=image,
                user=user
            )
            new_item.save()
        
            return HttpResponse(b"CREATED", status=201)
     ```
   - Hubungkan routing URL pada `urls.py` dari view tadi
     ```python
        path('create-item-entry-ajax', add_item_entry_ajax, name='add_item_entry_ajax'),
     ```
   - Hapus bagian mapping item dengan fungsi asinkronus dalam script di dalam `main.html`
     ```javascript
         async function refreshItemEntries() {
            document.getElementById("item_entry_cards").innerHTML = "";
            document.getElementById("item_entry_cards").className = "";
            const itemEntries = await getItemEntries();
            let htmlString = "";
            let classNameString = "";

            if (itemEntries.length === 0) {
                classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
                htmlString = `
                <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                    <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                    <p class="text-center text-gray-600 mt-4">Belum ada data item pada Toko Touhou.</p>
                </div>
            `;
            }
            else {
                classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full"
                itemEntries.forEach((item) => {
                    const name = DOMPurify.sanitize(item.fields.name);
                    const price = DOMPurify.sanitize(item.fields.price);
                    const description = DOMPurify.sanitize(item.fields.description);
                    const quantity = DOMPurify.sanitize(item.fields.quantity);
                    const image = DOMPurify.sanitize(item.fields.image);
                    htmlString += `
                <div class="relative break-inside-avoid">
                    <div class="w-full max-w-sm bg-white border border-pink-700 rounded-lg shadow dark:bg-pink-700 dark:border-pink-700">
                        <a href="#">
                            <img class="p-8 rounded-t-lg w-full object-cover" src="${item.fields.image}" alt="item image" />
                        </a>
                        <div class="px-5 pb-5">
                            <a href="#">
                                <h5 class="text-3xl font-bold tracking-tight text-gray-900 dark:text-pink-300 text-start">${item.fields.name}</h5>
                                <h5 class="text-xl tracking-tight text-gray-900 dark:text-pink-300 text-start">${item.fields.description}</h5>
                            </a>
                            <h5 class="text-2xl font-bold text-gray-900 dark:text-pink-300 text-start">Rp.${item.fields.price}</h5>  
                            <h5 class="text-xl font-semibold tracking-tight text-gray-900 dark:text-pink-300 text-start">Stock: ${item.fields.quantity}</h5>
                            <div class="flex flex-col gap-2 mt-4">
                                <a href="/edit-item/${item.pk}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto" viewBox="0 0 20 20" fill="currentColor">
                                    <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                                    </svg>
                                </a>
                                <a href="/delete/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                                    </svg>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>`
                });
            }
            document.getElementById("item_entry_cards").className = classNameString;
            document.getElementById("item_entry_cards").innerHTML = htmlString;
        }
     ```
2. Lakukan pengambilan data mood menggunakan AJAX `GET`. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in.
   Untuk menjamin bahawa data yang dimasukkan oleh pengguna yang logged-in saya menerapkan kode tersebut pada view `add_item_entry_ajax`
   ```python
       user = request.user

        new_item = ItemEntry(
            name=name, price=price,
            description=description,
            quantity=quantity,
            image=image,
            user=user
        )
        new_item.save()
   ```
3.  Membuat sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item
   - Implementasikan modal dengan kode berikut di `main.html`
     ```css
         <div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
        <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
            <!-- Modal header -->
            <div class="flex items-center justify-between p-4 border-b rounded-t">
            <h3 class="text-xl font-semibold text-gray-900">
                Add New Item Entry
            </h3>
            <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
                <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                </svg>
                <span class="sr-only">Close modal</span>
            </button>
            </div>
            <!-- Modal body -->
            <div class="px-6 py-4 space-y-6 form-style">
            <form id="itemEntryForm">
                <div class="mb-4">
                <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
                <input type="text" id="name" name="name" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter your Item" required style="color: black;" >
                </div>
                <div class="mb-4">
                <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
                <input type="number" id="price" name="price" min="1" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="What's the price?" required style="color: black;">
                </div>
                <div class="mb-4">
                <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
                <textarea id="description" name="description" rows="3" class="mt-1 block w-full h-52 resize-none border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="What's the description?" required style="color: black;"></textarea>
                </div>
                <div class="mb-4">
                <label for="quantity" class="block text-sm font-medium text-gray-700">Quantity</label>
                <input type="number" id="quantity" name="quantity" min="1"
                
                class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="How much?" required style="color: black;">
                </div>
                <div class="mb-4">
                <label for="image" class="block text-sm font-medium text-gray-700">Image</label>
                <input id="image" name="image" min="1" max="10" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter the image" required style="color: black;">
                </div>
                
            </form>
            </div>
            <!-- Modal footer -->
            <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
            <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
            <button type="submit" id="submitItemEntry" form="itemEntryForm" class="bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
            </div>
        </div>
     ```
     - Tambahkan fungsi `showModal()` dan `hideModal()` supaya modal bisa berjalan
       ```javascript
            const modal = document.getElementById('crudModal');
            const modalContent = document.getElementById('crudModalContent');
    
            function showModal() {
                const modal = document.getElementById('crudModal');
                const modalContent = document.getElementById('crudModalContent');
    
                modal.classList.remove('hidden'); 
                setTimeout(() => {
                    modalContent.classList.remove('opacity-0', 'scale-95');
                    modalContent.classList.add('opacity-100', 'scale-100');
                }, 50); 
            }
    
            function hideModal() {
                const modal = document.getElementById('crudModal');
                const modalContent = document.getElementById('crudModalContent');
    
                modalContent.classList.remove('opacity-100', 'scale-100');
                modalContent.classList.add('opacity-0', 'scale-95');
    
                setTimeout(() => {
                    modal.classList.add('hidden');
                }, 150); 
            }
    
            document.getElementById("cancelButton").addEventListener("click", hideModal);
            document.getElementById("closeModalBtn").addEventListener("click", hideModal);
       ```
4. Membuat fungsi view baru untuk menambahkan item baru ke dalam basis data
   Poin ini sudah saya terapkan di poin-poin sebelumnya dengan membuat view `add_item_entry_ajax`
5. Membuat path `/create-ajax/` yang mengarah ke fungsi view yang baru kamu buat
   Poin ini sudah saya terapkan di poin-poin sebelumnya dengan routing URL tadi ke `urls.py`
6. Hubungkan form yang telah kamu buat di dalam modal kamu ke path `/create-ajax/`
   Saya menghubungkan URL tadi dengan form dengan membuat fungsi `addItem()` di script di dalam `main.html` dengan menggunakan `fetch()`
   ```javascript
        function addItemEntry() {
            fetch("{% url 'main:add_item_entry_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#itemEntryForm')),
            })
            .then(response => refreshItemEntries())

            document.getElementById("itemEntryForm").reset(); 
            document.querySelector("[data-modal-toggle='crudModal']").click();

            return false;
        }
   ```
7. Melakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar mood terbaru tanpa reload halaman utama secara keseluruhan
   Poin ini saya sudah terapkan pada poin-poin sebelumnya dengan membuat fungsi `refreshItemEntries()` di dalam script dalam `main.html`
---
