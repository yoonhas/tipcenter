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
from django_pandas.io import read_frame
import matplotlib
matplotlib.use("Agg")
import mpld3
from mpld3 import plugins
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter


def EB_view1(request,surveyee_caseNum, survey):
    surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
    time=SurveyTimes.objects.filter(caseNum=surveyee_caseNum).count()

    try:
        if(EB.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            return redirect('PSS:ehs_start', surveyee_caseNum, survey)

        else:
            eb = EB(caseNum=surveyee, time=time, surveytime=survey,
                    EB1=request.POST['EB1'],EB2=request.POST['EB2'],EB3=request.POST['EB3'],EB4=request.POST['EB4'],EB5=request.POST['EB5'],
                    EB6=request.POST['EB6'], EB7=request.POST['EB7'], EB8=request.POST['EB8'], EB9=request.POST['EB9'],EB10=request.POST['EB10'],
                    EB11=request.POST['EB11'], EB12=request.POST['EB12'], EB13=request.POST['EB13'], EB14=request.POST['EB14'],
                    EB15=request.POST['EB15'],
                    EB16=request.POST['EB16'], EB17=request.POST['EB17'], EB18=request.POST['EB18'], EB19=request.POST['EB19'],
                    EB20=request.POST['EB20'],
                    EB21=request.POST['EB21'], EB22=request.POST['EB22'], EB23=request.POST['EB23'], EB24=request.POST['EB24'],
                    EB25=request.POST['EB25'],
                    EB26=request.POST['EB26'], EB27=request.POST['EB27'])
    except(KeyError, EB.DoesNotExist):
        return render(request, 'PSS/Survey/EB_tem1.html', {'surveyee_caseNum' :surveyee_caseNum})
    else:
        eb.save()
        return redirect('PSS:ehs_start', surveyee_caseNum, survey)


def EH_view1(request, surveyee_caseNum, survey):
    time = SurveyTimes.objects.filter(caseNum=surveyee_caseNum).count()
    surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)

    try:
        if (EH.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            return redirect('PSS:ess_start', surveyee_caseNum, survey)

        else:
            eh = EH(caseNum=surveyee, time=time, surveytime= survey,
                    EH1=request.POST['EH1'],EH2=request.POST['EH2'],EH3=request.POST['EH3'],EH4=request.POST['EH4'],EH5=request.POST['EH5'],
                    EH6=request.POST['EH6'], EH7=request.POST['EH7'], EH8=request.POST['EH8'], EH9=request.POST['EH9'],EH10=request.POST['EH10'],
                    EH11=request.POST['EH11'], EH12=request.POST['EH12'], EH13=request.POST['EH13'], EH14=request.POST['EH14'],
                    EH15=request.POST['EH15'],
                    EH16=request.POST['EH16'], EH17=request.POST['EH17'], EH18=request.POST['EH18'], EH19=request.POST['EH19'],
                    EH20=request.POST['EH20'],
                    EH21=request.POST['EH21'], EH22=request.POST['EH22'], EH23=request.POST['EH23'], EH24=request.POST['EH24']
                    )
    except(KeyError, EH.DoesNotExist):
        return render(request, 'PSS/Survey/EH_tem.html', {'surveyee_caseNum' :surveyee_caseNum})
    else:
        eh.save()
        return redirect('PSS:ess_start', surveyee_caseNum, survey)



def ES_view1(request, surveyee_caseNum, survey):
    time = SurveyTimes.objects.filter(caseNum=surveyee_caseNum).count()
    surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
    try:
        if (ES.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            return redirect('PSS:tip_start', surveyee_caseNum, survey)

        else:
            es = ES(caseNum=surveyee, time= time,surveytime= survey,
                    ES1=request.POST['ES1'], ES2=request.POST['ES2'], ES3=request.POST['ES3'], ES4=request.POST['ES4'],
                    ES5=request.POST['ES5'],
                    ES6=request.POST['ES6'], ES7=request.POST['ES7'], ES8=request.POST['ES8'], ES9=request.POST['ES9'],
                    ES10=request.POST['ES10'],
                    ES11=request.POST['ES11'], ES12=request.POST['ES12'], ES13=request.POST['ES13'],
                    ES14=request.POST['ES14'],
                    ES15=request.POST['ES15']
                    )
    except (KeyError, ES.DoesNotExist):
        return render(request, 'PSS/Survey/ES_tem.html', {'surveyee_caseNum' :surveyee_caseNum})

    else:

        es.save()
        return redirect('PSS:tip_start', surveyee_caseNum, survey)


def Tip_view1(request, surveyee_caseNum, survey):
    time = SurveyTimes.objects.filter(caseNum=surveyee_caseNum).count()
    surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
    try:
        if (Tip.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            return redirect('PSS:exf_start', surveyee_caseNum, survey)

        else:
            tip = Tip(caseNum=surveyee, time= time, surveytime=survey,
                    TIP1=request.POST['TIP1'], TIP2=request.POST['TIP2'], TIP3=request.POST['TIP3'], TIP4=request.POST['TIP4'],
                    TIP5=request.POST['TIP5'],
                    TIP6=request.POST['TIP6'], TIP7=request.POST['TIP7'], TIP8=request.POST['TIP8'], TIP9=request.POST['TIP9'],
                      TIP10=request.POST['TIP10'],
                      TIP11=request.POST['TIP11'], TIP12=request.POST['TIP12'], TIP13=request.POST['TIP13'],
                      TIP14=request.POST['TIP14'],
                      TIP15=request.POST['TIP15']
                    )
    except (KeyError, ES.DoesNotExist):
        return render(request, 'PSS/Survey/Tip_tem.html', {'surveyee_caseNum' :surveyee_caseNum})

    else:

        tip.save()
        return redirect('PSS:exf_start', surveyee_caseNum, survey)



def EXF_view1(request, surveyee_caseNum, survey):
    time = SurveyTimes.objects.filter(caseNum=surveyee_caseNum).count()
    surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
    try:
        if (EXF.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            return redirect('PSS:r_start', surveyee_caseNum, survey)

        else:
            exf = EXF(caseNum=surveyee, time= time, surveytime=survey,
                      A3=request.POST['A3'], B3=request.POST['B3'], C3=request.POST['C3'], D3=request.POST['D3'],
                      E2=request.POST['E2'],
                      F2=request.POST['F2'], G1=request.POST['G1'], H3=request.POST['H3'], I2=request.POST['I2'],
                      J3=request.POST['J3'],
                      K1=request.POST['K1'], K2=request.POST['K2'], K3=request.POST['K3'],
                      L1=request.POST['L1'],
                      L2=request.POST['L2'],L3=request.POST['L3']
                    )
    except (KeyError, EXF.DoesNotExist):
        return render(request, 'PSS/Survey/EXF_tem.html', {'surveyee_caseNum' :surveyee_caseNum})

    else:

        exf.save()
        return redirect('PSS:r_start', surveyee_caseNum, survey)



def R_SEF_GR_view1(request, surveyee_caseNum, survey):
    time = SurveyTimes.objects.filter(caseNum=surveyee_caseNum).count()
    surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
    try:
        if (R.objects.filter(caseNum=surveyee, surveytime=survey).exists()) and (SEF.objects.filter(caseNum=surveyee, surveytime=survey).exists()) \
                    (GR.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            return redirect('PSS:sef_start', surveyee_caseNum, survey)

        else:
            r = R(caseNum=surveyee, time=time, surveytime=survey,
                      R1=request.POST['R1'], R2=request.POST['R2']
                      )
            sef = SEF(caseNum=surveyee, time=time, surveytime=survey,
                      SEF1=request.POST['SEF1'], SEF2=request.POST['SEF2'], SEF3=request.POST['SEF3'],
                      SEF4=request.POST['SEF4'],
                      SEF5=request.POST['SEF5'],
                      SEF6=request.POST['SEF6'], SEF7=request.POST['SEF7'], SEF8=request.POST['SEF8']
                      )
            gr = GR(caseNum=surveyee, time=time, surveytime=survey,
                    GR1=request.POST['GR1'], GR2=request.POST['GR2'], GR3=request.POST['GR3'],
                    GR4=request.POST['GR4'],
                    GR5=request.POST['GR5'],
                    GR6=request.POST['GR6'], GR7=request.POST['GR7'], GR8=request.POST['GR8']
                    )
    except (KeyError, R.DoesNotExist, SEF.DoesNotExist, GR.DoesNotExist):
        return render(request, 'PSS/Survey/R_SEF_GR_tem.html', {'surveyee_caseNum': surveyee_caseNum})

    else:

        r.save()
        sef.save()
        gr.save()
        return redirect('PSS:spr_start', surveyee_caseNum,survey)



def R_view1(request, surveyee_caseNum, survey):
    time = SurveyTimes.objects.filter(caseNum=surveyee_caseNum).count()
    surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
    try:
        if (R.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            return redirect('PSS:sef_start', surveyee_caseNum, survey)

        else:
            r = R(caseNum=surveyee, time=time, surveytime=survey,
                      R1=request.POST['R1'], R2=request.POST['R2']
                      )

    except (KeyError, R.DoesNotExist):
        return render(request, 'PSS/Survey/SEF_tem.html', {'surveyee_caseNum': surveyee_caseNum})

    else:

        r.save()

        return redirect('PSS:sef_start', surveyee_caseNum,survey)



def SEF_view1(request, surveyee_caseNum,survey):
    time = SurveyTimes.objects.filter(caseNum=surveyee_caseNum).count()
    surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
    try:
        if (SEF.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            return redirect('PSS:gr_start', surveyee_caseNum, survey)

        else:
            sef = SEF(caseNum=surveyee, time= time, surveytime=survey,
                      SEF1=request.POST['SEF1'], SEF2=request.POST['SEF2'], SEF3=request.POST['SEF3'], SEF4=request.POST['SEF4'],
                      SEF5=request.POST['SEF5'],
                      SEF6=request.POST['SEF6'], SEF7=request.POST['SEF7'], SEF8=request.POST['SEF8']
                    )
    except (KeyError, SEF.DoesNotExist):
        return render(request, 'PSS/Survey/SEF_tem.html', {'surveyee_caseNum' :surveyee_caseNum})

    else:

        sef.save()
        return redirect('PSS:gr_start', surveyee_caseNum,survey)



def GR_view1(request, surveyee_caseNum, survey):
    time = SurveyTimes.objects.filter(caseNum=surveyee_caseNum).count()
    surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
    try:
        if (GR.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            return redirect('PSS:spr_start', surveyee_caseNum, survey)

        else:
            gr = GR(caseNum=surveyee, time=time,surveytime=survey,
                    GR1=request.POST['GR1'], GR2=request.POST['GR2'], GR3=request.POST['GR3'],
                    GR4=request.POST['GR4'],
                    GR5=request.POST['GR5'],
                    GR6=request.POST['GR6'], GR7=request.POST['GR7'], GR8=request.POST['GR8']
                      )
    except (KeyError, GR.DoesNotExist):
        return render(request, 'PSS/Survey/GR_tem.html', {'surveyee_caseNum': surveyee_caseNum})

    else:

        gr.save()
        return redirect('PSS:spr_start', surveyee_caseNum,survey)


def SPR_view1(request, surveyee_caseNum,survey):
    time = SurveyTimes.objects.filter(caseNum=surveyee_caseNum).count()
    surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
    try:
        if (SPR.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            return redirect('PSS:ssp_start', surveyee_caseNum, survey)

        else:
            spr = SPR(caseNum=surveyee, time=time,surveytime=survey,
                      SPR1=request.POST['SPR1'], SPR2=request.POST['SPR2'], SPR3=request.POST['SPR3'],
                      SPR4=request.POST['SPR4'],
                      SPR5=request.POST['SPR5'],
                      SPR6=request.POST['SPR6']
                      )
    except (KeyError, SPR.DoesNotExist):
        return render(request, 'PSS/Survey/SPR_tem.html', {'surveyee_caseNum': surveyee_caseNum})

    else:

        spr.save()
        return redirect('PSS:ssp_start', surveyee_caseNum, survey)



def SSP_view1(request, surveyee_caseNum,survey):
    time = SurveyTimes.objects.filter(caseNum=surveyee_caseNum).count()
    surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
    try:
        if (SSP.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            return redirect('PSS:f_start', surveyee_caseNum, survey)

        else:
            ssp = SSP(caseNum=surveyee, time=time,surveytime=survey,
                      SSP1=request.POST['SSP1'], SSP2=request.POST['SSP2'], SSP3=request.POST['SSP3'],
                      SSP4=request.POST['SSP4'],
                      SSP5=request.POST['SSP5'],
                      SSP6=request.POST['SSP6'], SSP7=request.POST['SSP7'], SSP8=request.POST['SSP8'], SSP9=request.POST['SSP9'],
                      SSP10=request.POST['SSP10'],
                      SSP11=request.POST['SSP11'], SSP12=request.POST['SSP12']
                      )
    except (KeyError, SSP.DoesNotExist):
        return render(request, 'PSS/Survey/SSP_tem.html', {'surveyee_caseNum': surveyee_caseNum})

    else:

        ssp.save()
        return redirect('PSS:f_start', surveyee_caseNum,survey)


def F_view1(request, surveyee_caseNum,survey):
    time = SurveyTimes.objects.filter(caseNum=surveyee_caseNum).count()
    surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
    try:
        if (F.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            return redirect('PSS:gd_start', surveyee_caseNum, survey)

        else:
            f = F(caseNum=surveyee, time=time,surveytime=survey,
                  F1=request.POST['F1'],F2=request.POST['F2'],F3=request.POST['F3'],F4=request.POST['F4'],F5=request.POST['F5'],
                  F6=request.POST['F6'], F7=request.POST['F7'], F8=request.POST['F8'], F9=request.POST['F9'],F10=request.POST['F10'],
                  F11=request.POST['F11'], F12=request.POST['F12'], F13=request.POST['F13'], F14=request.POST['F14'],
                  F15=request.POST['F15'],
                  F16=request.POST['F16'], F17=request.POST['F17'], F18=request.POST['F18']
                    )
    except(KeyError, F.DoesNotExist):
        return render(request, 'PSS/Survey/F_tem.html', {'surveyee_caseNum' :surveyee_caseNum})
    else:

        f.save()
        return redirect('PSS:gd_start', surveyee_caseNum,survey)



def GD_view1(request, surveyee_caseNum,survey):
    time = SurveyTimes.objects.filter(caseNum=surveyee_caseNum).count()
    surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
    try:
        if (GD.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            return redirect('PSS:hm_start', surveyee_caseNum, survey)

        else:
            gd = GD(caseNum=surveyee, time=time,surveytime=survey,
                    GD1=request.POST['GD1'], GD2=request.POST['GD2'], GD3=request.POST['GD3'],
                    GD4=request.POST['GD4'],
                    GD5=request.POST['GD5'],
                    GD6=request.POST['GD6']
                      )
    except (KeyError, GD.DoesNotExist):
        return render(request, 'PSS/Survey/GD_tem.html', {'surveyee_caseNum': surveyee_caseNum})

    else:

        gd.save()
        return redirect('PSS:hm_start', surveyee_caseNum,survey)


def HM_view1(request, surveyee_caseNum,survey):
    time = SurveyTimes.objects.filter(caseNum=surveyee_caseNum).count()
    surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
    try:
        if (HM.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            return redirect('PSS:health_start', surveyee_caseNum, survey)

        else:
            hm = HM(caseNum=surveyee, time=time,surveytime=survey,
                    HM1=request.POST['HM1'], HM2=request.POST['HM2'], HM3=request.POST['HM3'], HM4=request.POST['HM4'],
                    HM5=request.POST['HM5'],
                    HM6=request.POST['HM6'], HM7=request.POST['HM7'], HM8=request.POST['HM8'], HM9=request.POST['HM9'],
                    HM10=request.POST['HM10'],
                    HM11=request.POST['HM11'], HM12=request.POST['HM12'], HM13=request.POST['HM13'], HM14=request.POST['HM14'],
                    HM15=request.POST['HM15']
                  )
    except(KeyError, HM.DoesNotExist):
        return render(request, 'PSS/Survey/HM_tem.html', {'surveyee_caseNum': surveyee_caseNum})
    else:

        hm.save()
        return redirect('PSS:health_start', surveyee_caseNum,survey)



def HEALTH_view1(request, surveyee_caseNum,survey):
    time = SurveyTimes.objects.filter(caseNum=surveyee_caseNum).count()
    surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
    try:
        if (HEALTH.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            return redirect('PSS:dm_start', surveyee_caseNum, survey)

        else:
            health = HEALTH(caseNum=surveyee, time=time,surveytime=survey,
                            HEALTH1=request.POST['HEALTH1'], HEALTH2=request.POST['HEALTH2']
                  )
    except(KeyError, HEALTH.DoesNotExist):
        return render(request, 'PSS/Survey/HEALTH_tem.html', {'surveyee_caseNum': surveyee_caseNum})
    else:

        health.save()
        return redirect('PSS:dm_start',surveyee_caseNum,survey)



def DM_view1(request, surveyee_caseNum,survey):
    time = SurveyTimes.objects.filter(caseNum=surveyee_caseNum).count()
    surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
    try:
        if (DM.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            return redirect('PSS:thanks')

        else:
            dm = DM(caseNum=surveyee, time=time,surveytime=survey,
                    DM1=request.POST['DM1'],DM1_1_year=request.POST['DM1_1_year'],DM1_1_month=request.POST['DM1_1_month'],DM1_1_days=request.POST['DM1_1_days'],
                    DM1_2=request.POST['DM1_2'], DM1_3=request.POST['DM1_3'], DM1_4=request.POST['DM1_4'],
                    DM2=request.POST['DM2'], DM3=request.POST['DM3'], DM4=request.POST['DM4'],
                    DM5=request.POST['DM5'],
                    DM6=request.POST['DM6'], DM7=request.POST['DM7'], DM8=request.POST['DM8'], DM9=request.POST['DM9'], DM9_1=request.POST['DM9_1'],
                    DM10=request.POST['DM10'],
                     DM11_1=request.POST['DM11_1'],DM11_2=request.POST['DM11_2'],DM11_3=request.POST['DM11_4'],DM11_4=request.POST['DM11_4'],
                    DM12_1=request.POST['DM12_1'],DM12_3=request.POST['DM12_3'], DM13=request.POST['DM13'],
                    DM14=request.POST['DM14'],DM14_1=request.POST['DM14_1'],
                    DM15=request.POST['DM15'],DM16=request.POST['DM16'],DM17=request.POST['DM17'],DM18=request.POST['DM18'],DM19=request.POST['DM19']
                  )
    except(KeyError, HEALTH.DoesNotExist):
        return render(request, 'PSS/Survey/Dm_tem.html', {'surveyee_caseNum': surveyee_caseNum})
    else:

        dm.save()
        total_for_admin(surveyee_caseNum, survey, time, dm.id)
        return redirect('PSS:thanks')

def total_for_admin(surveyee_caseNum, survey, time, dm_id ):

    dm = DM.objects.get(id =dm_id)
    surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
    surveyTime = SurveyTimes.objects.get(caseNum=surveyee_caseNum, time=time)

    eb = EB.objects.get(caseNum=surveyee_caseNum, time=time, surveytime=survey)
    eh = EH.objects.get(caseNum=surveyee_caseNum, time=time, surveytime=survey)
    es = ES.objects.get(caseNum=surveyee_caseNum, time=time, surveytime=survey)
    exf = EXF.objects.get(caseNum=surveyee_caseNum, time=time, surveytime=survey)
    f = F.objects.get(caseNum=surveyee_caseNum, time=time, surveytime=survey)
    gd = GD.objects.get(caseNum=surveyee_caseNum, time=time, surveytime=survey)
    gr = GR.objects.get(caseNum=surveyee_caseNum, time=time, surveytime=survey)
    health = HEALTH.objects.get(caseNum=surveyee_caseNum, time=time, surveytime=survey)
    r = R.objects.get(caseNum=surveyee_caseNum, time=time, surveytime=survey)
    sef = SEF.objects.get(caseNum=surveyee_caseNum, time=time, surveytime=survey)
    spr = SPR.objects.get(caseNum=surveyee_caseNum, time=time, surveytime=survey)
    ssp = SSP.objects.get(caseNum=surveyee_caseNum, time=time, surveytime=survey)
    tip = Tip.objects.get(caseNum=surveyee_caseNum, time=time, surveytime=survey)
    dm = DM.objects.get(caseNum=surveyee_caseNum, time=time, surveytime=survey)

    health = round(float((eb.EB10 + eb.EB11+eb.EB12+eb.EB13)/4),6)
    community =  round(float((eb.EB15+eb.EB16+eb.EB17)/3),6)
    childcare = round(float((eb.EB6+eb.EB19+eb.EB18)/3),6)
    jobskills = round(float((eb.EB1+eb.EB2+eb.EB3+eb.EB4+eb.EB8)/5),6)
    softskill = round(float((eb.EB22+eb.EB23+eb.EB24+eb.EB25+eb.EB26)/5),6)
    peb_all = round(float((eb.EB10 + eb.EB11+eb.EB12+eb.EB13+eb.EB15+eb.EB16+eb.EB17+eb.EB6+eb.EB19+eb.EB18+
                           eb.EB1 + eb.EB2 + eb.EB3 + eb.EB4 + eb.EB8+eb.EB22+eb.EB23+eb.EB24+eb.EB25+eb.EB26)/20),6)

    empowerment =round(float((eh.EH3 + eh.EH4+eh.EH5+eh.EH6)/4),6)
    selfmotivation = round(float((eh.EH11 + eh.EH15) / 2), 6)
    skillresources = round(float((eh.EH17 + eh.EH18 + eh.EH19 + eh.EH20) / 4), 6)
    goalorientation = round(float((eh.EH21 + eh.EH22 + eh.EH23 + eh.EH24) / 4), 6)
    ehs_all = round(float((eh.EH3 + eh.EH4 + eh.EH5 + eh.EH6+eh.EH11 + eh.EH15+eh.EH17 + eh.EH18 + eh.EH19 + eh.EH20
                            +eh.EH21 + eh.EH22 + eh.EH23 + eh.EH24) / 14), 6)

    ess1 = round(float((es.ES2+es.ES8+es.ES9+es.ES10+es.ES12)/5),6)
    ess2 = round(float((es.ES1 + es.ES4 + es.ES13 + es.ES14) / 4), 6)
    ess3 = round(float((es.ES11 + es.ES7) / 2), 6)
    ess4 = round(float((es.ES3 + es.ES5 + es.ES6 ) / 3), 6)
    ess_all = round(float((es.ES2 + es.ES8 + es.ES9 + es.ES10 + es.ES12+es.ES1 + es.ES4 + es.ES13 + es.ES14
                           +es.ES11 + es.ES7+es.ES3 + es.ES5 + es.ES6 ) / 14), 6)
    pss = ehs_all-peb_all

    resilience =round(float((r.R1+r.R2)/2),6)
    self_efficacy = round(float((sef.SEF1+sef.SEF2+sef.SEF3+sef.SEF4+sef.SEF5+sef.SEF6+sef.SEF7+sef.SEF8)/8),6)
    gr_map={1:5, 2:4, 3:3,4:2, 5:1}
    gr_con = round(float((gr_map[gr.GR1]+gr_map[gr.GR3]+gr_map[gr.GR5]+gr_map[gr.GR6])/4),6)


    gr_per = round(float((gr.GR2+ gr.GR8+gr.GR4+ gr.GR7)/4),6)
    gr_all =round(float((gr_map[gr.GR1]+gr_map[gr.GR3]+gr_map[gr.GR5]+gr_map[gr.GR6]+gr.GR2+ gr.GR8+gr.GR4+ gr.GR7)/8),6)

    spr_map={0:10, 1:9, 2:8, 3:7,4:6, 5:5, 6:4, 7:3, 8:2, 9:1, 10:0}
    sprituallity = round(float((spr_map[spr.SPR2]+spr_map[spr.SPR5]+spr_map[spr.SPR6]+spr.SPR1+spr.SPR3+spr.SPR5)/6),6)

    f_map = { 1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}
    f_self = round(float((f.F1 + f_map[f.F2]+f.F3+f_map[f.F4]+f.F5+f_map[f.F6])/6),6)
    f_other = round(float((f.F8 + f_map[f.F7] + f.F10 + f_map[f.F9] + f.F12 + f_map[f.F11]) / 6), 6)
    f_situation = round(float((f.F14 + f_map[f.F13] + f.F16 + f_map[f.F15] + f.F18 + f_map[f.F17]) / 6), 6)
    f_all = round(float((f.F1 + f_map[f.F2]+f.F3+f_map[f.F4]+f.F5+f_map[f.F6]+f.F8 + f_map[f.F7] + f.F10
                         + f_map[f.F9] + f.F12 + f_map[f.F11]
                        +f.F14 + f_map[f.F13] + f.F16 + f_map[f.F15] + f.F18 + f_map[f.F17]) / 18), 6)


    total = Total_for_Admin(caseNum=surveyee, Agent=surveyee.agent_name, Time=time, Date=surveyTime.pub_Date,
                            Health=health, Community=community, Childcare=childcare, Jobskills=jobskills,
                            SoftSkill=softskill, Peb_all=peb_all,
                            Empowerment=empowerment,Selfmotivation=selfmotivation, SkilResources=skillresources,
                            GaolOrientation=goalorientation,Ehs_all=ehs_all,
                            Ess1=ess1, Ess2=ess2, Ess3=ess3, Ess4= ess4, Ess_all= ess_all,
                            PSS=pss, Resilience=resilience, Self_Efficacy=self_efficacy,
                            GR_Con=gr_con, GR_Per=gr_per, GR_all=gr_all, SPR_all=sprituallity,
                            F_self=f_self, F_other=f_other,F_situation=f_situation, F_all=f_all,
                            DM1=dm.DM1, DM1_1_year=dm.DM1_1_year,
                            DM1_1_month=dm.DM1_1_month,
                            DM1_1_days=dm.DM1_1_days,
                            DM1_2=dm.DM1_2, DM1_3=dm.DM1_3, DM1_4=dm.DM1_4,
                            DM2=dm.DM2, DM3=dm.DM3, DM4=dm.DM4,
                            DM5=dm.DM5,
                            DM6=dm.DM6, DM7=dm.DM7, DM8=dm.DM8, DM9=dm.DM9,
                            DM9_1=dm.DM9_1,
                            DM10=dm.DM10,
                            DM11_1=dm.DM11_1, DM11_2=dm.DM11_2, DM11_3=dm.DM11_3,
                            DM11_4=dm.DM11_4,
                            DM12_1=dm.DM12_1, DM12_3=dm.DM12_3, DM13=dm.DM13,
                            DM14=dm.DM14, DM14_1=dm.DM14_1,
                            DM15=dm.DM15, DM16=dm.DM16, DM17=dm.DM17, DM18=dm.DM18,
                            DM19=dm.DM19)

    total.save()
    surveyTime.doneSurvey = True
    surveyTime.readyToStart = False
    surveyTime.pub_Date = timezone.now()
    if time ==1:
        surveyee.survey1 = True
    elif time ==2:
        surveyee.survey2 = True
    elif time ==3:
        surveyee.survey3 = True
    elif time ==4:
        surveyee.survey4 = True
    surveyee.save()
    surveyTime.save()


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