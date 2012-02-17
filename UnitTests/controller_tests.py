
from UnitTests.lib import ControllerTestCase
from hamcrest import *
from pyDoubles.framework import *
from SimpleApp.domain import QuestionService, Question

__author__ = 'tdd'
import sys


class Controller_UnitTests(ControllerTestCase):
    controller_modules = ['controllers', 'factory']

    def setUp(self):
        super(Controller_UnitTests,self).setUp()

    def get_questions_page(self, questions):
        self.factory.question_service = spy(QuestionService())
        when(self.factory.question_service.get_questions).then_return(questions)

        return self.client.get("/question/list/")

    def test_empty_question_list(self):
        response = self.get_questions_page([])

        assert_that(response.content,
                    contains_string("NO_QUESTIONS"))

    def test_one_question_list(self):
        response = self.get_questions_page([Question(text="are you alive?")])

        assert_that(response.content,
                    contains_string("are you alive"))

    def test_create_question(self):
        # given
        self.question_service = spy(QuestionService())
        self.factory.question_service = method_returning(self.question_service)

        # when
        response = self.client.get("/question/create/",
            {"statement":"are you alive?"})

        # then
        assert_that(response.content, contains_string("Question Created"))
        assert_that_method(self.question_service.create_question).was_called()

    def test_create_question_empty_statement(self):
        # given
        self.question_service = spy(QuestionService())
        self.factory.question_service = method_returning(self.question_service)

        # when
        response = self.client.get("/question/create/",
            {"statement":""})

        # then
        assert_that(response.content,
                    contains_string("INVALID STATEMENT"))
