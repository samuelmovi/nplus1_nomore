from django.urls import path

from . import views

app_name = 'autopre'

urlpatterns = [
    path('', views.BookListBadView.as_view(), name='books-bad-auto'),
]
