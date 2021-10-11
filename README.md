              #Django Employee-Management Version

/ Before using this template users can kindly notice the requirements.txt file present in -->
                            template/requirements.txt
 ************************************************************************************
/ Definition of Django:
   
   Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. 
   Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. 
   It's free and open source.
  
******************************************************************************************
 /  Python:
  The language used in this project was python.Python is a general-purpose coding language—which means that, unlike HTML, 
  CSS, and JavaScript, it can be used for other types of programming and software development besides web development. 
  That includes back end development, software development, data science and writing system scripts among other things.
  
******************************************************************************************************
 / Content of this template:
   This template represents the coding of employee-management .In this concept, there are two users admin & login. Where admin uses CRUD operation to manage labours and also assign tasks with the labour_id ,were labours can view their tasks from their login id.
***********************************************************************************************************
/ API'S:
  The api's of this project are /register,/login ,/forgot-password, /add-labour,/update-labour,/get-labour ,/delete-labour,/labour-list,/ assign-tasks. From the labour side /login ,/forgot-password, /task-view
  In the register api user can fill up the requirement fields.As they fill up ,the default db sql lite3 will stores the data.As the user can user their data for later 
  reuse
  And for the login api only  idf useer apply username and password they will login in to their respective account
  The forgot password will generate if user enters their mail id then randomly generated password will sent to their mail.
  And admin can add,update,delete,get & list out the list of labours were added
From labour ,they login and use forgot passwword also they could view their tasks assigned by admin
************************************************************************************
/ Comments:
 Inbetween the code  comments  were added to understand by the user especially for beginners.

***********************************************************************************
/Purpose of this Template:
 In this template, email was used as an username to make an authtoken model, while in the login api registered email can be used to get the data.Also only valid email addrress
 will be taken otherwise it will calls error. And implies how can admin can manage their employees with some basic entities.
*************************************************************************************************
/Commands:
 1. First create a virtual environment because later  when we reuse the project scripts and librarypackages may vary, then project cannot be executed. To avoid such consequences if we create
    virtual env then it will support the file even we use in different version after many years ago.
 2. Then create a path in terminal where your file has to be stored.
 3. Then run your environment ,if it was success the env name must be displayed at the front of the terminal path itself.
 4. To create the project name--> django-admin startproject projectname
 5. Then type--> cd projectname
 6. Then run the python --> python manage.py runserver
 7. If it was successful then we can see the localhost domain point number.If you click that then it will take you to the django successful installation page.
 8. To create the app -->django-admin startapp appname
 9. Whatever field you adding in your app should always migrate-->python manage.py makemigrations
 10.Then try -->python manage.py migrate
 11.In the setings.py of the project file at the installed apps should mention third party apps-->rest_framework,rest_framework.authtoken,appname
 12.Then create a urls.py file in the app then mention those urls in the project urls file.
