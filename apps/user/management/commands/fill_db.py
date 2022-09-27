import random
import requests
import time

from django.contrib.auth.hashers import make_password
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db import transaction

from factory.django import DjangoModelFactory
from factory import Faker

from apps.user.models import User
from apps.post.models import Post, MediaContent
from apps.comment.models import Comment
from apps.chat.models import Message


FREEZE_TIME = 0

# medium settings
NUM_USERS = 10
NUM_POSTS = 40
MAX_PHOTOS_PER_POST = 5
MAX_LIKES_PER_POST = 8
MAX_COMMENTS_PER_POST = 5
MAX_LIKES_PER_COMMENT = 5
NUM_MESSAGES = 200
MAX_FOLLOWS = 6

FAKE_CONTENT = 'https://picsum.photos/1000'
FAKE_AVATAR = 'https://picsum.photos/200'


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    password = make_password('1')


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post
    text = Faker('paragraph', nb_sentences=5)


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment
    text = Faker('sentence', nb_words=7)


class MessageFactory(DjangoModelFactory):
    class Meta:
        model = Message
    text = Faker('paragraph', nb_sentences=3)


class MediaContentFactory(DjangoModelFactory):
    class Meta:
        model = MediaContent


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **kwargs):
        models = [User, Post, Comment, Message]
        for m in models:
            m.objects.all().delete()
        users = []
        posts = []

        # Users
        for i in range(NUM_USERS):
            user = UserFactory(email=f'{i+1}@sample.com')
            user.avatar.save(f'avatar_{i+1}.jpg', ContentFile(requests.get(FAKE_AVATAR).content))
            users.append(user)

        # Follows
        for user in users:
            follows_set = random.sample(users, random.randrange(2, MAX_FOLLOWS+2))
            if user in follows_set:
                follows_set.remove(user)
            user.follows.set(follows_set)

        # Posts +post_likes
        for i in range(NUM_POSTS):
            post = PostFactory(user=random.choice(users))
            post.likes.set(random.sample(users, random.randrange(MAX_LIKES_PER_POST)))
            posts.append(post)
            if FREEZE_TIME:
                time.sleep(FREEZE_TIME)

        # Content
        for post in posts:
            for i in range(1, random.randint(2, MAX_PHOTOS_PER_POST+1)):
                photo = MediaContentFactory(post=post)
                photo.content.save(
                    f'post{post.id}_fake_content_{i}.jpg',
                    ContentFile(requests.get(FAKE_CONTENT).content)
                )

        # Comments +comm_likes
        for post in posts:
            for i in range(1, random.randrange(MAX_COMMENTS_PER_POST)+2):
                comm = CommentFactory(post=post, user=random.choice(users))
                comm.likes.set(random.sample(users, random.randrange(MAX_LIKES_PER_COMMENT)))

        # Messages
        for i in range(NUM_MESSAGES):
            sender, recipient = random.sample(users, 2)
            MessageFactory(sender=sender, recipient=recipient)
            if FREEZE_TIME:
                time.sleep(FREEZE_TIME)
