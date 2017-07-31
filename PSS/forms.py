from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import EH, EB
from django.utils.safestring import mark_safe


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user




class EB_Form(forms.ModelForm):


    class Meta:
        question = ["1: Having less than high school education.", "2: Work limiting health conditions (illness / injury).",
                    "3: Lack of adequate job skills", "4: Lack of job experience", "5: Lack of transportation.",
                    "6: Lack of child care.",
                    "7: Racial discrimination.", "8: Lack of information about jobs.", "9: Lack of stable housing.",
                    "10: Drug / alcohol addiction.",
                    "11: Domestic violence.", "12: Physical disabilities", "13: Mental illness", "14: Fear of rejection",
                    "15: Lack of work clothing",
                    "16: No jobs in the community", "17: No jobs that match my skills / training", "18: Being a single parent.",
                    "19: Need to take care of young children. ", "20: Cannot speak English very well",
                    "21: Cannot read or write very well.",
                    "22: Problems with getting to job on time.", "23: Lack of confidence.", "24: Lack of support system.",
                    "25: Lack of coping skills for daily struggles", "26: Anger management", "27: Past criminal record."]
        model = EB
        fields = ('EB1','EB2','EB3','EB4','EB5','EB6','EB7','EB8','EB9','EB10','EB11','EB12','EB13','EB14','EB15',
                'EB16', 'EB17', 'EB18', 'EB19', 'EB20', 'EB21', 'EB22', 'EB23', 'EB24', 'EB25','EB26', 'EB27')
        widgets ={'EB1':forms.RadioSelect,'EB2':forms.RadioSelect,
                  'EB3':forms.RadioSelect,'EB4':forms.RadioSelect,'EB5':forms.RadioSelect,'EB6':forms.RadioSelect,
                  'EB7':forms.RadioSelect,'EB8':forms.RadioSelect,
                 'EB9':forms.RadioSelect,'EB10':forms.RadioSelect,'EB11':forms.RadioSelect,'EB12':forms.RadioSelect,
                  'EB13':forms.RadioSelect,'EB14':forms.RadioSelect,'EB15':forms.RadioSelect,
                'EB16':forms.RadioSelect, 'EB17':forms.RadioSelect, 'EB18':forms.RadioSelect, 'EB19':forms.RadioSelect,
                  'EB20':forms.RadioSelect, 'EB21':forms.RadioSelect, 'EB22':forms.RadioSelect, 'EB23':forms.RadioSelect,
                  'EB24':forms.RadioSelect, 'EB25':forms.RadioSelect,'EB26':forms.RadioSelect, 'EB27':forms.RadioSelect}
        labels ={'EB1':question[0],'EB2':question[1],'EB3':question[2],'EB4':question[3],'EB5':question[4],
                 'EB6': question[5],'EB7':question[6],'EB8':question[7],'EB9':question[8],'EB10':question[9],
                 'EB11': question[10],'EB12':question[11],'EB13':question[12],'EB14':question[13],'EB15':question[14],
                 'EB16': question[15],'EB17':question[16],'EB18':question[17],'EB19':question[18],'EB20':question[19],
                 'EB21': question[20],'EB22':question[21],'EB23':question[22],'EB24':question[23],'EB25':question[24],
                 'EB26': question[25],'EB27':question[26]}






class EH_Form(forms.ModelForm):

    class Meta:
        question =[ "1.  Thinking about working, I feel confident about myself.", "2.  I feel that I am good enough for any jobs out there.",
                    "3.  When working or looking for a job, I am respectful towards who I am.", "4.  I am worthy of working in a good job.",
                    "5.  I am capable of working in a good job.", "6.  I have the strength to overcome any obstacles when it comes to working.",
                    "7.  I can work in any job I want.", "8.  I am good at doing anything in the job if I set my mind to it.",
                    "9.  I feel positive about how I will do in my future job situation.", "10.  I don’t worry about falling behind bills in my future job.",
                    "11.  I am going to be working in a career job.", "12.  I will be in a better position in my future job than where I am now.",
                    "13.  I am able to tell myself to take steps toward reaching career goals.", "14.  I am committed to reaching my career goals. ",
                    "15.  I feel energized when I think about future achievement with my job.", "16.  I am willing to give my best effort to reach my career goals.",
                    "17.  I am aware of what my skills are to be employed in a good job.", "18.  I am aware of what my resources are to be employed in a good job.",
                    "19.  I am able to utilize my skills to move toward career goals.", "20.  I am able to utilize my resources to move toward career goals.",
                    "21.  I am on the road toward my career goals.", "22.  I am in the process of moving forward toward reaching my goals.",
                    "23.  Even if I am not able to achieve my financial goals right away, I will find a way to get there.",
                    "24.  My current path will take me to where I need to be in my career."
        ]
        model= EH
        fields = (
        'EH1', 'EH2', 'EH3', 'EH4', 'EH5', 'EH6', 'EH7', 'EH8', 'EH9', 'EH10', 'EH11', 'EH12',
        'EH13', 'EH14', 'EH15',
        'EH16', 'EH17', 'EH18', 'EH19', 'EH20', 'EH21', 'EH22', 'EH23', 'EH24')
        widgets = {'EH1': forms.RadioSelect, 'EH2': forms.RadioSelect,
                   'EH3': forms.RadioSelect, 'EH4': forms.RadioSelect, 'EH5': forms.RadioSelect,
                   'EH6': forms.RadioSelect,
                   'EH7': forms.RadioSelect, 'EH8': forms.RadioSelect,
                   'EH9': forms.RadioSelect, 'EH10': forms.RadioSelect, 'EH11': forms.RadioSelect,
                   'EH12': forms.RadioSelect,
                   'EH13': forms.RadioSelect, 'EH14': forms.RadioSelect, 'EH15': forms.RadioSelect,
                   'EH16': forms.RadioSelect, 'EH17': forms.RadioSelect, 'EH18': forms.RadioSelect,
                   'EH19': forms.RadioSelect,
                   'EH20': forms.RadioSelect, 'EH21': forms.RadioSelect, 'EH22': forms.RadioSelect,
                   'EH23': forms.RadioSelect,
                   'EH24': forms.RadioSelect}
        labels = {'EH1': question[0], 'EH2': question[1], 'EH3': question[2], 'EH4': question[3], 'EH5': question[4],
                  'EH6': question[5], 'EH7': question[6], 'EH8': question[7], 'EH9': question[8], 'EH10': question[9],
                  'EH11': question[10], 'EH12': question[11], 'EH13': question[12], 'EH14': question[13],
                  'EH15': question[14],
                  'EH16': question[15], 'EH17': question[16], 'EH18': question[17], 'EH19': question[18],
                  'EH20': question[19],
                  'EH21': question[20], 'EH22': question[21], 'EH23': question[22], 'EH24': question[23]}