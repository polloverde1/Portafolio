#!/bin/bash

# Obtiene la dirección IPv6
ip6=$(curl -s -6 ifconfig.co)

# Verifica si la dirección IPv6 se obtuvo correctamente
if [[ -z "$ip6" ]]; then
    echo "Error: No se pudo obtener la dirección IPv6."
    exit 1
fi

vieja_ipv6(){
    sudo ufw status numbered | grep 'v6' | grep 'ALLOW IN' | awk '{for(i=1;i<=NF;i++) if ($i ~ /:/) print $i}' | head -n 1
}

actual=$(vieja_ipv6)

echo "Direccion IPv6 vieja: $actual"
echo "Dirección IPv6 obtenida: $ip6"
echo ""


# Normaliza la dirección IPv6 eliminando máscaras
ip6_normalizada="${ip6%%/*}"

# Configuración para UFW
port= #puerto
proto= #protocolo
int= #interfaz_de_red

# Elimina reglas existentes que coincidan con el puerto y protocolo
reglas=$(sudo ufw status numbered | grep "${port}/${proto}" | grep "v6")
echo "$reglas" | while read -r line; do
    # Verifica si la línea contiene la interfaz y la palabra
    if [[ "$line" == *"ALLOW"* && "$line" == *"$actual"* ]]; then
        regla_num=$(echo "$line" | awk '{print $1}' | tr -d '[]')
        # Elimina la regla sin necesidad de confirmación
        yes | sudo ufw delete "$regla_num"
    fi
done

#Agrega la nueva regla con la dirección IPv6
sudo ufw allow in on "$int" to "$ip6" port "$port" proto "$proto"

echo "Regla actualizada para $ip6 en el puerto $port ($proto)."
