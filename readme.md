this page can give us the instruction of the project:

1. first install the python and django
2. run the command py -m vnev .vnev for crate the envirnoment setup which can create the .venve project
3. the install uv in project for the fast devlopment by the command pip install --upgrade uv
4. set up envirnoment by the command {uv venv}
5. for activate the envinomnet rin this command .venv\Scripts\activate
6. install django via this command uv pip install Django
7. start make project by using the django-admin startproject firstProject
8. for start making app in python run this command python manage.py startapp appName
9. for start server go to the root folder and run pythom manage.py runserver

after starting app setup:
go at the main project or root project in this project example firstProject/firstProject
path('newApp_Name/', include('newApp_Name.urls')) for accessing the new app routes or urls
and add the 'newApp_Name', at the installed app section for tell the root the app was installed

for using static folder where we can store photo css file or javascript file
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

for load the templates from project
changes this in template section at the setting.py files
'DIRS': ['templates'],
and load {% load static%}
