#!/bin/bash

IMAGE_NAME="gestion-usuarios:1.0"
CONTAINER_NAME="gestion-usuarios"
HOST_PORT=5000
CONTAINER_PORT=5000

if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    echo "El contenedor '$CONTAINER_NAME' ya existe. Eliminando..."
    docker stop $CONTAINER_NAME
    docker rm -f $CONTAINER_NAME
fi

if [ "$(docker ps -q -f publish=$HOST_PORT)" ]; then
    echo "El puerto $HOST_PORT está en uso por otro contenedor. Liberando el puerto..."

    container_to_stop=$(docker ps --filter "publish=$HOST_PORT" -q)
    if [ ! -z "$container_to_stop" ]; then
        docker stop $container_to_stop
        docker rm -f $container_to_stop
        echo "Contenedor detenido y eliminado para liberar el puerto $HOST_PORT."
    fi
fi

docker run -d --name $CONTAINER_NAME -p $HOST_PORT:$CONTAINER_PORT $IMAGE_NAME

if [ $? -eq 0 ]; then
    echo "El contenedor '$CONTAINER_NAME' se está ejecutando en segundo plano."
else
    echo "Error al ejecutar el contenedor '$CONTAINER_NAME'."
    exit 1
fi
