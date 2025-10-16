from django.shortcuts import render

from login_page.models import loginMode

from django.views.generic import View


# Create your views here.

class createLOginView(View):

    def get(self,request):


        return render(request,"login_user.html")
    
    def post(self,request):

        print(request.POST)

        loginMode.objects.create(name = request.POST.get("username"),
                                 email = request.POST.get("useremail"),
                                 password =  request.POST.get("userpassword")
                                 
                                 )
        return render(request,"login_user.html")
    

class Updatelogin(View):

    def get(self,request):

         emp_data = loginMode.objects.get(id = 1)

         return render(request,"user_update.html",{"emp_data":emp_data})
    
    def post(self,request):

         emp_data = loginMode.objects.get(id = 1)

         print(request.POST)

         emp_data.name = request.POST.get("username")

         emp_data.email = request.POST.get("useremail")

         emp_data.password = request.POST.get("userpassword")

         emp_data.save()

         return render(request,"user_update.html")
    
    






        


