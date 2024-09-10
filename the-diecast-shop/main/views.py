def show_main(request):
    context = {
        'app': 'The Diecast Store',
        'name': 'Arya Gilang Prasetya',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)