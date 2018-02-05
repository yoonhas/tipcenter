from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Surveyee(models.Model):
    caseNum = models.IntegerField(unique=True, primary_key=True)
    agent_name = models.ForeignKey(User, on_delete=models.CASCADE,
                                   help_text="If you delete agent, you will lose all surveyees")
    survey1 = models.BooleanField(default=False)
    survey2 = models.BooleanField(default=False)
    survey3 = models.BooleanField(default=False)
    survey4 = models.BooleanField(default=False)
    survey_kind = models.IntegerField(null=False, default=1)
    readyToStart = models.BooleanField(default=False)


    def __str__(self):
        return str(self.caseNum)

class SurveyTimes(models.Model):

    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    online = models.BooleanField(default=False)
    agent = models.ForeignKey(User,  on_delete=models.CASCADE)
    time = models.IntegerField(null=False, default=1)
    pub_Date = models.DateField()
    readyToStart = models.BooleanField(default=False)
    doneSurvey = models.BooleanField(default=False)



    def publish(self):
        self.pub_Date = timezone.localdate(timezone.now())
        self.save()

    def __str__(self):
        return "{}_{}".format( str(self.caseNum),str(self.time))



class EB(models.Model):

    surveytime = models.IntegerField()
    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    EB1 = models.IntegerField(default=1)
    EB2 = models.IntegerField(default=1)
    EB3 = models.IntegerField(default=1)
    EB4 = models.IntegerField(default=1)
    EB5 = models.IntegerField(default=1)
    EB6 = models.IntegerField(default=1)
    EB7 = models.IntegerField(default=1)
    EB8 = models.IntegerField(default=1)
    EB9 = models.IntegerField(default=1)
    EB10 = models.IntegerField(default=1)
    EB11 = models.IntegerField(default=1)
    EB12 = models.IntegerField(default=1)
    EB13 = models.IntegerField(default=1)
    EB14 = models.IntegerField(default=1)
    EB15 = models.IntegerField(default=1)
    EB16 = models.IntegerField(default=1)
    EB17 = models.IntegerField(default=1)
    EB18 = models.IntegerField(default=1)
    EB19 = models.IntegerField(default=1)
    EB20 = models.IntegerField(default=1)
    EB21 = models.IntegerField(default=1)
    EB22 = models.IntegerField(default=1)
    EB23 = models.IntegerField(default=1)
    EB24 = models.IntegerField(default=1)
    EB25 = models.IntegerField(default=1)
    EB26 = models.IntegerField(default=1)
    EB27 = models.IntegerField(default=1)

    def __str__(self):
        return "EB_{}_{}".format(str(self.caseNum),str(self.time))


class EB_Question(models.Model):
    EB1 = models.CharField(max_length=200)
    EB2 = models.CharField(max_length=200)
    EB3 = models.CharField(max_length=200)
    EB4 = models.CharField(max_length=200)
    EB5 = models.CharField(max_length=200)
    EB6 = models.CharField(max_length=200)
    EB7 = models.CharField(max_length=200)
    EB8 = models.CharField(max_length=200)
    EB9 = models.CharField(max_length=200)
    EB10 = models.CharField(max_length=200)
    EB11 = models.CharField(max_length=200)
    EB12 = models.CharField(max_length=200)
    EB13 = models.CharField(max_length=200)
    EB14 = models.CharField(max_length=200)
    EB15 = models.CharField(max_length=200)
    EB16 = models.CharField(max_length=200)
    EB17 = models.CharField(max_length=200)
    EB18 = models.CharField(max_length=200)
    EB19 = models.CharField(max_length=200)
    EB20 = models.CharField(max_length=200)
    EB21 = models.CharField(max_length=200)
    EB22 = models.CharField(max_length=200)
    EB23 = models.CharField(max_length=200)
    EB24 = models.CharField(max_length=200)
    EB25 = models.CharField(max_length=200)
    EB26 = models.CharField(max_length=200)
    EB27 = models.CharField(max_length=200)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in EB_Question._meta.fields ]

    def __str__(self):
        return str(self.pk)

