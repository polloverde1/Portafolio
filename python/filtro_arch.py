#Porgrama Filtro

import os

class FiltroArchivos:
    def __init__(self):
        self.car_extensiones = {}
        self.ruta_carpeta = None

    def primera(self):
        print("Programa Filtro.")
        ruta = input("Ingresa la ruta a guardar las carpetas ex.(/home/usuario): ")
        
        while True:
            print(f"Carpeta donde se va a guardar la carpeta {ruta}")
            
            carpetas = input("\nIngresa el nombre de las carpetas: ")
            self.ruta_carpeta = os.path.join(ruta, carpetas)
            os.makedirs(self.ruta_carpeta, exist_ok=True)
            
            extensiones = input("Extensiones a guardar en esta carpeta (separados por ,): ").split(",")
            self.car_extensiones[carpetas] = extensiones
            print(f"Carpeta {carpetas} con extensiones: {extensiones}\n")
            opc = input("Deseas agregar otra carpeta (s/n): ").lower()
            if opc != 's':
                break

    def Busqueda(self):
        ruta_archivos = input("Ingresa la ruta de archivos a filtrar: ")
        print(f"\nCarpeta donde se va a generar la busqueda {ruta_archivos}")

        total_archivos = 0
        procesados = 0

        for root, dirs, files in os.walk(ruta_archivos):
            total_archivos += 1
            for archivo in files:
                procesados += 1
                archivo_rcom = os.path.join(root, archivo)
                arch_ext = os.path.splitext(archivo)[1]

                for carpeta, extensiones in self.car_extensiones.items():
                    if arch_ext in extensiones:
                        destino = os.path.join(self.ruta_carpeta, archivo)
                        os.rename(archivo_rcom, destino)
                        print(f"[{procesados}/{total_archivos}]Archivo: {archivo} -> {destino}".encode('utf-8','replace').decode('utf-8'))
                        
        
        
            
filtro = FiltroArchivos()
filtro.primera()
filtro.Busqueda()
