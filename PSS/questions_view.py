from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Surveyee, SurveyTimes,EB, EH, EH_Question, ES_Question, ES, Tip_Question, Tip, EB_Question
from .models import EXF_Question,EXF, R, R_Question, SEF, SEF_Question, GR, GR_Question, SPR, SPR_Question,Total_for_Admin
from .models import SSP_Question, SSP, F, F_Question, GD, GD_Question, HM_Question, HM, HEALTH_Question, HEALTH, DM, DM_Question


def EB_view(request, surveyee_caseNum, survey):
    if "Korean" in request.POST:
        print("Korean")
        casenum= Surveyee.objects.get(caseNum=surveyee_caseNum)
        casenum.survey_kind = 2
        casenum.save()
    else:
        casenum= Surveyee.objects.get(caseNum=surveyee_caseNum)
        print("English")
        casenum.survey_kind = 1
        casenum.save()
    questions = EB_Question.objects.get(pk=casenum.survey_kind)
    choices = [ 1, 2, 3, 4, 5]
    print(casenum.survey_kind)
    return render(request, 'PSS/Survey/EB_tem1.html', {'surveyee_caseNum':surveyee_caseNum, 'questions':questions,
                                                       'choices':choices, "survey":survey, "version":casenum.survey_kind })
def EH_view(request, surveyee_caseNum, survey):
    casenum = Surveyee.objects.get(caseNum=surveyee_caseNum)
    questions = EH_Question.objects.get(pk=casenum.survey_kind)
    choices =[0,1,2,3,4,5,6,7,8,9,10]

    return render(request, 'PSS/Survey/EH_tem.html', {'surveyee_caseNum':surveyee_caseNum, 'questions':questions,
                                                      'choices':choices, 'survey':survey, "version":casenum.survey_kind})
def ES_view(request, surveyee_caseNum, survey):
    casenum = Surveyee.objects.get(caseNum=surveyee_caseNum)
    questions = ES_Question.objects.get(pk=casenum.survey_kind)
    choices = [ 1, 2, 3, 4, 5]
    return render(request, 'PSS/Survey/ES_tem.html', {'surveyee_caseNum':surveyee_caseNum, 'choices':choices,
                                                      'questions':questions, 'survey':survey, "version":casenum.survey_kind})
def Tip_view(request, surveyee_caseNum, survey):
    casenum = Surveyee.objects.get(caseNum=surveyee_caseNum)
    questions = Tip_Question.objects.get(pk=casenum.survey_kind)
    choices = [ 1, 2, 3, 4, 5, 6, 7]
    return render(request, 'PSS/Survey/Tip_tem.html', {'surveyee_caseNum':surveyee_caseNum, 'choices':choices,
                                                       'questions':questions, 'survey':survey, "version":casenum.survey_kind})
def EXF_view(request, surveyee_caseNum, survey):
    casenum = Surveyee.objects.get(caseNum=surveyee_caseNum)
    questions = EXF_Question.objects.get(pk=casenum.survey_kind)
    choices = [ 1, 2, 3, 4, 5, 6]
    return render(request, 'PSS/Survey/EXF_tem.html', {'surveyee_caseNum':surveyee_caseNum, 'choices':choices,
                                                       'questions':questions, 'survey':survey, "version":casenum.survey_kind})
def R_SEF_GR_view(request, surveyee_caseNum, survey):
    casenum = Surveyee.objects.get(caseNum=surveyee_caseNum)
    R_questions = R_Question.objects.get(pk=casenum.survey_kind)
    R_choices = [0, 1, 2, 3, 4]

    SEF_questions = SEF_Question.objects.get(pk=casenum.survey_kind)
    SEF_choices = [ 1, 2, 3, 4, 5]

    GR_questions = GR_Question.objects.get(pk=casenum.survey_kind)
    GR_choices = [1, 2, 3, 4, 5]
    return render(request, 'PSS/Survey/R_SEF_GR_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'R_choices': R_choices, 'R_questions': R_questions,
                   'SEF_choices': SEF_choices, 'SEF_questions': SEF_questions,
                   'GR_choices': GR_choices, 'GR_questions': GR_questions,'survey': survey})
