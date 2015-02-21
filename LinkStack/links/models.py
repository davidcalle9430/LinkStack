from django.db import models
from routes.models import Route

# Create your models here.
class Link(models.Model):
	link = models.CharField(max_length=500)
	description = models.TextField(max_length=500, blank=True, null=True)
	route = models.ForeignKey(Route,null=True)

	@staticmethod
	def create(p_link,p_description,p_route):
		new_link = Link()
		new_link.link = p_link
		new_link.description = p_description
		new_link.route= p_route
		return new_link

	def __unicode__(self):
		return self.link