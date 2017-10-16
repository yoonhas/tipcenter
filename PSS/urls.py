"""newtip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
from . import questions_view
from . import analysis_view
from . import survey_views

app_name = 'PSS'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add/participant/new', views.add_surveyee, name="add_new_participant"),
    url(r'^add/participant', views.add_paticipants_view, name="call_add_participant"),
    url(r'^(?P<agent_id>[0-9]+)/detail$', views.Surveyee_detail_view, name="agent_detail"),
    url(r'^select/agents/release$', views.release_survey_agent, name="release_survey_agent"),
    url(r'^set/participatns/ready$', views.set_ready, name="set_ready"),
    url(r'^show/participatns/links', views.show_links, name="show_links"),
    url(r'^(?P<agent_id>[0-9]+)/select/participants/release$', views.release_survey_participants, name="release_survey_participants"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/times/$', views.Surveytimes_view, name='surveyTimes'),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/peb/start/$',questions_view.EB_view, name='start'),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/peb/$', survey_views.EB_view1, name = "peb"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/ehs/start$', questions_view.EH_view, name = "ehs_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/ehs/(?P<survey>[0-9]+)/$', survey_views.EH_view1, name = "ehs"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/ess/start$', questions_view.ES_view, name = "ess_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/ess/(?P<survey>[0-9]+)/$', survey_views.ES_view1, name = "ess"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/tip/start$', questions_view.Tip_view, name = "tip_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/tip/(?P<survey>[0-9]+)/$', survey_views.Tip_view1, name="tip"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/exf/start$', questions_view.EXF_view, name="exf_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/exf/(?P<survey>[0-9]+)/$', survey_views.EXF_view1, name="exf"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/r/start$', questions_view.R_view, name="r_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/r/(?P<survey>[0-9]+)/$', survey_views.R_view1, name="r_scare"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/sef/start$', questions_view.SEF_view, name="sef_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/sef/(?P<survey>[0-9]+)/$', survey_views.SEF_view1, name="sef"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/gr/start$', questions_view.GR_view, name="gr_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/gr/(?P<survey>[0-9]+)/$', survey_views.GR_view1, name="gr"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/spr/start$', questions_view.SPR_view, name="spr_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/spr/(?P<survey>[0-9]+)/$', survey_views.SPR_view1, name="spr"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/ssp/start$', questions_view.SSP_view, name="ssp_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/ssp/(?P<survey>[0-9]+)/$', survey_views.SSP_view1, name="ssp"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/f/start$', questions_view.F_view, name="f_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/f/(?P<survey>[0-9]+)/$', survey_views.F_view1, name="f_scare"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/gd/start$', questions_view.GD_view, name="gd_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/gd/(?P<survey>[0-9]+)/$', survey_views.GD_view1, name="gd"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/hm/start$', questions_view.HM_view, name="hm_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/hm/(?P<survey>[0-9]+)/$', survey_views.HM_view1, name="hm"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/health/start$', questions_view.HEALTH_view, name="health_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/health/(?P<survey>[0-9]+)/$', survey_views.HEALTH_view1, name="health"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/dm/start$', questions_view.DM_view, name="dm_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/dm/(?P<survey>[0-9]+)/$', survey_views.DM_view1, name="dm"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/rsefgr/start$', questions_view.R_SEF_GR_view, name="r_sef_gr_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/rsefgr/(?P<survey>[0-9]+)/$', questions_view.R_SEF_GR_view, name="r_sef_gr"),
    url(r'^upload/csv/$', views.upload_csv, name= 'upload_csv'),
    url(r'^upload/csv/start/$', views.upload_csv, name= 'upload_csv_start'),
    url(r'^thankyou/$', views.Thanks, name="thanks"),
    url(r'^(?P<agent_id>[0-9]+)/summary/$', analysis_view.summary, name="summary"),
    url(r'^(?P<agent_id>[0-9]+)/summary/(?P<userId>[0-9]+)/agent/$', analysis_view.score_detail_agent, name="summary_agent"),
    url(r'^(?P<agent_id>[0-9]+)/score/(?P<userId>[0-9]+)/detail/$', analysis_view.score_detail, name="score_detail"),
    url(r'^compare/$', analysis_view.compare_view, name= 'compare_view'),
    url(r'^compare/detail/$', analysis_view.compare_detail, name= 'compare_detail'),
    url(r'^compare/(?P<agent_id>[0-9]+)/detail/$', analysis_view.compare_agent, name= 'compare_agent'),
    url(r'^compare/(?P<agent_id>[0-9]+)/detail/show/$', analysis_view.show_compare_agent, name= 'show_compare_agent'),
    url(r'^showgraph$', analysis_view.show_graph, name='show_graph'),

]
