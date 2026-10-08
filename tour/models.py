from django.db import models

class UserRegister(models.Model):
    username=models.CharField(max_length=255)
    email=models.EmailField(null=True)
    mobile_no=models.IntegerField(null=True)
    password=models.CharField(max_length=10,default='',)
    status=models.IntegerField(null=True)
    
class CreatePackage(models.Model):
    package_name = models.CharField(max_length=100)
    package_type = models.CharField(max_length=50)
    package_location = models.CharField(max_length=100)
    package_price = models.DecimalField(max_digits=10, decimal_places=2)
    package_features = models.TextField()
    package_details = models.TextField()
    package_image = models.ImageField(upload_to='package_images/')

    def __str__(self):
        return self.package_name
    
class Enquiry(models.Model):
    username = models.CharField(max_length=100)
    email=models.EmailField(null=True)
    mobile_no=models.IntegerField(null=True)
    subject=models.CharField(max_length=100)
    description=models.TextField()
    
class TicketRaised(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(null=True)
    tour_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    details=models.TextField()
    
class Bookings(models.Model):
    username = models.ForeignKey(UserRegister, on_delete=models.CASCADE)
    email = models.EmailField()
    package_name=models.ForeignKey(CreatePackage, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.username}"
    