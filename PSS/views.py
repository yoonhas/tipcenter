from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from  django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.views import generic
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from .forms import CreateUserForm,EB_Form, EH_Form
from django.contrib.auth.models import User
from .models import Surveyee, SurveyTimes,EB, EH, EH_Question, ES_Question, ES, Tip_Question, Tip, EB_Question
from .models import EXF_Question,EXF, R, R_Question, SEF, SEF_Question, GR, GR_Question, SPR, SPR_Question
from .models import SSP_Question, SSP, F, F_Question, GD, GD_Question, HM_Question, HM, HEALTH_Question, HEALTH, DM, DM_Question
from django.utils import timezone

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'PSS/index.html'
    context_object_name = 'agent_list'
    def get_queryset(self):
        return User.objects.filter()


class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('create_user_done')


class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'

def Surveyee_detail_view(request, agent_id):
    agent= get_object_or_404(User,pk=agent_id)
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
                SurveyTimes.objects.get(pk=surveyTime.pk).delete()
                for i in checklist:
                    i.delete()
                return



def Surveytimes_view(request, surveyee_caseNum):

    try:
        survey_list = SurveyTimes.objects.filter(caseNum = surveyee_caseNum)


        for i in range(len(survey_list)):
            checking_Survey_Status(surveyee_caseNum, i+1)
        surveyee = Surveyee.objects.get(caseNum=surveyee_caseNum)
        survey_time_list = SurveyTimes.objects.filter(caseNum=surveyee_caseNum)

    except (KeyError, SurveyTimes.DoesNotExist):

        return render(request, 'PSS/times.html',{'surveyee_caseNum':surveyee_caseNum,
                                                 'error_message':"Let's Start the First Survey."})


    count = SurveyTimes.objects.filter(caseNum=surveyee_caseNum).count()
    survey = SurveyTimes(caseNum=surveyee, time=count + 1, pub_Date=timezone.now())
    survey.save()

    return render(request, 'PSS/times.html', {'surveyee_caseNum':surveyee_caseNum,
                                              'survey_time_list': survey_time_list, 'survey':survey.pk, 'count':count})

def EB_view(request, surveyee_caseNum, survey):
    questions = EB_Question.objects.get(pk=1)
    choices = [ 1, 2, 3, 4, 5]
    return render(request, 'PSS/EB_tem1.html', {'surveyee_caseNum':surveyee_caseNum, 'questions':questions,'choices':choices, "survey":survey})


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
        return render(request, 'PSS/EB_tem1.html', {'surveyee_caseNum' :surveyee_caseNum})
    else:
        eb.save()
        return redirect('PSS:ehs_start', surveyee_caseNum, survey)

def EH_view(request, surveyee_caseNum, survey):
    questions = EH_Question.objects.get(pk=1)
    choices =[0,1,2,3,4,5,6,7,8,9,10]

    return render(request, 'PSS/EH_tem.html', {'surveyee_caseNum':surveyee_caseNum, 'questions':questions, 'choices':choices, 'survey':survey})

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
        return render(request, 'PSS/EH_tem.html', {'surveyee_caseNum' :surveyee_caseNum})
    else:
        eh.save()
        return redirect('PSS:ess_start', surveyee_caseNum, survey)

def ES_view(request, surveyee_caseNum, survey):
    questions = ES_Question.objects.get(pk=1)
    choices = [ 1, 2, 3, 4, 5]
    return render(request, 'PSS/ES_tem.html', {'surveyee_caseNum':surveyee_caseNum, 'choices':choices, 'questions':questions, 'survey':survey})

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
        print(KeyError)
        return render(request, 'PSS/ES_tem.html', {'surveyee_caseNum' :surveyee_caseNum})

    else:

        es.save()
        return redirect('PSS:tip_start', surveyee_caseNum, survey)

def Tip_view(request, surveyee_caseNum, survey):
    questions = Tip_Question.objects.get(pk=1)
    choices = [ 1, 2, 3, 4, 5, 6, 7]
    return render(request, 'PSS/Tip_tem.html', {'surveyee_caseNum':surveyee_caseNum, 'choices':choices, 'questions':questions, 'survey':survey})

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
        return render(request, 'PSS/Tip_tem.html', {'surveyee_caseNum' :surveyee_caseNum})

    else:

        tip.save()
        return redirect('PSS:exf_start', surveyee_caseNum, survey)

def EXF_view(request, surveyee_caseNum, survey):
    questions = EXF_Question.objects.get(pk=1)
    choices = [ 1, 2, 3, 4, 5, 6]
    return render(request, 'PSS/EXF_tem.html', {'surveyee_caseNum':surveyee_caseNum, 'choices':choices, 'questions':questions, 'survey':survey})

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
        return render(request, 'PSS/EXF_tem.html', {'surveyee_caseNum' :surveyee_caseNum})

    else:

        exf.save()
        return redirect('PSS:r_start', surveyee_caseNum, survey)

def R_SEF_GR_view(request, surveyee_caseNum, survey):
    R_questions = R_Question.objects.get(pk=1)
    R_choices = [0, 1, 2, 3, 4]

    SEF_questions = SEF_Question.objects.get(pk=1)
    SEF_choices = [ 1, 2, 3, 4, 5]

    GR_questions = GR_Question.objects.get(pk=1)
    GR_choices = [1, 2, 3, 4, 5]
    return render(request, 'PSS/R_SEF_GR_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'R_choices': R_choices, 'R_questions': R_questions,
                   'SEF_choices': SEF_choices, 'SEF_questions': SEF_questions,
                   'GR_choices': GR_choices, 'GR_questions': GR_questions,'survey': survey})

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
        return render(request, 'PSS/R_SEF_GR_tem.html', {'surveyee_caseNum': surveyee_caseNum})

    else:

        r.save()
        sef.save()
        gr.save()
        return redirect('PSS:spr_start', surveyee_caseNum,survey)


