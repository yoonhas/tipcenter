import pandas as pd
from django.contrib.auth.models import User
from .models import Surveyee, SurveyTimes,EB, EH, EH_Question, ES_Question, ES, Tip_Question, Tip, EB_Question
from .models import EXF_Question,EXF, R, R_Question, SEF, SEF_Question, GR, GR_Question, SPR, SPR_Question,Total_for_Admin
from .models import SSP_Question, SSP, F, F_Question, GD, GD_Question, HM_Question, HM, HEALTH_Question, HEALTH, DM, DM_Question

def checkEBnES(val):
    if 77 in val.unique():
        sum = 0
        col = 0
        for i in val:
            if i > 5 or i <0:
                sum += 0
                col += 0
            else:
                sum += i
                col += 1
        return (sum, col)
    elif 99 in val.unique():
        sum = 0
        col = 0
        for i in val:
            if i > 5 or i <0:
                sum += 0
                col += 0
            else:
                sum += i
                col += 1
        return (sum, col)
    else:
        return (val.sum(), len(val))

def checkEH(val):
    if 77 in val.unique():
        if (val.sum() == 77 * (len(val))):
            return (val.sum(), len(val))
        else:
            sum = 0
            col = 0
            for i in val:
                if i > 10 or i < 0 or i== None:
                    sum += 0
                    col += 0
                else:
                    sum += i
                    col += 1
            return (sum, col)
    elif 99 in val.unique():
        if(val.sum()==99*(len(val))):
            return (val.sum(), len(val))
        else:
            sum = 0
            col = 0
            for i in val:
                if i > 10 or i < 0 or i==None:
                    sum += 0
                    col += 0
                else:
                    sum += i
                    col += 1
            return (sum, col)
    else:
        return (val.sum(), len(val))

def checkR(val):
    if 77 in val.unique():
        if (val.sum() == 77 * (len(val))):
            return (val.sum(), len(val))
        else:
            sum = 0
            col = 0
            for i in val:
                if i > 4 or i < 0 or i== None:
                    sum += 0
                    col += 0
                else:
                    sum += i
                    col += 1
            return (sum, col)
    elif 99 in val.unique():
        if(val.sum()==99*(len(val))):
            return (val.sum(), len(val))
        else:
            sum = 0
            col = 0
            for i in val:
                if i > 4 or i < 0 or i==None:
                    sum += 0
                    col += 0
                else:
                    sum += i
                    col += 1
            return (sum, col)
    else:
        return (val.sum(), len(val))

def checkGR(val):
    dmap={1:5, 2:4, 3:3, 4:2, 5:1}
    if 77 in val.unique():
        sum = 0
        col = 0
        count=1
        for i in val:
            if i > 5 or i <0:
                sum += 0
                col += 0
            else:
                i = dmap[i]
                sum += i
                col += 1
            count+=1
        return (sum, col)

    elif 99 in val.unique():

        sum = 0
        col = 0
        count = 1
        for i in val:
            if i > 5 or i <0:
                sum += 0
                col += 0
            else:
                i = dmap[i]
                sum += i
                col += 1
            count += 1
        return (sum, col)
    else:
        sum=0
        count=1
        for i in val:
             if i > 5 or i < 0:
                sum += 0
             else:
                i = dmap[i]
                sum += i
             count += 1
        return (sum, len(val))


def checkSPR(val):
    dmap = {0:10, 1: 9, 2: 8, 3: 7, 4: 6, 5: 5, 6: 4, 7: 3, 8: 2, 9: 1, 10: 0}
    if 77 in val.unique():
        sum = 0
        col = 0
        count = 1
        for i in val:


            if i > 10 or i < 0:
                sum += 0
                col += 0
            else:
                if (count == 2 or count == 4 or count == 6):
                    i = dmap[i]
                sum += i
                col += 1
            count += 1
        return (sum, col)

    elif 99 in val.unique():

        sum = 0
        col = 0
        count = 1
        for i in val:

            if i > 10 or i < 0:
                sum += 0
                col += 0
            else:
                if (count == 2 or count == 4 or count == 6):
                    i = dmap[i]
                sum += i
                col += 1
            count += 1
        return (sum, col)
    else:
        sum = 0
        count = 1
        for i in val:

            if i > 10 or i < 0:
                sum += 0
            else:
                if (count == 2 or count == 4 or count == 6):
                    i = dmap[i]
                sum += i
            count += 1
        return (sum, len(val))

