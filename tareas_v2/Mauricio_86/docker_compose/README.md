# Docker Compose Postgres

## Material de apoyo
https://coffeebytes.dev/docker-compose-tutorial-con-comandos-en-gnu-linux/ 

## Ejecutar docker-compose

Commands to create the db table:
Lanza los contenedores desde especificados en docker-compose.yml.

Asegurate de estar en la carpeta .../codigo/docker_compose/

> docker-compose up
Para recostruir los contenedores que tienen `build`
> docker-compose up --build
## Entrar al jupyter lab 
Entra a tu navegador y pon l url:
`localhost:8887`

## Entrar a contenedores
Entrar al contendedor del app
> docker exec -it postgres_app /bin/bash
Entrar al contendedor de postgres 
> docker exec -it postgres_db /bin/bash

