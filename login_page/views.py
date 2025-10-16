from django.shortcuts import render

from login_page.models import loginMode

from django.views.generic import View


# Create your views here.

class createLOginView(View):

    def get(self,request):


        return render(request,"login_user.html")
    
    def post(self,request):

        print(request.POST)

        loginMode.objects.create(name = request.POST.get())



