from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Surveyee, Total_for_Admin
import numpy as np
import pandas as pd
import logging
from django_pandas.io import read_frame
import matplotlib
matplotlib.use("Agg")

from . import graph_function as Graph


def helper(df, str):
    pd.set_option('precision', 6)
    mean = df[str].mean()
    #mean = np.nanmean(df[str],axis=0)
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
        if i.get_username() != 'yoonhas' or i.get_username() != 'admin' or i.get_username() != 'Cross':
            agent = read_frame(Total_for_Admin.objects.filter(Agent=i.pk))
            p=(i.get_username(),i.id, describe(agent, fact_list))
            list1.append(p)

    if agent_id == '1' or agent_id == '27' or agent_id == '26':
        return render(request, "PSS/Analysis/summary.html", {'agent_id': User.objects.get(id=agent_id).get_username(), 'total': total, 'indi': list1})


    return render(request, "PSS/Analysis/summary.html", {'agent_id':User.objects.get(id=agent_id).get_username(),
                                                          'indi':list1})


def selection_index(request):
    return render(request, "PSS/Analysis/selection_index.html")

def score_detail_agent(request, agent_id):

    agent = User.objects.get(username=agent_id)
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


def score_detail(request, agent_id):
    pd.set_option('precision', 6)
    agent = User.objects.get(id=agent_id)

    i = 1
    list1=[]

    fact_list = ['Health', 'Community', 'Childcare', 'Jobskills', 'SoftSkill', 'Peb_all',
                 'Empowerment', 'Selfmotivation', 'SkilResources', 'GaolOrientation', 'Ehs_all',
                 'Ess1', 'Ess2', 'Ess3', 'Ess4', 'Ess_all', 'PSS']


    if agent_id == '1' or agent_id == '27' or agent_id == '26':

        while i != 5:
            pd.set_option('precision', 6)
            time = Total_for_Admin.objects.filter(Time=i)
            df = read_frame(time)
            list1.append((i, describe(df,fact_list)))
            i += 1
    else:

        while i != 5:
            pd.set_option('precision', 6)
            time = Total_for_Admin.objects.filter(Time=i, Agent=agent)
            df=read_frame(time)
            list1.append((i, describe(df,fact_list)))
            i += 1

    html_fig = Graph.draw_graph(list1, agent_id)
    return render(request, "PSS/Analysis/score_detail.html", {'agent':agent.get_username(), 'detail_list':list1, 'html_fig':html_fig})


def compare_view(request):
    agents = User.objects.all()
    surveyee = []
    for i in agents:
        tem_survey = Surveyee.objects.filter(agent_name=i)
        surveyee.append(tem_survey)
    return render(request, 'PSS/Analysis/compare.html', {'agents':agents, 'surveyee':surveyee})

def compare_indi_view(request):
    agents = User.objects.all()
    surveyee = []
    for i in agents:
        tem_survey = Surveyee.objects.filter(agent_name=i)
        surveyee.append(tem_survey)
    return render(request, 'PSS/Analysis/compare_indivisual.html', {'agents':agents, 'surveyee':surveyee})

def maskfunction( rawData, employ, welfare, race, marital, education, housing, age, income, gender,date):

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

    if '-' in income:
        incomes = list(income.split('-'))
        begin= incomes[0]
        end= incomes[1]
        incomeMask = (rawData['DM6']>=int(begin))&(rawData['DM6']<=int(end))
        rawData = rawData[incomeMask]
    elif income == '0':
        income =0
    else:
        incomes=int(income)
        incomeMask =(rawData['DM6']==incomes)
        rawData = rawData[incomeMask]

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

