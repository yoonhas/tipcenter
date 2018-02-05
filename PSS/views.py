from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic.base import TemplateView
from  django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from  django.contrib import messages
from django.urls import reverse
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Surveyee, SurveyTimes,EB, EH, EH_Question, ES_Question, ES, Tip_Question, Tip, EB_Question
from .models import EXF_Question,EXF, R, R_Question, SEF, SEF_Question, GR, GR_Question, SPR, SPR_Question,Total_for_Admin
from .models import SSP_Question, SSP, F, F_Question, GD, GD_Question, HM_Question, HM, HEALTH_Question, HEALTH, DM, DM_Question
from django.utils import timezone
from .readFile import readFile
import pandas as pd
import logging

from .upload_file import add_first_Survey

import matplotlib
matplotlib.use("Agg")

from . import survey_views

pd.set_option('precision', 6)
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'PSS/index.html'
    context_object_name = 'agent_list'
    def get_queryset(self):
        return User.objects.filter()

class CreateUserView(CreateView):
    template_name = 'PSS/registration/signup.html'
    form_class = CreateUserForm
    def get_success_url(self): # override this function if you want to use reverse

        return reverse('index')

class RegisteredView(TemplateView):
    template_name = 'PSS/registration/signup_done.html'

def add_paticipants_view(request):
    users = get_user_model()
    agents = users.objects.all()
    return render(request, 'PSS/add_participant.html', {'agents':agents})

def add_surveyee(request):
    agent_id = request.POST['agentid']
    users = get_user_model()
    agent = users.objects.get(id= agent_id)
    numbers= Surveyee.objects.filter(agent_name_id = agent.id).count()
    new_id = str(agent_id) + '000'+str(numbers)
    language = request.POST['language']
    new_surveyee = Surveyee(caseNum=int(new_id), agent_name=agent, survey_kind=int(language))
    new_surveyee.save()
    first_surveyTime =  SurveyTimes(caseNum=new_surveyee,agent=agent, time=1, pub_Date=timezone.now(), readyToStart=True)
    first_surveyTime.save()
    all_surveyee = Surveyee.objects.filter(agent_name_id=agent_id)

    return render(request, 'PSS/agent_detail.html', {'surveyee_list':all_surveyee, 'message':new_id})

def release_survey_agent(request):
    users = get_user_model()
    agents = users.objects.all()
    return render(request, 'PSS/release_show_agents.html', {'agents': agents})

def release_survey_participants(request, agent_id):
    users = get_user_model()
    agent = users.objects.get(id=agent_id)
    participants_1 = Surveyee.objects.filter(agent_name_id=agent.id, survey1=True,survey2=False,survey3=False,survey4=False, readyToStart=False)
    participants_2 = Surveyee.objects.filter(agent_name_id=agent.id, survey1=True,survey2=True,survey3=False,survey4=False, readyToStart=False)
    participants_3 = Surveyee.objects.filter(agent_name_id=agent.id, survey1=True,survey2=True,survey3=True,survey4=False, readyToStart=False)
    participants_4 = Surveyee.objects.filter(agent_name_id=agent.id,survey1=True,survey2=True,survey3=True,survey4=True, readyToStart=False)

    waitingList = Surveyee.objects.filter(agent_name_id=agent.id, readyToStart=True)

    return render(request, 'PSS/release_show_participants.html', {'participants_1': participants_1, 'participants_2': participants_2,'participants_3': participants_3
                                                                  ,'participants_4': participants_4, 'waiting':waitingList})


def set_ready(request):

    def helper(i, time):
        NAME = 'www.pssdatasolution.org/PSS/'
        TIMES = '/times/'
        surveyee = Surveyee.objects.get(caseNum=int(i))
        users = get_user_model()
        agent = users.objects.get(id = surveyee.agent_name_id)
        if SurveyTimes.objects.filter(caseNum=surveyee, agent = agent, time = time, readyToStart=True ).exists():
            surveyee.readyToStart = True
            surveyee.save()
            link = "{}{}{}".format(NAME,str(surveyee.caseNum),TIMES)
            return (surveyee.caseNum, link)
        surveyTime = SurveyTimes(caseNum=surveyee, agent = agent, time = time, pub_Date= timezone.now(), readyToStart=True )
        surveyee.readyToStart = True
        surveyee.save()
        surveyTime.save()
        link = "{}{}{}".format(NAME,str(surveyee.caseNum),TIMES)
        return (surveyee.caseNum, link)

    participants1=request.POST.getlist('participants1')
    participants2 = request.POST.getlist('participants2')
    participants3 = request.POST.getlist('participants3')
    link1 = [helper(i, 2) for i in participants1]
    link2 = [helper(i, 3) for i in participants2]
    link3 = [helper(i, 4) for i in participants3]

    return render(request, 'PSS/show_links.html', {'link1':link1,'link2':link2,'link3':link3 })

