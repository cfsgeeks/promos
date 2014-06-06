from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core.fields import FileField

# Create your models here.

class Promo(models.Model):
    CONTENT_STATUS_DRAFT = 1
    CONTENT_STATUS_PUBLISHED = 2
    CONTENT_STATUS_CHOICES = (
                (CONTENT_STATUS_DRAFT,"Draft"),
                    (CONTENT_STATUS_PUBLISHED, "Published"),
                    )
    title = models.CharField(
            max_length=128,
            help_text="A title for the promo.  Helps you to remember what it is.",
            blank=False)
    status = models.IntegerField(choices=CONTENT_STATUS_CHOICES,default=CONTENT_STATUS_DRAFT)
    publish_on = models.DateField(blank=False)
    publish_until = models.DateField(blank=True,null=True)
    url = models.URLField(blank=True)
    page = models.ForeignKey(Page)
    image = FileField( max_length=100, upload_to='galleries', format='Image')

    def __unicode__(self):
        return self.title

    def save(self,*args,**kwargs):
        if self.page:
            self.url = 'http://www.krrcfs.ca' + self.page.get_absolute_url()
        super(Promo,self).save(*args,**kwargs)
