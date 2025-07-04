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
10. for install pip run the command: python -m ensurepip --upgrade
    or use this command: pythom -m pip install --upgrade(recommended)

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

for make a layout page means the making of statics follw the structure(layout page inside template)
{
{% load static %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{% block tiltle%} default value {% endblock %}</title>
    <link rel="stylesheet" href="{%static 'index.css'%}" />
  </head>
  <body>
    <nav>this is our navbar</nav>
    {% block content%}{% endblock %}
  </body>
</html>
}
this is our layout.html file and     {% block content%}{% endblock %}
this line can access the conent and navbar is premanment in all page. then setup this rewrite the index.html file by this
{

}
// set up tailwind in django
install python using command: pip install pytailwindcss
after this run thsi command for start tailwind: tailwindcss init

another way to setup envirnoment

1. Run this command for set up envirnoment: python -m venv .venv
2. for active the envirnoment: .venv\Scripts\activate
3. for install django : pip install django
4. run this command for check installition django: python -m django --version
5. run this for start tailwind project: python .\manage.py tailwind init
   it can make theme app by default otherwise you can give any specific name
6. then update installed app by add theme
7. update setting.py in firstproject can upat eby this
   {
   TAILWIND_APP_NAME = 'theme'
   INTERNAL_IPS = ['127.0.0.1']
   }
8. again install tailwind app by this command: python manage.py tailwind install
