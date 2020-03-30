from django.conf import settings
from django.conf.urls import include, url

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtailcore_urls
from wagtail.documents import urls as wagtaildocs_urls


urlpatterns = [
    url(r"^admin/", include(wagtailadmin_urls)),
    url(r"^documents/", include(wagtaildocs_urls)),
    url(r"", include(wagtailcore_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
