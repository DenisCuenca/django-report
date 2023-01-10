
from django.contrib import admin
from django.urls import path

from mascota.views import Data, Reports

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Data),
    path('reports', Reports),
]
