from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from data.forms import loginform
from data import utils
import json
from django.contrib import messages
# Create your views here.
username=''
password=''
data=''
path='base'
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def login(request):
    doc=json.dumps(utils.get_doc_dir("mongodb+srv://login-app:DJ-logger-modal@cluster.u4txd.mongodb.net/database?retryWrites=true&w=majority","DB1","col1",{'title':'LoginDB'}))
    doc=json.loads(doc)
    form = loginform(request.POST)
    if form.is_valid():
        global username
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        if username in doc:
            global data
            global subobj
            data=doc[username]
            if password==data['password']:
                data=data['data']
                subobj=data
                return redirect('/dashboard')
            else:
                messages.error(request, f"wrong password")
        else:
            messages.error(request, f"no such username")
    return render(request, 'login.html', {'form': form})

def datahome(request):
    doc=json.dumps(utils.get_doc_dir("mongodb+srv://login-app:DJ-logger-modal@cluster.u4txd.mongodb.net/database?retryWrites=true&w=majority","DB1","col1",{'title':'LoginDB'}))
    doc=json.loads(doc)
    global data
    global username
    data=doc[username]['data']
    send={}
    for key in data:
        if type(data[key])!=dict:
            send[key]=['non-obj',data[key]]
        else:
            send[key]='o'
    return render(request, 'data.html', {'data': send,'user': username,'path':path})

def datasub(request,objs):
    doc=json.dumps(utils.get_doc_dir("mongodb+srv://login-app:DJ-logger-modal@cluster.u4txd.mongodb.net/database?retryWrites=true&w=majority","DB1","col1",{'title':'LoginDB'}))
    doc=json.loads(doc)
    global data
    global username
    data=doc[username]['data']
    global path
    subobj=data
    objs=objs.split('/')
    objsdot=''
    for i in objs:
        objsdot=objsdot + '.' + i
    path='base'+objsdot
    for step in objs:
        subobj=subobj[step]
    send={}
    for key in subobj:
        if type(subobj[key])!=dict:
            send[key]=['non-obj',subobj[key]]
        else:
            send[key]='o'
    return render(request, 'data.html', {'data': send,'user': username,'path':path})

def dashboard(request):
    path="base"
    return render(request, 'dashboard.html', {'user':username})

def editor(request):
    doc=json.dumps(utils.get_doc_dir("mongodb+srv://login-app:DJ-logger-modal@cluster.u4txd.mongodb.net/database?retryWrites=true&w=majority","DB1","col1",{'title':'LoginDB'}))
    doc=json.loads(doc)
    global data
    global username
    data=doc[username]['data']
    send={}
    for key in data:
        if type(data[key])!=dict:
            send[key]=['non-obj',data[key]]
        else:
            send[key]='o'
    return render(request, 'editor.html', {'data': send,'user': username,'path':path})

def editorsub(request,objs):
    doc=json.dumps(utils.get_doc_dir("mongodb+srv://login-app:DJ-logger-modal@cluster.u4txd.mongodb.net/database?retryWrites=true&w=majority","DB1","col1",{'title':'LoginDB'}))
    doc=json.loads(doc)
    global data
    data=doc[username]['data']
    global path
    subobj=data
    objs=objs.split('/')
    objsdot=''
    for i in objs:
        objsdot=objsdot + '.' + i
    path='base'+objsdot
    for step in objs:
        subobj=subobj[step]
    send={}
    for key in subobj:
        if type(subobj[key])!=dict:
            send[key]=['non-obj',subobj[key]]
        else:
            send[key]='o'
    return render(request, 'editor.html', {'data': send,'user': username,'path':path})

def actchoose(request,pth):
    return render(request, 'act.html', {'path': pth})

def choosedt(request,pth):
    return render(request, 'choosedt.html', {'path': pth})
    
