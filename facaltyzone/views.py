from django.shortcuts import render,redirect,reverse
from . models import Student, Leave,Feed, SNfc,SAttend
from adminzone.models import Facalty,Salary,Nfc
from studentzone.models import SLeave
import datetime
# Create your views here.
def index(request):
    return render(request,'findex.html')
def addstudent(request):
    if request.method=='POST':
        id=request.POST['stdid']
        name=request.POST['stdname']
        branch=request.POST['branch']
        dob=request.POST['dob']
        abt=request.POST['about']
        s=Student(image='',stdid=id,stdname=name,branch=branch,dob=dob,about=abt,mobile=0,email='---',address='---',gender='---',qua='---',exp='---')
        s.save()
    return render(request,'addstudent.html') 
def viewstudent(request):
    s=Student.objects.all()
    return render(request,'viewstudent.html',{'s':s})
def deletestudent(request,stdid):
    emp=Student.objects.get(stdid=stdid)
    emp.delete()
    return redirect(reverse('facaltyzone:viewstudent'))
def facaltyprofile(request):
    if request.session['userid']:
        a=request.session['userid']
        f=Facalty.objects.get(fid=a)
        return render(request,'facaltyprofile.html',{'f':f})
        
def updatefacalty(request):
    if request.session['userid']:
        if request.method=='POST':
            image=request.FILES.get('image')
            id=request.POST['fid']
            mobile=request.POST['mobile']
            email=request.POST['email']
            gender=request.POST['gender']
            qua=request.POST['qua']
            exp=request.POST['exp']
            address=request.POST['address']
            e=Facalty.objects.get(fid=id)
            e.image=image
            e.mobile=mobile
            e.email=email
            e.gender=gender
            e.qua=qua
            e.exp=exp
            e.address=address
            e.save()
            return redirect(reverse('facaltyzone:facaltyprofile'))
        a=request.session['userid']
        e=Facalty.objects.get(fid=a)
        return render(request,'updatefacalty.html',{'e':e})
def fleave(request):
    # Use session userid as the faculty id and validate input to avoid empty records
    a = request.session.get('userid')
    if request.method == 'POST' and a:
        name = request.POST.get('fname', '').strip()
        dept = request.POST.get('department', '').strip()
        sub = request.POST.get('subject', '').strip()
        fr = request.POST.get('fr', '').strip()
        to = request.POST.get('to', '').strip()
        msg = request.POST.get('msg', '').strip()
        if a and name and dept and sub:
            l = Leave(fid=a, fname=name, department=dept, subject=sub, fr=fr, to=to, status=0, msg=msg)
            l.save()
    l = Leave.objects.filter(fid=a).first() if a else None
    return render(request, 'fleave.html', {'l': l})
def ffeed(request):
    if request.method=='POST':
        id=request.POST['fid']
        name=request.POST['fname']
        dept=request.POST['department']
        feedtype=request.POST['feed']
        msg=request.POST['msg']
        f=Feed(fid=id,fname=name,department=dept,feedtype=feedtype,msg=msg)
        f.save()
    return render(request,'sendffeedback.html')
def leave(request):
    s=SLeave.objects.all()
    return render(request,'studentleave.html',{'s':s})
def accept(request,stdid):
     l=SLeave.objects.get(stdid=stdid)
     l.status=0
     l.save()
     return redirect(reverse('facaltyzone:leave'))
def reject(request,stdid):
     l=SLeave.objects.get(stdid=stdid)
     l.status=1
     l.save()
     return redirect(reverse('facaltyzone:leave'))
def viewsal(request):
    if request.session['userid']:
       a=request.session['userid'] 
       k=Salary.objects.get(fid=a)
       return render(request,'viewsalary.html',{'k':k})
def fnfc(request):
        x=Nfc.objects.all()
        return render(request,'viewmynfc.html',{'x':x})
def stdnfc(request):
    if request.method=='POST':
        nfcid = request.POST['nfcid']
        nfc = request.POST['nfc']
        nfcs=SNfc(nfcid=nfcid,nfc=nfc)
        nfcs.save()
    n=SNfc.objects.all() 
    return render(request,'sendstdnfc.html',{'n':n})    

def studentattend(request):
    e=Student.objects.all()
    return render(request,'stdattendance.html',{'e':e})
def p(request,stdid):
    e=Student.objects.get(stdid=stdid)
    id=e.stdid
    name=e.stdname
    dept=e.branch
    curr=datetime.datetime.today()
    status=1
    a=SAttend(stdid=id,stdname=name,branch=dept,date=curr,status=status)
    a.save()
    return redirect(reverse('facaltyzone:viewstdattend'))
def viewstdattend(request):
    a=SAttend.objects.all()
    return render(request,'viewstdattendance.html',{'a':a})
def abt(request,stdid):
     a=SAttend.objects.get(stdid=stdid)
     a.status=1
     a.save()
     return redirect(reverse('facaltyzone:viewstdattend'))
def pt(request,stdid):
     a=SAttend.objects.get(stdid=stdid)
     a.status=0
     a.save()
     return redirect(reverse('facaltyzone:viewstdattend'))