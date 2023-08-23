from django.contrib.gis.geos import Point
from django.db import models
from django.contrib.gis.db import models
# Create your models here.

class place(models.Model):
    # categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=50, default='placexx')
    description = models.CharField(max_length=250, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # modified_at = models.DateTimeField(auto_now=True)
    # image = models.ImageField(upload_to='place_images/', blank=True, null=True)
    active = models.BooleanField(default=True)
    point_geom = models.PointField(default=Point(0, 0), blank=True)

    class Meta:
        verbose_name_plural = 'Places'

    def __str__(self):
        return self.place_name