def iterate_dictionary(agent_filtered, new,frame_for_graph, factors):
    for key, values in agent_filtered.items():

        if key != 'yoonhas':
            if factors == 'Default':
                new[key + '_PEB_all'] = {}
                new[key + '_EHS_all'] = {}
                new[key + '_ESS_all'] = {}
                new[key + '_PSS_all'] = {}
                new[key + '_PEB_all']['Mean'] = {}
                new[key + '_PEB_all']['Count'] = {}
                new[key + '_PEB_all']['Min'] = {}
                new[key + '_PEB_all']['Max'] = {}
                new[key + '_PEB_all']['Std'] = {}
                new[key + '_EHS_all']['Mean'] = {}
                new[key + '_EHS_all']['Count'] = {}
                new[key + '_EHS_all']['Min'] = {}
                new[key + '_EHS_all']['Max'] = {}
                new[key + '_EHS_all']['Std'] = {}
                new[key + '_ESS_all']['Mean'] = {}
                new[key + '_ESS_all']['Count'] = {}
                new[key + '_ESS_all']['Min'] = {}
                new[key + '_ESS_all']['Max'] = {}
                new[key + '_ESS_all']['Std'] = {}
                new[key + '_PSS_all']['Mean'] = {}
                new[key + '_PSS_all']['Count'] = {}
                new[key + '_PSS_all']['Min'] = {}
                new[key + '_PSS_all']['Max'] = {}
                new[key + '_PSS_all']['Std'] = {}
                frame_for_graph[key + '_PEB_all'] = ""
                frame_for_graph[key + '_EHS_all'] = ""
                frame_for_graph[key + '_ESS_all'] = ""
                frame_for_graph[key + '_PSS_all'] = ""
                i=0
                while i !=4:
                    temp = values[values['Time'] == i+1]

                    frame_for_graph.at[i,key + '_PEB_all'] = temp['Peb_all'].mean()
                    frame_for_graph.ix[i][key + '_EHS_all'] = temp['Ehs_all'].mean()
                    frame_for_graph.ix[i][key + '_ESS_all'] = temp['Ess_all'].mean()
                    frame_for_graph.ix[i][key + '_PSS_all'] = temp['PSS'].mean()

                    new[key + '_PEB_all']['Mean'][i] = temp['Peb_all'].mean()
                    new[key + '_PEB_all']['Count'][i] =  temp['Peb_all'].count()
                    new[key + '_PEB_all']['Min'][i] =  temp['Peb_all'].min()
                    new[key + '_PEB_all']['Max'][i] = temp['Peb_all'].max()
                    new[key + '_PEB_all']['Std'][i] =temp['Peb_all'].std()

                    new[key + '_EHS_all']['Mean'][i] = temp['Ehs_all'].mean()
                    new[key + '_EHS_all']['Count'][i] = temp['Ehs_all'].count()
                    new[key + '_EHS_all']['Min'][i] = temp['Ehs_all'].min()
                    new[key + '_EHS_all']['Max'][i] = temp['Ehs_all'].max()
                    new[key + '_EHS_all']['Std'][i] =  temp['Ehs_all'].std()
                    new[key + '_ESS_all']['Mean'][i] = temp['Ess_all'].mean()
                    new[key + '_ESS_all']['Count'][i] = temp['Ess_all'].count()
                    new[key + '_ESS_all']['Min'][i] =  temp['Ess_all'].min()
                    new[key + '_ESS_all']['Max'][i] =  temp['Ess_all'].max()
                    new[key + '_ESS_all']['Std'][i] = temp['Ess_all'].std()
                    new[key + '_PSS_all']['Mean'][i] = temp['Ess_all'].mean()
                    new[key + '_PSS_all']['Count'][i] = temp['Ess_all'].count()
                    new[key + '_PSS_all']['Min'][i] = temp['Ess_all'].min()
                    new[key + '_PSS_all']['Max'][i] = temp['Ess_all'].max()
                    new[key + '_PSS_all']['Std'][i] = temp['Ess_all'].std()
                    i += 1

            else:
                i=0
                frame_for_graph[key + factors] = ""
                new[key+factors] = {}
                new[key + factors]['Mean'] = {}
                new[key + factors]['Count'] = {}
                new[key + factors]['Min'] = {}
                new[key + factors]['Max'] = {}
                new[key + factors]['Std'] = {}
                while i != 4:
                    temp = values[values['Time'] == i+1]
                    frame_for_graph.at[i, key + factors]=temp[factors].mean()


                    new[key+ factors]['Mean'][i] = temp[factors ].mean()
                    new[key+ factors]['Count'][i] =temp[factors ].count()
                    new[key+ factors]['Min'][i] = temp[factors ].min()
                    new[key+ factors]['Max'][i] = temp[factors ].max()
                    new[key+ factors]['Std'][i] = temp[factors ].std()
                    i+=1

    return (frame_for_graph, new)

def compare_detail(request):

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
    income = request.POST['income']
    gender = int(request.POST['gender'])
    date = request.POST['date']
    case = request.POST['indi_case']
    Demo_for_1 = map_function(employ,welfare,race,marital,education,housing,age,income,gender,date)


    if case != '-1':
        checking =1
        surveyee = Surveyee.objects.get(caseNum=case)
        individual = read_frame( Total_for_Admin.objects.filter(caseNum=surveyee))

    else:
        checking =0

    total =maskfunction(read_frame(Total_for_Admin.objects.all()), employ, welfare, race, marital, education, housing, age, income, gender,date)
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
    frame_for_graph = pd.DataFrame()
    if checking == 1:
        agent_filtered[case] = individual
    frame_for_graph, new = iterate_dictionary(agent_filtered, new, frame_for_graph,factors)


    html_fig=Graph.draw_graph_Admin_compare(frame_for_graph)
    return render(request, 'PSS/Analysis/compare_admin_show.html', {'detail_list':new,"html_fig":html_fig, 'key_list':list(new.keys()),
                                                                    'demo_com': Demo_for_1})

