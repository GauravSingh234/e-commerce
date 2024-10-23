from django.db import models

LOCATION_CHOICES = [
    ('front', 'Front'),
    ('back', 'Back'),
    ('side', 'Side'),
    ('others', 'Others'),
]



class item_gallery(models.Model):
    # item_id=models.ForeignKey(Item, on_delete=models.CASCADE, related_name='Item')
    Location = models.CharField(max_length=6, choices=LOCATION_CHOICES, default='top',null=True )
    images = models.ImageField(upload_to='images/')


class Item(models.Model): 
    image = models.ImageField(upload_to='images/' , null=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    discounted_price = models.IntegerField()

    def __str__(self): 
        return self.name


