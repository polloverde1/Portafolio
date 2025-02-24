#!/bin/bash

# Obtiene la nueva IPv6
nueva=$(curl -s -6 ifconfig.co)
if [[ -z "$nueva" ]]; then
    echo "Error: No se pudo obtener la IPv6 actual."
    exit 1
fi

# Normaliza la dirección IPv6 eliminando máscaras
nueva_normalizada="${nueva%%/*}"

# Función para obtener la IPv6 vieja de las reglas de UFW
vieja_ipv6(){
    sudo ufw status numbered | grep 'v6' | grep 'ALLOW IN' | awk '{for(i=1;i<=NF;i++) if ($i ~ /:/) print $i}' | head -n 1
}

# Obtiene la IPv6 actual configurada en UFW
actual=$(vieja_ipv6)
if [[ -z "$actual" ]]; then
    echo "No se encontró una IPv6 configurada en UFW."
    exit 1
fi

# Normaliza la dirección IPv6 eliminando máscaras
actual_normalizada="${actual%%/*}"

# Añadir mensajes de depuración
echo "IPv6 Nueva: $nueva_normalizada"
echo "IPv6 Actual: $actual_normalizada"

# Compara la IPv6 actual con la nueva
if [[ "$actual_normalizada" != "$nueva_normalizada" ]]; then
    echo "La IPv6 ha cambiado. Actualizando reglas de UFW..."
    echo "$nueva"
    #Se especifica el archivo .sh para efectuar los cambios de direccion ipv6.
else
    echo "La IPv6 no ha cambiado. No se necesitan actualizaciones."
    exit 0
fi

