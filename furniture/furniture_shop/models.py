from django.db import models

# Create your models here.
class reg(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone = models.IntegerField()
    Username = models.CharField(max_length=15)
    Password = models.IntegerField()
    Address = models.CharField(max_length=25, blank=True)
    Place = models.CharField(max_length=15, blank=True)
    District = models.CharField(max_length=15, blank=True)
    State = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.Username


class Product(models.Model):
    user = models.ForeignKey("reg", on_delete=models.CASCADE, null=True, blank=True)

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    CATEGORY_CHOICES = [
        ('storage', 'Storage Devices'),
        ('cables', 'Cables'),
        ('motherboard', 'Motherboards'),
        ('processor', 'Processors'),
        ('ram', 'RAM'),
        ('gpu', 'Graphics Cards'),
        ('peripheral', 'Peripherals'),
        ('others', 'Others'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    productName = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    # Optional fields
    storage_type = models.CharField(max_length=50, blank=True, null=True)
    capacity = models.CharField(max_length=50, blank=True, null=True)
    cable_type = models.CharField(max_length=50, blank=True, null=True)
    length = models.CharField(max_length=50, blank=True, null=True)
    cores = models.CharField(max_length=50, blank=True, null=True)
    clock_speed = models.CharField(max_length=50, blank=True, null=True)
    memory_size = models.CharField(max_length=50, blank=True, null=True)
    speed = models.CharField(max_length=50, blank=True, null=True)
    vram = models.CharField(max_length=50, blank=True, null=True)
    chipset = models.CharField(max_length=100, blank=True, null=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,default='pending' )

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.productName} ({self.category})"


class CartItem(models.Model):
    user = models.ForeignKey(reg, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.IntegerField()

class Order(models.Model):
    STATUS_CHOICES = [
        ('on the way', 'On the Way'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
        ('returned', 'Returned'),]
    user = models.ForeignKey(reg, on_delete=models.CASCADE)
    address = models.TextField()
    total_amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='on the way')
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()

class PasswordReset(models.Model):
    user=models.ForeignKey(reg,on_delete=models.CASCADE)
    #security
    token=models.CharField(max_length=4)