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
        inputFromPanda(df)

    return HttpResponseRedirect(reverse('PSS:upload_csv'))

def Thanks(request):
    return HttpResponse('Thank you')

'''def check_row_by_row(surveyee, time, agent, check_row):
    if  SurveyTimes.objects.filter(caseNum=surveyee).exists() and SurveyTimes.objects.filter(caseNum=surveyee,time=time).exists():'''
        







def inputFromPanda(df):
    agent_map = {1: 'CARA', 2: 'HPOG-Gateway', 3: 'HPOG-SouthLand', 4:'CHA', 5:'Inspiration', 6:'instituto-IDPL', 7:'instituto-IDPL',
                 8:'MBC', 9:'Cara-CWF', 10:'GrowingHome', 11:'CJC-CNH', 12: 'CJC-Safer', 13:'CJC-SER', 14:'HPOG2.0', 15:'GreaterWestTown',
                 16:'DuPagePads', 17:'HeartlandAlli', 18:'CTA', 19:'CentroRomero', 20:'St.Patricks-Mc' }

    for i in range(len(df)):

        users = get_user_model()
        agent = users.objects.get(username= agent_map[df.ix[i]['Site']])


        # surveyee
        if Surveyee.objects.filter(caseNum=df.ix[i]['CaseNum']).exists():
            surveyee = Surveyee.objects.get(caseNum=df.ix[i]['CaseNum'])
        else:
            surveyee = Surveyee(caseNum=df.ix[i]['CaseNum'], agent_name=agent)
            surveyee.save()

        # surveyTime
        Time = SurveyTimes.objects.filter(caseNum=surveyee).count()
        Time += 1
        if Time > 4:
            continue
        else:

            surveyTime = SurveyTimes(caseNum=surveyee, time=Time, agent= agent, pub_Date=df.ix[i]['cDATE'])
            surveyTime.save()

        # eb
        eb = EB(caseNum=surveyee, surveytime=surveyTime.pk, time=Time, EB1=df.ix[i]['EB1']
                , EB2=df.ix[i]['EB2'], EB3=df.ix[i]['EB3'], EB4=df.ix[i]['EB4'], EB5=df.ix[i]['EB5'],
                EB6=df.ix[i]['EB6'], EB7=df.ix[i]['EB7'], EB8=df.ix[i]['EB8'], EB9=df.ix[i]['EB9'],
                EB10=df.ix[i]['EB10'],
                EB11=df.ix[i]['EB11'], EB12=df.ix[i]['EB12'], EB13=df.ix[i]['EB13'], EB14=df.ix[i]['EB14'],
                EB15=df.ix[i]['EB15'],
                EB16=df.ix[i]['EB16'], EB17=df.ix[i]['EB17'], EB18=df.ix[i]['EB18'], EB19=df.ix[i]['EB19'],
                EB20=df.ix[i]['EB20'],
                EB21=df.ix[i]['EB21'], EB22=df.ix[i]['EB22'], EB23=df.ix[i]['EB23'], EB24=df.ix[i]['EB24'],
                EB25=df.ix[i]['EB25'],
                EB26=df.ix[i]['EB26'], EB27=df.ix[i]['EB27'])
        eb.save()

        # eh
        if 'EH15' in df.columns:
            eh = EH(caseNum=surveyee, time=Time, surveytime=surveyTime.pk,
                    EH1=df.ix[i]['EH1'], EH2=df.ix[i]['EH2'], EH3=df.ix[i]['EH3'], EH4=df.ix[i]['EH4'], EH5=df.ix[i]['EH5'],
                    EH6=df.ix[i]['EH6'], EH7=df.ix[i]['EH7'], EH8=df.ix[i]['EH8'], EH9=df.ix[i]['EH9'],
                    EH10=df.ix[i]['EH10'],
                    EH11=df.ix[i]['EH11'], EH12=df.ix[i]['EH12'], EH13=df.ix[i]['EH13'], EH14=df.ix[i]['EH14'],
                    EH15=df.ix[i]['EH15'],
                    EH16=df.ix[i]['EH16'], EH17=df.ix[i]['EH17'], EH18=df.ix[i]['EH18'], EH19=df.ix[i]['EH19'],
                    EH20=df.ix[i]['EH20'],
                    EH21=df.ix[i]['EH21'], EH22=df.ix[i]['EH22'], EH23=df.ix[i]['EH23'], EH24=df.ix[i]['EH24'])
        else:
            eh = EH(caseNum=surveyee, time=Time, surveytime=surveyTime.pk,
                    EH1=df.ix[i]['EH1'], EH2=df.ix[i]['EH2'], EH3=df.ix[i]['EH3'], EH4=df.ix[i]['EH4'], EH5=df.ix[i]['EH5'],
                    EH6=df.ix[i]['EH6'], EH7=df.ix[i]['EH7'], EH8=df.ix[i]['EH8'], EH9=df.ix[i]['EH9'],
                    EH10=df.ix[i]['EH10'],
                    EH11=df.ix[i]['EH11'], EH12=df.ix[i]['EH12'], EH13=df.ix[i]['EH13'], EH14=df.ix[i]['EH14'],
                    EH15=99,
                    EH16=99, EH17=99, EH18=99, EH19=99,
                    EH20=99,
                    EH21=99, EH22=99, EH23=99, EH24=99)#old data


        eh.save()

        # es
        es = ES(caseNum=surveyee, time=Time, surveytime=surveyTime.pk,
                ES1=df.ix[i]['SS1'], ES2=df.ix[i]['SS2'], ES3=df.ix[i]['SS3'], ES4=df.ix[i]['SS4'],
                ES5=df.ix[i]['SS5'],
                ES6=df.ix[i]['SS6'], ES7=df.ix[i]['SS7'], ES8=df.ix[i]['SS8'], ES9=df.ix[i]['SS9'],
                ES10=df.ix[i]['SS10'],
                ES11=df.ix[i]['SS11'], ES12=df.ix[i]['SS12'], ES13=df.ix[i]['SS13'],
                ES14=df.ix[i]['SS14'],
                ES15=df.ix[i]['SS15']
                )
        es.save()

        tip = Tip(caseNum=surveyee, time=Time, surveytime=surveyTime.pk,
                  TIP1=7, TIP2=7, TIP3=7,
                  TIP4=7,
                  TIP5=7,
                  TIP6=7, TIP7=7, TIP8=7,
                  TIP9=7,
                  TIP10=7,
                  TIP11=7, TIP12=7, TIP13=7,
                  TIP14=7,
                  TIP15=7
                  )
        tip.save()

        exf = EXF(caseNum=surveyee, time=Time, surveytime=surveyTime.pk,
                  A3=6, B3=6, C3=6, D3=6,
                  E2=6,
                  F2=6, G1=6, H3=6, I2=6,
                  J3=6,
                  K1=6, K2=6, K3=6,
                  L1=6,
                  L2=6, L3=6
                  )
        exf.save()

        r = R(caseNum=surveyee, time=Time, surveytime=surveyTime.pk,
              R1=df.ix[i]['R1'], R2=df.ix[i]['R2']
              )
        r.save()

        sef = SEF(caseNum=surveyee, time=Time, surveytime=surveyTime.pk,
                  SEF1=df.ix[i]['SEF1'], SEF2=df.ix[i]['SEF2'], SEF3=df.ix[i]['SEF3'],
                  SEF4=df.ix[i]['SEF4'],
                  SEF5=df.ix[i]['SEF5'],
                  SEF6=df.ix[i]['SEF6'], SEF7=df.ix[i]['SEF7'], SEF8=df.ix[i]['SEF8']
                  )
        sef.save()

        gr = GR(caseNum=surveyee, time=Time, surveytime=surveyTime.pk,
                GR1=df.ix[i]['GR1'], GR2=df.ix[i]['GR2'], GR3=df.ix[i]['GR3'],
                GR4=df.ix[i]['GR4'],
                GR5=df.ix[i]['GR5'],
                GR6=df.ix[i]['GR6'], GR7=df.ix[i]['GR7'], GR8=df.ix[i]['GR8']
                )
        gr.save()
        if 'SPR1' in df.columns:
            spr = SPR(caseNum=surveyee, time=Time, surveytime=surveyTime.pk,
                      SPR1=df.ix[i]['SPR1'], SPR2=df.ix[i]['SPR2'], SPR3=df.ix[i]['SPR3'],
                      SPR4=df.ix[i]['SPR4'],
                      SPR5=df.ix[i]['SPR5'],
                      SPR6=df.ix[i]['SPR6']
                      )
        else:
            spr = SPR(caseNum=surveyee, time=Time, surveytime=surveyTime.pk,
                      SPR1=99, SPR2=99, SPR3=99,
                      SPR4=99,
                      SPR5=99,
                      SPR6=99
                      )


        spr.save()
        ssp = SSP(caseNum=surveyee, time=Time, surveytime=surveyTime.pk,
                  SSP1=4, SSP2=4, SSP3=4,
                  SSP4=4,
                  SSP5=4,
                  SSP6=4, SSP7=4, SSP8=4, SSP9=4,
                  SSP10=4,
                  SSP11=4, SSP12=4
                  )
        ssp.save()

        if 'F1' in df.columns:
            f = F(caseNum=surveyee, time=Time, surveytime=surveyTime.pk,
                  F1=df.ix[i]['F1'], F2=df.ix[i]['F2'], F3=df.ix[i]['F3'], F4=df.ix[i]['F4'],
                  F5=df.ix[i]['F5'],
                  F6=df.ix[i]['F6'], F7=df.ix[i]['F7'], F8=df.ix[i]['F8'], F9=df.ix[i]['F9'],
                  F10=df.ix[i]['F10'],
                  F11=df.ix[i]['F11'], F12=df.ix[i]['F12'], F13=df.ix[i]['F13'], F14=df.ix[i]['F14'],
                  F15=df.ix[i]['F15'],
                  F16=df.ix[i]['F16'], F17=df.ix[i]['F17'], F18=df.ix[i]['F18']
                  )
        else:
            f = F(caseNum=surveyee, time=Time, surveytime=surveyTime.pk,
                  F1=99, F2=99, F3=99, F4=99,
                  F5=99,
                  F6=99, F7=99, F8=99, F9=99,
                  F10=99,
                  F11=99, F12=99, F13=99, F14=99,
                  F15=99,
                  F16=99, F17=99, F18=99
                  )

        f.save()
        gd = GD(caseNum=surveyee, time=Time, surveytime=surveyTime.pk,
                GD1=4, GD2=4, GD3=4,
                GD4=4,
                GD5=4,
                GD6=4
                )
        gd.save()

        hm = HM(caseNum=surveyee, time=Time, surveytime=surveyTime.pk,
                HM1=4, HM2=4, HM3=4, HM4=4,
                HM5=4,
                HM6=4, HM7=4, HM8=4, HM9=4,
                HM10=4,
                HM11=4, HM12=4, HM13=4, HM14=4,
                HM15=4
                )
        hm.save()

        health = HEALTH(caseNum=surveyee, time=Time, surveytime=surveyTime.pk,
                        HEALTH1=4, HEALTH2=4
                        )
        health.save()

        dm = DM(caseNum=surveyee, time=Time, surveytime=surveyTime.pk,
                DM1=df.ix[i]['Employed'], DM1_1_year=df.ix[i]['YearsEmployed'], DM1_1_month=df.ix[i]['MonthsEmployed'],
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
                DM19=1
                )

        dm.save()

        total = Total_for_Admin(caseNum= surveyee, Agent=agent, Time=Time, Date= df.ix[i]['cDATE'],
                                Health=df.ix[i]['Health'], Community=df.ix[i]['Community'],Childcare=df.ix[i]['ChildCare'],
                                Jobskills=df.ix[i]['JobSkills'], SoftSkill=df.ix[i]['SoftSkill'], Peb_all=df.ix[i]['PEBS_all'],
                                Empowerment=df.ix[i]['Empowerment'], Selfmotivation=df.ix[i]['SelfMotivation'],SkilResources=df.ix[i]['SkillResources'],
                                GaolOrientation=df.ix[i]['GoalOrientation'], Ehs_all=df.ix[i]['EHS_all'], Ess1=df.ix[i]['ESS1'], Ess2= df.ix[i]['ESS2'],
                                Ess3=df.ix[i]['ESS3'], Ess4=df.ix[i]['ESS4'], Ess_all=df.ix[i]['ESS_all'], PSS=df.ix[i]['EHS_all']-df.ix[i]['PEBS_all'],
                                Resilience=df.ix[i]['R_all'], Self_Efficacy=df.ix[i]['SEF_all'],GR_Con=df.ix[i]['GR_con'], GR_Per=df.ix[i]['GR_per'],
                                GR_all=df.ix[i]['GR_all'], SPR_all=df.ix[i]['SPR_all'], F_self=df.ix[i]['F_self'], F_other=df.ix[i]['F_other'],
                                F_situation=df.ix[i]['F_situation'], F_all=df.ix[i]['F_all'], DM1=df.ix[i]['Employed'], DM1_1_year=df.ix[i]['YearsEmployed'], DM1_1_month=df.ix[i]['MonthsEmployed'],
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
        if Time == 1:
            surveyee.survey1 = True
        elif Time == 2:
            surveyee.survey2 = True
        elif Time == 3:
            surveyee.survey3 = True
        elif Time == 4:
            surveyee.survey4 = True
        surveyee.save()
        total.save()