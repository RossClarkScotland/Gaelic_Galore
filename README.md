# **Gaelic Galore**

<img width="665" alt="responsive" src="https://user-images.githubusercontent.com/66358670/173203385-fde6f16a-8c94-438e-95af-8f6ce5ad758f.png">

###### image created via [Am I responsive](https://ui.dev/amiresponsive?ref=producthunt)

_Gaelic Galore_ is my final project submitted for assessment in the Diploma in Software Engineering with Code Institute. It forms the minimum viable product for an e-commerce site for a fictional Gaelic-language school. The site enables education professionals to offer their courses to potential clients and allows the growing number of learners interested in Scottish Gaelic to find a means of learning a language for which courses are often limited by the relatively low number of speakers.

The full site is deployed via Heroku at: [gaelic-galore · Activity | Heroku](https://gaelic-galore.herokuapp.com/)

## **User Experience**

A full user experience design document, detailing the five planes of design for _Gaelic Galore,_ complete with user stories, [appears as a separate PDF here.](https://github.com/RossClarkScotland/Gaelic_Galore/blob/main/pdfs/UX.pdf)

## **Database Design**

A database design diagram for the project [appears as a separate PDF here.](https://github.com/RossClarkScotland/Gaelic_Galore/blob/main/pdfs/DbDesign.pdf)

## **Features: Existing features (For screenshots of features, see the separate UX PDF)**

### **All pages**

- The navigation bar allows users to easily navigate the pages of the site by giving a simple site overview.
- To provide a cleaner aesthetic, the navigation bar appears on smaller devices the homepage in the form of a hamburger-style dropdown menu.

- The decorative favicon uses the Saltire, the Scottish flag, to both indicate that the Gaelic in question is Scottish Gaelic, i.e. as opposed to Gaelige, and to fit in with the overall (blue) design accentuating Scottish cultural aspects.
- These features, as well as Django messages, are enabled by the base.html template content applying to all pages of the website, other than index.html which was coded separately to better apply and style its background images.

### **Index.html**

- The homepage navigation changes its design arrangement to make best use of the device on which it appears. Index.html contains vivid background images (from Pixabay) depicting scenes from the Hebrides, where Gaelic has traditionally been spoken. Via media queries, the background image changes from a landscape image (for medium and large devices) to a horizontal image (for small devices).
- As stated above in the section on information architecture, the items in the navigation bar vary on the homepage, depending on whether or not the user is logged in.

### **Add location page**

- The add location page provides a form to enable superusers to add a new location to the database, entering appropriate text and up to three images.

### **Add course page**

- The add course page provides a form to enable superusers to add a new course to the database, entering the location, title, level, a description, and up to two images.

### **Courses: listview pages**

- The course listview pages, accessed vie the navbar _Courses_ element, filter the courses in the database to show Bootstrap cards with initial details for: all courses, advanced courses, intermediate courses, or beginners courses based on the user&#39;s choice.

### **Courses: detailview pages**

- The course detail view pages provide information on specific courses and allow users to add courses to their shopping carts. Users may also increase and decrease the amount of participants as they wish.
- Superusers may access the edit / delete course form from this page.
- Upon a user adding an item to their cart, a success toast appears which allows users to navigate directly to the checkout page.

### **Courses: Edit**

- The edit course page provides a form for superusers to change the content of course detail pages.

### **Cart**

- The shopping cart page allows users to increase, decrease or delete the number of items in their shopping cart
- If the user&#39;s cart is empty, a message tells them so and provides a button taking them back to the &#39;all courses&#39; list view

### **Locations: listview page**

- The course listview pages, accessed vie the navbar _Courses_ element, filter the courses in the database to show Bootstrap cards with initial details of all courses, advanced courses, intermediate courses or beginners courses based on the user&#39;s choice.

### **Contact page**

- This is a static html site which provides a contact email address for users.

### **Login page**

- The login page, powered by a Django allauth form, allows users to securely log in.
- A &#39;Forgot your password&#39; link takes users to a password reset page

### **Password reset page**

- This page provides a form to initiate the allauth reset password process

### **Logout page**

- The logout section of the navbar takes users to a page which asks them whether they are sure they want to log out and provides a button to allow them to do so. Logging out takes the user back to the homepage.

### **Checkout page**

- The checkout page provides a list of items in the user&#39;s cart, a Stripe-powered form for payment, and buttons to allow the user to either complete the purchase or go back to their shopping cart.
- A notification below the payment form also alerts users to how much they will be charged for their purchase.

### **Checkout success page**

- The checkout success page gives the reader a breakdown of their purchase and order number, and informs them of the automatic email they will receive to confirm the order. However, if the order is unsuccessful, a message appears at the bottom of the checkout page informing the user.

### **Profile page**

- The user profile page provides a form for users to change their billing address and a list of previous purchases.

### **Search results page**

- The search results page shows courses which contain the word that the user searched for, whether the words appear in either the course title or details

## **Features left to implement**

I initially began a version of the milestone 4 project in the Spring/Summer of 2021, but had to go on medical leave for around 10 months due to chronic pain issues. As such, I came back to the project having to start from scratch with limited time remaining, and a limited time that I could spend in front of the computer without experiencing pain. For that reason, there were a few sacrifices I had to make due to time constraints.

- More custom CSS. Due to the time constraints, I took Bootstrap at its purpose and used it as much as possible.
- Adding social media login functionality to the site.
- Adding other means of payment, e.g. PayPal.

Additionally, I had, despite the time constraints, planned a couple of features that I later had to sacrifice due to time lost trying to fix problems that occurred while coding.

- Automated testing: At this stage, the app has only been tested manually.
- A contact form: For the time being, a static page directs users to a contact email address.
- A timer graphic to show users that their order is being processed. For the time being, text on the Checkout page tells users that their purchase may take some moments to process.

## **Technologies used**

- GitHub: [https://github.com/](https://github.com/)
  - GitHub was used to host the application&#39;s repositories.
- GitPod: [https://www.gitpod.io/](https://www.gitpod.io/)
  - GitPod served as the integrated development environment used to code the site.
- Python: [Welcome to Python.org](https://www.python.org/)
  - Python was used to code the app&#39;s models, views, urls, etc.
- HTML: [https://developer.mozilla.org/en-US/docs/Web/HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
  - The website uses HTML to input the structure and content.
- CSS: [https://developer.mozilla.org/en-US/docs/Web/CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
  - The website uses CSS to style the HTML elements.
- Bootstrap: [Bootstrap · The most popular HTML, CSS, and JS library in the world. (getbootstrap.com)](https://getbootstrap.com/)
  - The website uses the Bootstrap framework to simplify the integration and styling of responsive elements.
- Django: [The web framework for perfectionists with deadlines | Django (djangoproject.com)](https://www.djangoproject.com/)
  - Django was used as the framework within the site was coded.
- Django allauth: [Installation — django-allauth 0.43.0 documentation](https://django-allauth.readthedocs.io/en/latest/installation.html)
  - This was used for customer authentication.
- Stripe: [Stripe® Official | Payment Processing Platform for the Internet](https://stripe.com/en-gb-de)
  - Stripe was used to handle secure credit card payments and to send purchase confirmation emails.
- Amazon Web Services: [https://aws.amazon.com/](https://aws.amazon.com/)
  - Cloud support to help manage static and database content.
- jQuery: [https://code.jquery.com/](https://code.jquery.com/)
  - The site uses jQuery to handle Stripe payments, allow users to manage their shopping carts, and to provide users with informative toasts.
- Google Fonts: [https://fonts.google.com/](https://fonts.google.com/)
  - The site uses Google Fonts to integrate the Lato font into the website.
- Fontawesome: [https://fontawesome.com/](https://fontawesome.com/)
  - The site uses Font Awesome to integrate icons site.
- Autoprefixer CSS online: [https://autoprefixer.github.io/](https://autoprefixer.github.io/)
  - Autoprefixer was used to automatically add vendor prefixes to style.css in order to aid cross-browser compatability.
- Favicon.io
  - favicon.io was used to add a favicon to the site. [https://favicon.io/emoji-favicons/flag-scotland/](https://favicon.io/emoji-favicons/flag-scotland/)
- word2md.com: [https://word2md.com/](https://word2md.com/)
  - To ensure correct markdown in the first draft of this Read Me file a Microsoft Word document of the text was run through word2md.com. The resulting markdown and text was then edited according to the preferences of the author using rules set out in the _Mastering Markdown_ document at GitHub.com. [https://guides.github.com/features/mastering-markdown/](https://guides.github.com/features/mastering-markdown/)

## **Testing**

- I manually tested the site for errors by having the Mozilla, Microsoft Edge, and Google Chrome Developer Tools console open while performing every user event possible on the site, both on the local and deployed versions.
- To ensure that the site contains valid HTML, the HTML code was checked by direct input using the W3C Markup Validation Service: [https://validator.w3.org/](https://validator.w3.org/)
- To check valid CSS, direct input via the W3C CSS Validation Service was used: [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)
- To test the validity of the jQuery / Javascript JS Hint was used: [https://jshint.com/](https://jshint.com/)
- To ensure that Python and Django templating code remained error-free, the Debug console was set to &#39;True&#39; throughout the entirety of the development process. Pylint was also used to ensure pep8 compliance as far as possible without breaking the code.
- To check that the website complies well with accessibility standards I used Siteimprove: [Website Accessibility Checker - Free Instant Accessibility Check (siteimprove.com)](https://www.siteimprove.com/toolkit/accessibility-checker/?utm_campaign=ww_fy21_ppc_dsa&amp;utm_medium=ppc&amp;utm_source=google&amp;utm_content=dsa&amp;gclid=CjwKCAjwtIaVBhBkEiwAsr7-cyjEJFpTsp-V1qjKOzTVgejNJyHGnAZGQFAvHKJTlfAajdUiQCXZ0xoC8GsQAvD_BwE)
- To ensure the site&#39;s functionality across various devices, I used the web developer tools inspection feature of each of the following browsers:
  - Google Chrome
  - Mozilla Firefox
  - Microsoft Edge
  - For each browser, I manually checked the preview of each of the site&#39;s pages and events, in both vertical and horizontal views, for devices ranging from the iPhone 5/SE at the smallest end to a width of 3840px / 4k at the highest. I also checked all the user events with the console of each browser&#39;s developer tools to ensure there were no errors.

In addition to checking the application&#39;s functionality using browser developer tools, the site has been manually checked and found to function as desired on the following devices:

### **Laptops:**

- Lenovo Yoga 530 (checked by both myself and my wife, Anita)
- HP 255 G5 Notebook (checked by both myself and my wife, Anita)
- Macbook Air (checked by my father, George)
- Lenovo Thinkpad x390 (checked by myself)

### **Tablets:**

- Kindle Fire 3 HD (checked by both myself and my wife, Anita)
- iPad mini 3 (checked by my father, George)

### **Smartphones:**

- Samsung Galaxy J4+ (checked by myself)
- Samsung A50 (checked by my wife, Anita)
- iPhone XR (checked by my brother, Greg)
- iPhone SE (checked by my friend, Kirill)

## **Bugs**
Occasionally, a Stripe-related error appears in the console when navigating through the site. Neither I nor Code Institite tutors have been able to reproduce it by performing any one particular action and I have therefore been advised by both Code Institute tutors and my project mentor that this is an issue on the Stripe end rather than an error in my code. 

At the time of writing, I have run out of time without being able to fix the bug in the method shown in the _Boutique Ado_ walkthrough project, i.e. that the minus button on the shopping cart button enables users to select quantities of less than zero.

Additionally, the cart allows users to continue to add a product to the cart once it has already sold out. On the advice of my tutor, I have focused on addressing other issues in the time remaining. As such, in a real-life scenario, website owners would need to keep an eye on purchases and remove a course from the site once it was sold out.

## **Requirements: Content**

To meet the needs required above, the website requires mixed multimedia content including: text, a search function, call-to-action buttons, photographs, forms, and site-wide navigation buttons,

## **Deployment**

To create this project, I used the Code Institute template: [https://github.com/Code-Institute-Org/gitpod-full-template](https://github.com/Code-Institute-Org/gitpod-full-template)

### **To create a project with this template:**

- Create GitHub and GitPod accounts.
- Navigate to [https://github.com/Code-Institute-Org/gitpod-full-template](https://github.com/Code-Institute-Org/gitpod-full-template)

- Click the &#39;use this template&#39; button.
- Give your repository a name and, optionally, a description.
- Click the _Create repository from template_ button to open a GitPod workspace.
- While working on the project, be sure to open it from your existing project workspace, i.e. do not open a new workspace.
- To open a port and run the local version of the site on the server, type _python manage.py runserver_ into the command line in the terminal and choose _open server_ from port 8000.
- To commit changes to the local project, type the following commands into the command line from the terminal:
  - git add.
  - git commit – m &quot;commit message&quot;
  - git push
- To create a superuser for the project, type _python manage.py createsuperuser_ into the command line in the terminal, then enter your chosen login credentials when prompted.
- To migrate changes to models to the Django database, type the following commands into the command line from the terminal:
  - python manage.py makemigrations
  - python manage.py migrate

### **Requirements:**

  - asgiref==3.5.1
  - boto3==1.23.8
  - botocore==1.26.8
  - dj-database-url==0.5.0
  - Django==3.2.13
  - django-allauth==0.41.0
  - django-countries==7.2.1
  - django-crispy-forms==1.14.0
  - django-storages==1.12.3
  - gunicorn==20.1.0
  - jmespath==1.0.0
  - oauthlib==3.2.0
  - Pillow==9.1.0
  - psycopg2-binary==2.9.3
  - python3-openid==3.2.0
  - pytz==2022.1
  - requests-oauthlib==1.3.1
  - s3transfer==0.5.2
  - sqlparse==0.4.2
  - stripe==3.0.0

### **Cloning the project:**

- To clone the project, follow the steps providedby GitHub here: [Cloning a repository - GitHub Docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
- The following environment variables must be added to the project&#39;s env.py file:

import os

os.environ[&quot;SECRET\_KEY&quot;] = &#39;Your secret key&#39;

os.environ[&quot;STRIPE\_PUBLIC\_KEY&quot;] = &#39;Stripe public key&#39;

os.environ[&quot;STRIPE\_SECRET\_KEY&quot;] = &#39;Stripe secret key&#39;

os.environ[&quot;STRIPE\_WH\_SECRET&quot;] = &#39;Stripe webhook secret&#39;

os.environ[&quot;EMAIL\_HOST\_USER&quot;] = &#39;Your email&#39;

os.environ[&quot;EMAIL\_HOST\_PASS&quot;] = &#39;Your email host password&#39;

os.environ[&quot;DEVELOPMENT&quot;] = &#39;1&#39;

os.environ[&quot;DATABASE\_URL&quot;] = &#39;Your database URL&#39;

USE\_AWS = [&quot;True&quot;]

os.environ[&quot;AWS\_ACCESS\_KEY\_ID&quot;] = &#39;Your AWS access key ID&#39;

os.environ[&quot;AWS\_SECRET\_ACCESS\_KEY&quot;] = &#39;Your AWS secret access key&#39;

- Information on how to get Stripe environment variables can be found in the Stripe documentation: [Stripe Documentation](https://stripe.com/docs)
- Information on how to get Amazon Web Services environment variables can be found in the AWS S3 documentation: [Amazon Simple Storage Service Documentation](https://docs.aws.amazon.com/s3/?id=docs_gateway)
- To get the Database URL from your Heroku app,
  - Log in to Heroku and navigate to your app.
  - Select the _Overview_ menu.
  - Click on the Heroku postgres addon.
  - Navigate to _Settings \&gt; View Credentials_
  - Find the URI and copy the whole thing in at the database url environment variable.

### **Heroku deployment**

To deploy the project on Heroku:

- Create a Heroku account.
- Create a new app.
- Name the app, choose the region closest to you, and click _Create app_.
- Navigate to the _Resources_ tab, type _posgres_ into the add ons search bar and choose _Heroku Postgres_.
- Provision the _Hobby Dev - Free Plan_ when prompted.
- If not already installed, install dj-database-url and psycopg2 by returning to GitPod and typing the following commands into the command line in the terminal:
  - pip3 install dj\_database\_url
  - pip3 install psycopg2-binary
  - pip3 freeze \&gt; requirements.txt
- _import dj\_database\_url_ to the project settings.py on GitPod.
- Comment out the default _DATABASES_ setting in _settings.py_ and replace it with:

DATABASES = {

&#39;default&#39;: dj\_database\_url.parse(&#39;Your database URL&#39;)

}

- You can get your database URL from the _Config Vars_ under the _Settings_ tab of your Heroku app.
- Set up the Heroku postgres database by typing _python3 manage.py migrate_ into the command line of the terminal.
- Create a superuser with _python3 manage.py createsuperuser_.
- Be sure to click the _verified_ and _primary_ boxes for the superuser in the Heroku Django admin page.
- Uncomment out the original _DATABASES_ setting in _settings.py_ and remove your Heroku / dj\_database one so that you don&#39;t push it to GitHub.
- Commit changes via the terminal.
- Set the if . . . else . . . statement below _in settings.py_. This will ensure that you connect to the postgres database when the app runs on Heroku and to sqlite otherwise.

```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
       'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```


- Type _pip3 install gunicorn_ into the command line, then freeze requirements.
- Create a Procfile and and the following to it:
  - web: gunicorn gaelic\_galore.wsgi:application
- To ensure that Heroku does not collect static files upon deployment, type the following into the command line:
  - heroku config:set DISABLE\_COLLECTSTATIC=1 –app name-of-your-heroku-app
- add the host name of the Heroku app to _ALLOWED\_HOSTS = []_ in _settings.py_.
- Additionally, add _localhost_ to _ALLOWED\_HOSTS = []_ to ensure that GitPod still works.
- Add, commit, and push changes in the command line.
- Initialize Heroku git remote in the command line with _heroku git:remote a- your-app-name_
- Type _git push heroku master_ into the command line.
- To set the heroku app to automatically deploy when you deploy to github, _Heroku app \&gt; Deploy \&gt; Deployment method \&gt; GitHub \&gt; search for your repository in the search bar \&gt; click connect \&gt; enable automatic deploys_
- Generate a Django _SECRET\_KEY_ and add it to the Heroku _config vars_ in _Settings._
- Replace the _SECRET\_KEY_ setting in _settings.py_ with a call to get it from the environment.
- SECRET\_KEY = os.environ.get(&#39;SECRET\_KEY&#39;, &#39;&#39;)
- Change the _DEBUG_ setting to:
- DEBUG = &#39;DEVELOPMENT&#39;in os.environ
- Commit and push the changes to initiate a Heroku build.
- N.B. At the time of coding this project, automatic deploys were not available, so I needed to migrate database changes and push other changes with the following commands:
  - To commit changes to the deployed project on Heroku type the following commands into the command line from the terminal:
    - heroku login –i
    - When prompted, enter your email and password.
    - git push heroku main
  - To migrate changes to models to the deployed Heroku Django, database type the following command into the command line from the terminal:
    - heroku run python3 manage.py migrate -a YOUR PROJECT NAME
- By the time I finished the project, however, automatic deploys were once again available.
- The full list of Config Vars in the Heroku settings should be as follows:
  - AWS\_ACCESS\_KEY\_ID
  - AWS\_SECRET\_ACCESS\_KEY
  - DATABASE\_URL
  - EMAIL\_HOST\_PASS
  - EMAIL\_HOST\_USER
  - SECRET\_KEY
  - STRIPE\_PUBLIC\_KEY
  - STRIPE\_SECRET\_KEY
  - STRIPE\_WH\_SECRET
  - USE\_AWS = True
- As stated above, information on how to find Stripe and AWS keys can be found in the Stripe and AWS documentation.

### **Amazon Web Services S3 Deployment**

- To store static files and images on AWS S3, follow the instructions in the AWS S3 User Guide here: [What is Amazon S3? - Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

### **Setting up automatic emails**

- Log into a gmail account and go to _settings._
- Click _Accounts and Import_ \&gt; _Other Google account settings \&gt; Security_
- Turn on two-step verification.
- Click _Get started_, enter your password, and go through your chosen verification method
- Click _Security \&gt; App passwords_
- Select _Mail_ as the app and _Other_ then type _Django_ under _Device_
- Click _Generate_ and copy the password you are given
- Paste this password in _Heroku \&gt; Settings \&gt; Config Vars_ as _EMAIL\_HOST\_PASS_
- Add another Config Var, _EMAIL\_HOST\_USER_, and set it as your gmail address.
- Ensure that the following is in your _Settings.py_:

```
if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'rossclarkscotland@gmail.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
```

- Add, commit, and push changes to GitHub/Heroku.

## **Credits**

### **Media:**

- All site images come from Pixabay

### **Code:**

- The project is largely based on the methods and code taught in the Boutique Ado walkthrough project in the as part of Code Institute&#39;s _Fullstack Frameworks_ module.
- I learned the static and template file structure, as well as how to build listviews and detailviews, from _Django for Professionals_ by William S. Vincent.

## **Acknowledgements:**

- I would like to thank my wife, Anita, for always being willing to lend a spare pair of eyes and, at times, keeping up an elaborate pretence that I was not in fact exhausting every swear word I know in several languages when my code wasn&#39;t working.
- I also owe a debt to my father, George, for agreeing to test and give feedback on site functionality, particularly as regards the various iterations of the game.
- I would also like to thank my friend Milana for being awesome at all things design and never being unwilling to say when some aspect of my design is less than awesome.
- A huge shout out must go to Rebecca of the Code Institute tutoring staff, who was there with great advice and fantastic explanations to help me out of the most difficult spots during this project.
- Thank you to everyone on the Code Institute Slack page for being willing to lend an eye and a word of advice when required.
- Particular Slack honorifics must go to mentor Eventyret, tutor Ed B_alum, and my fellow students Abi Westcott and Ken Wee Chin for helping out when they were already done with their own projects and deserving of spending their time on something far better than fielding my last-minute, panicky questions.
- Finally, I would like to express my gratitude to my course mentor, Spencer Barribal, for offering encouragement and useful ideas, and to the Code Institute tutors and Slack community for providing advice and for humouring me when I asked stupid questions.