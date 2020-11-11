# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## API Reference
### **Questions**

**GET /questions**
* General:
  * Returns a list of question objects, success value, total number of questions, a list of category names, and a dictionary of all available category id/name
  * Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.  
* Sample: `curl https://127.0.0.1:5000/questions`
    ```
    {
      "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
      },
      "current_category": [
        5,
        5,
        4,
        5,
        4,
        6,
        6,
        4,
        3,
        3
      ],
      "questions": [
        {
          "answer": "Apollo 13",
          "category": 5,
          "difficulty": 4,
          "id": 2,
          "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
          "answer": "Tom Cruise",
          "category": 5,
          "difficulty": 4,
          "id": 4,
          "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
          "answer": "Maya Angelou",
          "category": 4,
          "difficulty": 2,
          "id": 5,
          "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
          "answer": "Edward Scissorhands",
          "category": 5,
          "difficulty": 3,
          "id": 6,
          "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
          "answer": "Muhammad Ali",
          "category": 4,
          "difficulty": 1,
          "id": 9,
          "question": "What boxer's original name is Cassius Clay?"
        },
        {
          "answer": "Brazil",
          "category": 6,
          "difficulty": 3,
          "id": 10,
          "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
          "answer": "Uruguay",
          "category": 6,
          "difficulty": 4,
          "id": 11,
          "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
          "answer": "George Washington Carver",
          "category": 4,
          "difficulty": 2,
          "id": 12,
          "question": "Who invented Peanut Butter?"
        },
        {
          "answer": "Lake Victoria",
          "category": 3,
          "difficulty": 2,
          "id": 13,
          "question": "What is the largest lake in Africa?"
        },
        {
          "answer": "The Palace of Versailles",
          "category": 3,
          "difficulty": 3,
          "id": 14,
          "question": "In which royal palace would you find the Hall of Mirrors?"
        }
      ],
      "success": true,
      "total_questions": 44
    }
    ```
**POST /questions**
* General:
  * Creates a new question using the submitted question, answer, category, and difficulty
  * Returns success value and id of newly created question
* Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question": "What is Love?", "answer": "Baby Dont Hurt Me", "category": 3, "difficulty": 1}'`
    ```
    {
      "created": 20,
      "success": true
    }
    ```
**POST /questions/search**
* General:
  * Searches for a question that includes the submitted search term
  * Returns success value, all the questions that match the search term, the total number of matched questions, and the current categories of the matched questions
* Sample: `curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d '{"searchTerm":"love"}'`
    ```
    {
      "current_category": [
        5,
        2
      ],
      "questions": [
        {
          "answer": "Tom Cruise",
          "category": 5,
          "difficulty": 4,
          "id": 4,
          "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
          "answer": "Baby don't hurt me",
          "category": 2,
          "difficulty": 1,
          "id": 62,
          "question": "What is love?"
        }
      ],
      "success": true,
      "total_questions": 2
    }
    ```
**DELETE /questions/{question_id}**
* General:
  * Deletes the book of the given ID if it exists. Returns the id of the deleted book and success value.
  * Returns success value and id of newly created question
* Sample: `curl -X DELETE http://127.0.0.1:5000/questions/20`
    ```
    {
      "deleted": 20,
      "success": true
    }
    ```

### **Categories**

**GET /categories**
* General:
  * Returns a dictionary containing all category id/type.
  * Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.  
  * Sample: `curl https://127.0.0.1:5000/categories`
    ```
    {
      "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
      },
      "success": true
    }
    ```


**GET /categories/{category_id}**
* General:
  * Returns a success value, a list of current categories, a list of questions belonging to the given category, and their total count.
* Sample: `curl https://127.0.0.1:5000/categories/2`
    ```
    {
      "current_category": [
        2,
        2,
        2,
        2,
        2,
        2
      ],
      "questions": [
        {
          "answer": "Escher",
          "category": 2,
          "difficulty": 1,
          "id": 16,
          "question": "Which Dutch graphic artist?initials M C was a creator of optical illusions?"
        },
        {
          "answer": "Mona Lisa",
          "category": 2,
          "difficulty": 3,
          "id": 17,
          "question": "La Giaconda is better known as what?"
        },
        {
          "answer": "One",
          "category": 2,
          "difficulty": 4,
          "id": 18,
          "question": "How many paintings did Van Gogh sell in his lifetime?"
        },
        {
          "answer": "Jackson Pollock",
          "category": 2,
          "difficulty": 2,
          "id": 19,
          "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
        },
        {
          "answer": "Baby don't hurt me",
          "category": 2,
          "difficulty": 1,
          "id": 62,
          "question": "What is love?"
        },
        {
          "answer": "Abandoned places",
          "category": 2,
          "difficulty": 3,
          "id": 85,
          "question": "What are we looking for?"
        }
      ],
      "success": true,
      "total_questions": 6
    }
    ```

### **Quizzes**
**POST /quizzes**
* General:
  * Given a list of previous question ids and a quize category object, returns a success value, and a random question object.
* Sample: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions":[],"quiz_category":{"type":"Science","id":"1"}}'`
    ```
    {
      "question": {
        "answer": "The Liver",
        "category": 1,
        "difficulty": 4,
        "id": 20,
        "question": "What is the heaviest organ in the human body?"
      },
      "success": true
    }
    ```

## Error Handling
The API will return the following error types:

- 400: Bad Request
- 404: Not Fond
- 422: Not Processable

Errors are JSON formatted. For example:

```
{
    "success": False,
    "error": 404,
    "message": "resource not found"
}
```

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```