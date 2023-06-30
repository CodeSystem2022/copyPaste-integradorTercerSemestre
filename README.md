# CopyPaste - Trabajo Integrador del Tercer Semestre Año 2023

![Logo Copy:Paste](https://user-images.githubusercontent.com/103675851/232830051-f665dac5-7813-4c63-8612-a451b562bdf7.jpg)

<div id="header" align="end">
		<h3 align="end">Repositorio del trabajo integrador en Python del grupo Copy Paste</h3>
		<h4 align="end">En este repositorio se encuentra el trabajo integrador del grupo</h4>
</div>
 
<div >
  <h2> 📚 Tecnologías del repositorio: </h2>
	<br>
  <div align="center">
    	<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="PYTHON" width="35" height="35">&nbsp; PYTHON 
	   <br> <br>
	<img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain.svg" title="Django" alt="DJANGO" width="35" height="35">&nbsp; DJANGO
	  <br> <br>
	  <img src="https://github.com/devicons/devicon/blob/master/icons/html5/html5-original.svg" title="JavaScrip" alt="JS" width="35" height="35">&nbsp; JAVASCRIPT
	   <br> <br>
	  <img src="https://github.com/devicons/devicon/blob/master/icons/css3/css3-original.svg" title="Css3" alt="CSS3" width="35" height="35">&nbsp; CSS3
	   <br> <br>
	  <img src="https://github.com/devicons/devicon/blob/master/icons/javascript/javascript-plain.svg" title="Html5" alt="HTML5" width="35" height="35">&nbsp; HTML5
	   <br> <br>
	  <img src="https://github.com/devicons/devicon/blob/master/icons/bootstrap/bootstrap-original.svg" title="Bootstrap" alt="BOOTSTRAP" width="35" height="35">&nbsp; BOOTSTRAP
	  <br> <br>
	  <img src="https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original.svg" title="PostgreSql" alt="POSTGRESQL" width="35" height="35">&nbsp; POSTGRESQL
    <br>
  </div>
</div> 

<h2> 🗂 Proyecto del repositorio:</h2>
	<br>
<h4>  Nuestro turnero médico es una aplicación diseñada para gestionar turnos médicos de manera eficiente y sencilla. Este proyecto se enfoca en ofrecer una solución para cualquier tipo de consultorio médico, clinica u hospital que requiera de la organización de sus pacientes a través de consultas o turnos médicos. <br> <br>
  La app es una herramienta para gestionar y administrar las consultas y turnos médicos, optimizando la calidad del servicio al paciente y facilitandole al administrador la tarea de llevar a cabo las consultas y turnos médicos . La app puede ser utilizada tanto por los pacientes como por el personal médico o administrativo de la institución sanitaria ya que permite la creación de usuarios con diferentes roles.</h4>
<br>


<h2><strong><u> 👤 Integrantes</u></strong></h2>

<div align="center">	
<h3>	  
  Britez Neira Leila
  <br>
  Solán Leonardo
  <br>
  Viola Jésica
 </div>
   <br>

   <hr>

<h3><strong><u> ✅ Funcionalidades de la aplicación turnero: </u></strong></h3>
<br>
	✔️ Registro de clientes y servicios. <br>
	✔️ Asignación de turnos según servicio y su nivel de prioridad. <br>
	✔️ Visualización en vivo de los turnos actuales por fila. <br>
	✔️ Creación de diferentes filas según los servicios disponibles. <br>
	✔️ Panel de administración para gestionar los diferentes datos. <br>
	✔️ Gestión de usuarios y permisos.  <br>
<br>
<br>
<h3><strong><u> ▶️ Puesta en marcha del proyecto: </u></strong></h3>
1. Luego de clonar el repositorio : `git clone https://github.com/CodeSystem2022/CopyPaste_TercerSemestre.git `.<br>
2. Vamos a la carpeta del proyecto : `cd CopyPaste_TercerSemestre `.<br> 
3. Iniciamos nuestro entorno virtual que ya está creado y se llama turnero-env : `turnero-env\scripts\activate `.<br>
4. Instalamos los requerimientos de nuestro proyecto : `pip install -r requirements.txt `.<br>
5. Creamos una base de datos local y luego modificamos el archivo settings.py para conectar el proyecto con la base de datos PostgreSQL recién creada: <br> <br>
    ```
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '< nomobre de tu base de datos >',
        'USER': '< tu usuario >',
        'PASSWORD': '< tu contraseña >',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
    ```
6. Entramos a la carpeta del proyecto propiamente dicha : `cd turnero `.<br>
7. Realizamos las migraciones correspondientes de nuestras tablas a nuestra base de datos: `python manage.py makemigrations` + `python manage.py migrate `.<br>
8. Recolectamos nuestros archivos estáticos : `python manage.py collectstatic `.<br>
9. Iniciamos nuestro servidor : `python manage.py runserver `.<br>
10. Entramos al http://127.0.0.1:8000/ para poder ver las interfaces de nuestra aplicación.<br>


