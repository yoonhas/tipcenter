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

            i=dmap[i]

            if i > 5 or i <0:
                sum += 0
                col += 0
            else:
                sum += i
                col += 1
            count+=1
        return (sum, col)

    elif 99 in val.unique():

        sum = 0
        col = 0

        for i in val:

            i = dmap[i]
            if i > 5 or i <0:
                sum += 0
                col += 0
            else:
                sum += i
                col += 1
            count += 1
        return (sum, col)
    else:
        sum=0
        count=1
        for i in val:

            i = dmap[i]
            if i > 5 or i < 0:
                sum += 0
            else:
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
            if (count == 2 or count == 4 or count == 6):
                i = dmap[i]

            if i > 10 or i < 0:
                sum += 0
                col += 0
            else:
                sum += i
                col += 1
            count += 1
        return (sum, col)

    elif 99 in val.unique():

        sum = 0
        col = 0
        count = 1
        for i in val:
            if (count == 2 or count == 4 or count == 6):
                i = dmap[i]
            if i > 10 or i < 0:
                sum += 0
                col += 0
            else:
                sum += i
                col += 1
            count += 1
        return (sum, col)
    else:
        sum = 0
        count = 1
        for i in val:
            if (count == 2 or count == 4 or count == 6):
                i = dmap[i]
            if i > 10 or i < 0:
                sum += 0
            else:
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
            if (count%2==1):
                i = dmap[i]

            if i > 7 or i < 1:
                sum += 0
                col += 0
            else:
                sum += i
                col += 1
            count += 1
        return (sum, col)

    elif 99 in val.unique():

        sum = 0
        col = 0
        count = 1
        for i in val:
            if (count%2==1):
                i = dmap[i]
            if i > 7 or i < 1:
                sum += 0
                col += 0
            else:
                sum += i
                col += 1
            count += 1
        return (sum, col)
    else:
        sum = 0
        count = 1
        for i in val:
            if (count%2==1):
                i = dmap[i]
            if i > 7 or i < 1:
                sum += 0
            else:
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
    f_situation_sum, f_situation_col = checkF(row[['F13', 'F14', 'F15', 'F116', 'F17', 'F18']])

    if Resilience_sum ==0:Resilience = 0.0
    else: Resilience= round(float(RSSilience_sum/Resilience_col,6))
    if self_effi_sum ==0:self_effi = 0.0
    else: self_effi = round(float(self_effi_sum/self_effi_col,6))
    if gr_per_sum ==0:gr_per = 0.0
    else: gr_per= round(float(gr_per_sum/gr_per_col,6))
    if gr_con_sum == 0:gr_con = 0.0
    else:gr_con = round(float(gr_con_sum / gr_con_col, 6))
    if spr_all_sum == 0:
        spr_all = 0.0
    else:
        spr_all= round(float(spr_all_sum / spr_all_col, 6))

    if f_self_sum == 0:f_self = 0.0
    else:f_self = round(float(f_self_sum / f_self_col, 6))

    if f_other_sum == 0:f_other = 0.0
    else:f_other = round(float(f_other_sum / f_other_col, 6))
    if f_situation_sum == 0:f_situation = 0.0
    else:f_situation = round(float(f_situation_sum / f_situation_col, 6))

    if f_self_sum + f_other_sum + f_situation_sum == 0:
        f_all = 0.0
    else:
        f_all = round(float(f_self_sum + f_other_sum + f_situation / f_self_col + f_other_col + f_situation_col, 6))

    if gr_per_sum + gr_con_sum == 0:
        gr_all = 0.0
    else:
        gr_all = round(float(gr_per_sum + gr_con_sum  / gr_per_col + gr_con_col, 6))


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



def readFile():
    dateparse = lambda x: pd.datetime.strptime(x, '%Y.%m.%d')
    rawData = pd.read_csv('Sample_dataset1.csv', parse_dates=['cDATE'], date_parser=dateparse)
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



