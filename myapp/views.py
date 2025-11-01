from django.shortcuts import render,redirect,reverse
from . models import ad,Contact
from . smssender import sendsms
from adminzone.models import Facalty
from facaltyzone.models import Student
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    if request.method=='POST':
           mob=request.POST['mobile']
           name=request.POST['name']
           email=request.POST['email']
           msg=request.POST['msg']
           c=Contact(mobile=mob,name=name,email=email,msg=msg)
           c.save()
           mobile=request.POST['mobile']
           sendsms(mobile)    
       
    return render(request,"contact.html")
def about(request):
    return render(request,'about.html')
def gallery(request):
    return render(request,'gallery.html')
def adlogin(request):
    return render(request,'adlogin.html')
def validateuser(request):
        name=request.POST['aid']
        password=request.POST['apass']
        msg=''
        try:
            obj=ad.objects.get(name=name,password=password)
            if obj is not None:
               request.session['userid']=name
               return redirect(reverse('adminzone:index'))
        except ObjectDoesNotExist:
            msg='Invalid User'
       
        return render(request,"adlogin.html")
def facaltylogin(request):
    return render(request,'facaltylogin.html')
def validatefacalty(request):
        name=request.POST['fid']
        password=request.POST['fname']
        msg=''
        try:
            obj=Facalty.objects.get(fid=name,fname=password)
            if obj is not None:
                request.session['userid']=name
                return redirect(reverse('facaltyzone:index'))
        except ObjectDoesNotExist:
            msg='Invalid User'
        return render(request,"facaltylogin.html",{'msg':msg})
def studentlogin(request):
    return render(request,'studentlogin.html')
def validatestudent(request):
        name=request.POST['stdid']
        password=request.POST['stdname']
        msg=''
        try:
            obj=Student.objects.get(stdid=name,stdname=password)
            if obj is not None:
                request.session['userid']=name
                return redirect(reverse('studentzone:index'))
        except ObjectDoesNotExist:
            msg='Invalid User'
        return render(request,"studentlogin.html",{'msg':msg})