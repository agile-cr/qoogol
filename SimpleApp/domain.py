from django.db import models
__author__ = 'tdd'


class QuestionService(object):
    def get_questions(self):
        pass

    def create_question(self, statement):
        pass


class QuestionRespository(object):
    pass


class Question(models.Model):
    text = models.CharField(max_length=500)

    def __unicode__(self):
        return self.text

    def __repr__(self):
        return self.text
