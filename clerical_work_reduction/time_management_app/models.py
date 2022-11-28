from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    address = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=200,blank=True)


class ContractCompanies(models.Model):
    name = models.CharField(max_length=50,blank=True)
    address = models.CharField(max_length=50,blank=True)
    zip_code = models.CharField(max_length=8,blank=True)
    president = models.CharField(max_length=20,blank=True)
    phone_number = models.CharField(max_length=12,blank=True)


class SalesPeople(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=200,blank=True)
    mobile_phone_number = models.CharField(max_length=12,blank=True)
    user_id = models.IntegerField()
    company_id = models.IntegerField()


class Projects(models.Model):
    project_name = models.CharField(max_length=100)
    start_month = models.CharField(max_length=2)
    last_month = models.CharField(max_length=2)
    upper_work_hours = models.IntegerField()
    lower_work_hours = models.IntegerField()
    assigned_job = models.CharField(max_length=50,blank=True)
    summary = models.CharField(max_length=100,blank=True)
    user_id = models.IntegerField()
    company_id = models.IntegerField()


class Attendance(models.Model):
    date = models.DateTimeField()
    start_time = models.TimeField()
    close_time = models.TimeField()
    user_id = models.IntegerField()
    project_id = models.IntegerField()
    work_pattern_id = models.IntegerField()


class WorkPattern(models.Model):
    start_time = models.TimeField()
    close_time = models.TimeField()
    start_break_time = models.TimeField()
    close_break_time = models.TimeField()
    start_overtime_break = models.TimeField()
    close_overtime_break = models.TimeField()
    round_down_unit = models.IntegerField()