class EH(models.Model):

    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    EH1 = models.IntegerField(null=False, default=None)
    EH2 = models.IntegerField(null=False, default=None)
    EH3 = models.IntegerField(null=False, default=None)
    EH4 = models.IntegerField(null=False, default=None)
    EH5 = models.IntegerField(null=False, default=None)
    EH6 = models.IntegerField(null=False, default=None)
    EH7 = models.IntegerField(null=False, default=None)
    EH8 = models.IntegerField(null=False, default=None)
    EH9 = models.IntegerField(null=False, default=None)
    EH10 = models.IntegerField(null=False, default=None)
    EH11 = models.IntegerField(null=False, default=None)
    EH12 = models.IntegerField(null=False, default=None)
    EH13 = models.IntegerField(null=False, default=None)
    EH14 = models.IntegerField(null=False, default=None)
    EH15 = models.IntegerField(null=False, default=None)
    EH16 = models.IntegerField(null=False, default=None)
    EH17 = models.IntegerField(null=False, default=None)
    EH18 = models.IntegerField(null=False, default=None)
    EH19 = models.IntegerField(null=False, default=None)
    EH20 = models.IntegerField(null=False, default=None)
    EH21 = models.IntegerField(null=False, default=None)
    EH22 = models.IntegerField(null=False, default=None)
    EH23 = models.IntegerField(null=False, default=None)
    EH24 = models.IntegerField(null=False, default=None)

    def __str__(self):
        return "EH_{}_{}".format(str(self.caseNum),str(self.time))


class EH_Question(models.Model):
    EH1 = models.CharField(max_length=200)
    EH2 = models.CharField(max_length=200)
    EH3 = models.CharField(max_length=200)
    EH4 = models.CharField(max_length=200)
    EH5 = models.CharField(max_length=200)
    EH6 = models.CharField(max_length=200)
    EH7 = models.CharField(max_length=200)
    EH8 = models.CharField(max_length=200)
    EH9 = models.CharField(max_length=200)
    EH10 = models.CharField(max_length=200)
    EH11 = models.CharField(max_length=200)
    EH12 = models.CharField(max_length=200)
    EH13 = models.CharField(max_length=200)
    EH14 = models.CharField(max_length=200)
    EH15 = models.CharField(max_length=200)
    EH16 = models.CharField(max_length=200)
    EH17 = models.CharField(max_length=200)
    EH18 = models.CharField(max_length=200)
    EH19 = models.CharField(max_length=200)
    EH20 = models.CharField(max_length=200)
    EH21 = models.CharField(max_length=200)
    EH22 = models.CharField(max_length=200)
    EH23 = models.CharField(max_length=200)
    EH24 = models.CharField(max_length=200)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in EH_Question._meta.fields ]

    def __str__(self):
        return str(self.pk)

class ES(models.Model):

    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    ES1 = models.IntegerField(null=False, default=None)
    ES2 = models.IntegerField(null=False, default=None)
    ES3 = models.IntegerField(null=False, default=None)
    ES4 = models.IntegerField(null=False, default=None)
    ES5 = models.IntegerField(null=False, default=None)
    ES6 = models.IntegerField(null=False, default=None)
    ES7 = models.IntegerField(null=False, default=None)
    ES8 = models.IntegerField(null=False, default=None)
    ES9 = models.IntegerField(null=False, default=None)
    ES10 = models.IntegerField(null=False, default=None)
    ES11 = models.IntegerField(null=False, default=None)
    ES12 = models.IntegerField(null=False, default=None)
    ES13 = models.IntegerField(null=False, default=None)
    ES14 = models.IntegerField(null=False, default=None)
    ES15 = models.IntegerField(null=False, default=None)

    def __str__(self):
        return "ES_{}_{}".format(str(self.caseNum),str(self.time))

class ES_Question(models.Model):
    ES1 = models.CharField(max_length=200)
    ES2 = models.CharField(max_length=200)
    ES3 = models.CharField(max_length=200)
    ES4 = models.CharField(max_length=200)
    ES5 = models.CharField(max_length=200)
    ES6 = models.CharField(max_length=200)
    ES7 = models.CharField(max_length=200)
    ES8 = models.CharField(max_length=200)
    ES9 = models.CharField(max_length=200)
    ES10 = models.CharField(max_length=200)
    ES11 = models.CharField(max_length=200)
    ES12 = models.CharField(max_length=200)
    ES13 = models.CharField(max_length=200)
    ES14 = models.CharField(max_length=200)
    ES15 = models.CharField(max_length=200)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in ES_Question._meta.fields]

    def __str__(self):
        return str(self.pk)

