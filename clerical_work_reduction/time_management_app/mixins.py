import calendar
import datetime
from . import models
from django.views import generic
from collections import defaultdict

class BaseCalendarMixin:
    """カレンダー関連Mixinの基底クラス"""
    weekday = ['月', '火', '水', '木', '金', '土', '日']
    today = datetime.datetime.today()
    month_days = calendar.monthrange(today.year, today.month)[1]
    first_weekday = calendar.weekday(today.year, today.month, 1)


class MonthCalendarMixin(BaseCalendarMixin, generic.TemplateView):
    def get_timedelta(self, start_time, close_time):
        tdelta = datetime.datetime.combine(self.today, close_time) - datetime.datetime.combine(self.today, start_time)
        return tdelta
    
    def get_calendar_data(self, **kwargs):
        attendances = models.Attendance.objects.all() 
        calendar_data = defaultdict(dict)
        for d in range(self.month_days):
            calendar_data[d+1]['weekday'] = self.weekday[(d+self.first_weekday)%7]
        for a in attendances:
            calendar_data[a.date.day]['start_time'] = a.start_time
            calendar_data[a.date.day]['close_time'] = a.close_time
            calendar_data[a.date.day]['attend_time'] = self.get_timedelta(a.start_time, a.close_time)
            calendar_data[a.date.day]['work_time'] = self.get_timedelta(a.start_time, a.close_time) - self.get_timedelta(a.work_pattern.start_break_time, a.work_pattern.close_break_time) 
            calendar_data[a.date.day]['break_time'] = self.get_timedelta(a.work_pattern.start_break_time, a.work_pattern.close_break_time)
            calendar_data[a.date.day]['overtime_break_time'] = self.get_timedelta(a.work_pattern.start_break_time, a.work_pattern.close_break_time) 
            calendar_data[a.date.day]['today_todo'] = a.today_todo
            calendar_data[a.date.day]['today_issue'] = a.today_issue
            calendar_data[a.date.day]['work_pattern'] = a.work_pattern
        calendar = {'calendar_data': dict(calendar_data)} 
        return calendar