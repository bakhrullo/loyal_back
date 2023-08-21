from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="O'zgargan sana")

    class Meta:
        abstract = True


class User(Base):
    name = models.CharField(max_length=200, verbose_name='Ism', blank=True, null=True)
    tg_id = models.PositiveBigIntegerField(unique=True, null=False, verbose_name='Telegram id')
    phone = models.CharField(max_length=20, unique=True, verbose_name='Raqam', null=True)
    point = models.PositiveIntegerField(default=0, verbose_name='Ball')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Foydalanuvchilar"
        verbose_name_plural = "Foydalanuvchilar"


class Product(Base):
    name = models.CharField(max_length=200, verbose_name='Nomi')
    descr = models.TextField(verbose_name='Ma\'lumot')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tovarlar"
        verbose_name_plural = "Tovarlar"


class Type(Base):
    name = models.CharField(max_length=100, verbose_name='Diametr')
    prod = models.ForeignKey(Product, related_name='type', verbose_name='Tovar', on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField(verbose_name='Narxi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Diametrlar"
        verbose_name_plural = "Diametrlar"


class Bonus(Base):
    code = models.CharField(max_length=100, verbose_name='Bonus kod', unique=True)
    point = models.PositiveIntegerField(verbose_name='Bal')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Bonuslar"
        verbose_name_plural = "Bonuslar"


class News(Base):
    name = models.CharField(max_length=100, verbose_name="Sarlavha")
    descr = models.TextField(verbose_name="Tavsifi")
    photo = models.ImageField(default="media/no-photo_5TKbPdH.png")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Yangilikalar"
        verbose_name_plural = "Yangilikalar"