class Tip(models.Model):

    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    TIP1 = models.IntegerField(null=False, default=None)
    TIP2 = models.IntegerField(null=False, default=None)
    TIP3 = models.IntegerField(null=False, default=None)
    TIP4 = models.IntegerField(null=False, default=None)
    TIP5 = models.IntegerField(null=False, default=None)
    TIP6 = models.IntegerField(null=False, default=None)
    TIP7 = models.IntegerField(null=False, default=None)
    TIP8 = models.IntegerField(null=False, default=None)
    TIP9 = models.IntegerField(null=False, default=None)
    TIP10 = models.IntegerField(null=False, default=None)
    TIP11 = models.IntegerField(null=False, default=None)
    TIP12 = models.IntegerField(null=False, default=None)
    TIP13 = models.IntegerField(null=False, default=None)
    TIP14 = models.IntegerField(null=False, default=None)
    TIP15 = models.IntegerField(null=False, default=None)

    def __str__(self):
        return "Tip_{}_{}".format(str(self.caseNum),str(self.time))

class Tip_Question(models.Model):
    TIP1 = models.CharField(max_length=200)
    TIP2 = models.CharField(max_length=200)
    TIP3 = models.CharField(max_length=200)
    TIP4 = models.CharField(max_length=200)
    TIP5 = models.CharField(max_length=200)
    TIP6 = models.CharField(max_length=200)
    TIP7 = models.CharField(max_length=200)
    TIP8 = models.CharField(max_length=200)
    TIP9 = models.CharField(max_length=200)
    TIP10 = models.CharField(max_length=200)
    TIP11 = models.CharField(max_length=200)
    TIP12 = models.CharField(max_length=200)
    TIP13 = models.CharField(max_length=200)
    TIP14 = models.CharField(max_length=200)
    TIP15 = models.CharField(max_length=200)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Tip_Question._meta.fields]

    def __str__(self):
        return str(self.pk)

class EXF(models.Model):

    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    A_3 = models.IntegerField(null=False, default=None)
    B_3 = models.IntegerField(null=False, default=None)
    C_3 = models.IntegerField(null=False, default=None)
    D_3 = models.IntegerField(null=False, default=None)
    E_2 = models.IntegerField(null=False, default=None)
    F_2 = models.IntegerField(null=False, default=None)
    G_1 = models.IntegerField(null=False, default=None)
    H_3 = models.IntegerField(null=False, default=None)
    I_2 = models.IntegerField(null=False, default=None)
    J_3 = models.IntegerField(null=False, default=None)
    K_1 = models.IntegerField(null=False, default=None)
    K_2 = models.IntegerField(null=False, default=None)
    K_3 = models.IntegerField(null=False, default=None)
    L_1 = models.IntegerField(null=False, default=None)
    L_2 = models.IntegerField(null=False, default=None)
    L_3 = models.IntegerField(null=False, default=None)

    def __str__(self):
        return "EXF_{}_{}".format(str(self.caseNum),str(self.time))

class EXF_Question(models.Model):
    A3 = models.CharField(max_length=200)
    B3 = models.CharField(max_length=200)
    C3 = models.CharField(max_length=200)
    D3 = models.CharField(max_length=200)
    E2 = models.CharField(max_length=200)
    F2 = models.CharField(max_length=200)
    G1 = models.CharField(max_length=200)
    H3 = models.CharField(max_length=200)
    I2 = models.CharField(max_length=200)
    J3 = models.CharField(max_length=200)
    K1 = models.CharField(max_length=200)
    K2 = models.CharField(max_length=200)
    K3 = models.CharField(max_length=200)
    L1 = models.CharField(max_length=200)
    L2 = models.CharField(max_length=200)
    L3 = models.CharField(max_length=200)


    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in EXF_Question._meta.fields]

    def __str__(self):
        return str(self.pk)

