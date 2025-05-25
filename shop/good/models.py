from django.db import models

class Type (models.Model):
    t_name = models.CharField(max_length=25)

    def __str__(self):
        return self.t_name

class Good(models.Model):
    g_name = models.CharField(max_length=25)
    price = models.IntegerField()
    g_type = models.ForeignKey(Type, default=None, on_delete=models.CASCADE)









