from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
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

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.publish.year,
                                                        self.publish.month,
                                                        self.publish.day,
                                                        self.slug])

posts=Post.objects.all()
p_posts = Post.published.all()