class SSP(models.Model):

    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    SSP1 = models.IntegerField(null=False, default=None)
    SSP2 = models.IntegerField(null=False, default=None)
    SSP3 = models.IntegerField(null=False, default=None)
    SSP4 = models.IntegerField(null=False, default=None)
    SSP5 = models.IntegerField(null=False, default=None)
    SSP6 = models.IntegerField(null=False, default=None)
    SSP7 = models.IntegerField(null=False, default=None)
    SSP8 = models.IntegerField(null=False, default=None)
    SSP9 = models.IntegerField(null=False, default=None)
    SSP10 = models.IntegerField(null=False, default=None)
    SSP11 = models.IntegerField(null=False, default=None)
    SSP12 = models.IntegerField(null=False, default=None)


    def __str__(self):
        return "SSP_{}_{}".format(str(self.caseNum),str(self.time))

class SSP_Question(models.Model):
    SSP1 = models.CharField(max_length=200)
    SSP2 = models.CharField(max_length=200)
    SSP3 = models.CharField(max_length=200)
    SSP4 = models.CharField(max_length=200)
    SSP5 = models.CharField(max_length=200)
    SSP6 = models.CharField(max_length=200)
    SSP7 = models.CharField(max_length=200)
    SSP8 = models.CharField(max_length=200)
    SSP9 = models.CharField(max_length=200)
    SSP10 = models.CharField(max_length=200)
    SSP11 = models.CharField(max_length=200)
    SSP12 = models.CharField(max_length=200)


    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in SSP_Question._meta.fields]

    def __str__(self):
        return str(self.pk)


class F(models.Model):

    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    F1 = models.IntegerField(null=False, default=None)
    F2 = models.IntegerField(null=False, default=None)
    F3 = models.IntegerField(null=False, default=None)
    F4 = models.IntegerField(null=False, default=None)
    F5 = models.IntegerField(null=False, default=None)
    F6 = models.IntegerField(null=False, default=None)
    F7 = models.IntegerField(null=False, default=None)
    F8 = models.IntegerField(null=False, default=None)
    F9 = models.IntegerField(null=False, default=None)
    F10 = models.IntegerField(null=False, default=None)
    F11 = models.IntegerField(null=False, default=None)
    F12 = models.IntegerField(null=False, default=None)
    F13 = models.IntegerField(null=False, default=None)
    F14 = models.IntegerField(null=False, default=None)
    F15 = models.IntegerField(null=False, default=None)
    F16 = models.IntegerField(null=False, default=None)
    F17 = models.IntegerField(null=False, default=None)
    F18 = models.IntegerField(null=False, default=None)

    def __str__(self):
        return "F_{}_{}".format(str(self.caseNum),str(self.time))

class F_Question(models.Model):
    F1 = models.CharField(max_length=200)
    F2 = models.CharField(max_length=200)
    F3 = models.CharField(max_length=200)
    F4 = models.CharField(max_length=200)
    F5 = models.CharField(max_length=200)
    F6 = models.CharField(max_length=200)
    F7 = models.CharField(max_length=200)
    F8 = models.CharField(max_length=200)
    F9 = models.CharField(max_length=200)
    F10 = models.CharField(max_length=200)
    F11 = models.CharField(max_length=200)
    F12 = models.CharField(max_length=200)
    F13 = models.CharField(max_length=200)
    F14 = models.CharField(max_length=200)
    F15 = models.CharField(max_length=200)
    F16 = models.CharField(max_length=200)
    F17 = models.CharField(max_length=200)
    F18 = models.CharField(max_length=200)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in F_Question._meta.fields]

    def __str__(self):
        return str(self.pk)

class GD(models.Model):

    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    GD1 = models.IntegerField(null=False, default=None)
    GD2 = models.IntegerField(null=False, default=None)
    GD3 = models.IntegerField(null=False, default=None)
    GD4 = models.IntegerField(null=False, default=None)
    GD5 = models.IntegerField(null=False, default=None)
    GD6 = models.IntegerField(null=False, default=None)


    def __str__(self):
        return "GD_{}_{}".format(str(self.caseNum),str(self.time))

