
#LIBRERIAS
import os
from google.cloud import storage


#LLAVE
"""Se debe descargar el archivo json de credenciales desde google cloud"""
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'pruebas2.json'


#CREACIÓN DEL BUCKET
storage_client = storage.Client()
name = input("Ingrese el nombre: ") #Nombrar el bucket
bucket_name = name
bucket = storage_client.create_bucket(bucket_name, location='us') #Escoger región del servidor


#DETALLE DEL BUCKET
vars(bucket)


#ACCESO A UN BUCKET SPECIFICO
my_bucket = storage_client.get_bucket(bucket_name)



#CARGAR ARCHIVOS A UN BUCKET
def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False

#Ruta del archivo
file_path = r"C:\Users\yeiso\Documentos\Proyecto\Nueva carpeta\archivo1.txt" 
upload_to_bucket('archivoprueba1', file_path, bucket_name)


#DESCARGAR ARCHIVOS A UN BUCKET
def download_file_from_bucket(blob_name, file_path, bucket_name):
    try:
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.download_to_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False

bucket_name = bucket_name 
file_path = r"C:\\Users\yeiso\Documentos\Proyecto\archivoprueba1.txt"

download_file_from_bucket('archivoprueba1', file_path, bucket_name)
