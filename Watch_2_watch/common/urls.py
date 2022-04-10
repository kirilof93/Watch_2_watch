from django.urls import path
from Watch_2_watch.common.views import landing_page, about_us_page

urlpatterns = [
    path('', landing_page, name='index'),
    path('about/', about_us_page, name='about'),
]
