from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30, db_column='user_name')
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=50, null=True)
    gender = models.PositiveSmallIntegerField(default=0)
    avatar = models.CharField(max_length=50, null=True)
    follow_cnt = models.IntegerField(default=0)
    fan_cnt = models.IntegerField(default=0)
    friend_cnt = models.IntegerField(default=0)

class Follow(models.Model):
    user = models.ForeignKey(User)
    follow_user_id = models.IntegerField()
    follow_time = models.DateTimeField()

class Fan(models.Model):
    user = models.ForeignKey(User)
    fan_user_id = models.IntegerField()

class Friend(models.Model):
    user = models.ForeignKey(User)
    friend_user_id = models.IntegerField()

class Info(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=140)
    pic_name = models.CharField(max_length=50)

class Feed(models.Model):
    user = models.ForeignKey(User)
    info = models.ForeignKey(Info)
    feed_ts = models.BigIntegerField()
    feed_user_id = models.IntegerField()

class Comment(models.Model):
    user = models.ForeignKey(User)
    info = models.ForeignKey(Info)
    comment_note = models.CharField(max_length=140)
    comment_time = models.DateTimeField()

class News(models.Model):
    user = models.ForeignKey(User)
    news_time = models.DateTimeField()
    news_desc = models.CharField(max_length=400)
