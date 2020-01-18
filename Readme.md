# ResumeExtractor
> A Django web application to extract details from resume but for now it is limited to extracting skills.
>[pyresparser](https://github.com/OmkarPathak/pyresparser.git) is used to extract skills from pdf, doc or docx resumes.
# Installation
## Deploy to Local Machine
- Clone this repo to your local machine using `https://github.com/pawanpaudel93/ResumeExtractor`
- Create a virtual environment using virtualenv and activate it and install requirements from requirements.txt file.
   
   `$ virtualenv venv`

    `$ pip install -r requirements.txt`
    
- create `.env` file and view file `.env-example` for reference. For local environment LOCAL must be set to RUNNING_ENVIRON and for postgresql use as following else sqlite will be used.

  `RUNNING_ENVIRON=LOCAL`

  `DATABASE_NAME=postgresql`

- Then makemigrations and migrate you migrations.

  `$ python manage.py makemigrations`

  `$ python manage.py migrate`

- Then run your local environment server.

  `python manage.py runserver`

### Deploy to Heroku
- First, create a heroku app using command line or visiting heroku website and provision a database and configure environment variables.
- For serving media files (resume files) I have used [backblaze](https://www.backblaze.com) but you can also use AWS or others. 
Create an account at backblaze and create a bucket and also create App Keys from [App Keys](https://secure.backblaze.com/app_keys.htm) by clicking `Add a New Application Key` and after that configure heroku environment variables.
  
  `RUNNING_ENVIRON=PROD` for running settings for production
  
  `DATABASE_URL=` will be set automatically after provisioning app with database.

  `HB2_B2_ACCOUNT_ID=keyID` keyID from application key generated

  `HB2_B2_APP_KEY=applicationKey` applicationKey from key generated

  `HB2_B2_BUCKET_ID=Bucket ID` Bucket ID for created bucket

  `HB2_B2_BUCKET_NAME=Bucket name` Bucket name what you created

  > All value for the environment variables can be found as  the name specified. Please replace then with their respective values.
- After that run makemigrations and migrate for the migrations using heroku bash from the website or from command line.
## TODO
- Displaying important details from resume like education, email, phone, experience etc
- Adding more functionalities..