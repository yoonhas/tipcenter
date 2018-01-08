from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Surveyee, Total_for_Admin

import pandas as pd
import logging
from django_pandas.io import read_frame
import matplotlib
matplotlib.use("Agg")

from . import graph_function as Graph


def helper(df, str):
    pd.set_option('precision', 6)
    mean = df[str].mean()
    count = df[str].count()
    min = df[str].min()
    max = df[str].max()
    std = df[str].std()
    desc = {'mean': mean, 'count': count, 'min': min, 'max': max, 'std': std}
    return desc


def describe(df, fact_list):
    data ={}
    for i in fact_list:
        data[i] = helper(df, i)
    return data


def z_score(df):

    df['Peb_all_Z'] = (df.Peb_all - df.Peb_all.mean()) / df.Peb_all.std(ddof=0)
    df['Ehs_all_Z'] = (df.Ehs_all - df.Ehs_all.mean()) / df.Ehs_all.std(ddof=0)
    df['Ess_all_Z'] = (df.Ess_all - df.Ess_all.mean()) / df.Ess_all.std(ddof=0)
    df['PSS_Z'] = (df.PSS - df.PSS.mean()) / df.PSS.std(ddof=0)
    return df


def full_z_score(df):
    df['Health_Z']= (df.Health - df.Health.mean()) / df.Health.std(ddof=0)
    df['Community_Z'] = (df.Community - df.Community.mean()) / df.Community.std(ddof=0)
    df['Childcare_Z'] = (df.Childcare - df.Childcare.mean()) / df.Childcare.std(ddof=0)
    df['Jobskills_Z'] = (df.Jobskills - df.Jobskills.mean()) / df.Jobskills.std(ddof=0)
    df['SoftSkill_Z'] = (df.SoftSkill - df.SoftSkill.mean()) / df.SoftSkill.std(ddof=0)
    df['Peb_all_Z'] = (df.Peb_all - df.Peb_all.mean()) / df.Peb_all.std(ddof=0)

    df['Empowerment_Z'] = (df.Empowerment - df.Empowerment.mean()) / df.Empowerment.std(ddof=0)
    df['Selfmotivation_Z'] = (df.Selfmotivation - df.Selfmotivation.mean()) / df.Selfmotivation.std(ddof=0)
    df['SkilResources_Z'] = (df.SkilResources - df.SkilResources.mean()) / df.SkilResources.std(ddof=0)
    df['GaolOrientation_Z'] = (df.GaolOrientation - df.GaolOrientation.mean()) / df.GaolOrientation.std(ddof=0)
    df['Ehs_all_Z'] = (df.Ehs_all - df.Ehs_all.mean()) / df.Ehs_all.std(ddof=0)

    df['Ess1_Z'] = (df.Ess1 - df.Ess1.mean()) / df.Ess1.std(ddof=0)
    df['Ess2_Z'] = (df.Ess2 - df.Ess2.mean()) / df.Ess2.std(ddof=0)
    df['Ess3_Z'] = (df.Ess3 - df.Ess3.mean()) / df.Ess3.std(ddof=0)
    df['Ess4_Z'] = (df.Ess4 - df.Ess4.mean()) / df.Ess4.std(ddof=0)
    df['Ess_all_Z'] = (df.Ess_all - df.Ess_all.mean()) / df.Ess_all.std(ddof=0)
    df['PSS_Z'] = (df.PSS - df.PSS.mean()) / df.PSS.std(ddof=0)
    return df


def summary(request, agent_id):

    all = Total_for_Admin.objects.all()
    df = read_frame(all)
    fact_list = ['Peb_all', 'Ehs_all', 'Ess_all', 'PSS']
    total = describe(df,fact_list)

    users = User.objects.filter()
    list1=[]
    for i in users:
        if i.get_username() != 'yoonhas':
            agent = read_frame(Total_for_Admin.objects.filter(Agent=i.pk))
            p=(i.get_username(),i.id, describe(agent, fact_list))
            list1.append(p)
    return render(request, "PSS/Analysis/summary.html", {'agent_id':User.objects.get(id=agent_id).get_username(),
                                                         'total':total, 'indi':list1})


