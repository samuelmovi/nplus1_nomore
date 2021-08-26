from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('views_templates/', views.views_templates, name='views-templates'),
    path('rest/', views.rest, name='rest'),
    path('graphql/', views.graphql, name='graphql'),
    path('profiling/', views.profiling, name='profiling'),
    path('', views.main, name='main')
]
