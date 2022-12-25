import os

from django.core.files.storage import FileSystemStorage
from facerec.main import predict

from web.settings import MEDIA_ROOT

dir_pegawai = os.path.join(MEDIA_ROOT, 'pegawai')
dir_presensi = os.path.join(MEDIA_ROOT, 'presensi')

def predict_pegawai(image):
    fs = FileSystemStorage(dir_presensi)
    filename = fs.save(image.name, image)
    fileurl = os.path.join(dir_presensi, filename)
    predictions = predict(fileurl, model_path='media/model/model_wajah.clf')
    print(predictions)
    if len(predictions) != 1:
        return False
    else:
        return predictions[0][0]

def save_image(name, files):
    path = os.path.join(dir_pegawai, name)
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
    fs = FileSystemStorage(path)
    c = 1
    for file in files:
        filename = f'{name}{c}.jpg'
        fs.save(filename, file)
        c+=1
    return

