# Generated by Django 3.0.5 on 2021-02-02 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAnswerModel',
            fields=[
                ('Question_Unique_Id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('Student_Class', models.CharField(default='', max_length=55)),
                ('Subject', models.CharField(max_length=45)),
                ('Question', models.CharField(max_length=1200)),
                ('Answer_1', models.CharField(max_length=350)),
                ('Answer_2', models.CharField(max_length=350)),
                ('Answer_3', models.CharField(max_length=350)),
                ('Answer_4', models.CharField(max_length=350)),
                ('Answer_5', models.CharField(max_length=350)),
                ('Rightanswer', models.CharField(max_length=3)),
                ('user', models.CharField(default='', max_length=55)),
                ('Created_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('Student_UniqueId', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('Student_Image', models.ImageField(upload_to='quiz/students/images')),
                ('Student_First_Name', models.CharField(max_length=100)),
                ('Student_Last_Name', models.CharField(max_length=100)),
                ('Student_Birth_Date', models.DateField()),
                ('Student_MotherName', models.CharField(max_length=85)),
                ('Student_FatherName', models.CharField(max_length=85)),
                ('Student_ParentMobile', models.CharField(max_length=10)),
                ('Student_AlterMobile', models.CharField(max_length=10)),
                ('Student_ParentEmail', models.EmailField(max_length=250)),
                ('Student_State', models.CharField(max_length=100)),
                ('Student_City', models.CharField(max_length=100)),
                ('Student_School', models.CharField(max_length=250)),
                ('Student_Class', models.CharField(max_length=55)),
                ('Student_ClassGrade', models.CharField(max_length=16)),
                ('user', models.CharField(default='', max_length=55)),
                ('Created_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]