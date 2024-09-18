#!/bin/bash

docker build -t gestion-usuarios:1.0 .

if [ $? -eq 0 ]; then
    echo "La imagen Docker se ha construido correctamente."
else
    echo "Error al construir la imagen Docker."
    exit 1
fi
