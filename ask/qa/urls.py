from django.conf.urls import url, patterns

from qa.views import test, error, question_list_all, question_list_popular, \
    question_by_id, question_add, answer_add, signup, login_do


#urlpatterns = patterns('qa.views',
urlpatterns = [
    url(r'^$', question_list_all, name='qa-home'),
    url(r'^login/.*$', login_do, name='qa-login'),
    url(r'^signup/.*$', signup, name='qa-signup'),
    url(r'^ask/.*$', question_add, name='qa-ask'),
    url(r'^popular/.*$', question_list_popular, name='qa-popular'),
    url(r'^new/.*$', test, name='qa-new'),
    url(r'^answer/?$', answer_add, name='qa-answer'),
    url(r'^question/(?P<pk>\d+)/$', question_by_id, name='qa-question-by-id'),
#)
]