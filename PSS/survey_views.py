from django.shortcuts import render, redirect, HttpResponse
from .models import Surveyee, SurveyTimes, EB, EH, ES, Tip
from .models import EXF, R, SEF,  GR,  SPR, GENB
from .models import SSP, F,  GD,  HM,  HEALTH, DM,GENB,TIPI,K6
from django.core.urlresolvers import NoReverseMatch
import matplotlib
from django.utils import timezone
matplotlib.use("Agg")


def panic_view(reqest):
    return render(reqest, 'PSS/Survey/reverseError.html')


def EB_view1(request,surveyee_caseNum, survey):

    try:
        surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
        time = SurveyTimes.objects.get(caseNum=surveyee_caseNum, time=survey, readyToStart=True)
        if(EB.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            EB.objects.get(caseNum=surveyee, surveytime=survey).delete()


        eb = EB(caseNum=surveyee, time=time.time, surveytime=survey,
                EB1=request.POST['EB1'],EB2=request.POST['EB2'],EB3=request.POST['EB3'],EB4=request.POST['EB4'],EB5=request.POST['EB5'],
                EB6=request.POST['EB6'], EB7=request.POST['EB7'], EB8=request.POST['EB8'], EB9=request.POST['EB9'],EB10=request.POST['EB10'],
                EB11=request.POST['EB11'], EB12=request.POST['EB12'], EB13=request.POST['EB13'], EB14=request.POST['EB14'],
                EB15=request.POST['EB15'],
                EB16=request.POST['EB16'], EB17=request.POST['EB17'], EB18=request.POST['EB18'], EB19=request.POST['EB19'],
                EB20=request.POST['EB20'],
                EB21=request.POST['EB21'], EB22=request.POST['EB22'], EB23=request.POST['EB23'], EB24=request.POST['EB24'],
                EB25=request.POST['EB25'],
                EB26=request.POST['EB26'], EB27=request.POST['EB27'])
    except(KeyError, EB.DoesNotExist, NoReverseMatch) as E:
        return redirect('PSS:panic')
    else:
        eb.save()
        if surveyee.agent_name.username == 'HPOG2.0' or surveyee.agent_name.username == 'HPOG-Gateway':
            return redirect('PSS:genb_start', surveyee_caseNum, survey)

        return redirect('PSS:ehs_start', surveyee_caseNum, survey)


def EH_view1(request, surveyee_caseNum, survey):

    try:
        surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
        time = SurveyTimes.objects.get(caseNum=surveyee_caseNum, time=survey, readyToStart=True)
        if (EH.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            EH.objects.get(caseNum=surveyee, surveytime=survey).delete()
        if surveyee.agent_name.username == 'HPOG2.0' or surveyee.agent_name.username == 'HPOG-Gateway':
            eh = EH(caseNum=surveyee, time=time.time, surveytime=survey,
                    EH1=request.POST['EH1'], EH2=request.POST['EH2'], EH3=request.POST['EH3'], EH4=request.POST['EH4'],
                    EH5=request.POST['EH5'],
                    EH6=request.POST['EH6'], EH7=request.POST['EH7'], EH8=request.POST['EH8'], EH9=request.POST['EH9'],
                    EH10=request.POST['EH10'],
                    EH11=request.POST['EH11'], EH12=request.POST['EH12'], EH13=request.POST['EH13'],
                    EH14=request.POST['EH14'],
                    EH15=99,EH16=99, EH17=99, EH18=99,EH19=99, EH20=99,
                    EH21=99, EH22=99, EH23=99,EH24=99
                    )
        else:
            eh = EH(caseNum=surveyee, time=time.time, surveytime= survey,
                EH1=request.POST['EH1'],EH2=request.POST['EH2'],EH3=request.POST['EH3'],EH4=request.POST['EH4'],EH5=request.POST['EH5'],
                EH6=request.POST['EH6'], EH7=request.POST['EH7'], EH8=request.POST['EH8'], EH9=request.POST['EH9'],EH10=request.POST['EH10'],
                EH11=request.POST['EH11'], EH12=request.POST['EH12'], EH13=request.POST['EH13'], EH14=request.POST['EH14'],
                EH15=request.POST['EH15'],
                EH16=request.POST['EH16'], EH17=request.POST['EH17'], EH18=request.POST['EH18'], EH19=request.POST['EH19'],
                EH20=request.POST['EH20'],
                EH21=request.POST['EH21'], EH22=request.POST['EH22'], EH23=request.POST['EH23'], EH24=request.POST['EH24']
                    )
    except(KeyError, EH.DoesNotExist, NoReverseMatch) as E:
        return redirect('PSS:panic')
    else:
        eh.save()
        return redirect('PSS:tip_start', surveyee_caseNum, survey)



def ES_view1(request, surveyee_caseNum, survey):

    try:
        surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
        time = SurveyTimes.objects.get(caseNum=surveyee_caseNum, time=survey, readyToStart=True)
        if (ES.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            ES.objects.get(caseNum=surveyee, surveytime=survey).delete()



        es = ES(caseNum=surveyee, time= time.time,surveytime= survey,
                ES1=request.POST['ES1'], ES2=request.POST['ES2'], ES3=request.POST['ES3'], ES4=request.POST['ES4'],
                ES5=request.POST['ES5'],
                ES6=request.POST['ES6'], ES7=request.POST['ES7'], ES8=request.POST['ES8'], ES9=request.POST['ES9'],
                ES10=request.POST['ES10'],
                ES11=request.POST['ES11'], ES12=request.POST['ES12'], ES13=request.POST['ES13'],
                ES14=request.POST['ES14'],
                ES15=request.POST['ES15']
                    )
    except (KeyError, ES.DoesNotExist, NoReverseMatch):
        return redirect('PSS:panic')

    else:

        es.save()
        return redirect('PSS:exf_start', surveyee_caseNum, survey)


def Tip_view1(request, surveyee_caseNum, survey):

    try:
        surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
        time = SurveyTimes.objects.get(caseNum=surveyee_caseNum, time=survey, readyToStart=True)
        if (Tip.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            Tip.objects.get(caseNum=surveyee, surveytime=survey).delete()


        tip = Tip(caseNum=surveyee, time= time.time, surveytime=survey,
                TIP1=request.POST['TIP1'], TIP2=request.POST['TIP2'], TIP3=request.POST['TIP3'], TIP4=request.POST['TIP4'],
                TIP5=request.POST['TIP5'],
                TIP6=request.POST['TIP6'], TIP7=request.POST['TIP7'], TIP8=request.POST['TIP8'], TIP9=request.POST['TIP9'],
                  TIP10=request.POST['TIP10'],
                  TIP11=request.POST['TIP11'], TIP12=request.POST['TIP12'], TIP13=request.POST['TIP13'],
                  TIP14=request.POST['TIP14'],
                  TIP15=request.POST['TIP15']
                    )
    except (KeyError, ES.DoesNotExist, NoReverseMatch):
        return redirect('PSS:panic')

    else:

        tip.save()
        return redirect('PSS:ess_start', surveyee_caseNum, survey)



def EXF_view1(request, surveyee_caseNum, survey):

    try:
        surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
        time = SurveyTimes.objects.get(caseNum=surveyee_caseNum, time=survey, readyToStart=True)
        if (EXF.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            EXF.objects.get(caseNum=surveyee, surveytime=survey).delete()


        exf = EXF(caseNum=surveyee, time= time.time, surveytime=survey,
                  A_3=request.POST['A3'], B_3=request.POST['B3'], C_3=request.POST['C3'], D_3=request.POST['D3'],
                  E_2=request.POST['E2'],
                  F_2=request.POST['F2'], G_1=request.POST['G1'], H_3=request.POST['H3'], I_2=request.POST['I2'],
                  J_3=request.POST['J3'],
                  K_1=request.POST['K1'], K_2=request.POST['K2'], K_3=request.POST['K3'],
                  L_1=request.POST['L1'],
                  L_2=request.POST['L2'],L_3=request.POST['L3']
                )
    except (KeyError, EXF.DoesNotExist, NoReverseMatch):
        return redirect('PSS:panic')

    else:

        exf.save()
        return redirect('PSS:r_start', surveyee_caseNum, survey)



def R_view1(request, surveyee_caseNum, survey):

    try:
        surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
        time = SurveyTimes.objects.get(caseNum=surveyee_caseNum, time=survey, readyToStart=True)
        if (R.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            R.objects.get(caseNum=surveyee, surveytime=survey).delete()


        r = R(caseNum=surveyee, time=time.time, surveytime=survey,
                  R1=request.POST['R1'], R2=request.POST['R2']
                  )

    except (KeyError, R.DoesNotExist, NoReverseMatch):
        return redirect('PSS:panic')

    else:

        r.save()

        return redirect('PSS:sef_start', surveyee_caseNum,survey)



def SEF_view1(request, surveyee_caseNum,survey):

    try:
        surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
        time = SurveyTimes.objects.get(caseNum=surveyee_caseNum, time=survey, readyToStart=True)
        if (SEF.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            SEF.objects.get(caseNum=surveyee, surveytime=survey).delete()


        sef = SEF(caseNum=surveyee, time= time.time, surveytime=survey,
                  SEF1=request.POST['SEF1'], SEF2=request.POST['SEF2'], SEF3=request.POST['SEF3'], SEF4=request.POST['SEF4'],
                  SEF5=request.POST['SEF5'],
                  SEF6=request.POST['SEF6'], SEF7=request.POST['SEF7'], SEF8=request.POST['SEF8']
                )
    except (KeyError, SEF.DoesNotExist, NoReverseMatch):
        return redirect('PSS:panic')

    else:

        sef.save()
        return redirect('PSS:gr_start', surveyee_caseNum,survey)



def GR_view1(request, surveyee_caseNum, survey):

    try:
        surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
        time = SurveyTimes.objects.get(caseNum=surveyee_caseNum, time=survey, readyToStart=True)
        if (GR.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            GR.objects.get(caseNum=surveyee, surveytime=survey).delete()


        gr = GR(caseNum=surveyee, time=time.time,surveytime=survey,
                GR1=request.POST['GR1'], GR2=request.POST['GR2'], GR3=request.POST['GR3'],
                GR4=request.POST['GR4'],
                GR5=request.POST['GR5'],
                GR6=request.POST['GR6'], GR7=request.POST['GR7'], GR8=request.POST['GR8']
                  )
    except (KeyError, GR.DoesNotExist, NoReverseMatch):
        return redirect('PSS:panic')

    else:

        gr.save()
        if surveyee.agent_name.username == 'HPOG2.0' or surveyee.agent_name.username == 'HPOG-Gateway':
            return redirect('PSS:tipi_start', surveyee_caseNum,survey)
        return redirect('PSS:spr_start', surveyee_caseNum,survey)


def SPR_view1(request, surveyee_caseNum,survey):

    try:
        surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
        time = SurveyTimes.objects.get(caseNum=surveyee_caseNum, time=survey, readyToStart=True)
        if (SPR.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            SPR.objects.get(caseNum=surveyee, surveytime=survey).delete()


        spr = SPR(caseNum=surveyee, time=time.time,surveytime=survey,
                  SPR1=request.POST['SPR1'], SPR2=request.POST['SPR2'], SPR3=request.POST['SPR3'],
                  SPR4=request.POST['SPR4'],
                  SPR5=request.POST['SPR5'],
                  SPR6=request.POST['SPR6']
                  )
    except (KeyError, SPR.DoesNotExist, NoReverseMatch):
        return redirect('PSS:panic')

    else:

        spr.save()
        return redirect('PSS:ssp_start', surveyee_caseNum, survey)



def SSP_view1(request, surveyee_caseNum,survey):

    try:
        surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
        time = SurveyTimes.objects.get(caseNum=surveyee_caseNum, time=survey, readyToStart=True)
        if (SSP.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            SSP.objects.get(caseNum=surveyee, surveytime=survey).delete()


        ssp = SSP(caseNum=surveyee, time=time.time,surveytime=survey,
                  SSP1=request.POST['SSP1'], SSP2=request.POST['SSP2'], SSP3=request.POST['SSP3'],
                  SSP4=request.POST['SSP4'],
                  SSP5=request.POST['SSP5'],
                  SSP6=request.POST['SSP6'], SSP7=request.POST['SSP7'], SSP8=request.POST['SSP8'], SSP9=request.POST['SSP9'],
                  SSP10=request.POST['SSP10'],
                  SSP11=request.POST['SSP11'], SSP12=request.POST['SSP12']
                  )
    except (KeyError, SSP.DoesNotExist, NoReverseMatch):
        return redirect('PSS:panic')

    else:

        ssp.save()
        return redirect('PSS:f_start', surveyee_caseNum,survey)


def F_view1(request, surveyee_caseNum,survey):

    try:
        surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
        time = SurveyTimes.objects.get(caseNum=surveyee_caseNum, time=survey, readyToStart=True)
        if (F.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            F.objects.get(caseNum=surveyee, surveytime=survey).delete()


        f = F(caseNum=surveyee, time=time.time,surveytime=survey,
              F1=request.POST['F1'],F2=request.POST['F2'],F3=request.POST['F3'],F4=request.POST['F4'],F5=request.POST['F5'],
              F6=request.POST['F6'], F7=request.POST['F7'], F8=request.POST['F8'], F9=request.POST['F9'],F10=request.POST['F10'],
              F11=request.POST['F11'], F12=request.POST['F12'], F13=request.POST['F13'], F14=request.POST['F14'],
              F15=request.POST['F15'],
              F16=request.POST['F16'], F17=request.POST['F17'], F18=request.POST['F18']
                )
    except(KeyError, F.DoesNotExist, NoReverseMatch):
        return redirect('PSS:panic')
    else:

        f.save()
        return redirect('PSS:gd_start', surveyee_caseNum,survey)



def GD_view1(request, surveyee_caseNum,survey):

    try:
        surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
        time = SurveyTimes.objects.get(caseNum=surveyee_caseNum, time=survey, readyToStart=True)
        if (GD.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            GD.objects.get(caseNum=surveyee, surveytime=survey).delete()


        gd = GD(caseNum=surveyee, time=time.time,surveytime=survey,
                    GD1=request.POST['GD1'], GD2=request.POST['GD2'], GD3=request.POST['GD3'],
                    GD4=request.POST['GD4'],
                    GD5=request.POST['GD5'],
                    GD6=request.POST['GD6']
                      )
    except (KeyError, GD.DoesNotExist, NoReverseMatch):
        return redirect('PSS:panic')

    else:

        gd.save()
        return redirect('PSS:hm_start', surveyee_caseNum,survey)


def HM_view1(request, surveyee_caseNum,survey):

    try:
        surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
        time = SurveyTimes.objects.get(caseNum=surveyee_caseNum, time=survey, readyToStart=True)
        if (HM.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            HM.objects.get(caseNum=surveyee, surveytime=survey).delete()

        hm = HM(caseNum=surveyee, time=time.time,surveytime=survey,
                    HM1=request.POST['HM1'], HM2=request.POST['HM2'], HM3=request.POST['HM3'], HM4=request.POST['HM4'],
                    HM5=request.POST['HM5'],
                    HM6=request.POST['HM6'], HM7=request.POST['HM7'], HM8=request.POST['HM8'], HM9=request.POST['HM9'],
                    HM10=request.POST['HM10'],
                    HM11=request.POST['HM11'], HM12=request.POST['HM12'], HM13=request.POST['HM13'], HM14=request.POST['HM14'],
                    HM15=request.POST['HM15']
                  )
    except(KeyError, HM.DoesNotExist):
        return redirect('PSS:panic')
    else:

        hm.save()
        return redirect('PSS:health_start', surveyee_caseNum,survey)

def GENB_view1(request, surveyee_caseNum,survey):

    try:
        surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
        time = SurveyTimes.objects.get(caseNum=surveyee_caseNum, time=survey, readyToStart=True)
        if (GENB.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            GENB.objects.get(caseNum=surveyee, surveytime=survey).delete()

        genb = GENB(caseNum=surveyee, time=time.time,surveytime=survey,
                    GENB1=request.POST['GENB1'], GENB2=request.POST['GENB2'], GENB3=request.POST['GENB3'], GENB4=request.POST['GENB4'],

                  )
    except(KeyError, GENB.DoesNotExist):
        return redirect('PSS:panic')
    else:

        genb.save()
        return redirect('PSS:ehs_start', surveyee_caseNum,survey)


def TIPI_view1(request, surveyee_caseNum,survey):

    try:
        surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
        time = SurveyTimes.objects.get(caseNum=surveyee_caseNum, time=survey, readyToStart=True)
        if (TIPI.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            TIPI.objects.get(caseNum=surveyee, surveytime=survey).delete()

        tipi = TIPI(caseNum=surveyee, time=time.time,surveytime=survey,
                  TIPI1=request.POST['TIPI1'], TIPI2=request.POST['TIPI2'], TIPI3=request.POST['TIPI3'], TIPI4=request.POST['TIPI4'],
                  TIPI5=request.POST['TIPI5'],
                  TIPI6=request.POST['TIPI6'], TIPI7=request.POST['TIPI7'], TIPI8=request.POST['TIPI8'], TIPI9=request.POST['TIPI9'],
                  TIPI10=request.POST['TIPI10']
                  )
    except(KeyError, TIPI.DoesNotExist):
        return redirect('PSS:panic')
    else:

        tipi.save()
        return redirect('PSS:health_start', surveyee_caseNum,survey)

def K6_view1(request, surveyee_caseNum,survey):

    try:
        surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
        time = SurveyTimes.objects.get(caseNum=surveyee_caseNum, time=survey, readyToStart=True)
        if (K6.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            K6.objects.get(caseNum=surveyee, surveytime=survey).delete()

        k6 = K6(caseNum=surveyee, time=time.time,surveytime=survey,
                  Q1_a=request.POST['Q1_a'], Q1_b=request.POST['Q1_b'], Q1_c=request.POST['Q1_c'], Q1_d=request.POST['Q1_d'],
                Q1_e=request.POST['Q1_e'],
                Q1_f=request.POST['Q1_f'], Q2=request.POST['Q2'], Q3=request.POST['Q3'], Q4=request.POST['Q4'],
                Q5=request.POST['Q5'],Q6=request.POST['Q6']
                  )
    except(KeyError, K6.DoesNotExist):
        return redirect('PSS:panic')
    else:

        k6.save()
        return redirect('PSS:dm_start', surveyee_caseNum,survey)


def HEALTH_view1(request, surveyee_caseNum,survey):

    try:
        surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
        time = SurveyTimes.objects.get(caseNum=surveyee_caseNum, time=survey, readyToStart=True)
        if (HEALTH.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            HEALTH.objects.get(caseNum=surveyee, surveytime=survey).delete()


        health = HEALTH(caseNum=surveyee, time=time.time,surveytime=survey,
                            HEALTH1=request.POST['HEALTH1'], HEALTH2=request.POST['HEALTH2']
                  )
    except(KeyError, HEALTH.DoesNotExist, NoReverseMatch):
        return redirect('PSS:panic')
    else:

        health.save()
        if surveyee.agent_name.username == 'HPOG2.0' or surveyee.agent_name.username == 'HPOG-Gateway':
            return redirect('PSS:k6_start',surveyee_caseNum,survey)
        return redirect('PSS:dm_start',surveyee_caseNum,survey)



def DM_view1(request, surveyee_caseNum,survey):

    try:
        surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
        time = SurveyTimes.objects.get(caseNum=surveyee_caseNum, time=survey, readyToStart=True)

        if (DM.objects.filter(caseNum=surveyee, surveytime=survey).exists()):
            DM.objects.get(caseNum=surveyee, surveytime=survey).delete()


        dm = DM(caseNum=surveyee, time=time.time,surveytime=survey,
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
        surveyee.readyToStart = False
    except(KeyError, HEALTH.DoesNotExist, NoReverseMatch, SurveyTimes.DoesNotExist):
        return redirect('PSS:panic')
    else:
        time.online = True
        time.readyToStart = False
        time.doneSurvey = True
        time.pub_Date = timezone.localdate(timezone.now())
        time.save()
        dm.save()

        if time.time == 1:
            surveyee.survey1 = True
        elif time.time == 2:
            surveyee.survey2 = True
        elif time.time == 3:
            surveyee.survey3 = True
        elif time.time == 4:
            surveyee.survey4 = True
        surveyee.save()
        return redirect('PSS:thanks')



