from django.contrib.auth.models import AbstractUser
from django.db import models


USER_ROLE = (
    ('client', 'client'),
    ('teacher', 'teacher'),
    ('administrator', 'administrator')
)


class UserProfile(AbstractUser):
    role = models.CharField(max_length=15, choices=USER_ROLE, default='client')
    full_name = models.CharField(max_length=34)
    profile_picture = models.ImageField(upload_to='profile_picture/')
    bio = models.TextField()

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Teacher(UserProfile):
    experience = models.PositiveSmallIntegerField(default=1)


class Student(UserProfile):
    pass


class Links(models.Model):
    objects = None
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='links_student')
    links_url = models.URLField()


class Category(models.Model):
    objects = None
    category_name = models.CharField(max_length=34)

    def __str__(self):
        return self.category_name


COURSES_LEVEL = (
    ('Beginner', 'Beginner'),
    ('Inter', 'Inter'),
    ('Adverse', 'Adverse')
)


class Courses(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    courses_name = models.CharField(max_length=34)
    description = models.TextField()
    level = models.CharField(max_length=15, choices=COURSES_LEVEL, default='beginner')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.courses_name


class Lessons(models.Model):
    objects = None
    name_lessons = models.CharField(max_length=32)
    video_url = models.URLField()
    content = models.TextField(null=True, blank=True)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='lessons_courses')

    def __str__(self):
        return self.name_lessons


class Assignment(models.Model):
    name_assignment = models.CharField(max_length=32)
    description = models.TextField()
    due_date = models.DateTimeField()
    courses = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='assignment_courses')
    students = models.ManyToManyField(UserProfile, related_name='students')

    def __str__(self):
        return self.name_assignment


class Exam(models.Model):
    name_exam = models.CharField(max_length=32)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    passing_score = models.PositiveSmallIntegerField()
    duration = models.TimeField()

    def __str__(self):
        return self.name_exam


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    name_questions = models.CharField(max_length=32)

    def __str__(self):
        return self.name_questions


class Answers(models.Model):
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    answers = models.CharField(max_length=64)
    true_answers = models.BooleanField(default=False)


class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_certificate')
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='courses_certificate')
    issued_at = models.DateField(auto_now_add=True)
    certificate_file = models.FileField(upload_to='certificate_file')


class Review(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()



