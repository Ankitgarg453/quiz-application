from django.urls import path
from quizapp.views import LoginView,UserCreationView,ThanksTempalateView, UserLogout,ScheduleExamView,AddNewStudentView,Home,  DisplayAllStudentsListView, UpdateStudentsDetailsView, DeleteStudentRecordView, AddQuestionAnswerView,  UpdateQuestionAnswersVeiw,QuestionAnswerDeleteRecordView, QuestionAnswerDisplayListView

app_name = 'quizapp'

urlpatterns = [
    path('', UserCreationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='userlogin'),
    path('logout/',UserLogout, name = 'userlogout'),
    path('home/', Home, name='home'),
    path('addQuestions/', AddQuestionAnswerView.as_view(), name = 'addQuestions'),
    path('studentDetails/',AddNewStudentView.as_view(), name='student_details'),
    path('list/', QuestionAnswerDisplayListView.as_view(), name = 'questions_list'),
    path('edit/<str:pk>', UpdateQuestionAnswersVeiw.as_view(), name='edit_record'),
    path('delete/<str:pk>', QuestionAnswerDeleteRecordView.as_view() , name='question_delete'),
    path('stulist/', DisplayAllStudentsListView.as_view(), name= 'students_list'),
    path('edit-details/<str:pk>',UpdateStudentsDetailsView.as_view(), name='edit_student_details'),
    path('delete-record/<str:pk>',DeleteStudentRecordView.as_view(), name = 'delete_student_record'),
    path('exam/',ScheduleExamView.as_view(), name='schedulexam'),
    path('thankyou/', ThanksTempalateView.as_view(), name='thanks'),
] 