def score_detail_agent(request, agent_id, userId):

    agent = User.objects.get(id=agent_id)
    i=1
    list1=[]
    list2=[]
    fact_list = ['Peb_all', 'Ehs_all', 'Ess_all', 'PSS', 'Peb_all_Z', 'Ehs_all_Z',
                 'Ess_all_Z', 'PSS_Z']
    while i != 5:
        pd.set_option('precision', 6)
        time_total = Total_for_Admin.objects.filter(Time=i)
        time_agent = Total_for_Admin.objects.filter(Time=i, Agent=agent)
        df1 = z_score(read_frame(time_total))
        df2 = z_score(read_frame(time_agent))
        list1.append((i, describe(df1, fact_list)))
        list2.append((i, describe(df2, fact_list)))
        i += 1

    html_fig = Graph.draw_graph_Agent(list1,list2)
    return render(request, "PSS/Analysis/summary_agent.html",
                  {'agent': agent.get_username(), 'detail_list': list2, 'html_fig': html_fig})


def score_detail(request, agent_id, userId):
    pd.set_option('precision', 6)
    agent = User.objects.get(id=agent_id)

    i = 1
    list1=[]
    if userId == '1':
        fact_list = ['Health', 'Community', 'Childcare', 'Jobskills', 'SoftSkill', 'Peb_all',
                     'Empowerment', 'Selfmotivation', 'SkilResources', 'GaolOrientation', 'Ehs_all',
                     'Ess1', 'Ess2', 'Ess3', 'Ess4', 'Ess_all', 'PSS', 'Health_Z', 'Community_Z', 'Childcare_Z',
                     'Jobskills_Z', 'SoftSkill_Z', 'Peb_all_Z',
                     'Empowerment_Z', 'Selfmotivation_Z', 'SkilResources_Z', 'GaolOrientation_Z', 'Ehs_all_Z',
                     'Ess1_Z', 'Ess2_Z', 'Ess3_Z', 'Ess4_Z', 'Ess_all_Z', 'PSS_Z']
    else:
        fact_list = ['Peb_all',
                     'Ehs_all',
                     'Ess_all', 'PSS', 'Peb_all_Z',
                     'Ehs_all_Z',
                     'Ess_all_Z', 'PSS_Z']

    if agent_id == '1':

        while i != 5:
            pd.set_option('precision', 6)
            time = Total_for_Admin.objects.filter(Time=i)
            df = full_z_score(read_frame(time))
            print(df[df['Health']<1])
            list1.append((i, describe(df,fact_list)))
            i += 1
    else:

        while i != 5:
            pd.set_option('precision', 6)
            time = Total_for_Admin.objects.filter(Time=i, Agent=agent)
            df=full_z_score(read_frame(time))
            list1.append((i, describe(df,fact_list)))
            i += 1

    html_fig = Graph.draw_graph(list1, userId)
    return render(request, "PSS/Analysis/score_detail.html", {'agent':agent.get_username(), 'detail_list':list1, 'html_fig':html_fig})


def compare_view(request):
    agents = User.objects.all()
    surveyee = []
    for i in agents:
        tem_survey = Surveyee.objects.filter(agent_name=i)
        surveyee.append(tem_survey)
    return render(request, 'PSS/Analysis/compare.html', {'agents':agents, 'surveyee':surveyee})


