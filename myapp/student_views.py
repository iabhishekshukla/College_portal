from django.shortcuts import render,redirect
from .models import Student
from .models import Student_Feedback_Rating
from django.contrib import messages
from django.views import View
def show_home(request):
    st_id=request.session["student_key"]#fetching the value from dictonary
    # print(st_id)
    student_obj=Student.objects.get(student_id=st_id)#fetch a single object
    student_dict={"student_data":student_obj}#binding student obj in dict    
    return render(request,"myapp/student/student_home.html",student_dict)
#class based views for login function
class Login(View):
    def get(self,request):
        return render(request,"myapp/html/login.html")
    def post(self,request):
        s_id=request.POST["userid"]
        s_pass=request.POST.get("userpass")
        # print(s_id,s_pass)
        msg=self.check_length(s_pass)
        # msg_dict={"error_message":msg}
        if msg:

            messages.error(request,msg)
            return render(request,"myapp/html/login.html")
        else:

            student_list=Student.objects.filter(student_id=s_id,student_password=s_pass)
            length=len(student_list)

            if length>0:
                request.session["student_key"]=s_id #bind student id in session 
                request.session["role"]="student"
                return redirect("student_home")#it accept logical name
                return render(request,'myapp/student/student_home.html')#it accepts logical name 
        #it is used to
            else:
                messages.error(request,"invalid credentials")
                return render(request,'myapp/html/login.html')
    def check_length(self,password):
                if len(password)<=5:
                    return "must be greater then 5 char"
    
        
        
# def login(request):
#     if request.method=="GET":
#         return render(request,"myapp/html/login.html")
#     if request.method=="POST":
        # s_id=request.POST["userid"]
        # s_pass=request.POST.get("userpass")
        # print(s_id,s_pass)
        # student_list=Student.objects.filter(student_id=s_id,student_password=s_pass)
        # length=len(student_list)

        # if length>0:
        #     request.session["student_key"]=s_id #bind student id in session 
        #     # request.session["role"]="student"
        #     # return redirect("student_home")#it accept logical name
        #     return render(request,'myapp/student/student_home.html')
        # else:
        #     return render(request,'myapp/html/login.html')
        
#logout
def logout(request):
    del request.session["student_key"]
    return redirect("login")

def student_edit_profile(request):
    if request.method=="GET":
        s_id=request.session["student_key"]
        student_obj=Student.objects.get(student_id=s_id)
        student_dict={"student_data":student_obj}
        return render(request,'myapp/student/student_editprofile.html',student_dict)
    if request.method=="POST":
        em=request.POST["useremail"]
        ph=request.POST["userphone"]
        add=request.POST["useraddress"]
        s_id=request.session["student_key"]
        student_obj=Student.objects.get(student_id=s_id)
        student_obj.email=em
        student_obj.phone=ph
        student_obj.address=add
        student_obj.save()
        student_dict={"student_data":student_obj}
        return render(request,'myapp/student/student_home.html',student_dict)

def student_feedback_rating(request):
    if request.method=="GET":
        s_id=request.session["student_key"]
        student_obj=Student.objects.get(student_id=s_id)
        student_dict={"student_data":student_obj}
        return render(request,'myapp/student/student_feedback.html',student_dict)
    if request.method=="POST":
        rt=request.POST["feedback_rating"]
        fb=request.POST["userfeedback"]
        s_id=request.session["student_key"]
        student_obj=Student.objects.get(student_id=s_id)

        # student_object=Student_Feedback_Rating.objects.get(student_id=student_obj)
        student_object_List=Student_Feedback_Rating.objects.filter(student_id=student_obj)

    if student_object_List: #means if list is not empty -> feedback is present in the table
        student_dict={"student_data":student_obj}#binding student obj in dict  
        messages.info(request,"you already submitted your feedback")  
        return render(request,'myapp/student/student_home.html',student_dict)

    else:
        
        srf=Student_Feedback_Rating(student=student_obj,feedback_text=fb,feedback_rating=rt)
        srf.save()
        


    


    
    
    