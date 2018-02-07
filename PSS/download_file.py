import csv
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Surveyee, SurveyTimes,EB, EH, ES, Tip
from .models import EXF, R, SEF, GR, SPR,Total_for_Admin
from .models import SSP, F, GD,  HM, HEALTH, DM
from django_pandas.io import read_frame

from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
import pandas as pd
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


def join_dataFrames(df, dic):
    tem = pd.DataFrame(dic, index=[0])
    tem=tem.drop(['id', 'surveytime', 'time'], axis=1)
    df = df.join(tem.set_index('caseNum'), on='caseNum')
    return df

def adjust_column(df):
    print("===2====")
    print(df[['caseNum', 'cDate', 'Site',]])
    arrange = df[['caseNum', 'cDate', 'Site', 'time', 'EB1', 'EB2', 'EB3', 'EB4', 'EB5', 'EB6', 'EB7', 'EB8', 'EB9', 'EB10',
            'EB11', 'EB12', 'EB13', 'EB14', 'EB15', 'EB16', 'EB17', 'EB18', 'EB19', 'EB20', 'EB21', 'EB22', 'EB23',
            'EB24', 'EB25', 'EB26', 'EB27',
            'EH1', 'EH2', 'EH3', 'EH4', 'EH5', 'EH6', 'EH7', 'EH8', 'EH9', 'EH10', 'EH11', 'EH12', 'EH13', 'EH14',
            'EH15', 'EH16', 'EH17', 'EH18', 'EH19', 'EH20', 'EH21', 'EH22', 'EH23', 'EH24', 'TIP1', 'TIP2', 'TIP3', 'TIP4',
            'TIP5', 'TIP6', 'TIP7', 'TIP8', 'TIP9', 'TIP10', 'TIP11', 'TIP12', 'TIP13', 'TIP14', 'TIP15',
            'ES1', 'ES2', 'ES3', 'ES4', 'ES5', 'ES6', 'ES7', 'ES8', 'ES9', 'ES10', 'ES11', 'ES12', 'ES13', 'ES14', 'ES15',
            'A_3', 'B_3', 'C_3', 'D_3', 'E_2', 'F_2', 'G_1', 'H_3', 'I_2', 'J_3', 'K_1', 'K_2', 'K_3', 'L_1', 'L_2', 'L_3',
            'R1', 'R2',
            'SEF1', 'SEF2', 'SEF3', 'SEF4', 'SEF5', 'SEF6', 'SEF7', 'SEF8',
            'GR1', 'GR2', 'GR3', 'GR4', 'GR5', 'GR6', 'GR7', 'GR8',
            'SPR1', 'SPR2', 'SPR3', 'SPR4', 'SPR5', 'SPR6',
            'SSP1', 'SSP2', 'SSP3', 'SSP4', 'SSP5', 'SSP6', 'SSP7', 'SSP8', 'SSP9', 'SSP10', 'SSP11', 'SSP12',
            'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17',
            'F18', 'GD1', 'GD2', 'GD3', 'GD4', 'GD5', 'GD6',
            'HM1', 'HM2', 'HM3', 'HM4', 'HM5', 'HM6', 'HM7', 'HM8', 'HM9', 'HM10', 'HM11', 'HM12', 'HM13', 'HM14', 'HM15',
            'HEALTH1', 'HEALTH2', 'DM1',  'DM1_1_days', 'DM1_1_month', 'DM1_1_year', 'DM1_2', 'DM1_3', 'DM1_4', 'DM2', 'DM3',
            'DM4', 'DM5', 'DM6', 'DM7', 'DM8', 'DM9', 'DM9_1' , 'DM10', 'DM11_1', 'DM11_2', 'DM11_3', 'DM11_4', 'DM12_1',
            'DM12_3', 'DM13', 'DM14', 'DM14_1', 'DM15', 'DM16', 'DM17', 'DM18', 'DM19']]
    print("====3===")

    print(df[['caseNum', 'cDate', 'Site', ]])
    return arrange

