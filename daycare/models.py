from django.db import models

class Parent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    next_of_kin_name = models.CharField(max_length=100)
    next_of_kin_email = models.EmailField()
    next_of_kin_phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    year_of_birth = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class CheckIn(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date = models.DateField()
    check_in_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.child.first_name} {self.child.last_name} - {self.date}"