def compare_detail(request):


    def maskfunction( rawData, employ, welfare, race, marital, education, housing, age, born,gender,date):

        if sum(list(map(int,race))) != -1:
            mask = (rawData['DM14'].isin(race))
            rawData =rawData[mask]

        if employ!= 77:
            mask = (rawData['DM1'] == employ)
            rawData =rawData[mask]
        if welfare!= 77:
            mask = (rawData['DM7'] == welfare)
            rawData =rawData[mask]
        if sum(list(map(int,marital)))!= -1:
            mask = (rawData['DM8'].isin(marital))
            rawData =rawData[mask]
        if sum(list(map(int,education)))!= -1:
            mask = (rawData['DM16'].isin(education))
            rawData =rawData[mask]
        if sum(list(map(int,housing)))!= -1:
            mask = (rawData['DM9'].isin(housing))
            rawData =rawData[mask]
        if gender!= 77:
            mask = (rawData['DM13'] == gender)
            rawData =rawData[mask]

        if '-' in born:
            borns = list(born.split('-'))
            begin= borns[0]
            end= borns[1]
            bornMask = (rawData['DM12_3']>=int(begin))&(rawData['DM12_3']<=int(end))
            rawData = rawData[bornMask]
        elif born == '0':
            born =0
        else:
            borns=int(born)
            bornMask =(rawData['DM12_3']==borns)
            rawData = rawData[bornMask]

        if '-' in age:
            ages = list(age.split('-'))
            beginAge= ages[0]
            endAge= ages[1]
            ageMask = (rawData['DM12_1']>=int(beginAge))&(rawData['DM12_1']<=int(endAge))
            rawData = rawData[ageMask]
        elif age == '0':
            age =0
        else:
            ages=int(age)
            ageMask =(rawData['DM12_1']==ages)
            rawData = rawData[ageMask]

        if '-' in date:
            dates = list(date.split('-'))
            begin= pd.datetime.strptime(dates[0], '%Y.%m.%d')
            end= pd.datetime.strptime(dates[1], '%Y.%m.%d')
            dateMask = (rawData['cDATE']>=begin)&(rawData['cDATE']<=end)
            rawData = rawData[dateMask]
        elif date == '0':
            dates =0
        else:
            date=pd.datetime.strptime(date, '%Y.%m.%d')
            dateMask =(rawData['cDATE']==date)
            rawData = rawData[dateMask]

        return rawData


    fact_list = ['Health', 'Community', 'Childcare', 'Jobskills', 'SoftSkill', 'Peb_all',
                 'Empowerment', 'Selfmotivation', 'SkilResources', 'GaolOrientation', 'Ehs_all',
                 'Ess1', 'Ess2', 'Ess3', 'Ess4', 'Ess_all', 'PSS']
    users = get_user_model()

    compare = request.POST.getlist('compare')

    factors = request.POST['factors']

    employ = int(request.POST['employ'])
    welfare =int(request.POST['welfare'])
    race = request.POST.getlist('race')
    marital = request.POST.getlist('marital')
    education = request.POST.getlist('education')
    housing = request.POST.getlist('Housing')
    age = request.POST['age']
    born = request.POST['year']
    gender = int(request.POST['gender'])
    date = request.POST['date']
    case = request.POST['indi_case']


    if case != '-1':
        checking =1
        surveyee = Surveyee.objects.get(caseNum=case)
        individual = read_frame( Total_for_Admin.objects.filter(caseNum=surveyee))
        indi_z = full_z_score(individual)
    else:
        checking =0

    total =maskfunction(read_frame(Total_for_Admin.objects.all()), employ, welfare, race, marital, education, housing, age, born,gender,date)
    total_mask = full_z_score(total)

    agent_filtered ={}
    for key in compare:
        if key == '1':
            tem_list =[]
            agent_filtered['Total'] = total_mask
        else:
            agentObj = users.objects.get(id=key)
            agent_filtered[agentObj.username] = total_mask[(total_mask['Agent'] == agentObj.username)]

    new = {}
    frame_for_graph = pd.DataFrame([])

    for key, values in agent_filtered.items():

        if key != 'yoonhas':

            temp = values.groupby(values['Time'])
            frame_for_graph[key]=temp[factors+"_Z"].mean()

            new[key]={}
            new[key]['Mean'] = [x for x in temp[factors ].mean()]
            new[key]['Count'] = [x for x in temp[factors ].count()]
            new[key]['Min'] = [x for x in temp[factors ].min()]
            new[key]['Max'] = [x for x in temp[factors ].max()]
            new[key]['Std'] = [x for x in temp[factors ].std()]

    if checking == 1:
        frame_for_graph[case]=""
        temp1= indi_z.groupby(indi_z['Time'])
        frame_for_graph[case] = temp1[factors+"_Z"].mean()
        print("+++++++++++++")
        new[case]={}
        new[case]['Mean'] =[x for x in temp1[factors ].mean()]
        new[case]['Count'] =[x for x in temp1[factors ].count()]
        new[case]['Min'] = [x for x in temp1[factors ].min()]
        new[case]['Max'] = [x for x in temp1[factors ].max()]
        new[case]['Std'] = 0
        print(new)
    html_fig=Graph.draw_graph_Admin_compare(frame_for_graph)
    return render(request, 'PSS/Analysis/compare_admin_show.html', {'detail_list':new,"html_fig":html_fig, 'key_list':agent_filtered.keys()})


