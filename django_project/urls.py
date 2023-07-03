from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path,include

from pages.views import error404


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")), 
    path("accounts/", include("accounts.urls")), 
    path("", include("pages.urls")),
    path("books/", include("books.urls")),
]+ static( #para pillow
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

handler404 =error404.as_view()
