import cv2
import face_recognition_models
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://face-recognition-95fc2-default-rtdb.firebaseio.com/",
    'storageBucket':"face-recognition-95fc2.appspot.com"
})

#importing  images
folderimagespath='images'
imagespathlist=os.listdir(folderimagespath)
imgslist=[]
studentsIds=[]
print(imagespathlist)


for path in imagespathlist:
    imgslist.append(cv2.imread(os.path.join(folderimagespath,path)))
    studentsIds.append(os.path.splitext(path)[0])

    #for upload firebase storage
    filename=f'{folderimagespath}/{path}'
    bucket=storage.bucket()
    blob=bucket.blob(filename)
    blob.upload_from_filename(filename)
    # print(os.path.splitext(path)[0])
print(studentsIds)



def findencoding(imageslist):
    encodelist=[]
    for img in imageslist:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist
print('encoding started ..')
encodelistknonw=findencoding(imgslist)
encodelistknonwwithids=[encodelistknonw,studentsIds]
# print(encodelistknonw)
print('encoding complete')

file=open("encodefile.p",'wb')
pickle.dump(encodelistknonwwithids,file)
file.close()
print("file saved")