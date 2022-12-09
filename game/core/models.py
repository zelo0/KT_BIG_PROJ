# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Beautyproduct(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.ForeignKey('Brand', models.CASCADE)
    price = models.IntegerField(blank=True, null=True)
    effect = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)

    class Meta:
        db_table = 'beautyproduct'

    def __str__(self):
        return self.name


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'brand'

    def __str__(self):
        return self.name


class Coupon(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.ForeignKey(Brand, models.CASCADE)
    discount_rate = models.CharField(max_length=255)

    class Meta:
        db_table = 'coupon'
