from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from SimpleApp import controllers

urlpatterns = patterns(
    '',
    url(r'^question/list/$', controllers.get_questions),
    url(r'^question/create/$', controllers.create_question),
    url(r'^question/delete/(?P<question_id>\d+)$', controllers.delete_question),
    url(r'^question/modify/(?P<question_id>\d+)$', controllers.modify_question),
    url(r'^question/delete_selected/(?P<question_ids>[\d+,\,]+)$', controllers.delete_selected),
)
