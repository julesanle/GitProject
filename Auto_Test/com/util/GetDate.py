import time,datetime,locale


class GetDate:

    def start_time(self):
        # set_time = time.strptime('00:00:00', "%H:%M:%S")
        # start_time = time.strftime("%H:%M:%S", set_time)
        now = datetime.datetime.now()
        time_str = now + datetime.timedelta(minutes=2)  # seconds
        return time_str.strftime("%H:%M:%S")

    def set_datetime(self):
        stime = self.start_datetime()
        dtime = datetime.datetime.strptime(stime, "%Y-%m-%d %H:%M:%S")
        return dtime + datetime.timedelta(days=+7.5)

    def end_date(self):
        end_data = self.set_datetime().strftime('%Y/%m/%d')
        return end_data

    def end_time(self):
        end_time = self.set_datetime().strftime('%H:%M:%S')
        return end_time

    def start_datetime(self):  #2020-10-06 00:00
        # time_str = self.start_date()+' '+self.start_time()
        now = datetime.datetime.now()
        time_str = now+datetime.timedelta(seconds=+60) #seconds
        return time_str.strftime("%Y-%m-%d %H:%M:%S")

    def end_datetime(self):
        return self.set_datetime().strftime('%Y-%m-%d %H:%M:%S')
