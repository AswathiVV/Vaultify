from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def user_login(req):
    if 'user' in req.session:
        return redirect(user_home)
    else:
    
        if req.method=='POST':
            uname=req.POST['uname']
            password=req.POST['password']
            data=authenticate(username=uname,password=password)
            if data:
                login(req,data)
                if data.is_superuser:
                    req.session['shop']=uname     
                    return redirect(user_home)
                else:
                    req.session['user']=uname      
                    return redirect(user_home)
            else:
                messages.warning(req,"invalid uname or password")  
        return render(req,'login.html') 
    
def shop_logout(req):
    logout(req)
    req.session.flush()              
    return redirect(user_login) 

def  register(req):
     if req.method=='POST':
        name=req.POST['name']       
        email=req.POST['email']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=name,username=email,email=email,password=password)
            data.save()
            return redirect(user_login)
        except:
            messages.warning(req,"user details already exits")
            return redirect(register)
     else:
         return render(req,'register.html')  
    
def user_home(req):
    if 'user' in req.session:
        data=Images.objects.all()
        return render(req,'user_home.html',{'Images':data})
    else:
        return redirect(user_login) 

def images(req):
    img=Images.objects.all()
    return render(req,'view_img.html',{'Image':img})

def upload_image(req):
    if 'user' in req.session:
        if 'file' in req.FILES:
            img = req.FILES['file']
            data = Images.objects.create(file=img)
            data.save()
            print("File uploaded successfully!")
        else:
            print("img not found")
            return render(req,'upload_img.html') 
    return redirect(images)

def delete_img(req,id):
        data=Images.objects.get(pk=id)
        url=data.file.url
        url=url.split('/')[-1]
        os.remove('media/'+url)  
        data.delete()
        return redirect(user_home) 


def note(req):
    notes = Note.objects.all() 
    return render(req, 'view_note.html', {'Notes': notes})

def upload_note(req):
    if req.method=='POST':
        title=req.POST['title']
        content=req.POST['content']
        data=Note.objects.create(title=title,content=content)
        data.save()
        return redirect(note)
    return render(req,'upload_note.html')


def delete_note(req,id):
        data=Note.objects.get(pk=id)
        data.delete()
        return redirect(user_home) 

def video(req):
    vid= Video.objects.all()  
    return render(req, 'view_vid.html', {'Video': vid})

def upload_vid(req):
    if 'user' in req.session:
        if 'file' in req.FILES:
            img = req.FILES['file']
            data = Video.objects.create(file=img)
            data.save()
            print("File uploaded successfully!")
        else:
            print("img not found")
            return render(req,'upload_vid.html') 
    return redirect(video)

def delete_video(req,id):
        data=Video.objects.get(pk=id)
        url=data.file.url
        url=url.split('/')[-1]
        os.remove('media/'+url)  
        data.delete()
        return redirect(user_home) 

def audio(req):
    aud= Audio.objects.all()  
    return render(req, 'view_audio.html', {'Audio': aud})

def upload_aud(req):
    if 'user' in req.session:
        if 'file' in req.FILES:
            img = req.FILES['file']
            data = Audio.objects.create(file=img)
            data.save()
            print("File uploaded successfully!")
        else:
            print("img not found")
            return render(req,'upload_aud.html') 
    return redirect(audio)

def delete_aud(req,id):
        data=Audio.objects.get(pk=id)
        url=data.file.url
        url=url.split('/')[-1]
        os.remove('media/'+url)  
        data.delete()
        return redirect(user_home) 



    