class GD_Question(models.Model):
    GD1 = models.CharField(max_length=200)
    GD2 = models.CharField(max_length=200)
    GD3 = models.CharField(max_length=200)
    GD4 = models.CharField(max_length=200)
    GD5 = models.CharField(max_length=200)
    GD6 = models.CharField(max_length=200)


    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in GD_Question._meta.fields]

    def __str__(self):
        return str(self.pk)

class HM(models.Model):

    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    HM1 = models.IntegerField(null=False, default=None)
    HM2 = models.IntegerField(null=False, default=None)
    HM3 = models.IntegerField(null=False, default=None)
    HM4 = models.IntegerField(null=False, default=None)
    HM5 = models.IntegerField(null=False, default=None)
    HM6 = models.IntegerField(null=False, default=None)
    HM7 = models.IntegerField(null=False, default=None)
    HM8 = models.IntegerField(null=False, default=None)
    HM9 = models.IntegerField(null=False, default=None)
    HM10 = models.IntegerField(null=False, default=None)
    HM11 = models.IntegerField(null=False, default=None)
    HM12 = models.IntegerField(null=False, default=None)
    HM13 = models.IntegerField(null=False, default=None)
    HM14 = models.IntegerField(null=False, default=None)
    HM15 = models.IntegerField(null=False, default=None)

    def __str__(self):
        return "HM_{}_{}".format(str(self.caseNum),str(self.time))

class HM_Question(models.Model):
    HM1 = models.CharField(max_length=200)
    HM2 = models.CharField(max_length=200)
    HM3 = models.CharField(max_length=200)
    HM4 = models.CharField(max_length=200)
    HM5 = models.CharField(max_length=200)
    HM6 = models.CharField(max_length=200)
    HM7 = models.CharField(max_length=200)
    HM8 = models.CharField(max_length=200)
    HM9 = models.CharField(max_length=200)
    HM10 = models.CharField(max_length=200)
    HM11 = models.CharField(max_length=200)
    HM12 = models.CharField(max_length=200)
    HM13 = models.CharField(max_length=200)
    HM14 = models.CharField(max_length=200)
    HM15 = models.CharField(max_length=200)


    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in HM_Question._meta.fields]

    def __str__(self):
        return str(self.pk)

class HEALTH(models.Model):

    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    HEALTH1 = models.IntegerField(null=False, default=None)
    HEALTH2 = models.IntegerField(null=False, default=None)


    def __str__(self):
        return "HEALTH_{}_{}".format(str(self.caseNum),str(self.time))

class HEALTH_Question(models.Model):
    HEALTH1 = models.CharField(max_length=200)
    HEALTH2 = models.CharField(max_length=200)



    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in HEALTH_Question._meta.fields]

    def __str__(self):
        return str(self.pk)

class SEF(models.Model):

    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    SEF1 = models.IntegerField(null=False, default=None)
    SEF2 = models.IntegerField(null=False, default=None)
    SEF3 = models.IntegerField(null=False, default=None)
    SEF4 = models.IntegerField(null=False, default=None)
    SEF5 = models.IntegerField(null=False, default=None)
    SEF6 = models.IntegerField(null=False, default=None)
    SEF7 = models.IntegerField(null=False, default=None)
    SEF8 = models.IntegerField(null=False, default=None)


    def __str__(self):
        return "SEF_{}_{}".format(str(self.caseNum),str(self.time))

class SEF_Question(models.Model):
    SEF1 = models.CharField(max_length=200)
    SEF2 = models.CharField(max_length=200)
    SEF3 = models.CharField(max_length=200)
    SEF4 = models.CharField(max_length=200)
    SEF5 = models.CharField(max_length=200)
    SEF6 = models.CharField(max_length=200)
    SEF7 = models.CharField(max_length=200)
    SEF8 = models.CharField(max_length=200)



    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in SEF_Question._meta.fields]

    def __str__(self):
        return str(self.pk)


class GR(models.Model):

    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    GR1 = models.IntegerField(null=False, default=None)
    GR2 = models.IntegerField(null=False, default=None)
    GR3 = models.IntegerField(null=False, default=None)
    GR4 = models.IntegerField(null=False, default=None)
    GR5 = models.IntegerField(null=False, default=None)
    GR6 = models.IntegerField(null=False, default=None)
    GR7 = models.IntegerField(null=False, default=None)
    GR8 = models.IntegerField(null=False, default=None)

    def __str__(self):
        return "GR_{}_{}".format(str(self.caseNum),str(self.time))


