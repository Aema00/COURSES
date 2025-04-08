from .models import *
from modeltranslation.translator import TranslationOptions,register


@register(Courses)
class CoursesTranslationOptions(TranslationOptions):
    fields = ('courses_name', 'description')


@register(Lessons)
class LessonsTranslationOptions(TranslationOptions):
    fields = ('name_lessons', 'content')


@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('name_assignment', 'description')


@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('name_exam',)


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('name_questions',)


@register(Answers)
class AnswersTranslationOptions(TranslationOptions):
    fields = ('answers',)


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('comment',)