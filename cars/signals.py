from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum
from openai_api.client import get_car_ai_bio

def CarsInventoryUpdate():
    cars_count = Car.objects.all().count()
    #usa o ORM do django para fazer um sum no campo value da tabela Cars
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']

    CarInventory.objects.create(
        cars_count = cars_value,
        cars_value = cars_count
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):    
    if not instance.bio:
        #ai_bio = get_car_ai_bio(instance.model, instance.brand, instance.model_year)
        ai_bio = 'teste'
        instance.bio = ai_bio

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    CarsInventoryUpdate()
    
@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **kwargs):
    pass

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    CarsInventoryUpdate()


