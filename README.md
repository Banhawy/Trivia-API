# Full Stack API Final Project

## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a  webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out. 

This project is a webapp that allows users to view, add, and delete trivia questions. Users can also play trivia quizz games by answering random questions (which can be filtered to a specific category) and getting a score at the end of the quiz.

## About the Stack
### Backend
The `./backend` directory contains a completed Flask and SQLAlchemy server. API endpoints are defined in __init.py__ and reference models.py for DB and SQLAlchemy setup.   

### Frontend
The `./frontend` directory contains a complete React frontend that consumes the data from the Flask server. The views are stored in the `components/` folder.

## Getting Started

### Prerequisites

This project requires you to have the following prerequisites on your development environment:

1. Python >= 2.7
2. PIP
3. Nodejs >= 10.0
4. NPM
5. Postgresql >= 10

### Installation

#### **Setting Up DB**
Before starting the project, make sure you have a valid installation of Postgres and that it is running.
You can create databse using *psql* and the following commands in the `./backend/` folder:
```bash
createdb trivia
psql trivia < trivia.psql
```

#### **Setting Up Environment Variables**
To use environment variables, create a `config.py` file in the `./backend/` folder. All variables in this file are stored in a *key=value* format and are not tracked by version control

This project uses a production database and a test database aptly referred to as `prod_database_name` and `test_database_name` in environment variables.
Example `config.py`
```
prod_database_name = "trivia"
prod_database_path = "postgres://{}:{}@{}/{}".format('username', 'password','localhost:5432', prod_database_name)

```

#### Setting Up Backend
To install dependencies and start the bckend server, navigate to `./backend/`  and run the following commands:
```bash
pip install -r requirements.txt

export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

These commands put the application in development and directs our application to use the **__init__.py** file in our *flaskr* folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the Flask documentation.

The application backend server is run on http://127.0.0.1:5000/ by default and is a proxy in the frontend configuration.

### Setting Up Frontend
To install dependencies and start the frontend server, navigate to the `./frontend/` folder and run the following commands:
```
npm install
npm start
```
Open [http://localhost:3000](http://localhost:3000) to view the app in the browser.

## Tests
In order to run tests navigate to the backend folder and run the following commands:

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
The first time you run the tests, omit the dropdb command.

All tests are kept in that file and should be maintained as updates are made to app functionality.

## API Reference
Read the API documentation at the [`./backend/` README](./backend/README.md).
