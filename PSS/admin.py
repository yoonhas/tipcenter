from django.contrib import admin
from .models import Surveyee, SurveyTimes,EB,EH_Question,EH, ES_Question, Tip,Tip_Question,EXF_Question
from .models import F_Question, GD_Question, GR_Question, HEALTH_Question, R_Question, SEF_Question, SPR_Question, SSP_Question, HM_Question
from .models import EXF, F, GD, GR, HEALTH, R, SEF, SPR, SSP, HM, EB_Question, DM, DM_Question,Total_for_Admin, Image
from .models import TIPI, TIPI_Question, GENB,GENB_Question,K6,K6_Question, EH_Short_Question
# Register your models here.
admin.site.register(Surveyee)
admin.site.register(SurveyTimes)
admin.site.register(EB)
admin.site.register(EH)
admin.site.register(EH_Question)
admin.site.register(ES_Question)
admin.site.register(Tip_Question)
admin.site.register(EXF_Question)
admin.site.register(F_Question)
admin.site.register(GD_Question)
admin.site.register(GR_Question)
admin.site.register(HEALTH_Question)
admin.site.register(R_Question)
admin.site.register(SEF_Question)
admin.site.register(SPR_Question)
admin.site.register(SSP_Question)
admin.site.register(HM_Question)
admin.site.register(GENB_Question)
admin.site.register(K6_Question)
admin.site.register(TIPI_Question)
admin.site.register(TIPI)
admin.site.register(GENB)
admin.site.register(K6)
admin.site.register(EXF)
admin.site.register(F)
admin.site.register(GD)
admin.site.register(GR)
admin.site.register(HEALTH)
admin.site.register(R)
admin.site.register(SEF)
admin.site.register(SPR)
admin.site.register(SSP)
admin.site.register(HM)
admin.site.register(EB_Question)
admin.site.register(DM)
admin.site.register(DM_Question)
admin.site.register(Tip)
admin.site.register(Total_for_Admin)
admin.site.register(Image)
admin.site.register(EH_Short_Question)