def checkF(val):
    dmap = { 1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}
    if 77 in val.unique():
        sum = 0
        col = 0
        count = 1
        for i in val:
            if i > 7 or i < 1:
                sum += 0
                col += 0
            else:
                if (count % 2 == 1):
                    i = dmap[i]
                sum += i
                col += 1
            count += 1
        return (sum, col)

    elif 99 in val.unique():

        sum = 0
        col = 0
        count = 1
        for i in val:

            if i > 7 or i < 1:
                sum += 0
                col += 0
            else:
                if (count % 2 == 1):
                    i = dmap[i]
                sum += i
                col += 1
            count += 1
        return (sum, col)
    else:
        sum = 0
        count = 1
        for i in val:

            if i > 7 or i < 1:
                sum += 0
            else:
                if (count % 2 ==1):
                    i = dmap[i]
                sum += i
            count += 1
        return (sum, len(val))

def parsing(row):

    Empowerment_sum, Empowerment_col =checkEH(row[['EH3','EH4','EH5','EH6']])
    SelfMotivation_sum, SelfMotivation_col = checkEH(row[['EH11', 'EH15']])
    SkillResources_sum, SkillResources_col = checkEH(row[['EH17', 'EH18', 'EH19', 'EH20']])
    GoalOrientation_sum, GoalOrientation_col = checkEH(row[['EH21', 'EH22', 'EH23', 'EH24']])
    EHS_all_sum, EHS_all_col = checkEH(row[['EH3','EH4','EH5','EH6','EH11', 'EH15','EH17', 'EH18', 'EH19', 'EH20','EH21', 'EH22', 'EH23', 'EH24']])


    Health_sum, Health_col = checkEBnES(row[['EB10', 'EB11', 'EB12', 'EB13']])
    Community_sum, Community_col = checkEBnES(row[['EB15', 'EB16', 'EB17']])
    ChildCare_sum, ChildCare_col = checkEBnES(row[['EB6', 'EB19', 'EB18']])
    JobSkills_sum, JobSkills_col = checkEBnES(row[['EB1', 'EB2', 'EB3', 'EB4', 'EB8']])
    SoftSkill_sum , SoftSkill_col = checkEBnES(row[['EB22', 'EB23', 'EB24', 'EB25', 'EB26']])

    ESS1_sum, ESS1_col = checkEBnES(row[['SS2', 'SS8', 'SS9', 'SS10', 'SS12']])
    ESS2_sum, ESS2_col = checkEBnES(row[['SS1', 'SS4', 'SS13', 'SS14']])
    ESS3_sum, ESS3_col = checkEBnES(row[['SS11', 'SS7']])
    ESS4_sum, ESS4_col = checkEBnES(row[['SS3', 'SS5', 'SS6']])

    Resilience_sum,Resilience_col = checkR(row[['R1', 'R2']])
    self_effi_sum, self_effi_col = checkEBnES(row[['SEF1','SEF2','SEF3', 'SEF4','SEF5','SEF6','SEF7', 'SEF8']])
    gr_per_sum, gr_per_col = checkEBnES(row[['GR2','GR4', 'GR7', 'GR8']])
    gr_con_sum, gr_con_col = checkGR(row[['GR1', 'GR3', 'GR5', 'GR6']])
    spr_all_sum, spr_all_col = checkSPR(row[['SPR1', 'SPR2', 'SPR3','SPR4', 'SPR5', 'SPR6']])

    f_self_sum, f_self_col =checkF(row[['F2','F1', 'F4', 'F3',  'F6', 'F5']])
    f_other_sum, f_other_col = checkF(row[['F7', 'F8', 'F9', 'F10', 'F11', 'F12']])
    f_situation_sum, f_situation_col = checkF(row[['F13', 'F14', 'F15', 'F16', 'F17', 'F18']])

    if Resilience_sum ==0:Resilience = 0.0
    else: Resilience= round(float(Resilience_sum/Resilience_col),6)
    if self_effi_sum ==0:self_effi = 0.0
    else: self_effi = round(float(self_effi_sum/self_effi_col),6)
    if gr_per_sum ==0:gr_per = 0.0
    else: gr_per= round(float(gr_per_sum/gr_per_col),6)
    if gr_con_sum == 0:gr_con = 0.0
    else:gr_con = round(float(gr_con_sum / gr_con_col),6)
    if spr_all_sum == 0:
        spr_all = 0.0
    else:
        spr_all= round(float(spr_all_sum / spr_all_col),6)

    if f_self_sum == 0:f_self = 0.0
    else:f_self = round(float(f_self_sum / f_self_col),6)

    if f_other_sum == 0:f_other = 0.0
    else:f_other = round(float(f_other_sum / f_other_col),6)
    if f_situation_sum == 0:f_situation = 0.0
    else:f_situation = round(float(f_situation_sum / f_situation_col),6)

    if f_self_sum + f_other_sum + f_situation_sum == 0:
        f_all = 0.0
    else:
        f_all = round(float((f_self_sum + f_other_sum + f_situation )/ (f_self_col + f_other_col + f_situation_col)),6)

    if gr_per_sum + gr_con_sum == 0:
        gr_all = 0.0
    else:
        gr_all = round(float((gr_per_sum + gr_con_sum)  / (gr_per_col + gr_con_col)),6)


    if Empowerment_sum == 0:Empowerment = 0.0
    else: Empowerment = round(float(Empowerment_sum)/Empowerment_col,6)

    if SelfMotivation_sum ==0:SelfMotivation=0.0
    else: SelfMotivation=round(float(SelfMotivation_sum)/ SelfMotivation_col,6)

    if SkillResources_sum ==0: SkillResources=0.0
    else: SkillResources=round(float(SkillResources_sum)/ SkillResources_col,6)

    if GoalOrientation_sum ==0:GoalOrientation=0.0
    else: GoalOrientation=round(float(GoalOrientation_sum)/ GoalOrientation_col,6)
    if  (Empowerment_sum+SelfMotivation_sum+SkillResources_sum+GoalOrientation_sum)==0:EHS_all=0.0
    else:EHS_all = round(float(EHS_all_sum)/(EHS_all_col),6)

    if Health_sum==0:Health=0.0
    else:Health = round(float(Health_sum)/ Health_col,6)

    if Community_sum==0:Community=0.0
    else:Community =round(float(Community_sum)/Community_col,6)

    if ChildCare_sum==0:ChildCare=0.0
    else:ChildCare =round( float(ChildCare_sum)/ ChildCare_col,6)

    if JobSkills_sum==0: JobSkills=0.0
    else:JobSkills = round(float(JobSkills_sum)/ JobSkills_col,6)

    if SoftSkill_sum==0: SoftSkill=0.0
    else:SoftSkill = round(float(SoftSkill_sum)/ SoftSkill_col,6)

    if (Health_sum+Community_sum+ChildCare_sum+JobSkills_sum+SoftSkill_sum) ==0:PEBS_all=0
    else:PEBS_all = round(float(Health_sum+Community_sum+ChildCare_sum+JobSkills_sum+SoftSkill_sum)/(Health_col+Community_col+ChildCare_col+JobSkills_col+SoftSkill_col),6)

    if ESS1_sum ==0:ESS1=0.0
    else:ESS1 = round(float(ESS1_sum)/ ESS1_col,6)

    if ESS2_sum ==0:ESS2=0.0
    else:ESS2 = round(float(ESS2_sum) / ESS2_col,6)

    if ESS3_sum ==0: ESS3=0.0
    else:ESS3 = round(float(ESS3_sum) / ESS3_col,6)

    if ESS4_sum==0:ESS4=0.0
    else:ESS4 = round(float(ESS4_sum) / ESS4_col,6)

    if (ESS1_sum+ESS2_sum+ESS3_sum+ESS4_sum)==0:ESS_all =0.0
    else:ESS_all =round(float(ESS1_sum+ESS2_sum+ESS3_sum+ESS4_sum)/(ESS1_col+ESS2_col+ESS3_col+ESS4_col),6)





    return (Empowerment, SelfMotivation, SkillResources, GoalOrientation, EHS_all, Health, Community, ChildCare, JobSkills,
            SoftSkill, PEBS_all, ESS1, ESS2, ESS3, ESS4, ESS_all,Resilience,self_effi, gr_per, gr_con, spr_all, f_self, f_other, f_situation, f_all, gr_all )