def map_function(employ, welfare, race, marital, education, housing, age, income, gender,date):

    employ_map = {77: 'Default', 0:'Non-Employed', 1:'Employed'}
    welfare_map = {77: 'Default', 0:'Non-Wellfare Benfit', 1:'Wellfare Benfit'}
    gender_map = {77: 'Default', 0:'Male', 1:'Female'}
    race_map = {'-1': 'Default', '0':'Native American or Alaska Native', '1':'Asian or Pacific Islander', '2':'Black or African American',
                '3':'White or European American','4':'Non-White Hispanic', '5':'Bi-/ multi-racial','6':'Other'}
    marry_map = {'-1': 'Default', '0': 'Married, spouse present', '1': 'Married, spouse absent',
                '2': 'Never Married',
                '3': 'Separated', '4': 'Divorced', '5': 'Widowed'}
    education_map = {'-1': 'Default', '0': 'Less than High School', '1': 'High-School / GEDt',
                '2': 'Some College but no degree',
                '3': 'Diploma or certificate from vocational, technical or trade school', '4': 'Associates Degree', '5': 'Bachelors Degree',
                     '6':'Masters Degree', '7':'Professional School Degree', '8':'Doctorate'}
    housing_map = {'-1': 'Default', '0': 'Rental', '1': 'Own Home',
                '2': 'Homeless',
                '3': 'Public Housing', '4': 'Other', '5': 'Living with family or friend'}
    races = [race_map[x] for x in race]

    marry = [marry_map[x] for x in marital]
    edu = [education_map[x] for x in education]
    house = [housing_map[x] for x in housing]

    return {"Employ": employ_map[employ], 'Welfare Benefit': welfare_map[welfare],'Race':", ".join(races),
            "Gender": gender_map[gender], 'Martial Status': ", ".join(marry), 'Education': ", ".join(edu),
            'Housing': ", ".join(house), 'Age': age, 'Income': income, 'Date': date}

def compare_detail_indi(request):

    users = get_user_model()
    compare1 = request.POST['compare1']
    compare2 = request.POST['compare2']


    factors = request.POST['factors']

    employ1 = int(request.POST['employ1'])
    welfare1 =int(request.POST['welfare1'])
    race1 = request.POST.getlist('race1')
    marital1 = request.POST.getlist('marital1')
    education1 = request.POST.getlist('education1')
    housing1 = request.POST.getlist('Housing1')
    age1 = request.POST['age1']
    income1 = request.POST['income1']
    gender1 = int(request.POST['gender1'])
    date1 = request.POST['date1']
    Demo_for_1 = map_function(employ1,welfare1,race1,marital1,education1,housing1,age1,income1,gender1,date1)

    employ2 = int(request.POST['employ2'])
    welfare2 =int(request.POST['welfare2'])
    race2 = request.POST.getlist('race2')
    marital2 = request.POST.getlist('marital2')
    education2 = request.POST.getlist('education2')
    housing2 = request.POST.getlist('Housing2')
    age2 = request.POST['age2']
    income2 = request.POST['income2']
    gender2 = int(request.POST['gender2'])
    date2 = request.POST['date2']
    Demo_for_2 = map_function(employ2,welfare2,race2,marital2,education2,housing2,age2,income2,gender2,date2)



    total_for_1 =maskfunction(read_frame(Total_for_Admin.objects.all()), employ1, welfare1, race1, marital1, education1,
                        housing1, age1, income1, gender1,date1)
    total_for_2 = maskfunction(read_frame(Total_for_Admin.objects.all()), employ2, welfare2, race2, marital2,
                               education2, housing2, age2, income2, gender2, date2)


    agent_filtered ={}

    if compare1 == '1':
        agent_filtered['Total_1'] = total_for_1
    else:
        agentObj = users.objects.get(id=compare1)
        agent_filtered[agentObj.username+"_1"] = total_for_1[(total_for_1['Agent'] == agentObj.username)]
    if compare2 == '1':
        agent_filtered['Total_2'] = total_for_2
    else:
        agentObj = users.objects.get(id=compare2)
        agent_filtered[agentObj.username+"_2"] = total_for_2[(total_for_2['Agent'] == agentObj.username)]

    new = {}
    frame_for_graph = pd.DataFrame([])
    frame_for_graph, new = iterate_dictionary(agent_filtered, new, frame_for_graph, factors)

    html_fig=Graph.draw_graph_Admin_compare(frame_for_graph)
    return render(request, 'PSS/Analysis/compare_admin_show.html', {'detail_list':new,"html_fig":html_fig,
                    'key_list':new.keys(), "demo":zip(Demo_for_2.keys(), Demo_for_1.values(),Demo_for_2.values())})

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
        html_fig = Graph.draw_graph_Agent_compare(list1, list2,indi, case )
    else:
        html_fig = Graph.draw_graph_Agent(list1, list2 )

    return render(request, 'PSS/Analysis/compare_agent_show.html', {'agent': agent.get_username(), 'detail_list': list2, 'html_fig': html_fig})



def show_graph(request):
    return