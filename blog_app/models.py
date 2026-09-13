from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOIS=(
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255, unique_for_date="publish")
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name="blog_posts")
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10, choices=STATUS_CHOIS, default='draft')

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

    objects=models.Manager()
    published=PublishManager

posts=Post.objects.all()
pposts=Post.published.all()




