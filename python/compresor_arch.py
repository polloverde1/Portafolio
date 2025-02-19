import tarfile
import os

def compress_directory(directory_path, output_filename):
    # Verificar si el directorio existe
    if os.path.isdir(directory_path):
        with tarfile.open(output_filename, "w:gz") as tar:
            tar.add(directory_path, arcname=os.path.basename(directory_path))
        print(f"Directorio {directory_path} comprimido como {output_filename}")
    else:
        print(f"El directorio {directory_path} no existe.")

def main():
    # Directorios a comprimir
    directories = ['/home', '/var', '/etc']

    # Comprimir cada directorio
    for directory in directories:
        output_filename = f"/respaldos/{os.path.basename(directory)}.tar.gz"
        compress_directory(directory, output_filename)

if __name__ == "__main__":
    # Crear el directorio /respaldos si no existe
    if not os.path.exists('/respaldos'):
        os.makedirs('/respaldos')

    main()
