from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
                  path('', include('Watch_2_watch.common.urls')),
                  path('watches/', include('Watch_2_watch.watches.urls')),
                  path('admin/', admin.site.urls),
                  path('accounts/', include('Watch_2_watch.accounts.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
