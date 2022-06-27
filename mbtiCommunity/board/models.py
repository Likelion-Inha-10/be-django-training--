from django.db import models

# Create your models here.
class board(models.Model):
    title = models.CharField(max_length=200, verbose_name='제목')
    author = models.CharField(max_length=100, verbose_name='글쓴이')
    content = models.TextField(verbose_name='내용')
    published_date = models.DateTimeField(auto_now=True, verbose_name='등록일')

    def __str__(self):
        return self.title