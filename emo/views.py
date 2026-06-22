import json
from datetime import datetime
import cv2
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
import os
from _thread import start_new_thread
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import tkinter.ttk as ttk
import os
import time
import numpy as np
import cv2
from keras.preprocessing import image
from scipy.ndimage import rotate
root=Tk()
root.geometry('780x550+20+0')
import pymysql
# -----------------------------
# face expression recognizer initialization
from keras.models import model_from_json
# Create your views here.

from emo.models import *


def main(request):
    return render(request,"loginindex.html")

def logout(request):
    auth.logout(request)
    return render(request,"loginindex.html")


def login_code(request):
    un=request.POST['textfield']
    ps=request.POST['textfield2']
    try:
        ob=Login.objects.get(username=un,password=ps)
        if ob.type == "admin":
            request.session['lid']=ob.id
            # ob1=auth.authenticate(username='admin',password='admin')
            # if ob1 is not None:
            #     auth.login(request,ob1)
            return HttpResponse('''<script>alert('Welcome');window.location='/adminhome'</script>''')
        else:
            return HttpResponse('''<script>alert('Invalid');window.location='/'</script>''')
    except:
        return HttpResponse('''<script>alert('Invalid');window.location='/'</script>''')


def adminhome(request):
    return render(request,"adminindex.html")

def addplaylist(request):
    return render(request,"addplaylist.html")

def playlistcode(request):
    so=request.POST['textfield']
    gn=request.POST['textfield2']
    ms = request.POST['textfield3']
    en = request.POST['textfield4']
    fl = request.FILES['file']
    fs=FileSystemStorage()
    fn=fs.save(fl.name,fl)
    dl = request.POST['textarea']
    ob=Manageplaylist()
    ob.song=so
    ob.genre=gn
    ob.musician=ms
    ob.emotion=en
    ob.file=fn
    ob.details=dl
    ob.LOGIN=Login.objects.get(id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert('Added');window.location='/manageplaylist'</script>''')
def manageplaylist(request):
    ob=Manageplaylist.objects.all()
    return render(request,"manageplaylist.html",{'val':ob})

def editplaylist(request,id):
    request.session['ed']=id
    ob=Manageplaylist.objects.get(id=id)
    return render(request,"editplaylist.html",{"val":ob})

def editplylistcode(request):
    try:
        so = request.POST['textfield']
        gn = request.POST['textfield2']
        ms = request.POST['textfield3']
        en = request.POST['textfield4']
        fl = request.FILES['file']
        fs = FileSystemStorage()
        fn = fs.save(fl.name, fl)
        dl = request.POST['textarea']
        ob = Manageplaylist.objects.get(id=request.session['ed'])
        ob.song = so
        ob.genre = gn
        ob.musician = ms
        ob.emotion = en
        ob.file = fn
        ob.details = dl
        ob.save()
        return HttpResponse('''<script>alert('Edited');window.location='/manageplaylist'</script>''')

    except:
        so = request.POST['textfield']
        gn = request.POST['textfield2']
        ms = request.POST['textfield3']
        en = request.POST['textfield4']
        dl = request.POST['textarea']
        ob = Manageplaylist.objects.get(id=request.session['ed'])
        ob.song = so
        ob.genre = gn
        ob.musician = ms
        ob.emotion = en
        ob.details = dl
        ob.save()
        return HttpResponse('''<script>alert('Edited');window.location='/manageplaylist'</script>''')


def manageplaylist_search(request):
    so=request.POST['textfield']
    ob=Manageplaylist.objects.filter(song__icontains=so)
    return render(request,"manageplaylist.html",{'val':ob,'name':so})

def deleteplaylist(request,id):
    ob=Manageplaylist.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('Deleted');window.location='/manageplaylist'</script>''')

def sendreply(request,id):
     ob=Complaints.objects.get(id=id)
     request.session['cid']=ob.id
     return render(request,"sendreply.html")

def add_reply(request):
    a=request.POST['textfield']
    ob=Complaints.objects.get(id= request.session['cid'])
    ob.reply=a
    ob.date=datetime.now()
    ob.save()
    return HttpResponse('''<script>alert('Added');window.location='/viewcomplaints'</script>''')




def viewcomplaints(request):
    ob=Complaints.objects.all()
    return render(request,"viewcomplaints.html",{"val":ob})
def viewcomplaints_search(request):
    da=request.POST['textfield']
    ob=Complaints.objects.filter(date=da)
    return render(request,"viewcomplaints.html",{"val":ob,'name':da})
def viewrating(request):
    ob=Rating.objects.all()
    return render(request,"viewrating.html",{"val":ob})
