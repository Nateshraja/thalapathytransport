from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    number = models.CharField(max_length=20, unique=True)  # e.g., TN38BP7329
    driver_name = models.CharField(max_length=100)
    driver_contact = models.CharField(max_length=15, blank=True)
    vehicle_type = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.number} - {self.driver_name}"


class Trip(models.Model):
    date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=100)
    drop_location = models.CharField(max_length=100)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True,default=1)
    loading = models.BooleanField(default=False)  # Whether loading is required
    quantity = models.FloatField(default=0.0)  # Quantity of goods in tons or units
    loading_charge = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    unloading_charge = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    auto_rent = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    remarks = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.total = (self.loading_charge or 0) + (self.unloading_charge or 0) + (self.auto_rent or 0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.company.name} - {self.date}"

class MyCompany(models.Model):
    name = models.CharField(max_length=100, default="Thalapathi Transport")
    address = models.TextField(default="12, SNR Road, Coimbatore - 641012")
    phone = models.CharField(max_length=15, default="+91-9876543210")
    email = models.EmailField(default="thalapathi@example.com")
    upi_id = models.CharField(max_length=50, default="thalapathi@upi")

    logo = models.ImageField(upload_to='company/logo/', blank=True, null=True)
    qr_code = models.ImageField(upload_to='company/qr/', blank=True, null=True)

    def __str__(self):
        return self.name