import calendar
import datetime

class BaseCalendarMixin:
    """カレンダー関連Mixinの基底クラス"""
    weekday = ['月', '火', '水', '木', '金', '土', '日']
    today = datetime.datetime.today()
    month_days = calendar.monthrange(today.year, today.month)[1]
    first_weekday = calendar.weekday(today.year, today.month, 1)


class MonthCalendarMixin(BaseCalendarMixin):
    def get_timedelta(self, start_time, close_time):
        tdelta = datetime.datetime.combine(self.today, close_time) - datetime.datetime.combine(self.today, start_time)
        return tdelta