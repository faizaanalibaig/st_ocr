# st_ocr
STEPS TO FOLLOW TO DEPLOY TESSERACT OCR ON HEROKU
create your free account on Heroku
Once you are in your dashboard, click on new and create a new app (also name the app)
Download Heroku CLI and change the stack from 20 to 18
to change the stack open command prompt and login to Heroku CLI using the 'heroku login'command
type heroku app to see the list of all the apps created on heroku
to check for the available stack of the app 'heroku stack-a tesser-ocr'
Go back to Heroku dashboard... in the deployment method,click on Github and connect your github account
You can fork the tesser_ocr repository to create your own repo
Type the name of the repository in heroku and connect to it 
add this heroku buildpack in the settings menu https://github.com/heroku/heroku-buildpack-apt
also add the python builkpack in add buildpack option
set config vars to KEY :- TESDATA_PREFIX and VALUE:- ./apt/usr/share/tesseract-ocr/4.00/tessdata
Build and deploy the app and open app
