
from django.contrib import admin
from django.urls import path
from .views import home, biz_xaqimizda, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
    path("about/", biz_xaqimizda),
    path("contact/", contact),
]
