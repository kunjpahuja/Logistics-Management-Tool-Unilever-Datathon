from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views


app_name = 'warehouse'

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # path('', views.testPage),
    path('', views.emptyDash),
    path('update_budget/', views.update_budget),
    path('upload/', views.wareUpload),
    path('operations/', views.fullTable),
    path('operations/ru', views.ruTable),
    path('operations/ua', views.uaTable),
    # path('show_tests/', views.update_budgetDB),
]
