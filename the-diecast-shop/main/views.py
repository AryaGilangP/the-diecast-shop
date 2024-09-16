from django.shortcuts import render

def show_main(request):
    context = {
        'app': 'The Diecast Store',
        'name': 'Arya Gilang Prasetya',
        'class': 'PBP F',
        'price': '50.000',
        'description':'model ini memiliki warna hitam pekat, dengan detail berupa lampu depan dan belakang.\n'
                        'model ini juga memiliki fitur untuk membuka dan menutup pintu samping dan kap mesinnya.',
        'model_number':'12345',
        'user_reviews':'produk mobil diecast ini sangat bagus dan memiliki detail yang menarik. barang ori dan berkualitas bintang lima.'
        
    }

    return render(request, "main.html", context)