def show_links(request):
    return



def Surveyee_detail_view(request, agent_id):
    if agent_id == 1:
        all_surveyee = Surveyee.objects.all()
    else:
        all_surveyee = Surveyee.objects.filter(agent_name_id= agent_id)
    return render(request, 'PSS/agent_detail.html', {'surveyee_list':all_surveyee})

def checking_Survey_Status(surveyee_caseNum, time):

    if SurveyTimes.objects.filter(caseNum=surveyee_caseNum, time=time).exists():

        surveyTime=SurveyTimes.objects.get(caseNum=surveyee_caseNum, time=time)
        eb= EB.objects.filter(caseNum=surveyee_caseNum, time = time, surveytime=surveyTime.pk)
        eh =EH.objects.filter(caseNum=surveyee_caseNum, time = time, surveytime=surveyTime.pk)
        es =ES.objects.filter(caseNum=surveyee_caseNum, time = time, surveytime=surveyTime.pk)
        exf =EXF.objects.filter(caseNum=surveyee_caseNum, time = time, surveytime=surveyTime.pk)
        f = F.objects.filter(caseNum=surveyee_caseNum, time = time, surveytime=surveyTime.pk)
        gd = GD.objects.filter(caseNum=surveyee_caseNum, time = time, surveytime=surveyTime.pk)
        gr = GR.objects.filter(caseNum=surveyee_caseNum, time = time, surveytime=surveyTime.pk)
        health = HEALTH.objects.filter(caseNum=surveyee_caseNum, time = time, surveytime=surveyTime.pk)
        r =R.objects.filter(caseNum=surveyee_caseNum, time = time, surveytime=surveyTime.pk)
        sef=SEF.objects.filter(caseNum=surveyee_caseNum, time = time, surveytime=surveyTime.pk)
        spr=SPR.objects.filter(caseNum=surveyee_caseNum, time = time, surveytime=surveyTime.pk)
        ssp=SSP.objects.filter(caseNum=surveyee_caseNum, time = time, surveytime=surveyTime.pk)
        tip=Tip.objects.filter(caseNum=surveyee_caseNum, time = time, surveytime=surveyTime.pk)
        dm = DM.objects.filter(caseNum=surveyee_caseNum, time=time, surveytime=surveyTime.pk)
        checklist=[eb,eh,es,exf,f,gd,gr,health,r,sef,spr,ssp,tip,dm]
        for each in checklist:

            if each.count() == 0:
                #SurveyTimes.objects.get(pk=surveyTime.pk).delete()
                for i in checklist:
                    i.delete()
                return

def Surveytimes_view(request, surveyee_caseNum):

    surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
    users = get_user_model()
    agent = users.objects.get(id=surveyee.agent_name_id)

    surveyTime = SurveyTimes.objects.filter(caseNum=surveyee, agent=agent, readyToStart=False)

    if SurveyTimes.objects.filter(caseNum=surveyee, agent=agent, readyToStart=True).exists():
        startSurvey = SurveyTimes.objects.get(caseNum=surveyee, agent=agent, readyToStart=True)

        return render(request, 'PSS/times.html', {'surveyTime': surveyTime, 'startSurvey': startSurvey, 'surveyee_caseNum':surveyee_caseNum, 'survey':startSurvey.time })

    return render(request, 'PSS/times.html', {'surveyTime':surveyTime, 'message': "No Survey is avaialbe now"
                                              })


def Thanks(request):
    return HttpResponse('Thank you')



def deleteAll():
    DM.objects.all().delete()
    EB.objects.all().delete()
    EH.objects.all().delete()
    ES.objects.all().delete()
    EXF.objects.all().delete()
    F.objects.all().delete()
    GD.objects.all().delete()
    GR.objects.all().delete()
    HEALTH.objects.all().delete()
    HM.objects.all().delete()
    R.objects.all().delete()
    SEF.objects.all().delete()
    SPR.objects.all().delete()
    SSP.objects.all().delete()
    Tip.objects.all().delete()
    SurveyTimes.objects.all().delete()
    Surveyee.objects.all().delete()
    print("good to go")









