### Juan Diego Gonzalez Gomez – 201911031

## Proyecto 0

- Enlace Repositorio Github (Código fuente de la aplicación):
https://github.com/JuanDiegoGonzalez/Proyecto0_Cloud

- Enlace Sustentación (Video):
https://www.youtube.com/watch?v=z-OZsRIz8-Q

- Enlace Contenedores Docker:

https://hub.docker.com/repository/docker/juandigz/proyecto0_front/general
https://hub.docker.com/repository/docker/juandigz/proyecto0_back/general

- Instrucciones de Despliegue y Uso:

  -	Backend (Flask):
    - Desde una terminal de Powershell, ejecutar el comando:

  ```shell
  docker run --name proyecto0_back -p 5000:5000 -e -d juandigz/proyecto0_back
  ```

      -	Ir a la ruta http://127.0.0.1:5000/tareas/ (aparecerá un mensaje indicando que falta el header de autorización, ya que no se ha hecho login. Esto se puede realizar a través de una petición POST desde Postman)

  - Frontend (Angular):
    - Desde otra terminal de Powershell, ejecutar el comando:

  ```shell
  docker run --name proyecto0_front -p 8080:8080 -e -d juandigz/proyecto0_front
  ```

    -	Ir a la ruta http://127.0.0.1:8080/


- Enlace Documentación con Postman:
https://documenter.getpostman.com/view/12464767/2sA2r3YRC1

