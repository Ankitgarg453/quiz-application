from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import View
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import QuestionAnswerModel, StudentDetails
from .forms import CreateUserForm, LoginForm, QuestionAnswerForm, StudentDetailsForm
from django.http import JsonResponse
# Create your views here.

#----------------- New User Register/ New User Creation View-------------------------
class UserCreationView(SuccessMessageMixin, CreateView):
    form_class = CreateUserForm
    success_message = 'User Created Successfully'
    warning_message = "User not created. Please check below fields again."
    template_name = 'quiz/usercreation_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, self.warning_message)
        return super().form_invalid(form)

# class LoginView(CreateView):
#     form_class = LoginForm
#     warning_message = "Credentials are incorrect."
#     template_name = 'quiz/login_form.html'
#     success_url = '/quiz/thankyou/'

#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         valid = super(LoginView, self).form_valid(form)
#         username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password')
#         new_user = authenticate(username=username, password=password)
#         login(self.request, new_user)
#         return valid

#     def form_invalid(self, form):
#         messages.warning(self.request, self.warning_message)
#         return super().form_invalid(form)


#-------------------------- Login a User with right Credentials---------------------------
class LoginView(View):
    def get(self, request):
        return render(request, 'quiz/login_form.html', {'form' : LoginForm()})
    
    def post(self, request):
        user_name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = user_name, password = password)
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                request.session['userid'] = user_name
            else:
                request.session['userid'] = user_name
            return redirect('/home/')
        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect('/login/')


# ---------------------- Main Home Page----------------------------------
def Home(request):
    if request.user.is_authenticated:
        return render(request, 'quiz/homepage.html')
    else:
        return redirect('/login/')


#***- - -******** * * * Questions Answers Views, Add, Update, Display, Delete * * * *****- - - ****
#-------------------- Add New Questions View-Start----------------------
class AddQuestionAnswerView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    redirect_field_name = 'redirect_to'
    login_url = '/login/'
    model = QuestionAnswerModel
    form_class = QuestionAnswerForm
    success_message = 'Your Question saved successfully. Please enter your new Question.'
    warning_message = 'Your Question is not saved. Please try once again with right data.'
    template_name = 'quiz/addupdatequestions.html'
    success_url = '/addQuestions/'

    # def get_context_data(self, *args, **kwargs):
    # '''In case we required to send any other data to html page, apart from this table. We will use this fun'''
    #     context = super().get_context_data(*args,**kwargs)
    #     context['schoolData'] = StudentDetails.objects.values('Student_School','Student_Class').filter(user=self.request.session.get('userid')).order_by('Student_Class')
    #     return context

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.user = str(self.request.user)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, self.warning_message)
        return super().form_invalid(form)

#-------------------- Questions Answers Display records View -------------------------
class QuestionAnswerDisplayListView(LoginRequiredMixin,ListView):
    redirect_field_name = 'redirect_to'
    login_url = '/login/'
    model = QuestionAnswerModel
    fields = ['Question_Unique_Id','question','answer1','answer2','answer3','answer4','answer5','Student_Class','Subject','rightanswer']
    template_name = 'quiz/questionanswermodel_list.html'

    def get_queryset(self):
        return QuestionAnswerModel.objects.filter(user = self.request.session.get('userid'))

#---------------- Update Questions Answers View and related data------------------------ 
class UpdateQuestionAnswersVeiw(LoginRequiredMixin,SuccessMessageMixin, UpdateView):
    redirect_field_name = 'redirect_to'
    login_url = '/login/'
    model = QuestionAnswerModel
    form_class = QuestionAnswerForm
    success_message = 'Your Question updated successfully.'
    warning_message = 'Your Question is not saved. Please try once again with right data.'
    template_name = 'quiz/addupdatequestions.html'
    success_url = '/list/'

    def form_valid(self, form):
        # form.instance.created_by = self.request.user
        form.instance.user = str(self.request.user)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, self.warning_message)
        return super().form_invalid(form)

#--------------- Question Answers Delete records View -----------------------
class QuestionAnswerDeleteRecordView(LoginRequiredMixin, DeleteView):
    redirect_field_name = 'redirect_to'
    login_url = '/login/'
    model = QuestionAnswerModel
    # template_name = 'quiz/deletequestion.html'
    success_url = '/list/'

    # def get_queryset(self):
    #     return QuestionAnswerModel.objects.values('question','Student_Class','Subject').filter(user = self.request.session.get('userid'))

#******************** - - - - -* * END * * - - - - - **********************



#*****- - - *** * * * Student Details View, Add New, Update, Display, Delete * * * *** - - -******
#------------------------- Add New Student View -----------------------
class AddNewStudentView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    redirect_field_name = 'redirect_to'
    login_url = '/login/'
    form_class = StudentDetailsForm
    success_message = 'Child added successfully.'
    warning_message = 'Invalid data error. Please try once again with right data.'
    template_name = 'quiz/studentdetails.html'
    success_url = '/studentDetails/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.user = str(self.request.user)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, self.warning_message)
        return super().form_invalid(form)

#--------------------- Display Students View ------------------------------
class DisplayAllStudentsListView(LoginRequiredMixin, ListView):
    redirect_field_name = 'redirect_to'
    login_url = '/login/'
    model = StudentDetails
    fields = ['Student_UniqueId','Student_Image','Student_First_Name','Student_Last_Name','Student_Birth_Date','Student_ParentMobile','Student_ParentEmail','Student_City','Student_School','Student_Class','Student_ClassGrade']
    template_name = 'quiz/studentlistview.html'

    def get_queryset(self):
        return StudentDetails.objects.values('Student_UniqueId','Student_Image','Student_First_Name','Student_Last_Name','Student_Birth_Date','Student_ParentMobile','Student_ParentEmail','Student_City','Student_School','Student_Class','Student_ClassGrade').filter(user = self.request.session.get('userid'))

#----------------------- Update Student Details View----------------------
class UpdateStudentsDetailsView(LoginRequiredMixin, UpdateView):
    redirect_field_name = 'redirect_to'
    login_url = '/login/'
    model = StudentDetails
    form_class = StudentDetailsForm
    warning_message = 'Invalid data error. Please try once again with right data.'
    template_name = 'quiz/studentdetails.html'
    success_url = '/stulist/'
    
    def form_invalid(self, form):
        messages.warning(self.request, self.warning_message)
        return super().form_invalid(form)

#---------------------- Delete Student record View ---------------------
class DeleteStudentRecordView(LoginRequiredMixin, DeleteView):
    redirect_field_name = 'redirect_to'
    login_url = '/login/'
    model = StudentDetails
    success_url = '/stulist/'

#******************** - - - - -* * END * * - - - - - **********************


# -------------- Exam for/by Student View --------------------
class StudentQuestionAnsweredView(LoginRequiredMixin,CreateView):
    redirect_field_name = 'redirect_to'
    login_url = '/login/'
    template_name = 'quiz/studentquestionanswered.html'

# ----------------- User Logout ------------------
def UserLogout(request):
    print(request.session.get('userid'))
    # del request.session['userid']
    logout(request)
    return redirect('/login/')

# ------------------- Dummy View -----------------
class ThanksTempalateView(TemplateView):
    template_name = 'quiz/thanks.html'