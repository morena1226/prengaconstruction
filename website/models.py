from django.db import models


class Project(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	image = models.ImageField(upload_to='projects/')
	before_image = models.ImageField(upload_to='projects/before/', blank=True, null=True)
	after_image = models.ImageField(upload_to='projects/after/', blank=True, null=True)
	order = models.PositiveIntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['order', '-created_at']
		verbose_name = 'Punim'
		verbose_name_plural = 'Punime'

	def __str__(self):
		return self.title
