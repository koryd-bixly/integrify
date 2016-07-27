from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles import views as static_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'integrity.views.home', name='home'),
    url(r'^get-hash/$', 'integrity.views.get_hash', name='get_hash'),
]
# if settings.DEBUG:
#     urlpatterns += [
#         url(r'^static/(?P<path>.*)$', static_views.serve),
#     ]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)