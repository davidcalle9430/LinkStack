from django.db import models

# Create your models here.
class Route(models.Model):
	name = models.CharField(max_length=100, primary_key=True)
	insertion_password = models.CharField(max_length=30, blank= True, null=True)
	deletion_password = models.CharField(max_length=30, blank = True, null=True)
	user_email= models.EmailField(max_length=80, null=True)

	def __unicode__(self):
		return self.name
	
	
	@staticmethod
	def create(p_name, p_insertion_password, p_deletion_password, p_user_email):
		route = Route()
		route.name= p_name
		route.insertion_password= p_insertion_password
		route.deletion_password= p_deletion_password
		route.user_email= p_user_email
		return route
