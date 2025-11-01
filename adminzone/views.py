from django.shortcuts import render,redirect,reverse
from . models import Facalty,Nfc,Attend,Salary
import datetime
from facaltyzone.models import Leave, Feed as FacFeed
from studentzone.models import Feed as StuFeed
# Create your views here.
def index(request):
    return render(request,'adindex.html')
def addfacalty(request):
    if request.method=='POST':
        id=request.POST['fid']
        name=request.POST['fname']
        dept=request.POST['department']
        abt=request.POST['about']
        sal=request.POST['salary']
        f=Facalty(image='',fid=id,fname=name,department=dept,about=abt,salary=sal,mobile=0,email='---',address='---',gender='---',qua='---',exp='---')
        f.save()
    return render(request,'addfacalty.html') 
def viewfacalty(request):
    f=Facalty.objects.all()
    return render(request,'viewfacalty.html',{'f':f})
def deletefacalty(request,fid):
    emp=Facalty.objects.get(fid=fid)
    emp.delete()
    return redirect(reverse('adminzone:viewfacalty'))
def facaltynfc(request):
    if request.method=='POST':
        nfcid = request.POST['nfcid']
        nfc = request.POST['nfc']
        nfcs=Nfc(nfcid=nfcid,nfc=nfc)
        nfcs.save()
    n=Nfc.objects.all() 
    return render(request,'facaltynfc.html',{'n':n})
def facaltyattend(request):
    e=Facalty.objects.all()
    return render(request,'fattendance.html',{'e':e})
def present(request,fid):
    e=Facalty.objects.get(fid=fid)
    id=e.fid
    name=e.fname
    dept=e.department
    curr=datetime.datetime.today()
    status=1
    a=Attend(fid=id,fname=name,department=dept,date=curr,status=status)
    a.save()
    return redirect(reverse('adminzone:viewfattend'))
def viewfattend(request):
    a=Attend.objects.all()
    return render(request,'viewfattendance.html',{'a':a})
def ab(request,fid):
     a=Attend.objects.get(fid=fid)
     a.status=1
     a.save()
     return redirect(reverse('adminzone:viewfattend'))
def pr(request,fid):
     a=Attend.objects.get(fid=fid)
     a.status=0
     a.save()
     return redirect(reverse('adminzone:viewfattend'))
def sal(request):
    e=Facalty.objects.all()
    return render(request,'addsalary.html',{'e':e})
def addsal(request,fid):
    e=Facalty.objects.get(fid=fid)
    id=e.fid
    name=e.fname
    dept=e.department
    curr=datetime.datetime.today()
    sal=e.salary
    status=1
    s=Salary(fid=id,fname=name,department=dept,salary=sal,date=curr,status=status)
    s.save()
    return redirect(reverse('adminzone:sendsal'))
def sendsal(request):
    e=Salary.objects.all()
    return render(request,'sendsalary.html',{'e':e})
def send(request,fid):
     l=Salary.objects.get(fid=fid)
     l.status=0
     l.save()
     return redirect(reverse('adminzone:sendsal'))
def leave(request):
    l=Leave.objects.all()
    return render(request,'facaltyleave.html',{'l':l})
def accept(request,fid):
     l=Leave.objects.get(fid=fid)
     l.status=0
     l.save()
     return redirect(reverse('adminzone:leave'))
def reject(request,fid):
     l=Leave.objects.get(fid=fid)
     l.status=1
     l.save()
     return redirect(reverse('adminzone:leave'))
def ffeed(request):
    # show feedback submitted by faculty (use facaltyzone.Feed)
    f = FacFeed.objects.all()
    return render(request, 'ffeedback.html', {'f': f})
def stdfeed(request):
    # show feedback submitted by students (use studentzone.Feed)
    f = StuFeed.objects.all()
    return render(request, 'sfeedback.html', {'f': f})