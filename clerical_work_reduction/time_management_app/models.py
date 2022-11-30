from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    address = models.CharField(max_length=50, blank=True, verbose_name='住所')

    def __str__(self):
        return self.username


class ContractCompanies(models.Model):
    name = models.CharField(max_length=50, verbose_name='会社名')
    address = models.CharField(max_length=50, blank=True, verbose_name='会社住所')
    zip_code = models.CharField(max_length=8, blank=True, verbose_name='郵便番号')
    president = models.CharField(max_length=20, blank=True, verbose_name='代表名')
    phone_number = models.CharField(
        max_length=12, blank=True, verbose_name='電話番号')
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name='ユーザー')

    class Meta:
        verbose_name = "契約会社"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "user"],
                name="company_unique"
            ),
        ]

    def __str__(self):
        return self.name


class SalesPeople(models.Model):
    first_name = models.CharField(max_length=10, verbose_name='名')
    last_name = models.CharField(max_length=10, verbose_name='氏')
    email = models.EmailField(max_length=200, blank=True, verbose_name='Eメール')
    mobile_phone_number = models.CharField(
        max_length=13, blank=True, verbose_name='携帯電話番号')
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name='ユーザー')
    company = models.ForeignKey(
        ContractCompanies, on_delete=models.PROTECT, verbose_name='契約会社')

    class Meta:
        verbose_name = "営業"
        constraints = [
            models.UniqueConstraint(
                fields=["first_name", "last_name", "user", "company"],
                name="salespeople_unique"
            ),
        ]

    def __str__(self):
        return self.first_name


class Projects(models.Model):
    project_name = models.CharField(max_length=100, verbose_name='プロジェクト名')
    start_date = models.DateField(max_length=2, verbose_name='契約開始日')
    last_date = models.DateField(max_length=2, verbose_name='契約終了日')
    upper_work_hours = models.IntegerField(verbose_name='稼働上限時間')
    lower_work_hours = models.IntegerField(verbose_name='稼働下限時間')
    assigned_job = models.CharField(
        max_length=50, blank=True, verbose_name='担当業務')
    summary = models.CharField(max_length=100, blank=True, verbose_name='概要')
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name='ユーザー')
    company = models.ForeignKey(
        ContractCompanies, on_delete=models.PROTECT, verbose_name='契約会社')

    class Meta:
        verbose_name = "プロジェクト"

    def __str__(self):
        return self.project_name


class WorkPattern(models.Model):
    start_time = models.TimeField(verbose_name='勤務開始時刻')
    close_time = models.TimeField(verbose_name='勤務終了時刻')
    start_break_time = models.TimeField(verbose_name='休憩開始時刻')
    close_break_time = models.TimeField(verbose_name='休憩終了時刻')
    start_overtime_break = models.TimeField(verbose_name='時間外休憩開始時刻')
    close_overtime_break = models.TimeField(verbose_name='時間外休憩終了時刻')
    round_down_unit = models.IntegerField(verbose_name='時間切捨単位')

    class Meta:
        verbose_name = "ワークパターン"

    def __str__(self):
        return str(self.start_time) + "-" + str(self.close_time) + " ("+str(self.round_down_unit)+"単位"+")"


class Attendance(models.Model):
    date = models.DateField(verbose_name='年月日')
    start_time = models.TimeField(verbose_name='勤務開始時刻')
    close_time = models.TimeField(verbose_name='勤務終了時刻')
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name='ユーザー')
    project = models.ForeignKey(
        Projects, on_delete=models.PROTECT, verbose_name='プロジェクト')
    work_pattern = models.ForeignKey(
        WorkPattern, on_delete=models.PROTECT, verbose_name='勤務パターン')

    class Meta:
        verbose_name = "勤怠"
        constraints = [
            models.UniqueConstraint(
                fields=["date", "user", "project"],
                name="attendance_unique"
            ),
        ]

    def __str__(self):
        return str(self.date) + "(" + self.user.first_name + ")"
