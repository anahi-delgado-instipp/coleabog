from django.shortcuts import render

# Create your views here.
def pagina_informatica(request):
    return render(request, 'informativa/pagina_informatica.html')

def start_page(request):
    return render(request, 'informativa/starter_page.html')
