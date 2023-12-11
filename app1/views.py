from django.shortcuts import render
from app1.forms import *
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from datetime import datetime,timedelta


# Create your views here.
def sinup(request):
    obj=registerform()
    d={'obj':obj}
    if request.method=='POST':
        ur=registerform(request.POST)
        if ur.is_valid():
            us=ur.save(commit=False)
            #print(us.username)
            us.set_password(ur.cleaned_data['password'])
            us.save()
            ACT=authenticate(username=ur.cleaned_data['username'],password=ur.cleaned_data['password'])
            if ACT and ACT.is_active:
                login(request,ACT)
                request.session['username']=us.username
                return HttpResponseRedirect(reverse('profile_detail'))
            
            return HttpResponse('not valid')
        else:
            messages.success(request, "Thanks for joining our newsletter!")

    return render(request,'sinup.html',d)

def profile_detail(request):
    pro_f=profileform()
    user=request.session.get('username')
    username=User.objects.get(username=user)
    if request.method=='POST':
        pro_d=profileform(request.POST,request.FILES)
        if pro_d.is_valid():
            pd=pro_d.save(commit=False)
            pd.username=username
            pd.save()
            print(pd)
            md=Usermessages(username=username)
            md.save()
            return HttpResponseRedirect(reverse('home'))
    d={'p':pro_f,'user':username}
    return render(request,'profile_detail.html',d)
def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        ACT=authenticate(username=username,password=password)
        if ACT and ACT.is_active:
            login(request,ACT)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))

    return render(request,'userlogin.html')
def logouted(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
def register(request):
    return render (request,'register.html')

def home(request):
    if request.session.get('username'):
        us=request.session.get('username')
        user=User.objects.get(username=us)
        us=Usermessages.objects.all().order_by('-pk')
        l=[]
        for x in us:
            if x.username not in l:
                l.append(x.username)
                print(x.pk)
        print(l)
        pro=profile.objects.exclude(Q(username=user)) 
        print(pro)  
        d={'us':l,'pro':pro}
        return render(request,'home.html',d)
    return HttpResponseRedirect(reverse('register'))

@login_required
def message(request,pk):
    ud=request.session.get('username')
    user=User.objects.get(pk=pk)
    us=User.objects.get(username=ud)
    k=Usermessages.objects.all().order_by('-pk')
    message=''
    l=[]
    for x in k:
        if x.username not in l:
            l.append(x.username)
            print(x.pk)
    re=User.objects.get(username=user)
    pro=profile.objects.exclude(username=us)
    user_pro=profile.objects.get(username=user)
    ms=Usermessages.objects.filter(Q(username=us) & Q(reusername=re))
    p=profile.objects.all()
    if request.method=='POST' or request.FILES:
        
        if request.POST.get('message'):
            message=request.POST['message']
            if len(message)>1:
                st=Usermessages(username=us,message=message,reusername=re)
                sr=Usermessages(username=re,replay=message,reusername=us)
                st.save()
                sr.save()
                message=''
    
        
        if request.FILES:
            if request.FILES.get('image1'):
                img=request.FILES['image1']           
                st=Usermessages(username=us,imagevideo=img,reusername=re)
                sr=Usermessages(username=re,imagevideo=img,reusername=us)
                st.save()
                sr.save()
                print('hello')
            elif request.FILES.get('document1'):
                document=request.FILES['document1']           
                st=Usermessages(username=us,pdf_file=document,reusername=re)
                sr=Usermessages(username=re,pdf_file=document,reusername=us)
                st.save()
                sr.save()
            elif request.FILES.get('pdf1'):
                pdf1=request.FILES['pdf1'] 
                print(pdf1)          
                st=Usermessages(username=us,pdf_file=pdf1,reusername=re)
                sr=Usermessages(username=re,pdf_file=pdf1,reusername=us)
                st.save()
                sr.save()
                print(sr)
                print(st)
        ms=Usermessages.objects.filter(Q(username=us) & Q(reusername=re))
        k=Usermessages.objects.all().order_by('-pk')
        l=[]
        for x in k:
            if x.username not in l:
                l.append(x.username)
        d={'us':l,'use':ms,'pro':pro,'user_pro':user_pro}
        return render(request,'home.html',d)
    d={'us':l,'use':ms,'pro':pro,'user_pro':user_pro}
    
    return render(request,'home.html',d)
def display(request):
    user=User.objects.get(username='vinoth')
    k=User.objects.all()
    us=Usermessages.objects.filter(username=user)
    d={'us':us,'k':k}
    return render(request,'display.html',d)
def dummpy(request):
    us=User.objects.all()
    d={'use':us}
    return render (request,'dummpy.html',d)

def image(request):
    if request.method =='POST' or request.FILES:
        image=request.FILES['image']
        print(image)
    return render(request,'image.html')
def delete(request,y):
    us=user_status.objects.filter(id=int(y)).delete()
    return HttpResponseRedirect(reverse('status'))

def forward(request,pk):
    message_id=user_status.objects.get(pk=pk)
    us=request.session.get('username')
    username=User.objects.get(username=us)
    if request.method=="POST":
        send=request.POST.getlist('user')
        for x in send:
            l=User.objects.get(id=int(x))
            sending_user=User.objects.get(username=l.username)
            forward_send=Usermessages(username=username,message=f'{pk}.st3',reusername=sending_user)
            forward_rece=Usermessages(username=sending_user,replay=f'{pk}.st3',reusername=username)
            forward_send.save()
            forward_rece.save()
        return HttpResponseRedirect(reverse('req_status',args=(pk,)))

    use=User.objects.exclude(Q(username=username) | Q(username='admin'))
    d={'use':use}
    return render(request,'send.html',d)
def status(request):
    us=request.session.get('username')
    user=User.objects.get(username=us)
    pro=profile.objects.all()
    print('hi')
    if request.method=="POST" or request.FILES:
        print('hello')
        fi=request.FILES['status']
        print(fi)
        st=user_status(username=user,status_file=fi,status_time=datetime.now(),status_end=datetime.now()+timedelta(minutes=30))
        st.save()
        print(st)
        l=user_status.objects.filter(status_end__gte=datetime.now()).exclude(username=user).order_by('-pk')

    l=user_status.objects.filter(status_end__gte=datetime.now()).exclude(username=user).order_by('-pk')
    status=[]
    for x in l:
        if x.username not in status:
            status.append(x.username)
            
    d={'status':status,'pro':pro}
    return render(request,'status.html',d)

def req_status(request,id):
    
    rq_s=user_status.objects.filter(Q(username=int(id))&Q(status_end__gt=datetime.now()))
    if rq_s:
        d={'st':rq_s}
        print(d)
        return render(request,'req_status.html',d)
    else:
        return HttpResponseRedirect(reverse('status'))
    
def ok(request):
    return render(request,'req_status.html')