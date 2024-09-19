from django.db import models
from django.utils import timezone
class Contact(models.Model):
    name=models.CharField(max_length=45)
    email=models.EmailField(max_length=45)
    phone=models.CharField(max_length=10)
    user_query=models.TextField()
    date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.name
    
class FeedBack_Rating(models.Model):
    name=models.CharField(max_length=45)
    email=models.EmailField(max_length=45)
    feedback_text=models.TextField()
    rating=models.CharField(max_length=6)
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
class Event(models.Model):
    
    event_name=models.CharField(max_length=50,primary_key=True)
    event_venue=models.CharField(max_length=100)
    event_description=models.TextField()
    event_date=models.DateField(default=timezone.now)
    event_pic=models.FileField(max_length=100,upload_to="myapp/event_pic",default=" ")
    def __str__(self):
        return self.event_name
    
class Employee(models.Model):

    emp_name=models.CharField(max_length=40)
    emp_email=models.EmailField(max_length=45)
    emp_phone=models.CharField(max_length=10)
    emp_designation=models.CharField(max_length=40)
    emp_pic=models.FileField(max_length=100,upload_to="myapp/employee_pic",default=" ")
    def __str__(self):
        return self.emp_name
    

class Course(models.Model):
    course_name=models.CharField(max_length=45,primary_key=True,default="")
    course_fees=models.IntegerField()
    course_duration=models.CharField(max_length=40)
    course_contents=models.TextField(blank=True)
    course_pic=models.FileField(max_length=200,upload_to="myapp/course_pic",default="")

    def __str__(self):
        return self.course_name

gender=[
    ("m","male"),
    ("f","female")
]

    

class Student(models.Model):
    course=models.ForeignKey(Course,on_delete=models.DO_NOTHING,default="")
    name=models.CharField(max_length=45) 
    email=models.EmailField(max_length=45) 
    phone=models.CharField(max_length=10) 
    student_id=models.CharField(max_length=40,primary_key=True,default="") 
    student_password=models.CharField(max_length=40)
    gender=models.CharField(max_length=6,choices=gender)
   
    description=models.TextField() 
    address=models.TextField()  
    student_pic=models.FileField(max_length=200,upload_to="myapp/student_pic",default="")      
    def __str__(self):
        return self.name        
    
class Student_Feedback_Rating(models.Model):
    student=models.OneToOneField(Student,on_delete=models.DO_NOTHING)
    feedback_text=models.TextField()
    feedback_rating=models.CharField(max_length=6)
    feedback_date=models.DateField(default=timezone.now)


    
        
    
    

    