from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Surveyee, SurveyTimes,EB, EH, EH_Question, ES_Question, ES, Tip_Question, Tip, EB_Question
from .models import EXF_Question,EXF, R, R_Question, SEF, SEF_Question, GR, GR_Question, SPR, SPR_Question,Total_for_Admin
from .models import SSP_Question, SSP, F, F_Question, GD, GD_Question, HM_Question, HM, HEALTH_Question, HEALTH, DM, DM_Question


def EB_view(request, surveyee_caseNum, survey):
    questions = EB_Question.objects.get(pk=1)
    choices = [ 1, 2, 3, 4, 5]
    return render(request, 'PSS/Survey/EB_tem1.html', {'surveyee_caseNum':surveyee_caseNum, 'questions':questions, 'choices':choices, "survey":survey})
def EH_view(request, surveyee_caseNum, survey):
    questions = EH_Question.objects.get(pk=1)
    choices =[0,1,2,3,4,5,6,7,8,9,10]

    return render(request, 'PSS/Survey/EH_tem.html', {'surveyee_caseNum':surveyee_caseNum, 'questions':questions, 'choices':choices, 'survey':survey})
def ES_view(request, surveyee_caseNum, survey):
    questions = ES_Question.objects.get(pk=1)
    choices = [ 1, 2, 3, 4, 5]
    return render(request, 'PSS/Survey/ES_tem.html', {'surveyee_caseNum':surveyee_caseNum, 'choices':choices, 'questions':questions, 'survey':survey})
def Tip_view(request, surveyee_caseNum, survey):
    questions = Tip_Question.objects.get(pk=1)
    choices = [ 1, 2, 3, 4, 5, 6, 7]
    return render(request, 'PSS/Survey/Tip_tem.html', {'surveyee_caseNum':surveyee_caseNum, 'choices':choices, 'questions':questions, 'survey':survey})
def EXF_view(request, surveyee_caseNum, survey):
    questions = EXF_Question.objects.get(pk=1)
    choices = [ 1, 2, 3, 4, 5, 6]
    return render(request, 'PSS/Survey/EXF_tem.html', {'surveyee_caseNum':surveyee_caseNum, 'choices':choices, 'questions':questions, 'survey':survey})
def R_SEF_GR_view(request, surveyee_caseNum, survey):
    R_questions = R_Question.objects.get(pk=1)
    R_choices = [0, 1, 2, 3, 4]

    SEF_questions = SEF_Question.objects.get(pk=1)
    SEF_choices = [ 1, 2, 3, 4, 5]

    GR_questions = GR_Question.objects.get(pk=1)
    GR_choices = [1, 2, 3, 4, 5]
    return render(request, 'PSS/Survey/R_SEF_GR_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'R_choices': R_choices, 'R_questions': R_questions,
                   'SEF_choices': SEF_choices, 'SEF_questions': SEF_questions,
                   'GR_choices': GR_choices, 'GR_questions': GR_questions,'survey': survey})
def R_view(request, surveyee_caseNum, survey):
    questions = R_Question.objects.get(pk=1)
    choices = [0, 1, 2, 3, 4]
    return render(request, 'PSS/Survey/R_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'choices': choices, 'questions': questions, 'survey':survey})
def SEF_view(request, surveyee_caseNum, survey):
    questions = SEF_Question.objects.get(pk=1)
    choices = [ 1, 2, 3, 4, 5]
    return render(request, 'PSS/Survey/SEF_tem.html', {'surveyee_caseNum':surveyee_caseNum, 'choices':choices, 'questions':questions, 'survey':survey})
def GR_view(request, surveyee_caseNum,survey):
    questions = GR_Question.objects.get(pk=1)
    choices = [1, 2, 3, 4, 5]
    return render(request, 'PSS/Survey/GR_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'choices': choices, 'questions': questions,'survey':survey})
def SPR_view(request, surveyee_caseNum,survey):
    questions = SPR_Question.objects.get(pk=1)
    choices = [0,1, 2, 3, 4, 5, 6, 7, 8, 9,10]
    return render(request, 'PSS/Survey/SPR_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'choices': choices, 'questions': questions,'survey':survey})
def SSP_view(request, surveyee_caseNum,survey):
    questions = SSP_Question.objects.get(pk=1)
    choices = [1, 2, 3, 4]
    return render(request, 'PSS/Survey/SSP_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'choices': choices, 'questions': questions,'survey':survey})
def F_view(request, surveyee_caseNum,survey):
    questions = F_Question.objects.get(pk=1)

    choices =[1,2,3,4,5,6,7]

    return render(request, 'PSS/Survey/F_tem.html', {'surveyee_caseNum':surveyee_caseNum, 'questions':questions, 'choices':choices, 'survey':survey})
def GD_view(request, surveyee_caseNum,survey):
    questions = GD_Question.objects.get(pk=1)
    choices = [1, 2, 3, 4, 5, 6, 7]
    return render(request, 'PSS/Survey/GD_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'choices': choices, 'questions': questions,'survey':survey})
def HM_view(request, surveyee_caseNum,survey):
    questions = HM_Question.objects.get(pk=1)

    choices = [1, 2, 3, 4, 5]

    return render(request, 'PSS/Survey/HM_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'questions': questions, 'choices': choices,'survey':survey})
def HEALTH_view(request, surveyee_caseNum,survey):
    questions = HEALTH_Question.objects.get(pk=1)

    choices = [1, 2, 3, 4, 5]

    return render(request, 'PSS/Survey/HEALTH_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'questions': questions, 'choices': choices,'survey':survey})
def DM_view(request, surveyee_caseNum,survey):
    questions = DM_Question.objects.get(pk=1)

    choices = [0,1]

    return render(request, 'PSS/Survey/Dm_tem.html',
                  {'surveyee_caseNum': surveyee_caseNum, 'questions': questions, 'choices': choices,'survey':survey})
