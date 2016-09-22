from django.db import models  
from django.contrib import admin                 
  
# Create your models here.  
class BlogPost(models.Model):  
    title = models.CharField('标题',max_length=150)
    body = models.TextField('内容')  
    timestamp = models.DateTimeField('发表时间',auto_now_add = True,editable = True)
    timeregis = models.DateTimeField('修改时间',auto_now = True,null = True)

    def __str__(self):
        return self.title

#admin.site.register(BlogPost) 