def viewrating_search(request):
    da=request.POST['textfield']
    ob=Rating.objects.filter(date=da)
    return render(request,"viewrating.html",{"val":ob, 'name':da})
def viewuser(request):
    ob=User.objects.all()
    return render(request,"viewuser.html",{"val":ob})
def viewusersrch(request):
    a=request.POST['textfield']
    ob=User.objects.filter(fname__icontains=a)
    return render(request,"viewuser.html",{"val":ob,'name':a})
def delete_user(request,id):
    q=User.objects.get(LOGIN_id=id)
    q.delete()
    q=Login.objects.get(id=id)
    q.delete()
    return HttpResponse('''<script>alert('Deleted');window.location='/viewuser'</script>''')
# def addbooks(request):
#     if request.POST:
#         bo=request.POST['book']
#         gn=request.POST['textfield2']
#         au = request.POST['textfield3']
#         en = request.POST['textfield4']
#         fl = request.FILES['file']
#         fs=FileSystemStorage()
#         fn=fs.save(fl.name,fl)
#         dl = request.POST['textarea']
#         ob=Manage_books()
#         ob.book=bo
#         ob.genre=gn
#         ob.author=au
#         ob.emotion=en
#         ob.file=fn
#         ob.details=dl
#         ob.LOGIN=Login.objects.get(id=request.session['lid'])
#         ob.save()
#         return HttpResponse('''<script>alert('Added');window.location='/managebooks'</script>''')
#     return render(request,"add_books.html")
# def managebooks(request):
#     ob=Manage_books.objects.all()
#     return render(request,"manage_books.html",{'val':ob})

# def editbooks(request,id):
#     request.session['ed']=id
#     ob=Manageplaylist.objects.get(id=id)
#     return render(request,"edit_books.html",{"val":ob})

# def editbookscode(request):
#     try:
#         if request.POST:
#             so = request.POST['book']
#             gn = request.POST['textfield2']
#             ms = request.POST['textfield3']
#             en = request.POST['textfield4']
#             fl = request.FILES['file']
#             fs = FileSystemStorage()
#             fn = fs.save(fl.name, fl)
#             dl = request.POST['textarea']
#             ob = Manage_books.objects.get(id=request.session['ed'])
#             ob.book = so
#             ob.genre = gn
#             ob.author = ms
#             ob.emotion = en
#             ob.file = fn
#             ob.details = dl
#             ob.save()
#             return HttpResponse('''<script>alert('Edited');window.location='/managebooks'</script>''')
#         return render(request,"edit_books.html")

#     except:
#         if request.POST:
#             so = request.POST['book']
#             gn = request.POST['textfield2']
#             ms = request.POST['textfield3']
#             en = request.POST['textfield4']
#             dl = request.POST['textarea']
#             ob = Manage_books.objects.get(id=request.session['ed'])
#             ob.book = so
#             ob.genre = gn
#             ob.author = ms
#             ob.emotion = en
#             ob.details = dl
#             ob.save()
#             return HttpResponse('''<script>alert('Edited');window.location='/managebooks'</script>''')
#         return render(request,"edit_books.html")
    
# def managebook_search(request): 
#     if request.POST:
#         so=request.POST['book']
#         ob=Manage_books.objects.filter(book__icontains=so)
#     return render(request,"manage_books.html",{'val':ob,'name':so})

# def deletebooks(request,id):
#     ob=Manage_books.objects.get(id=id)
#     ob.delete()
#     return HttpResponse('''<script>alert('Deleted');window.location='/managebooks'</script>''')



#________________________ANDROID___________________________



