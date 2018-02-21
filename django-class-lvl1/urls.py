from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    # '',
    # Examples:
    # url(r'^$', 'tt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^polls/', include('polls.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        # "",
        url(r"^__debug__/", include(debug_toolbar.urls)),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
