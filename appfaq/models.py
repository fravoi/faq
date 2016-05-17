from django.db import models

class Theme(models.Model):
    theme_text = models.CharField(max_length=200)
    pub_date_theme = models.DateTimeField('date published')
    def __str__(self):
        return self.theme_text

class Questionreponse(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    reponse_text= models.CharField(max_length=200)
    pub_date_questionreponse = models.DateTimeField('date published')
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.question_text+self.reponse_text
    
        