if __name__ == "__main__":
    agent_map = {1:'cara', 2:'hello', 3:'Tara'}

    df= readFile()

    for i in range(len(df)):
        agent = User.objects.get(username=agent_map[df[i]['PROGRAM']])
        
        # surveyee
        if Surveyee.objects.filter(caseNum=df.ix[i]['caseNum']).exists():
            surveyee = Surveyee.objects.filter(caseNum=i.iloc['caseNum'])
        else:
            surveyee = Surveyee(caseNum=df.ix[i]['caseNum'], agent_name=agent )
            surveyee.save()
        
        #surveyTime
        Time = SurveyTimes.objects.filter(caseNum=surveyee).count()
        Time += 1
        if Time>4:
            continue
        else:
            
            surveyTime = SurveyTimes(caseNum=surveyee, time= Time, pub_Date= df.ix[i]['cDATE'])
            surveyTime.save()
    
        
        #eb
        eb = EB(caseNum=surveyee, surveytime=surveyTime.pk, time=Time, EB1=df.ix[i]['EB1']
                ,EB2=df.ix[i]['EB2'],EB3=df.ix[i]['EB3'],EB4=df.ix[i]['EB4'],EB5=df.ix[i]['EB5'],
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
        
        #eh
        eh = EH(caseNum=surveyee, time=Time, surveytime= surveyTime.pk,
                    EH1=df.ix[i]['EH1'],EH2=df.ix[i]['EH2'],EH3=df.ix[i]['EH3'],EH4=df.ix[i]['EH4'],EH5=df.ix[i]['EH5'],
                    EH6=df.ix[i]['EH6'], EH7=df.ix[i]['EH7'], EH8=df.ix[i]['EH8'], EH9=df.ix[i]['EH9'],EH10=df.ix[i]['EH10'],
                    EH11=df.ix[i]['EH11'], EH12=df.ix[i]['EH12'], EH13=df.ix[i]['EH13'], EH14=df.ix[i]['EH14'],
                    EH15=df.ix[i]['EH15'],
                    EH16=df.ix[i]['EH16'], EH17=df.ix[i]['EH17'], EH18=df.ix[i]['EH18'], EH19=df.ix[i]['EH19'],
                    EH20=df.ix[i]['EH20'],
                    EH21=df.ix[i]['EH21'], EH22=df.ix[i]['EH22'], EH23=df.ix[i]['EH23'], EH24=df.ix[i]['EH24'])
        
        eh.save()
        
        #es
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
                  A3=6, B3=6, C3=6, D3=d6,
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

        spr = SPR(caseNum=surveyee, time=time, surveytime=survey,
                  SPR1=df.ix[i]['SPR1'], SPR2=df.ix[i]['SPR2'], SPR3=df.ix[i]['SPR3'],
                  SPR4=df.ix[i]['SPR4'],
                  SPR5=df.ix[i]['SPR5'],
                  SPR6=df.ix[i]['SPR6']
                  )

        spr.save()
        ssp = SSP(caseNum=surveyee, time=Time,surveytime=surveyTime.pk,
                      SSP1=4, SSP2=4, SSP3=4,
                      SSP4=4,
                      SSP5=4,
                      SSP6=4, SSP7=4, SSP8=4, SSP9=4,
                      SSP10=4,
                      SSP11=4, SSP12=4
                      )
        ssp.save()
        f = F(caseNum=surveyee, time=Time, surveytime=surveyTime.pk,
              F1=df.ix[i]['F1'], F2=df.ix[i]['F2'], F3=df.ix[i]['F3'], F4=df.ix[i]['F4'],
              F5=df.ix[i]['F5'],
              F6=df.ix[i]['F6'], F7=df.ix[i]['F7'], F8=df.ix[i]['F8'], F9=df.ix[i]['F9'],
              F10=df.ix[i]['F10'],
              F11=df.ix[i]['F11'], F12=df.ix[i]['F12'], F13=df.ix[i]['F13'], F14=df.ix[i]['F14'],
              F15=df.ix[i]['F15'],
              F16=df.ix[i]['F16'], F17=df.ix[i]['F17'], F18=df.ix[i]['F18']
              )
        f.save()
        gd = GD(caseNum=surveyee, time=Time,surveytime=surveyTime.pk,
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
                HM11=4, HM12=4, HM13=4,HM14=4,
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
                DM12_1=1, DM12_3=1, DM13=df.ix[i]['Gender'],
                DM14=df.ix[i]['Race'], DM14_1=' ',
                DM15=1, DM16=df.ix[i]['EDULevel'], DM17=1, DM18=1,
                DM19=1
                )

        dm.save()