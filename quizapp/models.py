from django.db import models
import secrets 
import string 
# Create your models here.

class StudentDetails(models.Model):
    Student_UniqueId = models.CharField(max_length=150, primary_key=True, null=False)
    Student_Image = models.ImageField(upload_to='quiz/students/images')
    Student_First_Name = models.CharField(max_length=100, null=False)
    Student_Last_Name = models.CharField(max_length=100, null=False)
    Student_Birth_Date = models.DateField(null=False)
    # Student_Age = models.IntegerField()
    Student_MotherName = models.CharField(max_length=85, null=False)
    Student_FatherName = models.CharField(max_length=85, null=False)
    Student_ParentMobile = models.CharField(max_length=10, null=False)
    Student_AlterMobile = models.CharField(max_length=10)
    Student_ParentEmail = models.EmailField(max_length=250, null=False)
    Student_State = models.CharField(max_length=100, null=False)
    Student_City = models.CharField(max_length=100, null=False)
    Student_School = models.CharField(max_length=250, null=False)
    Student_Class = models.CharField(max_length=55, null=False)
    Student_ClassGrade = models.CharField(max_length= 16, null=False)
    user = models.CharField(default='',max_length=55, null=False)
    Created_Date = models.DateTimeField(auto_now_add=True, null=False)

    def unique_id_generator(self):
        '''User-Defined Function: This function helps to creates the random secret key for every new student created, with his/her name, DOB, Parent Mobile 6 digit. Syntax: Name-DOB-UniqueCode-Mobile'''
        li = [i for i in str(self.Student_Birth_Date).replace("-",'')]# yyyy-dd-mm
        dt = ''
        for i in li[2:]:
            dt= dt + i
        mob = []
        for j in self.Student_ParentMobile:
            mob.append(j)
        mob_num = ''
        for j in mob[0:6]:
            mob_num += j
        rec = ''.join(secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.ascii_letters) for i in range(6))
        return self.Student_First_Name.replace(" ","") +'-'+ dt +'-'+ rec + '-' + mob_num
    
    def save(self, *args, **kwargs):
        if not self.Student_UniqueId:
            self.Student_UniqueId = self.unique_id_generator()
        super(StudentDetails, self).save(*args, **kwargs)
    objects = models.Manager

class QuestionAnswerModel(models.Model):
    Question_Unique_Id = models.CharField(max_length=45, primary_key=True, null=False)
    Student_Class = models.CharField(max_length=55, null=False, default='')
    Subject = models.CharField(max_length=45, null=False)
    Question = models.CharField(max_length=1200, null=False)
    Answer_1 = models.CharField(max_length=350, null=False)
    Answer_2 = models.CharField(max_length=350, null=False)
    Answer_3 = models.CharField(max_length=350, null=False)
    Answer_4 = models.CharField(max_length=350, null=False)
    Answer_5 = models.CharField(max_length=350)
    Rightanswer = models.CharField(max_length=3, null=False)
    user = models.CharField(default='',max_length=55)
    Created_Date = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return str(self.Question_Unique_Id)
    objects = models.Manager

    def get_unique_id(self):
        uni = ''.join(secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.ascii_letters) for i in range(10))
        return self.Student_Class +'-'+ self.Subject +'-'+ uni

    def save(self, *args, **kwargs):
        for field_name in ['Question','Answer_1','Answer_2','Answer_3','Answer_4','Answer_5','Rightanswer']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())

        if not self.Question_Unique_Id:
            self.Question_Unique_Id = self.get_unique_id()
        super(QuestionAnswerModel, self).save(*args, **kwargs)

