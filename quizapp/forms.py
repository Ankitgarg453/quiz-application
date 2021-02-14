from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import QuestionAnswerModel, StudentDetails

Class_Choice = [('','Select'),
    ('UKG','UKG'),
('LKG','LKG'),
('Pre-Primary','Pre-Primary'),
('KG','KG'),
('1','1st'),
('2','2nd'),
('3','3rd'),
('4','4th'),
('5','5th'),
('6','6th'),
('7','7th'),
('8','8th'),
('9','9th'),
('10','10th'),
('Other','Other')
]

Answer_Choice = [('', 'Select'),
('1','Option 1st is the right answer'),
('2','Option 2nd is the right answer'),
('3','Option 3rd is the right answer'),
('4','Option 4th is the right answer'),
('5','Option 5th is the right answer')]

Subject_Choice = [('', 'Select'),
    ('English','English'),
('Math','Mathematics'),
('EVS','EVS'),
('Science','Science'),
('Physics','Physics'),
('SocialScience','Social Science'),
('Biology','Biology')]

class CreateUserForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder' : 'Password' }))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder' : 'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email']
        labels = {
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'email' : 'Email',
        }
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Username'}),
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Last Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder' : 'Email'}),
        }
    def __init__(self, *args, **kwargs):#this function gives SELECT will come at dropdown rather empty(1)--.
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class' : 'form-control', 'placeholder' : 'Username'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class' : 'form-control', 'placeholder' : 'Password'}),
    )

class QuestionAnswerForm(forms.ModelForm):
    class Meta:
        model = QuestionAnswerModel
        fields = ('Student_Class','Subject','Question','Answer_1','Answer_2','Answer_3','Answer_4','Answer_5','Rightanswer')
        labels = {
            'Student_Class': 'Select Class',
            'Subject' : 'Subject',
            'Question':'Question:',
            'Answer_1':'Option 1:',
            'Answer_2':'Option 2:',
            'Answer_3':'Option 3:',
            'Answer_4':'Option 4:',
            'Answer_5':'Option 5:',
            'Rightanswer': 'Answer:'
        }
        widgets = {
            'Student_Class': forms.Select(choices= Class_Choice, attrs={'class':'form-control'}),
            'Subject' : forms.Select(choices=Subject_Choice,attrs={'class':'form-control'}),
            'Question':forms.Textarea(attrs={'rows':4,'class':'form-control'}),
            'Answer_1':forms.TextInput(attrs={'class':'form-control'}),
            'Answer_2':forms.TextInput(attrs={'class':'form-control'}),
            'Answer_3':forms.TextInput(attrs={'class':'form-control'}),
            'Answer_4':forms.TextInput(attrs={'class':'form-control'}),
            'Answer_5':forms.TextInput(attrs={'class':'form-control'}),
            'Rightanswer':forms.Select(choices=Answer_Choice,attrs={'class':'form-control'}),
        }
    # def clean(self):
    # '''While data gets insert from user and then to convert that data into lower case or in Upper case in that case we can use this function.'''
    #    for field, value in self.cleaned_data.items():
    #        self.cleaned_data['field'] = value.lower()


class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        fields = ('Student_Image','Student_First_Name','Student_Last_Name','Student_Birth_Date','Student_MotherName','Student_FatherName','Student_ParentMobile','Student_AlterMobile','Student_ParentEmail','Student_State','Student_City','Student_School','Student_Class','Student_ClassGrade')  
        labels = {
            'Student_Image' : 'Image',
            'Student_First_Name' : 'First Name',
            'Student_Last_Name' : 'Last Name',
            'Student_Birth_Date' : 'Birth Date',
            # 'Student_Age' : 'Age',
            'Student_MotherName' : 'Mother Name',
            'Student_FatherName' : 'Father Name',
            'Student_ParentMobile' : 'Parent Contact',
            'Student_AlterMobile' : 'Alter Mobile',
            'Student_ParentEmail' : 'Parent Email',
            'Student_State' : 'State',
            'Student_City' : 'City',
            'Student_School' : 'School',
            'Student_Class' : 'Class',
            'Student_ClassGrade' : 'Class Grade'
        }
        widgets={  
            #'answer1':forms.TextInput(attrs={'class':'form-control'}),
            # 'Student_Image' : forms.(attrs={}),
            'Student_First_Name': forms.TextInput(attrs={'class':'form-control'}),
            'Student_Last_Name' :forms.TextInput(attrs={'class':'form-control'}),
            'Student_Birth_Date' : forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control datetimepicker-input','placeholder':'yyyy-mm-dd'}),
            # 'Student_Age' : forms.TextInput(attrs={'class':'form-control'}),
            'Student_MotherName' :forms.TextInput(attrs={'class':'form-control'}),
            'Student_FatherName' : forms.TextInput(attrs={'class':'form-control'}),
            'Student_ParentMobile' : forms.TextInput(attrs={'class':'form-control'}),
            'Student_AlterMobile' : forms.TextInput(attrs={'class':'form-control'}),
            'Student_ParentEmail' :forms.EmailInput(attrs={'class':'form-control'}),
            'Student_State' : forms.TextInput(attrs={'class':'form-control'}),
            'Student_City' :forms.TextInput(attrs={'class':'form-control'}),
            'Student_School' : forms.TextInput(attrs={'class':'form-control'}),
            'Student_Class' : forms.Select(choices= Class_Choice, attrs={'class':'form-control', 'placeholder':'Select Class'}),
            'Student_ClassGrade' :forms.TextInput(attrs={'class':'form-control'})
        }
        
    def __init__(self, *args, **kwargs):#this function gives SELECT will come at dropdown rather empty(1)--.
        super(StudentDetailsForm, self).__init__(*args, **kwargs)
        self.fields['Student_Class'].empty_label='Select'
        self.fields['Student_AlterMobile'].required = False
        # self.fields['Student_Image'].required = False
    