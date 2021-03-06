import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from  sqlalchemy.sql.expression import func
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
  page = request.args.get('page', 1, type=int)
  start = (page - 1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE

  questions = [question.format() for question in selection]
  current_questions = questions[start:end]

  return current_questions

def get_current_categories(current_questions=[]):
  categories_slection = Category.query.order_by(Category.id).all()
  categories = {}
  
  for category in categories_slection:
    categories[category.id] = category.type
  
  current_category = [question['category'] for question in current_questions]
  
  return (current_category, categories)

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @DONE: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  CORS(app)

  '''
  @DONE: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response
  '''
  @DONE: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories')
  def retrieve_categories():
    try:
      categories = get_current_categories()[1]
      
      return jsonify({
        'success': True,
        'categories': categories
      }) 
    except:
      abort(422)

  '''
  @DONE:
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions')
  def retrieve_quesions():
    selection = Question.query.order_by(Question.id).all()
    current_questions = paginate_questions(request, selection)
    current_category = get_current_categories(current_questions)[0]
    categories = get_current_categories(current_questions)[1]

    if len(current_questions) == 0:
      abort(404)
    
    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions': len(Question.query.all()),
      'current_category': current_category,
      'categories': categories
    })
  '''
  @DONE: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.filter(Question.id == question_id).one_or_none()

      if question is None:
        abort(404)

      question.delete()

      return jsonify({
        'success': True,
        'deleted': question_id
      })

    except:
      abort(422)

  '''
  @DONE: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/questions', methods=['POST'])
  def create_questions():
    body = request.get_json()

    new_question = body.get('question', None)
    new_answer = body.get('answer', None)
    new_category = body.get('category', None)
    new_difficulty = body.get('difficulty', None)

    try:
      question = Question(question=new_question, answer=new_answer, difficulty=new_difficulty, category=new_category)
      question.insert()
      
      return jsonify({
        'success': True,
        'created': question.id
      })

    except:
      abort(422)

  '''
  @DONE: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route('/questions/search', methods=['POST'])
  def search_questions():
    body = request.get_json()
    search_term = body.get('searchTerm', None)
    try:
      questions = Question.query.filter(Question.question.ilike('%' + search_term + '%'))
      current_questions = paginate_questions(request, questions)
      current_category = get_current_categories(current_questions)[0]
      
      return jsonify({
        'success': True,
        'questions': current_questions,
        'total_questions': len(current_questions),
        'current_category': current_category
      })
    except:
      abort(422)
  '''
  @DONE: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:category_id>')
  def get_category_questions(category_id):
    try:
      category_questions = Question.query.filter(Question.category == category_id).all()
      if len(category_questions) == 0:
        raise Exception('category not found')
      questions = [question.format() for question in category_questions]
      current_category = get_current_categories(questions)[0]

      return jsonify({
        "success": True,
        "questions": questions,
        "total_questions": len(questions),
        "current_category": current_category
      })
    
    except Exception as e:
      if (e.args[0] == 'category not found'):
        abort(404)
      else:
        abort(422)

  '''
  @DONE: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quizzes', methods=['POST'])
  def get_quiz():
    body = request.get_json()
    
    previous_questions = body.get('previous_questions', None) # list of question id's
    quiz_category = body.get('quiz_category', None) # a category object {type, id}
    try:
      if quiz_category['id'] is not 0:
        current_question = Question.query\
                                    .filter(~Question.id.in_(previous_questions), 
                                            Question.category == quiz_category['id'])\
                                    .order_by(func.random())\
                                    .first()
      else:
        current_question = Question.query\
                                    .filter(~Question.id.in_(previous_questions))\
                                    .order_by(func.random())\
                                    .first()

      # Condition for the case where we run out of questions in a category
      if current_question is not None:
        current_question = current_question.format()
      else:
        print('fuck')
        print(current_question)
        abort(422)

      return jsonify({
        'success': True,
        'question': current_question
      })

    except:
      abort(422)
  '''
  @DONE: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False,
      "error": 404,
      "message": "resource not found"
    }), 404

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False, 
      "error": 400,
      "message": "bad request"
      }), 400

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False, 
      "error": 422,
      "message": "unprocessable"
      }), 422
  
  return app

    