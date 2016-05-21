from django.conf.urls import url, patterns

from qa.views import test, error


urlpatterns = patterns('qa.views',
    url(r'^$', test, name='home'),
    url(r'^login/.*$', test, name='login'),
    url(r'^signup/.*$', test, name='signup'),
    url(r'^ask/.*$', test, name='ask'),
    url(r'^popular/.*$', test, name='popular'),
    url(r'^new/.*$', test, name='new'),
    url(r'^question/(?P<pk>\d+)/$', test, name='question-by-id'),
)