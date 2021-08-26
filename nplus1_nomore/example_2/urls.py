from django.urls import path

from . import views

app_name = 'example_2'

urlpatterns = [
    path('book_list_bad/', views.BookListBadView.as_view(), name='books-bad'),
    path('book_list_good/', views.BookListGoodView.as_view(), name='books-good'),

]
