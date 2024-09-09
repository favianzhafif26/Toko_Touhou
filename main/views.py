from django.shortcuts import render

def show_main(request):
    context = {
        'products': [
            {
                'nama': 'Fumo Cirno Touhou Project Plushie',
                'harga': 'Harga: Rp500.000',
                'deskripsi': 'wleowleo',
                'image': 'https://imgur.com/7QgART5.jpeg',
                'stok': 'Stok: 3'
            },
            {
                'nama': 'Fumo Reimu Hakurei Touhou Project Plushie',
                'harga': 'Harga: Rp500.000',
                'deskripsi': 'wleowleo',
                'image': 'https://imgur.com/T08ac3K.jpeg',
                'stok': 'Stok: 3'
            },
            {
                'nama': 'Fumo Koishi Komeji Touhou Project Plushie',
                'harga': 'Harga: Rp500.000',
                'deskripsi': 'wleowleo',
                'image': 'https://i.imgur.com/eNe8RTJ.jpeg',
                'stok': 'Stok: 3'
            },
            {
                'nama': 'Fumo Marisa Kirisame Touhou Project Plushie',
                'harga': 'Harga: Rp500.000',
                'deskripsi': 'wleowleo',
                'image': 'https://imgur.com/5Mg568I.jpeg',
                'stok': 'Stok: 3'
            },
            {
                'nama': 'Fumo Youmu Konpaku Touhou Project Plushie',
                'harga': 'Harga: Rp500.000',
                'deskripsi': 'wleowleo',
                'image': 'https://imgur.com/5MeXVZm.jpeg',
                'stok': 'Stok: 3'
            },
            {
                'nama': 'Fumo Tenshi Hinanawi Touhou Project Plushie',
                'harga': 'Harga: Rp500.000',
                'deskripsi': 'wleowleo',
                'image': 'https://imgur.com/akw6Amw.jpeg',
                'stok': 'Stok: 3'
            }
        ]
    }

    return render(request, "main.html", context)