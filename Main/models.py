from django.db import models


# Create your models here.
class Dog(models.Model):
	"""A dog available for adoption."""
	name = models.CharField(max_length=200)
	age_text = models.CharField(max_length=100, blank=True, help_text="Human-friendly age text, e.g. '1-2 years'")
	gender = models.CharField(max_length=50, blank=True)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='dogs/', blank=True, null=True)
	apply_url = models.URLField(blank=True, null=True)
	is_available = models.BooleanField(default=True)
	order = models.PositiveIntegerField(default=0, help_text="Ordering integer; lower shows first")

	class Meta:
		ordering = ['order', 'name']

	def __str__(self):
		return self.name
