# from django.conf.urls import patterns, include, url
#
# from django.contrib import admin
# admin.autodiscover()
#
# urlpatterns = patterns(
#     #'',
#     url(r'^$', 'ronweb.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#
#     url(r'^admin/', include(admin.site.urls)),
# )

from django.conf.urls import url
from views import home


urlpatterns = [
    url(r'^$', home, name='home'),
]