def compare_agent(request, agent_id):
    users = get_user_model()
    agent = users.objects.get(id= agent_id)
    surveylist = Surveyee.objects.filter(agent_name_id= agent_id)
    return render(request, 'PSS/Analysis/compare_agent.html', {'surveylist': surveylist})


def show_compare_agent(request,agent_id):

    def maskfunction(raw_data,races,age,gender,education):

        if races != 77:
            mask = (raw_data['DM14'] == races)
            raw_data =raw_data[mask]


        if '-' in age:
            ages = list(age.split('-'))
            beginAge= ages[0]
            endAge= ages[1]
            ageMask = (raw_data['DM12_1']>=int(beginAge))&(raw_data['DM12_1']<=int(endAge))
            raw_data = raw_data[ageMask]
        elif age == '0':
            age =0
        else:
            ages=int(age)
            ageMask =(raw_data['DM12_1']==ages)
            raw_data = raw_data[ageMask]


        if gender != 77:

            genderMask =(raw_data['DM13']==gender)
            raw_data = raw_data[genderMask]

        if education != 77:
            educationMask =(raw_data['DM16']==education)
            raw_data = raw_data[educationMask]

        return raw_data

    races = int(request.POST['race'])
    age = request.POST['age']
    gender = int(request.POST['gender'])
    education = int(request.POST['education'])
    case = int(request.POST['caseNum'])
    users = get_user_model()
    agent = users.objects.get(id=agent_id)

    if case != -1:
        checking =1
        surveyee = Surveyee.objects.get(caseNum=case)
        individual = Total_for_Admin.objects.filter(caseNum=surveyee)
    else:
        checking =0

    fact_list = ['Peb_all', 'Ehs_all', 'Ess_all', 'PSS', 'Peb_all_Z', 'Ehs_all_Z',
                 'Ess_all_Z', 'PSS_Z']
    i = 1
    list1 = []
    list2 = []
    while i != 5:
        pd.set_option('precision', 6)
        time_total = Total_for_Admin.objects.filter(Time=i)
        time_agent = Total_for_Admin.objects.filter(Time=i, Agent=agent)
        total_mask = maskfunction(read_frame(time_total), races,age, gender, education)
        agent_mask = maskfunction(read_frame(time_agent), races,age, gender, education)
        df1 = z_score(total_mask)
        df2 = z_score(agent_mask)
        list1.append((i, describe(df1,fact_list)))
        list2.append((i, describe(df2,fact_list)))
        i += 1


    if checking == 1:
        indi = read_frame(individual)
        html_fig = Graph.draw_graph_Agent_compare(list1, list2,indi )
    else:
        html_fig = Graph.draw_graph_Agent(list1, list2 )

    return render(request, 'PSS/Analysis/compare_agent_show.html', {'agent': agent.get_username(), 'detail_list': list2, 'html_fig': html_fig})



def show_graph(request):
    return