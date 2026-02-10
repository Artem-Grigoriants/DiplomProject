from celery import shared_task
from easy_thumbnails.files import get_thumbnailer

@shared_task
def generate_thumbnails(model_name, instance_pk, field_name):
    """
    A Celery task to generate thumbnails for a given model instance and field.
    """
    from django.apps import apps
    Model = apps.get_model(model_name)
    instance = Model.objects.get(pk=instance_pk)
    field = getattr(instance, field_name)

    if field:
        thumbnailer = get_thumbnailer(field)
        # This will generate all aliases defined in settings
        thumbnailer.generate_all()

