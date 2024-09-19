from django.shortcuts import render,HttpResponse
from .models import Employee,FeedBack_Rating,Contact,Event
from django.contrib import messages
# Create your views here.
def home(request):
    # contact_object_list=contact.object.all()
    # contact_contents={
    #     "contact_key":contact_object_list,
    #     "title":"MyHomePage"
    # }
    employee_object_list=Employee.objects.all()
    event_object_list=Event.objects.all()
    employee_contents={
        "employee_key":employee_object_list,

    
        "event_key":event_object_list
    }
    

    
    
    
    return render(request,"myapp/html/home.html",employee_contents)
def about_us(request):
    return render(request,"myapp/html/about.html")
def feedback(request):
    if request.method == "GET":
        return render(request,"myapp/html/feedback.html")
    if request.method == "POST":
        f_name=request.POST["username"]
        f_email=request.POST["useremail"]
        f_feedback=request.POST["userfeedback"]
        # f_rating=request.POST["userdropdown"]
        feedback_obj=FeedBack_Rating(name=f_name,email=f_email,feedback_text=f_feedback)
        feedback_obj.save() 
        messages.success(request,"thanks for your feedback")
        return render(request,"myapp/html/feedback.html")
def contact(request):
    if request.method == "GET":
        
        return render(request,"myapp/html/contact_us.html")
    if request.method == "POST":
        u_name=request.POST["username"]
        # print(uname)
        u_email=request.POST["useremail"]
        u_phone=request.POST["userphone"]
        u_query=request.POST["userquery"]
        contact_obj=Contact(name=u_name,email=u_email,phone=u_phone,user_query=u_query) #object creation of contact model
        contact_obj.save() #using orm concept
        messages.success(request,"thankyou for contacting us we will reach you soon!!!")
        print("in post method")
        return render(request,"myapp/html/contact_us.html")
        
def cources(request):
    return render(request,"myapp/html/cources.html")
def login(request):
    return render(request,"myapp/html/login.html")

def employee_details(request):
    employee_object_list=Employee.objects.all()
    employee_dict={
        "employee_key":employee_object_list
    }
    return render(request,"myapp/html/employee_details.html",employee_dict)


    

    
      


    
    
    