def readFile(file):
    dateparse = lambda x: pd.datetime.strptime(x, '%m/%d/%Y')
    rawData = pd.read_csv(file, parse_dates=['cDATE'], date_parser=dateparse)
    df = pd.DataFrame(rawData)
    df.fillna(99, inplace=True)
    df['Empowerment'] = ""
    df['SelfMotivation'] = ""
    df['SkillResources'] = ""
    df['GoalOrientation'] = ""
    df['EHS_all'] = ""
    df['Health'] = ""
    df['Community'] = ""
    df['ChildCare'] = ""
    df['JobSkills'] = ""
    df['SoftSkill'] = ""
    df['PEBS_all'] = ""
    df['ESS1'] = ""
    df['ESS2'] = ""
    df['ESS3'] = ""
    df['ESS4'] = ""
    df['ESS_all'] = ""
    df['R_all'] = ""
    df['SEF_all'] = ""
    df['GR_con'] = ""
    df['GR_per'] = ""
    df['GR_all'] = ""
    df['SPR_all'] = ""
    df['F_self'] = ""
    df['F_other'] = ""
    df['F_situation'] = ""
    df['F_all'] = ""


    for i in range(len(df)):
        Empowerment, SelfMotivation, SkillResources, GoalOrientation, EHS_all, Health, Community, ChildCare, JobSkills, SoftSkill, PEBS_all, ESS1, ESS2, ESS3, ESS4, ESS_all\
            ,Resilience,self_effi, gr_per, gr_con, spr_all, f_self, f_other, f_situation, f_all, gr_all = parsing(df.iloc[i])
        df.set_value(i, 'Empowerment',Empowerment)
        df.set_value(i, 'SelfMotivation', SelfMotivation)
        df.set_value(i, 'SkillResources', SkillResources)
        df.set_value(i, 'GoalOrientation', GoalOrientation)
        df.set_value(i, 'EHS_all', EHS_all)
        df.set_value(i, 'Health', Health)
        df.set_value(i, 'Community', Community)
        df.set_value(i, 'ChildCare', ChildCare)
        df.set_value(i, 'JobSkills', JobSkills)
        df.set_value(i, 'SoftSkill', SoftSkill)
        df.set_value(i, 'PEBS_all', PEBS_all)
        df.set_value(i, 'ESS1', ESS1)
        df.set_value(i, 'ESS2', ESS2)
        df.set_value(i, 'ESS3', ESS3)
        df.set_value(i, 'ESS4', ESS4)
        df.set_value(i, 'ESS_all', ESS_all)
        df.set_value(i, 'R_all', Resilience)
        df.set_value(i, 'SEF_all', self_effi)
        df.set_value(i, 'GR_con', gr_con)
        df.set_value(i, 'GR_per', gr_per)
        df.set_value(i, 'GR_all', gr_all)
        df.set_value(i, 'SPR_all', spr_all)
        df.set_value(i, 'F_self', f_self)
        df.set_value(i, 'F_other', f_other)
        df.set_value(i, 'F_situation', f_situation)
        df.set_value(i, 'F_all', f_all)



    return df



