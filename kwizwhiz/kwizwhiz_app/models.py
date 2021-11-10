from django.db import models
import re
import bcrypt

email_regex1 = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.edu+$')
email_regex2 = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.mil+$')


class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        user_emails = User.objects.filter(email = postData['email'])
        if len(postData['first_name']) == 0:
            errors['blank_first'] = 'First name cannot be blank'
        if len(postData['first_name']) < 2:
            errors['short_first'] = 'First name must be 2 letters or more'
        if len(postData['last_name']) == 0:
            errors['blank_last'] = 'Last name cannot be blank'
        if len(postData['last_name']) < 2:
            errors['short_last'] = 'Last name must be 2 letters or more'
        if len(postData['email']) == 0:
            errors['blank_email'] = 'Email cannot not be blank'
        if not email_regex1.match(postData['email']) or not email_regex2.match(postData['email']):
            errors['user_email'] = 'Not a valid email address'
        if user_emails:
            errors['email_exists'] = 'Email already in use'
        if len(postData['password']) == 0:
            errors['blank_password'] = 'Password is required'
        if len(postData['password']) < 8:
            errors['short_password'] = 'Password must be at least 8 characters'
        if postData['password'] != postData['pw_conf']:
            errors['confirm'] = 'Passwords do not match'
        return errors

    def log_validator(self, postData):
        errors = {}
        user_emails = User.objects.filter(email = postData['email'])
        if not email_regex.match(postData['email']):
            errors['email'] = 'Invalid email address'
        if not user_emails:
            errors['nonexistent'] = 'Email does not exist'
        if len(postData['password']) < 8:
            errors['short_pass'] = 'Password must be at least 8 characters'
        if bcrypt.checkpw(postData['password'].encode(), user_emails[0].password.encode()):
            print("password matches")
        else:
            errors['bad_pass'] = 'Email and password do not match'
        return errors

    def account_validator(self, postData):
        errors = {}
        user_emails = User.objects.filter(email = postData['email'])
        if len(postData['first_name']) == 0:
            errors['blank_first'] = "First name cannot be blank"
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be 2 letters or more"
        if len(postData['last_name']) == 0:
            errors['blank_last'] = 'Last name cannot be blank'
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be 2 letters or more"
        if len(postData['email']) == 0:
            errors['blank_email'] = "Email cannot be blank"
        if not email_regex.match(postData['email']):
            errors['email'] = "Invalid email address"
        if not user_emails:
            errors['mismatch'] = "Email does not exist"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = UserManager()

class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['selection']
        
    selection = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.selection

class Topic(models.Model):
    categories = models.ManyToManyField(Category, related_name='topics')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Quiz(models.Model):

    class Meta:
        verbose_name_plural = "Quizzes"
        ordering = ['id']

    topic = models.ForeignKey(Topic, related_name='quizzes', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100, default='New Quiz')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Question(models.Model):

    class Meta:
        ordering = ['quiz']

    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
# Create your models here.
