from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from movies import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/', app_views.sample_view),
    path('api/', include('movies.api.urls')),
    path('v1/', include('movies.api.v1.urls'))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
