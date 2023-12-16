from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', default='images/me.png')
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    ## Quit and manually define a default value in models.py. for example: 
    ## comment = models.TextField(default='No comment')

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
