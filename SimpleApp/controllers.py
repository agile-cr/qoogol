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

    return render_to_response(
        "question_list.html",
        {"questions": questions, "questions_len": len(questions)})


def get_questionaries(request):
    questionaries = factory.questionary_service.get_questionaries()
    if not questionaries:
        return HttpResponse("NO_QUESTIONARIES")

    return render_to_response(
        "questionary_list.html",
        {"questionaries": questionaries, "questionaries_len": len(questionaries)})


def create_question(request):
    if "statement" not in request.GET:
        return HttpResponse("Error to create question")

    statement = request.GET['statement']

    if not statement:
        return HttpResponse("INVALID STATEMENT")

    factory.question_service().create_question(statement)
    return HttpResponse("Question Created")


def delete_question(request, question_id):
    factory.question_service.delete_question(int(question_id))
    return get_questions(request)


def modify_question(request, question_id):
    statement = request.GET['statement']

    factory.question_service.modify_question(int(question_id), statement)

    return get_questions(request)


def delete_selected(request, question_ids):
    factory.question_service.delete_selected([int(x) for x in question_ids.split(',')])
    return get_questions(request)


def get_questionary(request, questionary_id):
    questionary = factory.questionary_service.get_questionary(int(questionary_id))

    return render_to_response(
        "questionary.html",
        {"subject": questionary.subject,
         "questions_len": len(questionary.question_set.all())})
