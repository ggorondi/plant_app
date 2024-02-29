from django.db import models
import numpy as np
import PIL
from pillow_heif import register_heif_opener
register_heif_opener() # Lets PIL open HEIC files
from .services import process_uploaded_image
from django.core.validators import validate_image_file_extension
# Create your models here.

class Image(models.Model):
    img = models.ImageField(upload_to='images')
    scientific_name = models.CharField(max_length=100, blank=True, validators=[validate_image_file_extension])
    # field for percentage of certainty of the model
    certainty = models.FloatField(blank=True, null=True)
    model_top_picks = models.JSONField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        pil_img = PIL.Image.open(self.img)
        if pil_img.mode == 'RGBA':
            pil_img = pil_img.convert('RGB')
        small_img = pil_img.resize((224, 224))
        img_array = np.array(small_img)

        top_plants = process_uploaded_image(img_array)
        
        # Get the scientific name of the first plant dict in the list
        self.scientific_name = top_plants[0][0]['scientific_name']
        #self.certainty = [f'{prob*100:.1f}%' for prob in top_3_probabilities]
        self.certainty = top_plants[0][1]
        
        
        #self.img.delete()
        super().save(*args, **kwargs)
        
        return top_plants