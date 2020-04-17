from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name="home"),
    path('careers/',views.careers, name="careers"),
    path('aboutus/',views.about,name="aboutus"),
    path('service/',views.service,name="services")
]