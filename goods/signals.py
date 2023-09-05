from django.dispatch import receiver
from django.db.models.signals import post_delete, post_init, post_save
from goods.models import GoodsImages
from utils.images import delete_image, image_processing


@receiver(post_init, sender=GoodsImages)
def user_post_init(instance, **kwargs):
    instance._current_image = instance.image


@receiver(post_save, sender=GoodsImages)
def user_post_save(instance, **kwargs):
    image_processing(instance.image, instance._current_image, 600, 800)


@receiver(post_delete, sender=GoodsImages)
def user_post_delete(instance, **kwargs):
    delete_image(instance._current_image)
