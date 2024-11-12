# Universidad de las Fuerzas Armadas ESPE

## Taller 1: Creación de una API para la Gestión de Libros con Flask, PostgreSQL y Docker
### Materia: Aplicaciones Distribuidas 2553

### Integrantes:
- Matías Padrón
- David Cantuña
- Mateo Román
- William Leon

---

### Descripción
Bienvenido al Taller 1, el cual consiste en la creación de una API REST utilizando Flask para gestionar una biblioteca de libros. Las operaciones básicas que soporta esta API son agregar, consultar, actualizar y eliminar libros. La aplicación utiliza PostgreSQL como base de datos para almacenar los datos y Docker para facilitar el despliegue y la portabilidad del entorno.

---

### Pasos de Despliegue del Proyecto

#### 1. Clonar el Repositorio
```bash
git clone https://github.com/mspadron28/Taller1_APIRESTFlask
```

#### 2. Configuración del Proyecto

##### 2.1. Creación de la Imagen
Después de clonar el repositorio, se debe construir la imagen utilizando el Dockerfile. Para ello, ejecuta el siguiente comando:
```bash
docker build -t flaskapi:v1 .
```

##### 2.2. Creación de una Red en Docker
Es importante crear una red para que los contenedores (tanto el de la base de datos como el de la aplicación) puedan conectarse entre sí. Utiliza el siguiente comando:
```bash
docker network create flasknetwork
```

##### 2.3. Creación del Contenedor de la Base de Datos (PostgreSQL)
Crea un contenedor para PostgreSQL con el siguiente comando:
```bash
docker run -d --network flasknetwork -p 5478:5432 --name container-flaskpg -e POSTGRES_USER=tallerapiflask -e POSTGRES_PASSWORD=tallerapiflask -e POSTGRES_DB=library postgres:latest
```

##### 2.4. Creación del Contenedor para la API
Despliega el contenedor que contiene la imagen de la API con el siguiente comando:
```bash
docker run -p 5000:5000 -d --network flasknetwork --name container-appflask flaskapi:v1
```

---

### Uso de la API

Con los contenedores en funcionamiento, puedes utilizar Postman (o cualquier otra herramienta para probar APIs) para realizar peticiones a la API en el siguiente endpoint:
```
http://localhost:5000/books
```

#### Métodos Disponibles
- **GET**: Para obtener la lista de libros.
- **POST**: Para agregar un nuevo libro.
- **PUT**: Para actualizar un libro existente.
- **DELETE**: Para eliminar un libro.

---
