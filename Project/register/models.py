from django.db import models

# Create your models here.
class registration(models.Model):
    customer_id = models.AutoField(auto_created=True, primary_key=True)
    user_name = models.CharField(max_length=200)
    user_email = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_confirm_password= models.CharField(max_length=100)
    user_country = models.CharField(max_length=100)

    class Meta:
        db_table = "User_info"
