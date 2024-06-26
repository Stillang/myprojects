from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    follows = models.ManyToManyField('self', symmetrical=False, related_name='follower', blank=True)
    photo_url = models.URLField(default="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png")
    
    
    def __str__(self):
        return self.username

class Post(models.Model):
    content = models.TextField(max_length= 500)
    creation_date = models.DateField(default=timezone.now().date())
    creation_time = models.TimeField(default=timezone.now().time())
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return f"""
                {self.content}
                ... posted by {self.user}. 
                Posted on {self.creation_date},
                {self.creation_time.strftime('%H:%M:%S')}
                """
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")

    class Meta:
            unique_together = ['user', 'post']

    def __str__(self):
        return f"{self.user} liked {self.post}"