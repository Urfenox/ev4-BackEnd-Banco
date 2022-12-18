# ev4-BackEnd-Banco
Todo muy temático.

## Setup
Para hacer funcionar el proyecto debes:

 1. Tener Python
 2. Tener PIP (de Python)
 3. PyMySQL (pip de Python)
 4. Tener Django
 5. Tener Wampserver o XAMPP
 6. Tener Django Rest Framework

## Iniciando
Para que todo funcione:

### Base de Datos MySQL
 1. Ejecuta Wampserver
 2. En el tray icon de Wampserver, mantén el ítem "PhPMyAdmin" y luego selecciona una versión para el panel MySQL.
 3. En el panel, crea una nueva base de datos llamada `banquito`.
 
 Ahora debes tener instalado *PyMySQL*:
 
 1. Inicia una consola de comandos (cmd.exe)
 2. Escribe `pip install PyMySQL` y presiona `Enter`.
 3. Espera a que el proceso de instalación termine.

Ahora debes instalar *Django REST Framework*:

 1. En la consola de comandos `(cmd.exe)`
 2. Escribe `pip install djangorestframework` y presiona `Enter`.
 3. Espera a que el proceso de instalación termine.

### Django
Ahora debes migrar la aplicación para usar la base de datos ya creada.

 1. Dentro de la carpeta principal del proyecto, mantén la tecla `SHIFT` y has clic derecho.
 2. Selecciona el ítem "Abrir la ventana PowerShell aquí"
 3. Escribe `py manage.py makemigrations` y presiona `Enter`
 4. Ahora escribe `py manage.py migrate` y presiona `Enter`

### Ejecución
Ahora que todo debería estar listo:

 1. En la consola PowerShell y otro
 2. Escribe `py manage.py runserver` y presiona `Enter`

### Listo
Ahora te vas a [127.0.0.1:8000](http://127.0.0.1:8000/) para ver el proyecto en ejecución.

---
### Solución de problemas

 - **Boo hoo. Cuando hago las migraciones, Django me dice que una tabla no existe.**
 *Django cree que la base de datos ya existe porque un trozo de código está tratando de acceder a los modelos muy tempranamente.* ***Lo que debes hacer*** es comentar toda línea de código que use algún modelo, o conexión a base de datos.
	 - views.py
	 - urls.py
	 - models.py
