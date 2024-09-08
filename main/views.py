from django.shortcuts import render
from django.templatetags.static import static

def show_main(request):
    context = {
        'nama' : 'Fumo Cirno V1.5 Touhou Project Plushie + Bonus Pin - Down Payment',
        'deskripsi': '''BARANG PRE ORDER

    Fumo Cirno V1.5 dengan bonus pin fumonya
    
    Tutup PO 02 Oktober 2024
    
    Release date : April 2025, kemungkinan sampai sini sekitar Mei - Juni 2025
    
    Per fumo maksimal pemesanan 3 slot. (sisa 2 slot)
    
    Note,
    
    Untuk pembayaran via DP, silahkan pilih varian Down Payment. Setelah itu akan dikirim barang dummy berupa invoice atau yang lainnya. Jika barang sudah sampai di Indonesia akan dikontak melalui nomor HP yang digunakan ketika pre order dan melakukan pelunasan dengan membeli produk ini lagi dengan varian Pelunasan.''',
        'harga': '500000',
        'image': static('gambar_untuk_tugas2_pbp.jpg'),
    }

    return render(request, "main.html", context)