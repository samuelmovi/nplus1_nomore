from django.urls import path

from . import views

app_name = 'example_0'

urlpatterns = [
    path('people_list_bad/', views.PersonListBadView.as_view(), name='people-bad'),
    path('people_list_good/', views.PersonListGoodView.as_view(), name='people-good'),
]
