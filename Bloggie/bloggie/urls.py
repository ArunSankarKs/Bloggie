

#This is your root URL PAGE

from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from bloggie import settings
from web.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path("web/", include('web.urls')),
    path('', home, name='home'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
