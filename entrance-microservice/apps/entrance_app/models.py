from django.db import models

# Create your models here.
class Request(models.Model):
    log_id = models.OneToOneField('Log', on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    key = models.CharField(max_length=255)
    is_used = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

class Log(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    entrance_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True)

class LogDateHistory(models.Model):
    entrance_time_range = models.DateTimeField(auto_now_add=True)
    exit_time_range = models.DateTimeField(null=True)

class LogHistory(models.Model):
    logs_date_history_id = models.ForeignKey(LogDateHistory, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    entrance_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True)