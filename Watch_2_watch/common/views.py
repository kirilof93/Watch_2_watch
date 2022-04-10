from django.shortcuts import render


def landing_page(request):
    return render(request, 'landing_page.html')


def about_us_page(request):
    return render(request, 'about_us_page.html')
