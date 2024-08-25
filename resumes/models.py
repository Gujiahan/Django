from django.db import models

# Create your models here.

class Archive(models.Model):
    LOCATION_CHOICES =[
        ('taipei', '台北'),
        ('taichung', '台中'),
        ('kaohsiung', '高雄'),
    ]
    
    name = models.CharField(max_length=32)
    price = models.PositiveIntegerField()
    profile = models.TextField()
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='taipei')


    class Meta:
        db_table = 'test_rseumes'
        managed = False
    

    def __str__(self):
        return f"{self.name} - {self.price}"