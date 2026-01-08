1. Create a venv using : **uv venv**
2. Activate the environment :**.\\.venv\\Scripts\\activate\\**
3. Install Django using: **uv pip install Django**
4. Then Create a project using : *django-admin startproject ProjectName*
5. To run the project : *python manage.py runserver*
6. For Html file Create folder : **templates** at level 1 i.e projectName/templates
7. For Css/Javascript Create folfer : **static** at level 1
8. To tell the project to render the index.html go to *settings.py* then to TEMPLATES, 'DIRS' : [ ] here add *'templates'*
9. To load the css on web page in index.html file href="{% static 'style.css %}" and at the 1st line of the page add  
{% load static %} 
10. In *settings.py* create a new static directory to load the css file or the error will occur :  
**STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]**


## **To create an app**
*python manage.py startapp AppName*  
### Django only creates app the project is not aware of the apps, the first step is to make the whole project aware of the app

#### so make it aware in *settings.py* in **INSTALLED_APPS** add 'AppName'
