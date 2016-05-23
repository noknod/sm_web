from django.conf.urls import url, patterns

from qa.views import test, error, question_list_all, question_list_popular, \
    question_by_id


#urlpatterns = patterns('qa.views',
urlpatterns = [
    url(r'^$', question_list_all, name='qa-home'),
    url(r'^login/.*$', test, name='qa-login'),
    url(r'^signup/.*$', test, name='qa-signup'),
    url(r'^ask/.*$', test, name='qa-ask'),
    url(r'^popular/.*$', question_list_popular, name='qa-popular'),
    url(r'^new/.*$', test, name='qa-new'),
    url(r'^question/(?P<pk>\d+)/$', question_by_id, name='qa-question-by-id'),
#)
]