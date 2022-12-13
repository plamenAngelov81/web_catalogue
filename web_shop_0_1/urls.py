from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_shop_0_1.user_profile.urls')),
    path('', include('web_shop_0_1.projects.urls')),
    path('', include('web_shop_0_1.company_info.urls')),
    path('', include('web_shop_0_1.products.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
