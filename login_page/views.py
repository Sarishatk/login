from django.shortcuts import render

from login_page.models import loginMode

from django.views.generic import View


# Create your views here.

class createLOginView(View):

    def get(self,request):

        loginMode.objects.create()

        return render(request,"login_user.html")

