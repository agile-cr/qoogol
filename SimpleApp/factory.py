__author__ = 'tdd'

import domain

def report_service():
    return domain.ReportService()

def comment_service():
    return domain.CommentService

def comment_respository():
    return domain.CommentRespository