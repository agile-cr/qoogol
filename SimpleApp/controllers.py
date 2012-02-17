# Create your views here.

import simplejson
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login

import factory


def get_questions(request):
    questions = factory.question_service.get_questions()
    if not questions:
        return HttpResponse("NO_QUESTIONS")

    return render_to_response("question_list.html",
                              {"questions": questions})


def create_question(request):
    if "statement" not in request.GET:
        return HttpResponse("Error to create question")

    statement = request.GET['statement']

    if not statement:
        return HttpResponse("INVALID STATEMENT")

    factory.question_service().create_question(statement)
    return HttpResponse("Question Created")
