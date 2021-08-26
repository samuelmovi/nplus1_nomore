"""nplus1_nomore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

import debug_toolbar
from graphene_django.views import GraphQLView

from core.views import main, views_templates, render, graphql, profiling
from rest.routers import router
from graph.views import CustomGraphQLView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('example_0/', include('example_0.urls')),
    path('example_1/', include('example_1.urls')),
    path('example_2/', include('example_2.urls')),
    path('example_3/', include('example_3.urls')),
    path('autopre/', include('autopre.urls')),
    path("rest/api/", include(router.urls)),
    # path('graphql_bad/', GraphQLView.as_view(graphiql=True)),
    path('graphql_endpoint/', CustomGraphQLView.as_view(graphiql=True)),
    path('', include('core.urls')),
]

if settings.SILK == True:
    urlpatterns = [path('silk/', include('silk.urls', namespace='silk'))] + urlpatterns
elif settings.HEALTH == True:
    urlpatterns = [path('health/', include('health_check.urls'))] + urlpatterns
elif settings.DEBUG_TOOLBAR == True:
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
elif settings.PG_METRICS == True:
    urlpatterns = [path('admin/postgres-metrics/', include('postgres_metrics.urls'))] + urlpatterns

