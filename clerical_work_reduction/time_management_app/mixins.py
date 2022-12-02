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
        close = datetime.datetime.combine(self.today, close_time)
        start = datetime.datetime.combine(self.today, start_time)
        time_diff = close - start
        return time_diff
    
    def get_hh_mm(self, time_diff):
        mm, ss = divmod(time_diff.seconds, 60)
        hh, mm = divmod(mm, 60)
        str = "%02d:%02d:%02d" % (hh, mm, ss)
        return str
    
    def get_timedelta_str(self, start_time, close_time):
        time_diff = self.get_timedelta(start_time, close_time)
        timedelta_str = self.get_hh_mm(time_diff)
        return timedelta_str
    
    def get_work_time(self):
        # attend_time = self.get_timedelta(start, close) 
        # break_time = self.get_timedelta(break_start, break_close)
        # overtime_break = self.get_timedelta(overtime_break_start, overtime_break_close)
        pass

    def get_calendar_data(self, **kwargs):
        attendances = models.Attendance.objects.all() 
        calendar_data = defaultdict(dict)
        for d in range(self.month_days):
            calendar_data[d+1]['weekday'] = self.weekday[(d+self.first_weekday)%7]
        for a in attendances:
            day = a.date.day
            start = a.start_time 
            close = a.close_time
            break_start = a.work_pattern.start_break_time
            break_close = a.work_pattern.close_break_time
            overtime_break_start = a.work_pattern.start_overtime_break
            overtime_break_close = a.work_pattern.close_overtime_break


            start_str = start.strftime('%H:%M:%S')
            close_str = close.strftime('%H:%M:%S')
            attend_time_str = self.get_timedelta_str(start, close)
            break_time_str = self.get_timedelta_str(break_start, break_close) 
            overtime_break_str = self.get_timedelta_str(overtime_break_start, overtime_break_close)

            calendar_data[day]['start_time'] = start_str
            calendar_data[day]['close_time'] = close_str
            calendar_data[day]['attend_time'] = attend_time_str
            calendar_data[day]['work_time'] = '' 
            calendar_data[day]['break_time'] = break_time_str 
            calendar_data[day]['overtime_break_time'] = overtime_break_str 
            calendar_data[day]['today_todo'] = a.today_todo
            calendar_data[day]['today_issue'] = a.today_issue
            calendar_data[day]['work_pattern'] = a.work_pattern
        
        calendar = {'calendar_data': dict(calendar_data)} 
        return calendar