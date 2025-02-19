import os
import multiprocessing
import time

sem_docs = multiprocessing.Semaphore(1)

def creacion(archivo):
    sem_docs.acquire()
    try:
        print(f"Proceso hijo con PID: {os.getpid()}")
        print("Creación de archivos.")
        print(f"Creando el archivo {archivo}")
        a = open(archivo, "w")
        a.close()
        time.sleep(2)
        print(f"Archivo {archivo} creado.\n")
    except FileExistsError:
        print(f"El archivo {archivo} ya existe.\n")
    finally:
        sem_docs.release()

def listado():
    sem_docs.acquire()
    try:
        print(f"Proceso de listado con PID: {os.getpid()}")
        archivos = os.listdir('.')
        print("Lista de archivos:")
        print(archivos)
        print("\n")
    finally:
        sem_docs.release()

def eliminacion(archivo):
    sem_docs.acquire()
    try:
        print(f"Proceso para eliminación de archivos con PID: {os.getpid()}")
        os.remove(archivo)
        print(f"Archivo {archivo} eliminado.\n")
        time.sleep(2)
    except FileNotFoundError:
        print(f"Archivo {archivo} no encontrado.\n")
    finally:
        sem_docs.release()

archivos = ["archivo1.txt", "archivo2.txt", "archivo3.txt"]

print(f"Proceso padre PID:{os.getpid()}")

procesos_list = []

for n_arch in archivos:
    c = multiprocessing.Process(target=creacion, args=(n_arch,))
    procesos_list.append(c)
    c.start()

for c in procesos_list:
    c.join()

c_list = multiprocessing.Process(target=listado)
c_list.start()
c_list.join()

for n_arch in archivos:
    c = multiprocessing.Process(target=eliminacion, args=(n_arch,))
    procesos_list.append(c)
    c.start()

for n_arch in archivos:
	c = multiprocessing.Process(target=creacion, args=(n_arch,))
	procesos_list.append(c)
	c.start()

for c in procesos_list:
    c.join()

print(f"El procesos padre ha terminado PID: {os.getpid()}")
