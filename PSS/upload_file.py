from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic.base import TemplateView
from  django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from  django.contrib import messages
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
from . import survey_views





def upload_view(request):
    return render(request, 'PSS/Analysis/upload.html')

def upload_csv(request):
    if "GET" == request.method:
        return render(request, "PSS/Analysis/upload.html")

    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return HttpResponseRedirect(reverse("PSS:upload_csv"))

        if csv_file.multiple_chunks():
            messages.error(request, "Uploaded file is too big (%.2f MB)." % (csv_file.size / (1000 * 1000),))
            return HttpResponseRedirect(reverse("PSS:upload_csv"))


    except Exception as e:
        logging.getLogger("error_logger").error("unable to upload file."+repr(e))
        messages.error(request, "unable to upload file."+repr(e))

    else:
        df = readFile(csv_file)
        succeed, fail = add_first_Survey(df)

    return render(request, 'PSS/Analysis/complete_upload.html', {"succeed":succeed, "fail":fail})

def Thanks(request):
    return HttpResponse('Thank you')


def add_first_Survey(df):
    agent_map = {1: 'CARA', 2: 'HPOG-Gateway', 3: 'HPOG-SouthLand', 4: 'CHA', 5: 'Inspiration', 6: 'instituto-IDPL',
                 7: 'instituto-IDPL',
                 8: 'MBC', 9: 'Cara-CWF', 10: 'GrowingHome', 11: 'CJC-CNH', 12: 'CJC-Safer', 13: 'CJC-SER',
                 14: 'HPOG2.0', 15: 'GreaterWestTown',
                 16: 'DuPagePads', 17: 'HeartlandAlli', 18: 'CTA', 19: 'CentroRomero', 20: 'St.Patricks-Mc'}

    #exting participants
    fail= []
    succeed = []

    for i in range(len(df)):
        users = get_user_model()
        agent = users.objects.get(username = agent_map[df.ix[i]['Site']])

        #if the participant is existing retu
        if Surveyee.objects.filter(caseNum=df.ix[i]['CaseNum']).exists():
            fail.append(df.ix[i]['CaseNum'])
            print("hereereer==========")
        else:
            #creating a new participant
            surveyee = Surveyee(caseNum=df.ix[i]['CaseNum'], agent_name=agent, survey1=True)
            surveyee.save()
            succeed.append(df.ix[i]['CaseNum'])
            surveyTime = SurveyTimes(caseNum=surveyee, time=1, agent=agent, pub_Date=df.ix[i]['cDATE'])
            surveyTime.save()
            try:
                total = Total_for_Admin(caseNum=surveyee, Agent=agent, Time=1, Date=df.ix[i]['cDATE'],
                                        Health=df.ix[i]['Health'], Community=df.ix[i]['Community'],
                                        Childcare=df.ix[i]['ChildCare'],
                                        Jobskills=df.ix[i]['JobSkills'], SoftSkill=df.ix[i]['SoftSkill'],
                                        Peb_all=df.ix[i]['PEBS_all'],
                                        Empowerment=df.ix[i]['Empowerment'], Selfmotivation=df.ix[i]['SelfMotivation'],
                                        SkilResources=df.ix[i]['SkillResources'],
                                        GaolOrientation=df.ix[i]['GoalOrientation'], Ehs_all=df.ix[i]['EHS_all'],
                                        Ess1=df.ix[i]['ESS1'], Ess2=df.ix[i]['ESS2'],
                                        Ess3=df.ix[i]['ESS3'], Ess4=df.ix[i]['ESS4'], Ess_all=df.ix[i]['ESS_all'],
                                        PSS=df.ix[i]['EHS_all'] - df.ix[i]['PEBS_all'],
                                        Resilience=df.ix[i]['R_all'], Self_Efficacy=df.ix[i]['SEF_all'],
                                        GR_Con=df.ix[i]['GR_con'], GR_Per=df.ix[i]['GR_per'],
                                        GR_all=df.ix[i]['GR_all'], SPR_all=df.ix[i]['SPR_all'], F_self=df.ix[i]['F_self'],
                                        F_other=df.ix[i]['F_other'],
                                        F_situation=df.ix[i]['F_situation'], F_all=df.ix[i]['F_all'],
                                        DM1=df.ix[i]['Employed'], DM1_1_year=df.ix[i]['YearsEmployed'],
                                        DM1_1_month=df.ix[i]['MonthsEmployed'],
                                        DM1_1_days=df.ix[i]['DaysEmployed'],
                                        DM1_2=0, DM1_3=0, DM1_4=0,
                                        DM2=0, DM3=0, DM4=0,
                                        DM5=0,
                                        DM6=0, DM7=0, DM8=2, DM9=1,
                                        DM9_1='',
                                        DM10=1,
                                        DM11_1=1, DM11_2=1, DM11_3=1,
                                        DM11_4=1,
                                        DM12_1=df.ix[i]['Age'], DM12_3=1, DM13=df.ix[i]['Gender'],
                                        DM14=df.ix[i]['Race'], DM14_1=' ',
                                        DM15=1, DM16=df.ix[i]['EDULevel'], DM17=1, DM18=1,
                                        DM19=1)
                surveyTime.doneSurvey = True
                surveyTime.readyToStart = False
                surveyTime.pub_Date = timezone.now()
                surveyTime.save()
                surveyee.survey1 = True
                surveyee.save()
                total.save()
            except Exception as e:
                for k in df.ix[i]:
                    print(k)
                print(e)

    return (succeed, fail)

