import cv2
import os
import pickle
import face_recognition_models
import face_recognition
import numpy as np
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://face-recognition-95fc2-default-rtdb.firebaseio.com/",
    'storageBucket':"face-recognition-95fc2.appspot.com"
})

bucket=storage.bucket()


cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

imgbackground=cv2.imread('resources/background.png')

#importing modes images
foldermodepath='resources/Modes'
modepathlist=os.listdir(foldermodepath)
imgmodelist=[]
for path in modepathlist:
    imgmodelist.append(cv2.imread(os.path.join(foldermodepath,path)))

# load the encod file
print("loading encoded file...")
file=open('encodefile.p','rb')
encodelistknonwwithids=pickle.load(file)
file.close()
encodelistknonw,studentsIds=encodelistknonwwithids
# print(studentsIds)
print("encode file loaded")


#for mode when face detection
modetype=0
counter=0
id
imgstudent=[]


while True:
    success,img=cap.read()

    imgs=cv2.resize(img,(0,0),None,0.25,0.25)
    imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
    
    #the new faces encoding
    facecurrentframe=face_recognition.face_locations(imgs)
    encodecurrentframe=face_recognition.face_encodings(imgs,facecurrentframe)

    imgbackground[162:162+480,55:55+640]=img
    imgbackground[44:44+633,808:808+414]=imgmodelist[modetype]

   #the compare between faces encoded and new face encoded
    for encodeface,facelocation in zip(encodecurrentframe,facecurrentframe):
        matches=face_recognition.compare_faces(encodelistknonw,encodeface)
        facedistance=face_recognition.face_distance(encodelistknonw,encodeface)
        # print("matches",matches)
        # print("facedis",facedistance)

        matchindex=np.argmin(facedistance)
        # print("match index",matchindex)

        if matches[matchindex]:

            # print("known face detected")
            # print(studentsIds[matchindex])
            y1,x2,y2,x1=facelocation
            y1,x2,y2,x1= y1*4,x2*4,y2*4,x1*4
            bbox= 55+x1,162+y1,x2-x1,y2-y1
            imagebackground= cvzone.cornerRect(imgbackground,bbox,rt=0)
            id=studentsIds[matchindex]
            if counter==0:
                counter=1
                modetype=1
        #download from firebase
        if counter!=0:
            if counter==1:
                #get data 
                studentinfo=db.reference(f'students/{id}').get()
                print(studentinfo)

                #get the image from the storage in firebase
                blob=bucket.blob(f'images/{id}.png')
                array=np.frombuffer(blob.download_as_string(),np.uint8)
                imgstudent=cv2.imdecode(array,cv2.COLOR_BGRA2BGR)
            cv2.putText(imgbackground,str(studentinfo['dep']),(1006,550),cv2.FONT_HERSHEY_COMPLEX,.5,(100,100,100),1)
            cv2.putText(imgbackground,str(studentinfo['name']),(1006,493),cv2.FONT_HERSHEY_COMPLEX,.5,(100,100,100),1)
            cv2.putText(imgbackground,str(studentinfo['number']),(861,125),cv2.FONT_HERSHEY_COMPLEX,.6,(255,255,255),1)

            #put image downloaded from firebase in graphic
           
            imgstudent_resized = cv2.resize(imgstudent, (216, 216))
            imgbackground[175:175+216,909:909+216]=  imgstudent_resized

            counter+=1

    cv2.imshow("face Attendance",imgbackground)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
