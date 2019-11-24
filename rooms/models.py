from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

# import 순서 1.파이썬 2.장고,외부 패키지 3.내가 만든 패키지


class AbstractItem(core_models.TimeStampModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """ RoomType Model Definition """

    class Meta:
        verbose_name = "RoomType"

    pass


class Amenity(AbstractItem):

    """ Amenity Model Definition """

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facility Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """HouseRule Model Definition """

    pass


class Photo(core_models.TimeStampModel):

    """ photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.str(room)


class Room(core_models.TimeStampModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField(help_text="최대 몇명이 머물 수 있나요?")
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenity = models.ManyToManyField("Amenity", blank=True)
    facility = models.ManyToManyField("Facility", blank=True)
    houseRule = models.ManyToManyField("HouseRule", blank=True)

    def __str__(self):
        return self.name
