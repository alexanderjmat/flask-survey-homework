import re
from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
import surveys

app = Flask(__name__)
survey = surveys.satisfaction_survey

app.config['SECRET_KEY'] = "ballade4op52"

debug = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

responses = []
question_number = 0


@app.route("/")
def home_page():
    global responses
    responses = []
    title = survey.title
    instructions = survey.instructions
    return render_template('base.html', title = title, instructions = instructions)

@app.route("/answers", methods=["POST"])
def answer_page():
    global question_number
    form_data = request.form["survey_choice"]
    responses.append(form_data)
    if question_number >= len(survey.questions) - 1:
        question_number = 0
        return redirect('/thanks')
    else:
        question_number += 1
        return redirect(f"/questions/{question_number}")
    








@app.route("/questions/0")
def question_0():
    question = survey.questions[0]
    question_body = question.question
    next_question_number = "/questions/1"
    yes_answer = question.choices[0]
    no_answer = question.choices[1]
    text = question.question

    return render_template("question.html", question=question_body, yes = yes_answer, no = no_answer, text = text, next_q = next_question_number)


@app.route("/questions/1")
def question_1():
    global responses
    if not len(responses) == 1:
        flash("Must fill current field")
        return redirect(f"/questions/{len(responses)}")
        
    question = survey.questions[1]
    question_body = question.question
    next_question_number = "/questions/2"
    yes_answer = question.choices[0]
    no_answer = question.choices[1]
    text = question.question
    return render_template("question.html", question=question_body, yes = yes_answer, no = no_answer, text = text, next_q = next_question_number)


@app.route("/questions/2")
def question_2():
    if not len(responses) == 2:
        flash("Must fill current field")
        return redirect(f"/questions/{len(responses)}")
    question = survey.questions[2]
    question_body = question.question
    next_question_number = "/questions/3"
    yes_answer = question.choices[0]
    no_answer = question.choices[1]
    text = question.question
    return render_template("question.html", question=question_body, yes = yes_answer, no = no_answer, text = text, next_q = next_question_number)


@app.route("/questions/3")
def question_3():
    if not len(responses) == 3:
        flash("Must fill current field")
        return redirect(f"/questions/{len(responses)}")
    question = survey.questions[3]
    question_body = question.question
    next_question_number = "/"
    yes_answer = question.choices[0]
    no_answer = question.choices[1]
    text = question.question
    return render_template("question.html", question=question_body, yes = yes_answer, no = no_answer, text = text, next_q = next_question_number)


@app.route("/thanks")
def thanks_page():
    global responses
    print(responses)
    return render_template("thanks.html", )