def call_from_model(participant, time):

    eb = model_to_dict(EB.objects.get(caseNum=participant, time=time))

    eb_tem = pd.DataFrame(eb, index=[0])

    eh = model_to_dict(EH.objects.get(caseNum=participant, time=time))
    eb_tem = join_dataFrames(eb_tem, eh)
    es = model_to_dict(ES.objects.get(caseNum=participant, time=time))
    eb_tem = join_dataFrames(eb_tem, es)
    tip = model_to_dict(Tip.objects.get(caseNum=participant, time=time))
    eb_tem = join_dataFrames(eb_tem, tip)
    exf = model_to_dict(EXF.objects.get(caseNum=participant, time=time))
    eb_tem = join_dataFrames(eb_tem, exf)
    r = model_to_dict(R.objects.get(caseNum=participant, time=time))
    eb_tem = join_dataFrames(eb_tem, r)
    sef = model_to_dict(SEF.objects.get(caseNum=participant, time=time))
    eb_tem = join_dataFrames(eb_tem, sef)
    gr = model_to_dict(GR.objects.get(caseNum=participant, time=time))
    eb_tem = join_dataFrames(eb_tem, gr)
    spr = model_to_dict(SPR.objects.get(caseNum=participant, time=time))
    eb_tem = join_dataFrames(eb_tem, spr)
    ssp = model_to_dict(SSP.objects.get(caseNum=participant, time=time))
    eb_tem = join_dataFrames(eb_tem, ssp)
    f = model_to_dict(F.objects.get(caseNum=participant, time=time))
    eb_tem = join_dataFrames(eb_tem, f)
    gd = model_to_dict(GD.objects.get(caseNum=participant, time=time))
    eb_tem = join_dataFrames(eb_tem, gd)
    hm = model_to_dict(HM.objects.get(caseNum=participant, time=time))
    eb_tem = join_dataFrames(eb_tem, hm)
    health = model_to_dict(HEALTH.objects.get(caseNum=participant, time=time))
    eb_tem = join_dataFrames(eb_tem, health)
    dm = model_to_dict(DM.objects.get(caseNum=participant, time=time))
    eb_tem = join_dataFrames(eb_tem, dm)
    return eb_tem

def get_online_data(date):
    agent_map = {'CARA':1, 'HPOG-Gateway':2, 'HPOG-SouthLand':3, 'CHA':4, 'Inspiration':5, 'instituto-IDPL':6,

                 'MBC':7, 'Cara-CWF':9,  'GrowingHome':10,'CJC-CNH':11,  'CJC-Safer':12, 'CJC-SER':13,
                 14: 'HPOG2.0', 'GreaterWestTown':15,
                 'DuPagePads':16, 'HeartlandAlli':17,  'CTA':18,  'CentroRomero':19, 'St.Patricks-Mc':20, 'YeonSungUniv':23}


    online_survey = SurveyTimes.objects.filter(online=True,pub_Date=date, doneSurvey=True)
    temp_dataframe = pd.DataFrame()

    for i in online_survey:

        caseNumber = i.caseNum.caseNum
        time = i.time
        participant = Surveyee.objects.get(caseNum=caseNumber)
        tem=call_from_model(participant, time)
        tem['cDate'] =date
        tem['Site'] =agent_map[participant.agent_name]
        tem['time'] =time

        temp_dataframe=temp_dataframe.append(tem)

    temp = adjust_column(temp_dataframe)
    return temp


def show_online_survey_Date(request):

    try:
        online_survey = SurveyTimes.objects.filter(online= True, doneSurvey=True, readyToStart=False)
        survey_times = read_frame(online_survey)
        by_date = survey_times.groupby(survey_times['pub_Date'])
        download_list = list(by_date.groups.keys())

    except ObjectDoesNotExist:
        return redirect('PSS:thanks')

    return render(request, "PSS/Analysis/download.html", {"date_list":download_list})


def export_csv_date(request, date):

    data_list = get_online_data(date)
    #print(data_list)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(date)

    writer = csv.writer(response)
    writer.writerow(list(data_list))
    temp_list = data_list.values.tolist()

    for i in temp_list:
        writer.writerow(i)

    return response

