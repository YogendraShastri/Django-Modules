from django.db import models

# Create your models here.

class AlbumPost(models.Model):
    p_id = models.AutoField(primary_key=True)
    print(p_id)
    album_title = models.CharField(max_length=50)
    album_subtitle = models.CharField(max_length=200, default="")
    album_image = models.FileField(upload_to='./images/',max_length=300,null=True,default="")
    album_area = models.CharField(max_length=500, default="")
    
    def __str__(self):
        return self.album_title
