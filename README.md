# Pythonando  


Todos os projetos do evento 4 Days 4 Projects, promovido pela Pythonando | Fevereiro de 2025  



  
## Projeto 1 - Controle de Finanças Pessoais com Python Puro  


* Primeiro devemos criar o ambiente virtual: 


--> Linux  


python3 -m venv venv  


--> Windows  


python -m venv venv  


* Após a criação do venv vamos ativa-lo:

 
--> Linux  


source venv/bin/activate 


--> Windows  


venv\Scripts\Activate  


* Caso algum comando retorne um erro de permissão execute o código e tente novamente:

   
Set-ExecutionPolicy Scope CurrentUser ExecutionPolicy RemoteSigned


* Agora vamos fazer a instalação das bibliotecas necessárias:


pip install sqlmodel  




## Projeto 2 - Aplicação Web Fullstack com Python e Django  

  
* Primeiro devemos criar o ambiente virtual:  


--> Linux  


python3 -m venv venv  


--> Windows  


python -m venv venv  


* Após a criação do venv vamos ativa-lo:

  
--> Linux 


source venv/bin/activate


--> Windows  


venv\Scripts\Activate  

  
* Caso algum comando retorne um erro de permissão execute o código e tente novamente:


Set-ExecutionPolicy Scope CurrentUser ExecutionPolicy RemoteSigned  

  
* Agora vamos fazer a instalação do Django e as demais bibliotecas:


pip install django  
pip install pillow  


* Rode o servidor para testar:


python manage.py runserver  


  
* Para preparar migrações, execute:

  
python manage.py makemigrations  

  
* Para realizar migrações, execute:

  
python manage.py makemigrations  



  
## Projeto 3 - Rest API com Python e Django  

  
* Primeiro devemos criar o ambiente virtual:

  
--> Linux  


python3 -m venv venv  


--> Windows 


python -m venv venv  

  
* Após a criação do venv vamos ativa-lo:

  
--> Linux  


source venv/bin/activate  


--> Windows  


venv\Scripts\Activate  

  
* Caso algum comando retorne um erro de permissão execute o código e tente novamente:

    
Set-ExecutionPolicy Scope CurrentUser ExecutionPolicy RemoteSigned

  
* Agora vamos fazer a instalação do Django e as demais bibliotecas:

   
pip install django  
pip install pillow  
pip install django-ninja  

  
* Rode o servidor para testar:

  
python manage.py runserver  

  
* Para preparar migrações, execute:

   
python manage.py makemigrations  

  
* Para realizar migrações, execute:

  
python manage.py makemigrations


  
  
## Projeto 4 - APP Mobile + Rest API com Python e Django  

  
* Primeiro devemos criar o ambiente virtual:


--> Linux  


python3 -m venv venv  


--> Windows  


python -m venv venv  

  
* Após a criação do venv vamos ativa-lo:

   
--> Linux 


source venv/bin/activate  


--> Windows  


venv\Scripts\Activate 

  
* Caso algum comando retorne um erro de permissão execute o código e tente novamente:

  
Set-ExecutionPolicy Scope CurrentUser ExecutionPolicy RemoteSigned

  
* Agora vamos fazer a instalação do Django e as demais bibliotecas:

  
pip install flet  
pip install requests  


* Para executar a interface, execute:

  
flet run app.py  


* Ou, a depender de seu sistema operacional:

   
python app.py  


python3 app.py  

  
### Esse projeto está relacionado ao projeto 3, por isso, é necessário que ele esteja rodando.  


* Rode o servidor para testar:

   
python manage.py runserver  

  
* Para preparar migrações, execute:

  
python manage.py makemigrations  

  
* Para realizar migrações, execute:

  
python manage.py makemigrations
