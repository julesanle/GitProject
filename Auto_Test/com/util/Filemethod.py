import time

class Filemethod:
	"""日期一些格式
		%a 英文星期简写     %A 英文星期的完全
		%b 英文月份的简写   %B 英文月份的完全
		%c 显示本地日期时间   %d 日期，取1-31
		%H 小时， 0-23    %I 小时， 0-12
		%m 月， 01 -12   %M 分钟，1-59   %j 年中当天的天数
		%w 显示今天是星期几  %W 第几周
		%x 当天日期    %X 本地的当天时间
		%y 年份 00-99间   %Y 年份的完整拼写
	"""
	# 获取当前日期字符串  yyy-mm-dd
	def getDate(self):
		return time.strftime("%Y-%m-%d", time.localtime())
	
# 获取当前日期字符串  yyy-mm-dd hh:mm:ss
	def getTime(self):
		return time.strftime("%Y-%m-%d %X", time.localtime())
	
# 获取前一月同一天的日期
	def getLastMonth(self):
		current_mon = time.localtime().tm_mon
		date = current_mon - 1
		last_month = time.localtime().tm_mon-1

	    # cal.add(Calendar.MONTH, -1);
		# String date=df.format(cal.getTime());
		return date


