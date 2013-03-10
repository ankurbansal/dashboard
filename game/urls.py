from django.conf.urls import patterns, include, url
from bridge import gamescript


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Dashboard1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^uploadData/',gamescript.fetchGameInfoAndPersist)
)
