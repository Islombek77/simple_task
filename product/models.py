from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=57)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    NEW = 'new'
    FINISH = 'finish'
    STATUS = ((NEW, NEW), (FINISH, FINISH))
    product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    status = models.CharField(choices=STATUS, default=NEW, max_length=10)

    def __str__(self):
        return "Order for => {}, count => {}".format(self.product, self.count)

