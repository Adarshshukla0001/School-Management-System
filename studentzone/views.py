from django.shortcuts import render,redirect,reverse
from studentzone.models import Feed,SLeave
from facaltyzone.models import Student,SNfc
# Create your views here.
def index(request):
    if request.session['userid']:
        a=request.session['userid']
        s=Student.objects.get(stdid=a)
    return render(request,'stdindex.html',{'s':s})
def updatestudent(request):
    if request.session['userid']:
        if request.method=='POST':
            image=request.FILES.get('image')
            id=request.POST['stdid']
            mobile=request.POST['mobile']
            email=request.POST['email']
            gender=request.POST['gender']
            qua=request.POST['qua']
            exp=request.POST['exp']
            address=request.POST['address']
            e=Student.objects.get(stdid=id)
            e.image=image
            e.mobile=mobile
            e.email=email
            e.gender=gender
            e.qua=qua
            e.exp=exp
            e.address=address
            e.save()
            return redirect(reverse('studentzone:index'))
        a=request.session['userid']
        e=Student.objects.get(stdid=a)
        return render(request,'updatestudent.html',{'e':e})
def stdfeed(request):
    if request.method=='POST':
        id=request.POST['stdid']
        name=request.POST['stdname']
        dept=request.POST['branch']
        feedtype=request.POST['feed']
        msg=request.POST['msg']
        f=Feed(stdid=id,stdname=name,branch=dept,feedtype=feedtype,msg=msg)
        f.save()
    return render(request,'stdfeedback.html')
def stdleave(request):
    # Use session userid as the student id and validate inputs to avoid creating empty records
    m = request.session.get('userid')
    if request.method == 'POST' and m:
        # prefer .get() to avoid KeyError and strip values
        name = request.POST.get('stdname', '').strip()
        dept = request.POST.get('branch', '').strip()
        sub = request.POST.get('subject', '').strip()
        fr = request.POST.get('fr', '').strip()
        to = request.POST.get('to', '').strip()
        msg = request.POST.get('msg', '').strip()
        # basic validation: require id (from session) and some key fields
        if m and name and dept and sub:
            l = SLeave(stdid=m, stdname=name, branch=dept, subject=sub, fr=fr, to=to, status=0, msg=msg)
            l.save()
    k = SLeave.objects.filter(stdid=m).first() if m else None
    return render(request, 'stdleave.html', {'k': k})
def stdnfc(request):
        x=SNfc.objects.all()
        return render(request,'viewstdnfc.html',{'x':x})