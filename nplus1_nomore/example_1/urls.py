from django.urls import path

from . import views

app_name = 'example_1'

urlpatterns = [
    path('report_list_bad/', views.ReportsListBadView.as_view(), name='reports-bad'),
    path('report_list_good/', views.ReportsListGoodView.as_view(), name='reports-good'),
    path('report_list_best/', views.ReportsListBestView.as_view(), name='reports-best'),
]