class GR_Question(models.Model):
    GR1 = models.CharField(max_length=200)
    GR2 = models.CharField(max_length=200)
    GR3 = models.CharField(max_length=200)
    GR4 = models.CharField(max_length=200)
    GR5 = models.CharField(max_length=200)
    GR6 = models.CharField(max_length=200)
    GR7 = models.CharField(max_length=200)
    GR8 = models.CharField(max_length=200)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in GR_Question._meta.fields]

    def __str__(self):
        return str(self.pk)

class SPR(models.Model):

    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    SPR1 = models.IntegerField(null=False, default=None)
    SPR2 = models.IntegerField(null=False, default=None)
    SPR3 = models.IntegerField(null=False, default=None)
    SPR4 = models.IntegerField(null=False, default=None)
    SPR5 = models.IntegerField(null=False, default=None)
    SPR6 = models.IntegerField(null=False, default=None)


    def __str__(self):
        return "SPR_{}_{}".format(str(self.caseNum),str(self.time))


class SPR_Question(models.Model):
    SPR1 = models.CharField(max_length=200)
    SPR2 = models.CharField(max_length=200)
    SPR3 = models.CharField(max_length=200)
    SPR4 = models.CharField(max_length=200)
    SPR5 = models.CharField(max_length=200)
    SPR6 = models.CharField(max_length=200)


    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in SPR_Question._meta.fields]

    def __str__(self):
        return str(self.pk)

class R(models.Model):

    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    R1 = models.IntegerField(null=False, default=None)
    R2 = models.IntegerField(null=False, default=None)


    def __str__(self):
        return "R_{}_{}".format(str(self.caseNum),str(self.time))

class R_Question(models.Model):
    R1 = models.CharField(max_length=200)
    R2 = models.CharField(max_length=200)



    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in R_Question._meta.fields]

    def __str__(self):
        return str(self.pk)

class DM(models.Model):

    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()

    DM1 = models.IntegerField(null=False,default=None)
    DM1_1_year = models.IntegerField(default=0)
    DM1_1_month = models.IntegerField(default=0)
    DM1_1_days =  models.IntegerField(default=0)
    DM1_2=  models.IntegerField(default=0)
    DM1_3 = models.IntegerField(default=0)
    DM1_4 = models.IntegerField(default=0)
    DM2 =  models.IntegerField(default=0)
    DM3 =models.IntegerField(default=0)
    DM4 =models.IntegerField(default=0)
    DM5 =models.IntegerField(default=0)
    DM6 =models.IntegerField(default=0)
    DM7 =models.IntegerField(default=0)

    DM8 =models.IntegerField()

    DM9= models.IntegerField()
    DM9_1 = models.CharField(max_length=200, default="")
    DM10 = models.IntegerField()

    DM11_1 = models.IntegerField()
    DM11_2 = models.IntegerField()
    DM11_3 = models.IntegerField()
    DM11_4 = models.IntegerField()
    DM12_1 = models.IntegerField()
    DM12_3 = models.IntegerField()
    DM13 = models.IntegerField()

    DM14 = models.IntegerField()
    DM14_1 = models.CharField(max_length=200, default="")
    DM15 = models.IntegerField()

    DM16 = models.IntegerField()
    DM17 = models.IntegerField()
    DM18 = models.IntegerField()
    DM19 = models.IntegerField()

    def __str__(self):
        return "DM_{}_{}".format(str(self.caseNum),str(self.time))


