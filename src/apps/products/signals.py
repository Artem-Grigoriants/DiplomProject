from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product
from apps.core.tasks import generate_thumbnails

@receiver(post_save, sender=Product)
def product_post_save(sender, instance, created, **kwargs):
    if instance.image:
        generate_thumbnails.delay('products.Product', instance.pk, 'image')

