from django.conf.urls import url, patterns

from qa.views import test, error


#urlpatterns = patterns('qa.views',
urlpatterns = [
    url(r'^$', test, name='qa-home'),
    url(r'^login/.*$', test, name='qa-login'),
    url(r'^signup/.*$', test, name='qa-signup'),
    url(r'^ask/.*$', test, name='qa-ask'),
    url(r'^popular/.*$', test, name='qa-popular'),
    url(r'^new/.*$', test, name='qa-new'),
    url(r'^question/(?P<pk>\d+)/$', test, name='qa-question-by-id'),
#)
]