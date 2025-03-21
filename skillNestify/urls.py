from django.contrib import admin
from django.urls import path, include, re_path
from debug_toolbar.toolbar import debug_toolbar_urls
from api.views import home
urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
] + debug_toolbar_urls()
