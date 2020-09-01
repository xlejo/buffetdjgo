from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from product.views import product_detail_view
from accounts.views import login_view, register_view, logout_view

urlpatterns = [
    path('', product_detail_view),
    path('login/', login_view),
    path('admin/', admin.site.urls),
    path('register/', register_view),
    path('logout/', logout_view)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)