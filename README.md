To run this app locally on Ubuntu 20.04 LTS without docker:

Update repositories on Ubuntu: sudo apt-get update

Clone GitHub repository: git clone https://github.com/jimmyread-99/T4A2-B.git

Install python virtual environment: sudo apt-get install python3.8-venv

Create virtual environment: python3.8 -m venv venv

Activate the virtual environment source venv/bin/activate

Install pip: python -m pip install --upgrade pip

Install modules from src/requirements.txt: pip install -r requirements.txt

Create a .env file and insert variables in the file:

DB_URI= FLASK_APP= FLASK_ENV= JWT_SECRET_KEY= SECRET_KEY=

Install and setup Postgres:

apt-get install postgresql-12

sudo -i -u postgres
createdb tennisclub
createuser coach

#Now connect to postgres and run the grant and alter commands

psql

grant all privileges on database tennisclub to coach;

alter user coach with encrypted password 'Testing1';

Add PostgreSQLdetails to .env file:

DB_URI=postgresql+psycopg2://(username):(password)@localhost:5432/(database)

flask db-custom drop (If there are any tables in the database previously)

flask db upgrade (to add the tables in the migrations directory)

flask db-custom seed - to create the time slots for each day and insert them into the Database
and creates the admin account

Username - test1@test.com
Password - 123456

flask run and access the app at localhost:5000

# Note all new accounts are not set to VALID - the admin has to set it to valid so they can do book anything in the system 


