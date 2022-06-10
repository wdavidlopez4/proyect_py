# proyect_py
proyecto de py para prueba técnica 

## creacion entorno virtual
  debe tener instalado el manejador 'pip install virtuallenv'
  python -m venv

## acticacion entorno virtual
  se posiciona en el directoro principal
  ejecutamos el .bat desde la ruta '.\venv\Scripts\activate.bat'
  
## instalacion de plugins
  pip install -r requirements.txt
  
## crear db con el nombre 
  en app.js configurar el coneccion string con el puerto, predenciales y nombre de la db
  postgresql://postgres:1234@localhost:5432/pruebadb
  
## creacion del primer usuario en el sistema para poder ingresar
  INSERT INTO public."Users"(
	id, name, password, mail, "isLogin")
	VALUES (?, ?, ?, ?, ?);
  
##listo disfrutar del software

#caracteristicas arquitectonicas

## sistema diseñado en capas
  DAL capa de acceso a datos
  BLL capa de logica de negosio
  APP capa de integracion

##stack architectonico
  flask 
  virtual ejecucion pip
