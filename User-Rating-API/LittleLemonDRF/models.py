from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.name

class Rating(models.Model):
	menuitem_id = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
	rating = models.SmallIntegerField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self) -> str:
		return User.objects.get(id=self.user_id).username + " rated " + MenuItem.objects.get(id=self.menuitem_id_id).name + " " + str(self.rating) + " stars"