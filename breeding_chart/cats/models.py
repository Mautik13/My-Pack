from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Home(models.Model):
    Cat = "Cat"
    Tomcat = "Tomcat"
    Kitten = "Kitten"
    About_rase = "About rase"
    Parent = "Parents"


class Color(models.Model):
    class ColorCode(models.TextChoices):
        BLACK = "n", _("black - n")
        BLUE = "a", _("blue - a")
        RED = "d", _("red - d")
        CREAMY = "e", _("creamy - e")
        BLACK_TORTOISESHELL = "f", _("black tortoiseshell - f")
        BLUE_TORTOISESHELL = "g", _("blue tortoiseshell - g")
        SILVER_SMOKY = "s", _("silver/smoky - s")
        WHITE = "w", _("white - w")

    color_code = models.CharField(
        max_length=1,
        choices=ColorCode,
        default=ColorCode.BLACK
    )

    class DrawingCode(models.TextChoices):
        SHADED = "11", _("shaded - 11")
        SHELL = "12", _("shell - 12")
        UNSPECIFIED_DRAWING = '21', _("unspecified drawing - 21")
        MARBLED_DRAWING = '22', _("marble drawing (blotched - 22)")
        TIGER_DRAWING = '23', _("tiger drawing (mackerel - 23)")
        DOT_DRAWING = '24', _("dot drawing (spotted - 24)")
        TICKED_DRAWING = '25', _("ticked drawing (ticked - 25)")
        NONE = "None"

    drawing_code = models.CharField(
        max_length=4,
        choices=DrawingCode,
        default=DrawingCode.NONE,
    )

    class WhiteMottleCode(models.TextChoices):
        FROM = "01", _("from - 01")
        HARLEQUIN = "02", _("harlequin - 02")
        BICOLOR = "03", _("bicolor - 03")
        WITH_UNSPECIFIED_WHITE_SPOTS = "09", _("with unspecified white spots - 09")
        NONE = "None"

    white_mottle_code = models.CharField(
        max_length=4,
        choices=WhiteMottleCode,
        default=WhiteMottleCode.NONE,
    )

    class EyeColorCode(models.TextChoices):
        BLUE = "61", _("blue eyes - 61")
        ORANGE_AMBER = "62", _("orange/amber eyes - 62")
        ODD = "63", _("unevenly colored eyes (odd eyed) - 63")
        GREEN = "64", _("green eyes - 64")

    eye_color_code = models.CharField(
        max_length=2,
        choices=EyeColorCode,
        default=EyeColorCode.BLUE,
    )

    def __str__(self):
        return f"{self.color_code} {self.drawing_code} {self.white_mottle_code} {self.eye_color_code}"


"""
class Parent(models.Model):
    mothers_name = models.CharField(max_length=100)
    mothers_breeder = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    fathers_breeder = models.CharField(max_length=100)
"""


class Cat(models.Model):
    cats_name = models.CharField(max_length=255)
    breeder_name = models.CharField(max_length=255)
    color = models.OneToOneField(Color, on_delete=models.PROTECT, null=True)
    mothers_name = models.CharField(max_length=100, blank=True, null=True)
    fathers_name = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='cats_photos/', blank=True, null=True)

#    def __str__(self):
#       return f"{self.cats_name} {self.breeder_name}"

    def __str__(self):
        return self.cats_name


class Tomcat(models.Model):
    cats_name = models.CharField(max_length=255)
    breeder_name = models.CharField(max_length=255)
    color = models.OneToOneField(Color, on_delete=models.PROTECT, null=True)
    mothers_name = models.CharField(max_length=100, blank=True, null=True)
    fathers_name = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='cats_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.cats_name} {self.breeder_name}"


class Kitten(models.Model):
    cats_name = models.CharField(max_length=255)
    breeder_name = models.CharField(max_length=255)
    color = models.OneToOneField(Color, on_delete=models.PROTECT, null=True)
    mothers_name = models.CharField(max_length=100, blank=True, null=True)
    fathers_name = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.cats_name} {self.breeder_name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'