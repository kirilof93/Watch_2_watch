from django.urls import path

from Watch_2_watch.watches.views import list_watches, watch_details, delete_watch, comment_watch, create_watch, edit_watch

urlpatterns = [
    path('watches/', list_watches, name='list watches'),
    path('create/', create_watch, name='create watch'),
    path('details/<int:pk>/', watch_details, name='watch details'),
    path('edit/<int:pk>/', edit_watch, name='edit watch'),
    path('delete/<int:pk>/', delete_watch, name='delete watch'),
    path('comment/<int:pk>/', comment_watch, name='comment watch'),
]