def R_view(request, surveyee_caseNum, survey):
    questions = R_Question.objects.get(pk=1)
    choices = [0, 1, 2, 3, 4]
    return render(request, 'PSS/R_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'choices': choices, 'questions': questions, 'survey':survey})


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
        return render(request, 'PSS/sef_tem.html', {'surveyee_caseNum': surveyee_caseNum})

    else:

        r.save()

        return redirect('PSS:sef_start', surveyee_caseNum,survey)

def SEF_view(request, surveyee_caseNum, survey):
    questions = SEF_Question.objects.get(pk=1)
    choices = [ 1, 2, 3, 4, 5]
    return render(request, 'PSS/SEF_tem.html', {'surveyee_caseNum':surveyee_caseNum, 'choices':choices, 'questions':questions,'survey':survey})

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
        return render(request, 'PSS/SEF_tem.html', {'surveyee_caseNum' :surveyee_caseNum})

    else:

        sef.save()
        return redirect('PSS:gr_start', surveyee_caseNum,survey)


def GR_view(request, surveyee_caseNum,survey):
    questions = GR_Question.objects.get(pk=1)
    choices = [1, 2, 3, 4, 5]
    return render(request, 'PSS/GR_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'choices': choices, 'questions': questions,'survey':survey})


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
        return render(request, 'PSS/GR_tem.html', {'surveyee_caseNum': surveyee_caseNum})

    else:

        gr.save()
        return redirect('PSS:spr_start', surveyee_caseNum,survey)

def SPR_view(request, surveyee_caseNum,survey):
    questions = SPR_Question.objects.get(pk=1)
    choices = [0,1, 2, 3, 4, 5, 6, 7, 8, 9,10]
    return render(request, 'PSS/SPR_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'choices': choices, 'questions': questions,'survey':survey})


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
        return render(request, 'PSS/SPR_tem.html', {'surveyee_caseNum': surveyee_caseNum})

    else:

        spr.save()
        return redirect('PSS:ssp_start', surveyee_caseNum, survey)

def SSP_view(request, surveyee_caseNum,survey):
    questions = SSP_Question.objects.get(pk=1)
    choices = [1, 2, 3, 4]
    return render(request, 'PSS/SSP_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'choices': choices, 'questions': questions,'survey':survey})


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
        return render(request, 'PSS/SSP_tem.html', {'surveyee_caseNum': surveyee_caseNum})

    else:

        ssp.save()
        return redirect('PSS:f_start', surveyee_caseNum,survey)

def F_view(request, surveyee_caseNum,survey):
    questions = F_Question.objects.get(pk=1)

    choices =[1,2,3,4,5,6,7]

    return render(request, 'PSS/F_tem.html', {'surveyee_caseNum':surveyee_caseNum, 'questions':questions, 'choices':choices,'survey':survey})

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
        return render(request, 'PSS/F_tem.html', {'surveyee_caseNum' :surveyee_caseNum})
    else:

        f.save()
        return redirect('PSS:gd_start', surveyee_caseNum,survey)


def GD_view(request, surveyee_caseNum,survey):
    questions = GD_Question.objects.get(pk=1)
    choices = [1, 2, 3, 4, 5, 6, 7]
    return render(request, 'PSS/GD_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'choices': choices, 'questions': questions,'survey':survey})


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
        return render(request, 'PSS/GD_tem.html', {'surveyee_caseNum': surveyee_caseNum})

    else:

        gd.save()
        return redirect('PSS:hm_start', surveyee_caseNum,survey)


def HM_view(request, surveyee_caseNum,survey):
    questions = HM_Question.objects.get(pk=1)

    choices = [1, 2, 3, 4, 5]

    return render(request, 'PSS/HM_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'questions': questions, 'choices': choices,'survey':survey})


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
        return render(request, 'PSS/HM_tem.html', {'surveyee_caseNum': surveyee_caseNum})
    else:

        hm.save()
        return redirect('PSS:health_start', surveyee_caseNum,survey)

def HEALTH_view(request, surveyee_caseNum,survey):
    questions = HEALTH_Question.objects.get(pk=1)

    choices = [1, 2, 3, 4, 5]

    return render(request, 'PSS/HEALTH_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'questions': questions, 'choices': choices,'survey':survey})


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
        return render(request, 'PSS/HEALTH_tem.html', {'surveyee_caseNum': surveyee_caseNum})
    else:

        health.save()
        return redirect('PSS:dm_start',surveyee_caseNum,survey)

def DM_view(request, surveyee_caseNum,survey):
    questions = DM_Question.objects.get(pk=1)

    choices = [0,1]

    return render(request, 'PSS/DM_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'questions': questions, 'choices': choices,'survey':survey})

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
        return render(request, 'PSS/DM_tem.html', {'surveyee_caseNum': surveyee_caseNum})
    else:

        dm.save()
        return redirect('PSS:thanks')



def Thanks(request):
    return HttpResponse('Thank you')