def edit_Profile(request):
    lid = request.POST['lid']
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    phone = request.POST['phone']
    place = request.POST['place']
    # lid = request.POST['lid']
    # password = request.POST['pass']
    try:
        users = User.objects.get(LOGIN_id=lid)
        if users is None:
            data = {"task": "invalid"}

        else:
            users.fname=fname
            users.lname=lname
            users.email=email
            users.phone=phone
            users.place=place
            users.save()
            data = {"task": "valid", "id": users.id}
            r = json.dumps(data)
            return HttpResponse(r)
    except:
        data = {"task": "invalid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)

#________________________ANDROID___________________________



def login_code1(request):
    username = request.POST['uname']
    password = request.POST['pass']
    try:
        users = Login.objects.get(username=username, password=password)
        if users is None:
            data = {"task": "invalid"}

        else:
            data = {"task": "valid", "id": users.id}
            r = json.dumps(data)
            return HttpResponse(r)
    except:
        data = {"task": "invalid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)


def registration(request):
    print (request.POST)

    Fname = request.POST['firstname']
    Lname = request.POST['lastname']
    place = request.POST['place']

    phone = request.POST['phone']
    email_id = request.POST['email']
    uname = request.POST['username']
    passwd = request.POST['password']

    gender = request.POST['Gender']

    if Login.objects.filter(username=uname).exists():
        data = {"task": "not"}
        r = json.dumps(data)
        return HttpResponse(r)
    else:
        lob = Login()
        lob.username = uname
        lob.password = passwd
        lob.type = 'user'
        lob.save()

        user_obj = User()
        user_obj.fname = Fname
        user_obj.lname = Lname
        user_obj.place = place
        # user_obj.post = post_office
        # user_obj.pin = pin_code
        user_obj.phone = phone
        user_obj.gender = gender
        user_obj.email = email_id
        user_obj.LOGIN = lob
        user_obj.save()
        data = {"task": "success"}
        r = json.dumps(data)
        return HttpResponse(r)



def send_complaint_app(request):
    complaints = request.POST["Complaint"]
    u_id = request.POST["lid"]
    date = datetime.now()
    reply = "waiting"
    complaint_obj = Complaints()
    complaint_obj.Complaints = complaints
    complaint_obj.date = date
    complaint_obj.reply = reply
    complaint_obj.user = User.objects.get(LOGIN__id=u_id)
    complaint_obj.save()
    data = {'task': 'success'}
    r = json.dumps(data)
    return HttpResponse(r)



def send_Rating_app(request):
    print(request.POST)
    Ratings = request.POST["Ratings"]
    feedback = request.POST["feedback"]
    u_id = request.POST["lid"]
    date = datetime.now()
    complaint_obj =  Rating()
    complaint_obj. rating = Ratings
    complaint_obj.date = date
    complaint_obj.feedback = feedback
    complaint_obj.user = User.objects.get(LOGIN__id=u_id)
    complaint_obj.save()
    data = {'task': 'success'}
    r = json.dumps(data)
    return HttpResponse(r)


def send_addplaylist_app(request):
    song = request.POST["song"]
    genre = request.POST["genre"]
    musician = request.POST["musician"]
    details = request.POST["details"]
    file = request.FILES["file"]
    emotion = request.POST["emotion"]
    lid = request.POST["lid"]
    fs=FileSystemStorage()
    fn=fs.save(file.name,file)
    complaint_obj =  Manageplaylist()
    complaint_obj.song = song #.song is the name in the column of the database
    complaint_obj.genre = genre
    complaint_obj.musician = musician
    complaint_obj.details = details
    complaint_obj.file = fn
    complaint_obj.emotion = emotion
    complaint_obj.LOGIN = Login.objects.get(id=lid)
    complaint_obj.save()
    data = {'task': 'success'}
    r = json.dumps(data)
    return HttpResponse(r)



def reply_app(request):
    user_id = request.POST['lid']
    complaint_obj = Complaints.objects.filter(user__LOGIN__id=user_id)
    data = []
    for i in complaint_obj:
        row = {'Complaint': i.Complaints, 'Reply': i.reply, 'Date': str(i.date)}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)


def chatwithuser(request):
    lid=request.POST['lid']
    complaint_obj = User.objects.exclude(LOGIN__id=lid)
    data = []
    for i in complaint_obj:
        row = {'name': i.fname+" "+i.lname,'id':i.LOGIN.id}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)


def viewplaylist(request):
    lid = request.POST['lid']
    complaint_obj = Manageplaylist.objects.filter(LOGIN__id=lid)
    data = []
    for i in complaint_obj:
        row = {'song': i.song, 'genre': i.genre, 'musician':i.musician, 'details':i.details, 'file':i.file.url, 'emotion':i.emotion,"mid":i.id}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)
def view_comp(request):
    lid = request.POST['lid']
    complaint_obj = Complaints.objects.filter(user__LOGIN__id=lid)
    data = []
    for i in complaint_obj:
        row = {'song': i.Complaints, 'genre': str(i.date), 'musician':i.reply, 'details':i.id}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)

def view_profile(request):
    lid = request.POST['lid']
    q = User.objects.get(LOGIN_id=lid)
    data = []
    row={'fname': q.fname, 'lname': q.lname, 'phone':q.phone, 'email':q.email,'place':q.place}
    data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)

def rplaylist(request):
    mid = request.POST['mid']
    complaint_obj = Manageplaylist.objects.get(id=mid)
    complaint_obj.delete()
    r = json.dumps({"task":"ok"})
    return HttpResponse(r)

def delete_comp(request):
    mid = request.POST['mid']
    complaint_obj = Complaints.objects.get(id=mid)
    complaint_obj.delete()
    r = json.dumps({"task":"ok"})
    return HttpResponse(r)