class DM_Question(models.Model):
    DM1 = models.CharField(max_length=200)
    DM1_1_year = models.CharField(max_length=200)
    DM1_1_month =models.CharField(max_length=200)
    DM1_1_days = models.CharField(max_length=200)
    DM1_2 = models.CharField(max_length=200)
    DM1_3 =models.CharField(max_length=200)
    DM1_4 =models.CharField(max_length=200)
    DM2 = models.CharField(max_length=200)
    DM3 = models.CharField(max_length=200)
    DM4 = models.CharField(max_length=200)
    DM5 = models.CharField(max_length=200)
    DM6 = models.CharField(max_length=200)
    DM7 = models.CharField(max_length=200)
    DM8 = models.CharField(max_length=200)
    DM9 = models.CharField(max_length=200)
    DM9_1 = models.CharField(max_length=200)
    DM10 = models.CharField(max_length=200)
    DM11 = models.CharField(max_length=200)
    DM11_1 =  models.CharField(max_length=200)
    DM11_2 =  models.CharField(max_length=200)
    DM11_3 =  models.CharField(max_length=200)
    DM11_4 =  models.CharField(max_length=200)
    DM12 = models.CharField(max_length=200)
    DM12_1 = models.CharField(max_length=200)
    DM13 = models.CharField(max_length=200)
    DM14 = models.CharField(max_length=200)
    DM14_1 = models.CharField(max_length=200)
    DM15 = models.CharField(max_length=200)
    DM16 = models.CharField(max_length=200)
    DM17 = models.CharField(max_length=200)
    DM18 = models.CharField(max_length=200)
    DM19 = models.CharField(max_length=200)



    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in DM_Question._meta.fields]

    def __str__(self):
        return str(self.pk)

class Total_for_Admin(models.Model):

    caseNum= models.ForeignKey('Surveyee',on_delete=models.CASCADE)
    Agent = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    Time=models.IntegerField(null=False)
    Date = models.DateField()
    Health =models.FloatField(null=True)
    Community=models.FloatField(null=True)
    Childcare =models.FloatField(null=True)
    Jobskills =models.FloatField(null=True)
    SoftSkill =models.FloatField(null=True)
    Peb_all =models.FloatField(null=True)
    Empowerment =models.FloatField(null=True)
    Selfmotivation =models.FloatField(null=True)
    SkilResources =models.FloatField(null=True)
    GaolOrientation=models.FloatField(null=True)
    Ehs_all =models.FloatField(null=True)
    Ess1=models.FloatField(null=True)
    Ess2=models.FloatField(null=True)
    Ess3=models.FloatField(null=True)
    Ess4=models.FloatField(null=True)
    Ess_all=models.FloatField(null=True)
    PSS =models.FloatField(null=True)
    Resilience=models.FloatField(null=True)
    Self_Efficacy =models.FloatField(null=True)
    GR_Con =models.FloatField(null=True)
    GR_Per=models.FloatField(null=True)
    GR_all=models.FloatField(null=True)
    SPR_all=models.FloatField(null=True)
    F_self=models.FloatField(null=True)
    F_other=models.FloatField(null=True)
    F_situation=models.FloatField(null=True)
    F_all=models.FloatField(null=True)
    DM1 = models.IntegerField(null=False, default=None)
    DM1_1_year = models.IntegerField(default=0)
    DM1_1_month = models.IntegerField(default=0)
    DM1_1_days = models.IntegerField(default=0)
    DM1_2 = models.IntegerField(default=0)
    DM1_3 = models.IntegerField(default=0)
    DM1_4 = models.IntegerField(default=0)
    DM2 = models.IntegerField(default=0)
    DM3 = models.IntegerField(default=0)
    DM4 = models.IntegerField(default=0)
    DM5 = models.IntegerField(default=0)
    DM6 = models.IntegerField(default=0)
    DM7 = models.IntegerField(default=0)

    DM8 = models.IntegerField()

    DM9 = models.IntegerField()
    DM9_1 = models.CharField(max_length=200, default="")
    DM10 = models.IntegerField()

    DM11_1 = models.IntegerField()
    DM11_2 = models.IntegerField()
    DM11_3 = models.IntegerField()
    DM11_4 = models.IntegerField()
    DM12_1 = models.IntegerField()
    DM12_3 = models.IntegerField()
    DM13 = models.IntegerField()

    DM14 = models.IntegerField()
    DM14_1 = models.CharField(max_length=200, default="")
    DM15 = models.IntegerField()

    DM16 = models.IntegerField()
    DM17 = models.IntegerField()
    DM18 = models.IntegerField()
    DM19 = models.IntegerField()


    def __str__(self):
        return "TOTAL_{}_{}".format(str(self.caseNum),str(self.time))



