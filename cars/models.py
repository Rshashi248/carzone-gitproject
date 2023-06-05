from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


# Create your models here.

class Car(models.Model):
    state_choice = (
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CG', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JK', 'Jammu and Kashmir'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Orissa'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TR', 'Tripura'),
        ('UK', 'Uttarakhand'),
        ('UP', 'Uttar Pradesh'),
        ('WB', 'West Bengal'),
        ('CH', 'Chandigarh'),
        ('AN', 'Andaman and Nicobar Islands'),
        ('DH', 'Dadra and Nagar Haveli'),
        ('DD', 'Daman and Diu'),
        ('DL', 'Delhi'),
        ('LD', 'Lakshadweep'),
        ('PY', 'Pondicherry'),
    )
    
    year_choice = []
    for r in range(2015, (datetime.now().year+1)):
        year_choice.append((r,r))
        
    features_choices = (
       ('Cruise Control', 'Cruise Control'),
       ('Audio Interface', 'Audio Interface'),
       ('Airbags', 'Airbags'),
 )   
 
    Door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
   )   
        
    car_title = models.CharField(max_length=25)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description =RichTextField(max_length=1000)
    car_photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices,)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField( choices=Door_choices,max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_types = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date= models.DateTimeField(default=datetime.now,blank=True)
    





