# R1 Description of your website, including:


Having an actual small tennis club outside my back door with a small but enthusiastic crowd, they have a rudimentary booking system and rely on facebook to communicate between the members as well as post news and updates. The purpose of this site is to speed up the booking system and allow more users to see what is coming up and easily book lessons and casual playing. 


#### Purpose


The purpose is to make it easier for the members to easily see availability of the courts, and easily book them in advanced. They are able to book up a number of sessions per week depending on their membership level.


#### Functionality / features


Users will be able to sign in or reset their password - users are created upon payment or updating their membership and emailed to their nominated account. User will be able to see a calendar view of the availability at a high level and select days to further define availability. Users will be able to book a time and court of their choosing over a 7-day week roster. Users will be able to view their account and status as well as their playing history in each category - casual tennis, lessons attended.


#### Target audience


The local tennis club operates on a call to book service, being such a smaller club, all bookings are to be made via phone and then noted down. To speed up this process as not all calls are immediately answered or returned in an acceptable time limit.  The target audience will be the members to book when they need without needing to call to book each time and to track the courts usage.  Users will be able to also book a lesson with the resident pro coach through the application and see availability slots. 



#### Running the application locally


To run this app locally on Ubuntu 20.04 LTS without docker:

- Update repositories on Ubuntu: sudo apt-get update

- Clone GitHub repository: git clone https://github.com/jimmyread-99/T4A2-B

-Install python virtual environment: sudo apt-get install python3.8-venv

- Create virtual environment: python3.8 -m venv venv

- Activate the virtual environment source venv/bin/activate

- Install pip: python -m pip install --upgrade pip

- Install modules from src/requirements.txt: pip install -r requirements.txt

- Install Postgres and setup database and user and grant access:

1. apt-get install postgresql-12
2. sudo -i -u postgres
3. createdb tennisclub
4. createuser coach



#### Now connect to postgres and run the grant and alter commands



1. psql
2. grant all privileges on database tennisclub to coach;
3. alter user coach with encrypted password 'Testing1';



- Create a .env file in the src/ directory and insert variables in the file:

>> DB_URI= FLASK_APP= FLASK_ENV= JWT_SECRET_KEY= DB_URI=postgresql+psycopg2://(username):(password)@localhost:5432/(database)
>> DB_URI=postgresql+psycopg2://coach:Testing1@localhost:5432/tennisclub


- for e.g. FLASK_APP=src/main.py, FLASK_ENV=development The app will NOT work if these variables are not set.

- flask db-custom drop (If there are any tables in the database previously)

- flask db upgrade (to add the tables in the migrations directory)

- flask db-custom seed (this will seed the databse with time slots and create an admin user u-test1@test.com and p-123456)

- flask run and access the app at localhost:5000

- ###### Note all new accounts are set to not valid when signing up - the admin needs to set them to True for the users to be able to make bookings



## Tech stack



##### Back End

- Python

- Gunicorn

- Nginx

- Amazon EC2

- Amazon Load Balancer 

- AMAZON RDS / PostgreSQL 

- NAT/ROUTE 53



##### Front End

- Jinga/bootstrap/Bulma/Javascript

- HTML/CSS



##### DevOps

- Github - CI/CD pipeline



# R2 Dataflow Diagram



![Dataflow Diagram](docs/dataflowdiagram.jpg)



- A user will have their account created by the admin upon payment of membership

- User can login to their account or reset their password - this is done through the web/tablet/mobile front end login page that connects to the user database

- Once a user is logged in a JWT token is created for their session that includes their details

- Once in the system, the user is able to view their account and its status from the User Database

- When the user selects the Calender View, the bookings are populated from the Bookings database that includes - casual, lessons bookings

- When a user requests a particular day the booking database then gets more detailed information about the bookings for the day

- User is able to make a casual booking in the day view, edit or delete them - the LOGIN user authentication session will make sure correct access is maintained

- Users are able to view the lessons that are stored in the Bookings database and are able to Create/Cancel or attend lessons

- Upon log out the authentication token is destroyed



# R3 Application Architecture Diagram



![Application Architecture Diagram](docs/appdiag.jpg)



#### Back End

- Python REST FlaskAPI will be deployed on amaxons EC2 instances - these instances will also have gunicorn and nginx running on them to handle the http requests called to it

- Amazon Services will be deployed to create a Virtual Private Network to host the instance, these instances will be load balanced connection with the network address transalator as this will point to a website address

- Amazon RDS Postgres database will be used to store the bookings and information that the site will need to dispaly. lessons will be added by the admin. Admin will also be able to login and book in private sessions

- CI/CD pipeline for updating and deployment

- Admin user will have programmatic IAM access to be able to managage the amazon services

- Freenom to get a site, and hosted via Route 53 in amazon

- NGINX will issue SSL certificate via Certbot



#### Front End

- Jinga/Bootstrap/Bulma and Javascipt - A basic web front end is used to create the interaction for the users and the database, general funationality in view the calendar, days, lessons and account. Easy to use.

- User Authentication - allowing the user to login and verify with the database and create a session token. Admin creates users upon membership payment - users can only login or reset password once created.



# R4 User Stories

![User Story 1](docs/1_user_story.jpg) 



# R5 Wireframes for multiple standard screen sizes, created using industry standard software



### Main Page

![Wireframe 1](docs/1_mainpage.jpg)



### Want To Play

![Wireframe 2](docs/2_wanttoplay.jpg)



### Memberships

![Wireframe 3](docs/3_memberships.jpg)



### Contact

![Wireframe 4](docs/4_contact.jpg)



### Login and Reset

![Wireframe 5](docs/5a_pclogin_reset.jpg)

![Wireframe 5a](docs/5b_tabletmobilelogin_reset.jpg)



### Account Page

![Wireframe 6](docs/6_loginaccount.jpg)



### Calendar View

![Wireframe 7](docs/7_calandermonthview.jpg)



### Day View

![Wireframe 8](docs/8_calanderdayview.jpg)



### Lesson Page

![Wireframe 9](docs/9_lessons.jpg)



### View Challenges Page

![Wireframe 10](docs/10a_challengeacceptview.jpg)



### Create Challenges Page

![Wireframe 11](docs/10b_challengeacreate.jpg)



# R6 Screenshots of your Trello board throughout the duration of the project



### February 9th

![Trello Board 1](docs/trello1_feb9_2021.jpg)



### February 11th

![Trello Board 2](docs/trello2_feb11_2021.jpg)



### February 14th

![Trello Board 3](docs/trello3_feb16_2021.jpg)



### February 19th

![Trello Board 4](docs/trello4_feb19_2021.jpg)



### February 21th

![Trello Board 5](docs/trello5_feb21_2021.jpg)



### March 4thth

![Trello Board 5](docs/trello6_2021.jpg)



### March 5th

![Trello Board 5](docs/trello7_2021.jpg)



### March 10th

![Trello Board 5](docs/trello8_2021.jpg)



### March 11th

![Trello Board 5](docs/trello9_2021.jpg)



### March 12th

![Trello Board 5](docs/trello10_2021.jpg)



