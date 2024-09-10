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