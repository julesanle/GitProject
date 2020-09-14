import time,datetime,locale


class GetDate:

    now = datetime.datetime.now()
    next_date = now + datetime.timedelta(days=+1)

    def start_date(self):
        # 取当天后一天
        locale.setlocale(locale.LC_CTYPE, 'chinese')
        start_date = self.next_date.strftime("%Y/%m/%d")
        return start_date

    def start_time(self):
        set_time = time.strptime('00:00:00', "%H:%M:%S")
        start_time = time.strftime("%H:%M", set_time)
        return start_time

    def set_datetime(self):
        return self.next_date + datetime.timedelta(hours=+72)

    def end_date(self):
        end_data = self.set_datetime().strftime('%Y/%m/%d')
        return end_data

    def end_time(self):
        end_time = self.set_datetime().strftime('%H:%M')
        return end_time

    def start_datetime(self):  #2020-10-06 00:00
        time_str = self.start_date()+self.start_time()
        return time_str

    def end_datetime(self):
        self.set_datetime()
