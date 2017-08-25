from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

##hi
##newline
#hellolow
# modified
### new new line
# Create your models here.
class Surveyee(models.Model):
    caseNum = models.IntegerField(unique=True, primary_key=True)
    agent_name = models.ForeignKey(User, on_delete=models.CASCADE,
                                   help_text="If you delete agent, you will lose all surveyees")

    def __str__(self):
        return str(self.caseNum)


class SurveyTimes(models.Model):
    choices = ((1, '1'), (2, '2'), (3, '3'), (4, '4'))
    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField(null=False, default=1, choices=choices)
    pub_Date = models.DateTimeField()

    def publish(self):
        self.pub_Date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.pk)


class EB(models.Model):
    choices = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    surveytime = models.IntegerField()
    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    EB1 = models.IntegerField(default=1, choices=choices)
    EB2 = models.IntegerField(default=1, choices=choices)
    EB3 = models.IntegerField(default=1, choices=choices)
    EB4 = models.IntegerField(default=1, choices=choices)
    EB5 = models.IntegerField(default=1, choices=choices)
    EB6 = models.IntegerField(default=1, choices=choices)
    EB7 = models.IntegerField(default=1, choices=choices)
    EB8 = models.IntegerField(default=1, choices=choices)
    EB9 = models.IntegerField(default=1, choices=choices)
    EB10 = models.IntegerField(default=1, choices=choices)
    EB11 = models.IntegerField(default=1, choices=choices)
    EB12 = models.IntegerField(default=1, choices=choices)
    EB13 = models.IntegerField(default=1, choices=choices)
    EB14 = models.IntegerField(default=1, choices=choices)
    EB15 = models.IntegerField(default=1, choices=choices)
    EB16 = models.IntegerField(default=1, choices=choices)
    EB17 = models.IntegerField(default=1, choices=choices)
    EB18 = models.IntegerField(default=1, choices=choices)
    EB19 = models.IntegerField(default=1, choices=choices)
    EB20 = models.IntegerField(default=1, choices=choices)
    EB21 = models.IntegerField(default=1, choices=choices)
    EB22 = models.IntegerField(default=1, choices=choices)
    EB23 = models.IntegerField(default=1, choices=choices)
    EB24 = models.IntegerField(default=1, choices=choices)
    EB25 = models.IntegerField(default=1, choices=choices)
    EB26 = models.IntegerField(default=1, choices=choices)
    EB27 = models.IntegerField(default=1, choices=choices)

    def __str__(self):
        return 'EB'+str(self.caseNum)+ '_' + str(self.time)


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
    choices = ((0, '0'),(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'))
    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    EH1 = models.IntegerField(null=False, default=None, choices=choices)
    EH2 = models.IntegerField(null=False, default=None, choices=choices)
    EH3 = models.IntegerField(null=False, default=None, choices=choices)
    EH4 = models.IntegerField(null=False, default=None, choices=choices)
    EH5 = models.IntegerField(null=False, default=None, choices=choices)
    EH6 = models.IntegerField(null=False, default=None, choices=choices)
    EH7 = models.IntegerField(null=False, default=None, choices=choices)
    EH8 = models.IntegerField(null=False, default=None, choices=choices)
    EH9 = models.IntegerField(null=False, default=None, choices=choices)
    EH10 = models.IntegerField(null=False, default=None, choices=choices)
    EH11 = models.IntegerField(null=False, default=None, choices=choices)
    EH12 = models.IntegerField(null=False, default=None, choices=choices)
    EH13 = models.IntegerField(null=False, default=None, choices=choices)
    EH14 = models.IntegerField(null=False, default=None, choices=choices)
    EH15 = models.IntegerField(null=False, default=None, choices=choices)
    EH16 = models.IntegerField(null=False, default=None, choices=choices)
    EH17 = models.IntegerField(null=False, default=None, choices=choices)
    EH18 = models.IntegerField(null=False, default=None, choices=choices)
    EH19 = models.IntegerField(null=False, default=None, choices=choices)
    EH20 = models.IntegerField(null=False, default=None, choices=choices)
    EH21 = models.IntegerField(null=False, default=None, choices=choices)
    EH22 = models.IntegerField(null=False, default=None, choices=choices)
    EH23 = models.IntegerField(null=False, default=None, choices=choices)
    EH24 = models.IntegerField(null=False, default=None, choices=choices)

    def __str__(self):
        return 'EH'+str(self.caseNum)+ '_' + str(self.time)


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
    choices = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    ES1 = models.IntegerField(null=False, default=None, choices=choices)
    ES2 = models.IntegerField(null=False, default=None, choices=choices)
    ES3 = models.IntegerField(null=False, default=None, choices=choices)
    ES4 = models.IntegerField(null=False, default=None, choices=choices)
    ES5 = models.IntegerField(null=False, default=None, choices=choices)
    ES6 = models.IntegerField(null=False, default=None, choices=choices)
    ES7 = models.IntegerField(null=False, default=None, choices=choices)
    ES8 = models.IntegerField(null=False, default=None, choices=choices)
    ES9 = models.IntegerField(null=False, default=None, choices=choices)
    ES10 = models.IntegerField(null=False, default=None, choices=choices)
    ES11 = models.IntegerField(null=False, default=None, choices=choices)
    ES12 = models.IntegerField(null=False, default=None, choices=choices)
    ES13 = models.IntegerField(null=False, default=None, choices=choices)
    ES14 = models.IntegerField(null=False, default=None, choices=choices)
    ES15 = models.IntegerField(null=False, default=None, choices=choices)

    def __str__(self):
        return 'ES'+str(self.caseNum)+ '_' + str(self.time)

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
    choices = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'))
    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    TIP1 = models.IntegerField(null=False, default=None, choices=choices)
    TIP2 = models.IntegerField(null=False, default=None, choices=choices)
    TIP3 = models.IntegerField(null=False, default=None, choices=choices)
    TIP4 = models.IntegerField(null=False, default=None, choices=choices)
    TIP5 = models.IntegerField(null=False, default=None, choices=choices)
    TIP6 = models.IntegerField(null=False, default=None, choices=choices)
    TIP7 = models.IntegerField(null=False, default=None, choices=choices)
    TIP8 = models.IntegerField(null=False, default=None, choices=choices)
    TIP9 = models.IntegerField(null=False, default=None, choices=choices)
    TIP10 = models.IntegerField(null=False, default=None, choices=choices)
    TIP11 = models.IntegerField(null=False, default=None, choices=choices)
    TIP12 = models.IntegerField(null=False, default=None, choices=choices)
    TIP13 = models.IntegerField(null=False, default=None, choices=choices)
    TIP14 = models.IntegerField(null=False, default=None, choices=choices)
    TIP15 = models.IntegerField(null=False, default=None, choices=choices)

    def __str__(self):
        return 'TIP'+str(self.caseNum)+ '_' + str(self.time)

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
    choices = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'))
    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    A3 = models.IntegerField(null=False, default=None, choices=choices)
    B3 = models.IntegerField(null=False, default=None, choices=choices)
    C3 = models.IntegerField(null=False, default=None, choices=choices)
    D3 = models.IntegerField(null=False, default=None, choices=choices)
    E2 = models.IntegerField(null=False, default=None, choices=choices)
    F2 = models.IntegerField(null=False, default=None, choices=choices)
    G1 = models.IntegerField(null=False, default=None, choices=choices)
    H3 = models.IntegerField(null=False, default=None, choices=choices)
    I2 = models.IntegerField(null=False, default=None, choices=choices)
    J3 = models.IntegerField(null=False, default=None, choices=choices)
    K1 = models.IntegerField(null=False, default=None, choices=choices)
    K2 = models.IntegerField(null=False, default=None, choices=choices)
    K3 = models.IntegerField(null=False, default=None, choices=choices)
    L1 = models.IntegerField(null=False, default=None, choices=choices)
    L2 = models.IntegerField(null=False, default=None, choices=choices)
    L3 = models.IntegerField(null=False, default=None, choices=choices)

    def __str__(self):
        return 'TIP'+str(self.caseNum)+ '_' + str(self.time)

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
    choices = ((1, '1'), (2, '2'), (3, '3'), (4, '4'))
    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    SSP1 = models.IntegerField(null=False, default=None, choices=choices)
    SSP2 = models.IntegerField(null=False, default=None, choices=choices)
    SSP3 = models.IntegerField(null=False, default=None, choices=choices)
    SSP4 = models.IntegerField(null=False, default=None, choices=choices)
    SSP5 = models.IntegerField(null=False, default=None, choices=choices)
    SSP6 = models.IntegerField(null=False, default=None, choices=choices)
    SSP7 = models.IntegerField(null=False, default=None, choices=choices)
    SSP8 = models.IntegerField(null=False, default=None, choices=choices)
    SSP9 = models.IntegerField(null=False, default=None, choices=choices)
    SSP10 = models.IntegerField(null=False, default=None, choices=choices)
    SSP11 = models.IntegerField(null=False, default=None, choices=choices)
    SSP12 = models.IntegerField(null=False, default=None, choices=choices)


    def __str__(self):
        return 'ES'+str(self.caseNum)+ '_' + str(self.time)

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
    choices = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'))
    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    F1 = models.IntegerField(null=False, default=None, choices=choices)
    F2 = models.IntegerField(null=False, default=None, choices=choices)
    F3 = models.IntegerField(null=False, default=None, choices=choices)
    F4 = models.IntegerField(null=False, default=None, choices=choices)
    F5 = models.IntegerField(null=False, default=None, choices=choices)
    F6 = models.IntegerField(null=False, default=None, choices=choices)
    F7 = models.IntegerField(null=False, default=None, choices=choices)
    F8 = models.IntegerField(null=False, default=None, choices=choices)
    F9 = models.IntegerField(null=False, default=None, choices=choices)
    F10 = models.IntegerField(null=False, default=None, choices=choices)
    F11 = models.IntegerField(null=False, default=None, choices=choices)
    F12 = models.IntegerField(null=False, default=None, choices=choices)
    F13 = models.IntegerField(null=False, default=None, choices=choices)
    F14 = models.IntegerField(null=False, default=None, choices=choices)
    F15 = models.IntegerField(null=False, default=None, choices=choices)
    F16 = models.IntegerField(null=False, default=None, choices=choices)
    F17 = models.IntegerField(null=False, default=None, choices=choices)
    F18 = models.IntegerField(null=False, default=None, choices=choices)

    def __str__(self):
        return 'F'+str(self.caseNum)+ '_' + str(self.time)

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
    choices = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'))
    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    GD1 = models.IntegerField(null=False, default=None, choices=choices)
    GD2 = models.IntegerField(null=False, default=None, choices=choices)
    GD3 = models.IntegerField(null=False, default=None, choices=choices)
    GD4 = models.IntegerField(null=False, default=None, choices=choices)
    GD5 = models.IntegerField(null=False, default=None, choices=choices)
    GD6 = models.IntegerField(null=False, default=None, choices=choices)


    def __str__(self):
        return 'GD'+str(self.caseNum)+ '_' + str(self.time)

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
    choices = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    HM1 = models.IntegerField(null=False, default=None, choices=choices)
    HM2 = models.IntegerField(null=False, default=None, choices=choices)
    HM3 = models.IntegerField(null=False, default=None, choices=choices)
    HM4 = models.IntegerField(null=False, default=None, choices=choices)
    HM5 = models.IntegerField(null=False, default=None, choices=choices)
    HM6 = models.IntegerField(null=False, default=None, choices=choices)
    HM7 = models.IntegerField(null=False, default=None, choices=choices)
    HM8 = models.IntegerField(null=False, default=None, choices=choices)
    HM9 = models.IntegerField(null=False, default=None, choices=choices)
    HM10 = models.IntegerField(null=False, default=None, choices=choices)
    HM11 = models.IntegerField(null=False, default=None, choices=choices)
    HM12 = models.IntegerField(null=False, default=None, choices=choices)
    HM13 = models.IntegerField(null=False, default=None, choices=choices)
    HM14 = models.IntegerField(null=False, default=None, choices=choices)
    HM15 = models.IntegerField(null=False, default=None, choices=choices)

    def __str__(self):
        return 'HM'+str(self.caseNum)+ '_' + str(self.time)

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
    choices = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    HEALTH1 = models.IntegerField(null=False, default=None, choices=choices)
    HEALTH2 = models.IntegerField(null=False, default=None, choices=choices)


    def __str__(self):
        return 'HEALTH'+str(self.caseNum)+ '_' + str(self.time)

class HEALTH_Question(models.Model):
    HEALTH1 = models.CharField(max_length=200)
    HEALTH2 = models.CharField(max_length=200)



    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in HEALTH_Question._meta.fields]

    def __str__(self):
        return str(self.pk)

class SEF(models.Model):
    choices = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    SEF1 = models.IntegerField(null=False, default=None, choices=choices)
    SEF2 = models.IntegerField(null=False, default=None, choices=choices)
    SEF3 = models.IntegerField(null=False, default=None, choices=choices)
    SEF4 = models.IntegerField(null=False, default=None, choices=choices)
    SEF5 = models.IntegerField(null=False, default=None, choices=choices)
    SEF6 = models.IntegerField(null=False, default=None, choices=choices)
    SEF7 = models.IntegerField(null=False, default=None, choices=choices)
    SEF8 = models.IntegerField(null=False, default=None, choices=choices)


    def __str__(self):
        return 'SEF'+str(self.caseNum)+ '_' + str(self.time)

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
    choices = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    GR1 = models.IntegerField(null=False, default=None, choices=choices)
    GR2 = models.IntegerField(null=False, default=None, choices=choices)
    GR3 = models.IntegerField(null=False, default=None, choices=choices)
    GR4 = models.IntegerField(null=False, default=None, choices=choices)
    GR5 = models.IntegerField(null=False, default=None, choices=choices)
    GR6 = models.IntegerField(null=False, default=None, choices=choices)
    GR7 = models.IntegerField(null=False, default=None, choices=choices)
    GR8 = models.IntegerField(null=False, default=None, choices=choices)

    def __str__(self):
        return 'GR' + str(self.caseNum) + '_' + str(self.time)


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
    choices = ((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'))
    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    SPR1 = models.IntegerField(null=False, default=None, choices=choices)
    SPR2 = models.IntegerField(null=False, default=None, choices=choices)
    SPR3 = models.IntegerField(null=False, default=None, choices=choices)
    SPR4 = models.IntegerField(null=False, default=None, choices=choices)
    SPR5 = models.IntegerField(null=False, default=None, choices=choices)
    SPR6 = models.IntegerField(null=False, default=None, choices=choices)


    def __str__(self):
        return 'SPR' + str(self.caseNum) + '_' + str(self.time)


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
    choices = ( (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'))
    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()
    R1 = models.IntegerField(null=False, default=None, choices=choices)
    R2 = models.IntegerField(null=False, default=None, choices=choices)


    def __str__(self):
        return 'R'+str(self.caseNum)+ '_' + str(self.time)

class R_Question(models.Model):
    R1 = models.CharField(max_length=200)
    R2 = models.CharField(max_length=200)



    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in R_Question._meta.fields]

    def __str__(self):
        return str(self.pk)

class DM(models.Model):
    choices = (( 1,'YES'), (0,'NO'))
    caseNum = models.ForeignKey('Surveyee', on_delete=models.CASCADE)
    time = models.IntegerField()
    surveytime = models.IntegerField()

    DM1 = models.IntegerField(null=False,default=None, choices=choices)
    DM1_1_year = models.IntegerField(default=0)
    DM1_1_month = models.IntegerField(default=0)
    DM1_1_days =  models.IntegerField(default=0)
    DM1_2=  models.IntegerField(default=0)
    DM1_3 = models.IntegerField(default=0, choices=choices)
    DM1_4 = models.IntegerField(default=0, choices=choices)
    DM2 =  models.IntegerField(default=0, choices=choices)
    DM3 =models.IntegerField(default=0)
    DM4 =models.IntegerField(default=0)
    DM5 =models.IntegerField(default=0)
    DM6 =models.IntegerField(default=0)
    DM7 =models.IntegerField(default=0)
    choices8 = ((0, 'Married, spouse present'), (1, 'Married, spouse absent'), (2, 'Never married'), (3, 'Sperated'), (4, 'Divorced'), (5, 'Widowed'))
    DM8 =models.IntegerField(choices=choices8)
    choices9 = ((0, 'Rental'), (1, 'Own home'), (2, 'Homeless'), (3, 'Public Housing'),
                (4, 'Other'), (5, 'Living with family or friend'))
    DM9= models.IntegerField(choices=choices9)
    DM9_1 = models.CharField(max_length=200, default="")
    DM10 = models.IntegerField(choices=choices)
    choices11 = ((0, 'Worse'), (1, 'Same'), (2, 'Better'), (3, 'Do Not Know'))
    DM11_1 = models.IntegerField(choices=choices11)
    DM11_2 = models.IntegerField(choices=choices11)
    DM11_3 = models.IntegerField(choices=choices11)
    DM11_4 = models.IntegerField(choices=choices11)
    DM12_1 = models.IntegerField()
    DM12_3 = models.IntegerField()
    DM13 = models.IntegerField(choices=choices)
    choices14 = ((0, 'Native American or Alaska Native'), (1, 'Asian or Pacific Islande'), (2, 'Black or African American'), (3, 'White or European American'),
                (4, 'Non-White Hispanic'), (5, 'Bi- / multi-racial'),(6, 'Other'))
    DM14 = models.IntegerField(choices=choices14)
    DM14_1 = models.CharField(max_length=200, default="")
    DM15 = models.IntegerField()
    choices16 = (
    (0, 'Less than High School'), (1, 'High-School / GED'), (2, 'Some College but no degree'),
    (3, 'Diploma or certificate from vocational, technical or trade school'),
    (4, 'Associates Degree'), (5, 'Bachelors Degree'), (6, 'Masters Degree'), (7, ' Professional School Degree'), (8, 'Doctorate'))
    DM16 = models.IntegerField(choices=choices16)
    DM17 = models.IntegerField()
    DM18 = models.IntegerField()
    DM19 = models.IntegerField()

    def __str__(self):
        return 'DM'+str(self.caseNum)+ '_' + str(self.time)


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
    choices = ((1, 'YES'), (0, 'NO'))
    caseNum= models.ForeignKey('Surveyee')
    Agent = models.ForeignKey(User)
    Time=models.IntegerField(null=False)
    Date = models.DateField()
    Health =models.FloatField(null=False)
    Community=models.FloatField(null=False)
    Childcare =models.FloatField(null=False)
    Jobskills =models.FloatField(null=False)
    SoftSkill =models.FloatField(null=False)
    Peb_all =models.FloatField(null=False)
    Empowerment =models.FloatField(null=False)
    Selfmotivation =models.FloatField(null=False)
    SkilResources =models.FloatField(null=False)
    GaolOrientation=models.FloatField(null=False)
    Ehs_all =models.FloatField(null=False)
    Ess1=models.FloatField(null=False)
    Ess2=models.FloatField(null=False)
    Ess3=models.FloatField(null=False)
    Ess4=models.FloatField(null=False)
    Ess_all=models.FloatField(null=False)
    PSS =models.FloatField(null=False)
    Resilience=models.FloatField(null=False)
    Self_Efficacy =models.FloatField(null=False)
    GR_Con =models.FloatField(null=False)
    GR_Per=models.FloatField(null=False)
    GR_all=models.FloatField(null=False)
    SPR_all=models.FloatField(null=False)
    F_self=models.FloatField(null=False)
    F_other=models.FloatField(null=False)
    F_situation=models.FloatField(null=False)
    F_all=models.FloatField(null=False)
    DM1 = models.IntegerField(null=False, default=None, choices=choices)
    DM1_1_year = models.IntegerField(default=0)
    DM1_1_month = models.IntegerField(default=0)
    DM1_1_days = models.IntegerField(default=0)
    DM1_2 = models.IntegerField(default=0)
    DM1_3 = models.IntegerField(default=0, choices=choices)
    DM1_4 = models.IntegerField(default=0, choices=choices)
    DM2 = models.IntegerField(default=0, choices=choices)
    DM3 = models.IntegerField(default=0)
    DM4 = models.IntegerField(default=0)
    DM5 = models.IntegerField(default=0)
    DM6 = models.IntegerField(default=0)
    DM7 = models.IntegerField(default=0)
    choices8 = ((0, 'Married, spouse present'), (1, 'Married, spouse absent'), (2, 'Never married'), (3, 'Sperated'),
                (4, 'Divorced'), (5, 'Widowed'))
    DM8 = models.IntegerField(choices=choices8)
    choices9 = ((0, 'Rental'), (1, 'Own home'), (2, 'Homeless'), (3, 'Public Housing'),
                (4, 'Other'), (5, 'Living with family or friend'))
    DM9 = models.IntegerField(choices=choices9)
    DM9_1 = models.CharField(max_length=200, default="")
    DM10 = models.IntegerField(choices=choices)
    choices11 = ((0, 'Worse'), (1, 'Same'), (2, 'Better'), (3, 'Do Not Know'))
    DM11_1 = models.IntegerField(choices=choices11)
    DM11_2 = models.IntegerField(choices=choices11)
    DM11_3 = models.IntegerField(choices=choices11)
    DM11_4 = models.IntegerField(choices=choices11)
    DM12_1 = models.IntegerField()
    DM12_3 = models.IntegerField()
    DM13 = models.IntegerField(choices=choices)
    choices14 = (
    (0, 'Native American or Alaska Native'), (1, 'Asian or Pacific Islande'), (2, 'Black or African American'),
    (3, 'White or European American'),
    (4, 'Non-White Hispanic'), (5, 'Bi- / multi-racial'), (6, 'Other'))
    DM14 = models.IntegerField(choices=choices14)
    DM14_1 = models.CharField(max_length=200, default="")
    DM15 = models.IntegerField()
    choices16 = (
        (0, 'Less than High School'), (1, 'High-School / GED'), (2, 'Some College but no degree'),
        (3, 'Diploma or certificate from vocational, technical or trade school'),
        (4, 'Associates Degree'), (5, 'Bachelors Degree'), (6, 'Masters Degree'), (7, ' Professional School Degree'),
        (8, 'Doctorate'))
    DM16 = models.IntegerField(choices=choices16)
    DM17 = models.IntegerField()
    DM18 = models.IntegerField()
    DM19 = models.IntegerField()


    def __str__(self):
        return str(self.caseNum)+"_"+str(self.Time)