def R_view(request, surveyee_caseNum, survey):
    casenum = Surveyee.objects.get(caseNum=surveyee_caseNum)
    questions = R_Question.objects.get(pk=casenum.survey_kind)
    choices = [0, 1, 2, 3, 4]
    return render(request, 'PSS/Survey/R_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'choices': choices, 'questions': questions, 'survey':survey, "version":casenum.survey_kind})
def SEF_view(request, surveyee_caseNum, survey):
    casenum = Surveyee.objects.get(caseNum=surveyee_caseNum)
    questions = SEF_Question.objects.get(pk=casenum.survey_kind)
    choices = [ 1, 2, 3, 4, 5]
    return render(request, 'PSS/Survey/SEF_tem.html', {'surveyee_caseNum':surveyee_caseNum, 'choices':choices,
                                                       'questions':questions, 'survey':survey, "version":casenum.survey_kind})
def GR_view(request, surveyee_caseNum,survey):
    casenum = Surveyee.objects.get(caseNum=surveyee_caseNum)
    questions = GR_Question.objects.get(pk=casenum.survey_kind)
    choices = [1, 2, 3, 4, 5]
    return render(request, 'PSS/Survey/GR_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'choices': choices, 'questions': questions,'survey':survey, "version":casenum.survey_kind})
def SPR_view(request, surveyee_caseNum,survey):
    casenum = Surveyee.objects.get(caseNum=surveyee_caseNum)
    questions = SPR_Question.objects.get(pk=casenum.survey_kind)
    choices = [0,1, 2, 3, 4, 5, 6, 7, 8, 9,10]
    return render(request, 'PSS/Survey/SPR_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'choices': choices, 'questions': questions,'survey':survey, "version":casenum.survey_kind})
def SSP_view(request, surveyee_caseNum,survey):
    casenum = Surveyee.objects.get(caseNum=surveyee_caseNum)
    questions = SSP_Question.objects.get(pk=casenum.survey_kind)
    choices = [1, 2, 3, 4]
    return render(request, 'PSS/Survey/SSP_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'choices': choices, 'questions': questions,'survey':survey, "version":casenum.survey_kind})
def F_view(request, surveyee_caseNum,survey):
    casenum = Surveyee.objects.get(caseNum=surveyee_caseNum)
    questions = F_Question.objects.get(pk=casenum.survey_kind)

    choices =[1,2,3,4,5,6,7]

    return render(request, 'PSS/Survey/F_tem.html', {'surveyee_caseNum':surveyee_caseNum, 'questions':questions,
                                                     'choices':choices, 'survey':survey, "version":casenum.survey_kind})
def GD_view(request, surveyee_caseNum,survey):
    casenum = Surveyee.objects.get(caseNum=surveyee_caseNum)
    questions = GD_Question.objects.get(pk=casenum.survey_kind)
    choices = [1, 2, 3, 4, 5, 6, 7]
    return render(request, 'PSS/Survey/GD_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'choices': choices, 'questions': questions,'survey':survey, "version":casenum.survey_kind})
def HM_view(request, surveyee_caseNum,survey):
    casenum = Surveyee.objects.get(caseNum=surveyee_caseNum)
    questions = HM_Question.objects.get(pk=casenum.survey_kind)

    choices = [1, 2, 3, 4, 5]

    return render(request, 'PSS/Survey/HM_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'questions': questions, 'choices': choices,'survey':survey, "version":casenum.survey_kind})
def HEALTH_view(request, surveyee_caseNum,survey):
    casenum = Surveyee.objects.get(caseNum=surveyee_caseNum)
    questions = HEALTH_Question.objects.get(pk=casenum.survey_kind)

    choices = [1, 2, 3, 4, 5]

    return render(request, 'PSS/Survey/HEALTH_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'questions': questions, 'choices': choices,'survey':survey, "version":casenum.survey_kind})
def DM_view(request, surveyee_caseNum,survey):
    casenum = Surveyee.objects.get(caseNum=surveyee_caseNum)
    questions = DM_Question.objects.get(pk=casenum.survey_kind)

    choices = [0,1]
    if casenum.survey_kind != 1:
        return render(request, 'PSS/Survey/Dm_tem_kor.html',
                      {'surveyee_caseNum': surveyee_caseNum, 'questions': questions, 'choices': choices,
                       'survey': survey, "version": casenum.survey_kind})

    return render(request, 'PSS/Survey/Dm_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'questions': questions, 'choices': choices,'survey':survey, "version":casenum.survey_kind})
