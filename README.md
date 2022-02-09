
# Project Habit

### Descripción
para este proyecto, se decidió no utilizar frameworks, solo con Python se creo la api. Para cumplir con los requerimientos se crearon los siguientes archivos.

* ####  connection.py 
     En este módulo nos conectamos a la bd y realizamos las consultas.
* #### controllers.py
     En este módulo tenemos la logica del negocio
* #### serializers.py
     En este módulo serializamos la data obtenida de la bd
* ### server.py
    En este módulo tenemos el proceso de iniciacion del server y el procesamiento
    de los request.


### la tecnologias utilizadas son: 

* [python](https://www.python.org/) - Lenguaje de programación
* [python-dotenv](https://pypi.org/project/python-dotenv/) -  dependencia para manejo de variables 
* [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) - paquete para conectar base de datos

### Pre-requisitos:
* Se debe intalar Python
* Se debe crea un entorno python -m venv 
* Iniciar el entorno


### Instalación: 
 * pip install -r requirements.txt 
 * git clone https://github.com/lagm1290/habit.git 
 * python server.py

### Ejemplo JSON fronted
* http://127.0.0.1:8080/property?ano=2021&ciudad=pereira&estado=pre_venta