def in_message2(request):
    print(request.POST)
    fromid = request.POST['fid']
    print("fromid",fromid)

    toid = request.POST['toid']
    print("toid",toid)

    message=request.POST['msg']
    ob=Chat()
    ob.Fromid=Login.objects.get(id=fromid)
    ob.Toid=Login.objects.get(id=toid)
    ob.message=message
    ob.date=datetime.today()
    ob.save()

    return JsonResponse({"status":'send'})


def view_message2(request):
    print("wwwwwwwwwwwwwwww")
    print(request.POST)
    fromid=request.POST['fid']
    print(fromid)
    toid=request.POST['toid']
    print(toid)
    lmid = request.POST['lastmsgid']
    print("msgggggggggggggggggggggg"+lmid)
    sen_res = []
    ob=Chat.objects.filter(Fromid__id=fromid,Toid__id=toid,id__gt=lmid)
    ob1=Chat.objects.filter(Fromid__id=toid,Toid__id=fromid,id__gt=lmid)
    ob=ob.union(ob1).order_by("id")

    data=[]
    # date[i] = jsob.getString("date");
    # msg[i] = jsob.getString("message");
    # fid[i] = jsob.getString("fromid");
    # mid[i] = jsob.getString("msgid");
    for i in ob:
        r={"date":str(i.date),"message":i.message,"fromid":i.Fromid.id,"msgid":i.id}
        data.append(r)


    if len(data)>0:
        return JsonResponse({"status":'ok', "res1":data})
    else:
        return JsonResponse({"status":'not found'})

def capture(request):
    try:
        os.remove(r"E:\25-03-2024\Web\emo_player\media\s.jpg")
    except:
        pass
    f = request.FILES['files']
    # =================================================
    fn=FileSystemStorage()
    import time
    ffl = time.strftime("%Y%m%d_%H%M%S")
    reg = time.strftime("%Y%m%d_%H%M%S")+ ".jpg"
    kk = "pic.jpg"
    pp=os.path.join(r'E:\25-03-2024\Web\emo_player\media\emotion\\', reg)
    fn.save(r'E:\25-03-2024\Web\emo_player\media\emotion\\'+ reg, f)
    ff = fn.save(f.name,f)
    # ff = secure_filename(file.filename)
    em = ""
    emotion="neutral"
    model = model_from_json(open(r"E:\25-03-2024\Web\emo_player\emo\model\facial_expression_model_structure.json", "r").read())
    model.load_weights(r'E:\25-03-2024\Web\emo_player\emo\model\facial_expression_model_weights.h5')  # load weights

    global rec_emotions
    face_cascade = cv2.CascadeClassifier(r'E:\25-03-2024\Web\emo_player\emo\model\haarcascade_frontalface_default.xml')

    # cap = cv2.VideoCapture(0)

    emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
    i=0
    global flag


    img = cv2.imread(pp)
    print(pp,'zzzzzzzzzzzzzzzzzzzzzzzzz')

    path=r"E:\25-03-2024\Web\emo_player\media\emotion\\"

    try:
        img = rotate(img, 90)
        cv2.imwrite(path+"pic.jpg", img)
        #

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        print(faces)

    except Exception as e:
        faces=[]
        print(e,"++++++++++++++++++")

    for (x,y,w,h) in faces:
        try:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #draw rectangle to main image

            detected_face = img[int(y):int(y+h), int(x):int(x+w)] #crop detected face
            detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY) #transform to gray scale
            detected_face = cv2.resize(detected_face, (48, 48)) #resize to 48x48

            img_pixels = image.img_to_array(detected_face)
            img_pixels = np.expand_dims(img_pixels, axis = 0)

            img_pixels /= 255 #pixels are in scale of [0, 255]. normalize all pixels in scale of [0, 1]

            predictions = model.predict(img_pixels) #store probabilities of 7 expressions

            #find max indexed array 0: angry, 1:disgust, 2:fear, 3:happy, 4:sad, 5:surprise, 6:neutral
            max_index = np.argmax(predictions[0])

            emotion = emotions[max_index]
            # rec_emotions.append(emotion)
            # print ("dd",emotion)
        except Exception as e:
            print(e,"+++++++++++++++++++++++++++++")

        # if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
        #     break

        # kill open cv things
    # cap.release()
    # cv2.destroyAllWindows()
    em=emotion
    print(em,'/////////////////////////////??????????????????????????????????????/')
    # ====================================================================================================
    data = {"task": em}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)

def viewplaylist_emo(request):
    lid=request.POST['lid']
    emo=request.POST['emo']
    complaint_obj = Manageplaylist.objects.filter(emotion=emo)
    data = []
    for i in complaint_obj:
        row = {'song': i.song, 'genre': i.genre, 'musician': i.musician, 'details': i.details, 'file': i.file.url,
               'emotion': i.emotion, "mid": i.id}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)