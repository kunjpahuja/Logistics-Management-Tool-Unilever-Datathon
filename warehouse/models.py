from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Plant(models.Model):
    plantCode = models.CharField(max_length = 10)
    coutryCode = models.CharField(max_length = 5)
    companyCode = models.IntegerField()
    conversion = models.FloatField()

    def __str__(self):
        return self.coutryCode + ' - ' + self.plantCode

class Cost(models.Model):
    cost_element = models.IntegerField()
    name = models.CharField(max_length = 1000)
    type = models.CharField(max_length = 1000)

    def __str__(self):
        return str(self.cost_element) + ' - ' + self.name

class Operation(models.Model):
    cost_center = models.IntegerField()
    operation_type = models.CharField(max_length = 100)
    category = models.IntegerField()

    def __str__(self):
        return  self.operation_type + '- Category ' + str(self.category)


class Consolidated_Data(models.Model):
    # location = models.CharField(max_length = 3)
    # plant = models.CharField(max_length = 5)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    cost_Type = models.ForeignKey(Cost, on_delete=models.CASCADE)
    operation_Type = models.ForeignKey(Operation, on_delete=models.CASCADE)
    period = models.IntegerField(default=1, validators=[MaxValueValidator(12), MinValueValidator(1)])
    value = models.FloatField()
    actual = models.BooleanField(default=False)
    # variance = models.IntegerField(default=0)

    def __str__(self):
        return  self.plant.plantCode + ' - ' + self.cost_Type.name +" : "+str(self.value)
