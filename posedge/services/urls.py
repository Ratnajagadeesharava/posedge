from django.urls import path
from .import views
urlpatterns = [
    path('',views.service,name="index"),
    path('vlsidesign',views.vlsidesign,name="vlsidesign"),
    path('socverfication',views.soc,name="soc"),
    path('physical-design',views.phy,name="phy"),
    path('fpgadesign',views.fgpa, name="fgpa"),
    path('embeddedsystem',views.esystem, name="esystem"),
    path('high-speed-circuit-design',views.hcircuit, name="hcircuit"),
    path('firmware-devlopment',views.firmware, name="firmware"),
    # path('fpgadesin',views.fgpa, name="fgpa"),
    path('bsp-driver-development',views.bsp,name="bsp"),
    path("product-testing",views.product,name="product"),
    path("cloud-application",views.cloud,name="cloud")
    
]