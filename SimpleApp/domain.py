from django.db import models
__author__ = 'tdd'


class QuestionaryService(object):
    def __init__(self):
        self.content = {}
        self.last_id = 1

    def add_questionaries(self, questionaries):
        for i, questionary in enumerate(questionaries):
            questionary.id = self.last_id + i
            self.content[questionary.id] = questionary

        self.last_id += len(questionaries)

    def get_questionaries(self):
        return self.content.values()

    def get_questionary(self, questionary_id):
        return self.content[questionary_id]


class QuestionService(object):
    def __init__(self):
        self.content = {}
        self.last_id = 1

    def get_questions(self):
        return self.content.values()

    def add_questions(self, questions):
        for i, question in enumerate(questions):
            question.id = self.last_id + i
            self.content[question.id] = question

        self.last_id += len(questions)

    def create_question(self, statement):
        self.content.add_questions([Question(statement)])

    def delete_question(self, question_id):
        del self.content[question_id]

    def modify_question(self, question_id, statement):
        self.content[question_id] = statement

    def delete_selected(self, question_ids):
        for qid in question_ids:
            self.delete_question(qid)


class QuestionRespository(object):
    pass


class Questionary(models.Model):
    subject = models.CharField(max_length=128)

    def __unicode__(self):
        return self.subject

    def __repr__(self):
        return self.subject


class Question(models.Model):
    text = models.CharField(max_length=500)
    questionary = models.ForeignKey(Questionary)

    def __unicode__(self):
        return self.text

    def __repr__(self):
        return self.text
