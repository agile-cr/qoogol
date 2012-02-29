# -*- mode:python; coding:utf-8; tab-width:4 -*-

import sys, os
prj_root = os.path.dirname(os.path.dirname(__file__))
sys.path.append(prj_root)

from .lib import ControllerTestCase
from hamcrest import *
from pyDoubles.framework import *
from SimpleApp.domain import QuestionService, Question

__author__ = 'tdd'


class Controller_UnitTests(ControllerTestCase):
    controller_modules = ['controllers', 'factory']

    def setUp(self):
        super(Controller_UnitTests, self).setUp()
        self.factory.question_service = QuestionService()

    def add_questions(self, questions):
        self.factory.question_service.add_questions(questions)

    def test_empty_question_list(self):
        self.add_questions([])

        response = self.client.get("/question/list/")

        assert_that(response.content,
                    contains_string("NO_QUESTIONS"))

    def test_one_question_list(self):
        self.add_questions([Question(text="are you alive?")])

        response = self.client.get("/question/list/")

        assert_that(response.content,
                    contains_string("are you alive"))

    def test_create_question(self):
        # given
        self.question_service = spy(QuestionService())
        self.factory.question_service = method_returning(self.question_service)

        # when
        response = self.client.get("/question/create/",
            {"statement": "are you alive?"})

        # then
        assert_that(response.content, contains_string("Question Created"))
        assert_that_method(self.question_service.create_question).was_called()

    def test_create_question_empty_statement(self):
        # given
        self.question_service = spy(QuestionService())
        self.factory.question_service = method_returning(self.question_service)

        # when
        response = self.client.get("/question/create/",
            {"statement": ""})

        # then
        assert_that(response.content,
                    contains_string("INVALID STATEMENT"))

    def test_delete_last_question(self):
        question = Question(text="are you alive?")
        self.add_questions([question])

        response = self.client.get("/question/delete/%s" % question.id)

        assert_that(response.content,
                    contains_string("NO_QUESTIONS"))

    def test_delete_one_question(self):
        # given
        question_alive = Question(text="are you alive?")
        question_dead = Question(text="are you dead?")

        self.add_questions([question_alive, question_dead])

        # when
        response = self.client.get("/question/delete/%s" % question_alive.id)

        # then
        assert_that(response.content,
                    not contains_string("are you alive?"))
        assert_that(response.content,
                    contains_string("are you dead?"))

    def test_modify_question(self):
        question = Question(text="are you alive?")
        self.add_questions([question])

        response = self.client.get("/question/modify/%s" % question.id,
                                   {"statement": "are you dead?"})

        assert_that(response.content,
                    contains_string("are you dead"))
        assert_that(response.content,
                    not contains_string("alive"))

    def test_delete_selected_questions(self):
        #given
        questions = [
            Question(text="are you alive?"),
            Question(text="are you dead?"),
            Question(text="are you sleeping?")]

        self.add_questions(questions)

        # when
        question_ids = str.join(",", [str(q.id) for q in questions[::2]])
        response = self.client.get("/question/delete_selected/%s" % question_ids)

        # then
        assert_that(response.content,
                    contains_string("are you dead?"))
        assert_that(response.content,
                    contains_string("QUESTIONS_LEN:1"))
