from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
import random
from home.models import *
from home.templates import *

def registrationForm(request):
    template=loader.get_template('RegistrationForm.html')
    res=template.render()
    return HttpResponse(res)
def contactForm(request):
    template=loader.get_template('ContactUs.html')
    res=template.render()
    return HttpResponse(res)
@csrf_exempt
def storeUser(request):
    if request.method == 'POST':
        usernamee=request.POST['username']
        if(len(Users.objects.filter(username=usernamee))):
            userStatus=1
        else:
            user=Users()
            user.firstname=request.POST['firstname']
            user.lastname=request.POST['lastname']
            user.username=usernamee
            user.phone=request.POST['phone']
            user.email=request.POST['email']
            user.password=request.POST['password']
            user.save()
            userStatus=2
    else:
        userStatus=3
    context={'userStatus':userStatus}
    res=render(request,'RegistrationStatus.html',context)
    return res
@csrf_exempt
def login(request):
    if request.method=='POST':
        username=request.POST['email']
        password=request.POST['password']
        user=Users.objects.filter(email=username,password=password)
        if len(user)==0:
            loginError="Invalid Username or passowrd"
            res=render(request,'LoginForm.html',{'loginError':loginError})
        else:
            request.session['username']=user[0].username
            request.session['name']=user[0].firstname
            res=render(request,'UsersHome.html')
    else:
        res=render(request,'LoginForm.html')
    return HttpResponse(res)
def userHome(request):
    if 'name' not in request.session.keys():
       res=render(request,'landing.html')
    else:
       res=render(request,'UsersHome.html')
    return res
def testPaper(request):
    if 'name' not in request.session.keys():
        res=HttpResponse("LoginForm")
    else:
        n=int(request.GET['n'])
        question_pool=list(Questions.objects.all())
        random.shuffle(question_pool)
        qusetions_list=question_pool[:n]
        context={'questions':qusetions_list}
        res=render(request,'TestPaper.html',context)
    return res
def calculateTest(request):
    if 'name' not in request.session.keys():
        res=HttpResponse("LoginForm")
    total_attempt=0
    total_right=0
    total_wrong=0
    qid_list=[]
    for k in request.POST:
        if k.startswith('q'):
            qid_list.append(int(request.POST[k]))
    for n in qid_list:
        question=Questions.objects.get(qid=n)
        # try:
        if str(n) in request.POST.keys():
            if question.ans==request.POST[str(n)]:
                total_right+=1
            else:
                total_wrong+=1
            total_attempt+=1
        # except:
            # pass
    points=(total_right-total_wrong)/len(qid_list)*10

    #store result in Result Table

    result=Result()
    result.username=Users.objects.get(username=request.session['username'])
    result.attends=total_attempt
    result.right=total_right
    result.wront=total_wrong
    result.points=points
    result.save()

    #update user table

    candidate=Users.objects.get(username=request.session['username'])
    candidate.testattempted+=1
    candidate.points=(candidate.points*(candidate.testattempted-1)+points)/candidate.testattempted
    candidate.save()

    return HttpResponseRedirect("result")
def showTestResult(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect("LoginForm")
    #fetch latest result from result table
    result=Result.objects.filter(resultid=Result.objects.latest('resultid').resultid,username_id=request.session['username'])
    context={'result':result}
    res=render(request,'testresult.html',context)
    return res
def testHistory(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect("LoginForm")
    
    candidate=Users.objects.filter(username=request.session['username'])
    resutls=Result.objects.filter(username_id=candidate[0].username)
    context={'results':resutls,'candidate':candidate[0]}
    res=render(request,'user_history.html',context)
    return res
def logOut(request):
    if 'name' in request.session.keys():
        del request.session['name']
        del request.session['username']
    res=HttpResponseRedirect("/userHome")
    return res
