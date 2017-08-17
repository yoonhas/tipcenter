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

app_name = 'PSS'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<agent_id>[0-9]+)/detail$', views.Surveyee_detail_view, name="agent_detail"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/times/$', views.Surveytimes_view, name='surveyTimes'),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/peb/start/$',views.EB_view, name='start'),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/peb/$', views.EB_view1, name = "peb"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/ehs/start$', views.EH_view, name = "ehs_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/ehs/(?P<survey>[0-9]+)/$', views.EH_view1, name = "ehs"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/ess/start$', views.ES_view, name = "ess_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/ess/(?P<survey>[0-9]+)/$', views.ES_view1, name = "ess"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/tip/start$', views.Tip_view, name = "tip_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/tip/(?P<survey>[0-9]+)/$', views.Tip_view1, name="tip"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/exf/start$', views.EXF_view, name="exf_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/exf/(?P<survey>[0-9]+)/$', views.EXF_view1, name="exf"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/r/start$', views.R_view, name="r_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/r/(?P<survey>[0-9]+)/$', views.R_view1, name="r_scare"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/sef/start$', views.SEF_view, name="sef_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/sef/(?P<survey>[0-9]+)/$', views.SEF_view1, name="sef"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/gr/start$', views.GR_view, name="gr_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/gr/(?P<survey>[0-9]+)/$', views.GR_view1, name="gr"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/spr/start$', views.SPR_view, name="spr_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/spr/(?P<survey>[0-9]+)/$', views.SPR_view1, name="spr"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/ssp/start$', views.SSP_view, name="ssp_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/ssp/(?P<survey>[0-9]+)/$', views.SSP_view1, name="ssp"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/f/start$', views.F_view, name="f_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/f/(?P<survey>[0-9]+)/$', views.F_view1, name="f_scare"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/gd/start$', views.GD_view, name="gd_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/gd/(?P<survey>[0-9]+)/$', views.GD_view1, name="gd"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/hm/start$', views.HM_view, name="hm_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/hm/(?P<survey>[0-9]+)/$', views.HM_view1, name="hm"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/health/start$', views.HEALTH_view, name="health_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/health/(?P<survey>[0-9]+)/$', views.HEALTH_view1, name="health"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/dm/start$', views.DM_view, name="dm_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/dm/(?P<survey>[0-9]+)/$', views.DM_view1, name="dm"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/(?P<survey>[0-9]+)/rsefgr/start$', views.R_SEF_GR_view, name="r_sef_gr_start"),
    url(r'^(?P<surveyee_caseNum>[0-9]+)/rsefgr/(?P<survey>[0-9]+)/$', views.R_SEF_GR_view, name="r_sef_gr"),
    url(r'^upload/csv/$', views.upload_csv, name= 'upload_csv'),
    url(r'^upload/csv/start/$', views.upload_csv, name= 'upload_csv_start'),
    url(r'^thankyou/$', views.Thanks, name="thanks"),
    url(r'^(?P<agent_id>[0-9]+)/summary/$', views.summary, name="summary"),
    url(r'^(?P<agent_id>[0-9]+)/score/detail/$', views.score_detail, name="score_detail"),
    url(r'^compare/$', views.compare_view, name= 'compare_view'),
    url(r'^compare/detail/$', views.compare_detail, name= 'compare_detail'),
    url(r'^showgraph$', views.show_graph, name='show_graph'),

]
