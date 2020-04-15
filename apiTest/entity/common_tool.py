from _datetime import datetime


class Common_Tools:
    '''提供一些公共的方法'''

    def format_date(self) -> str:
        current_time = datetime.now()
        c_year = current_time.year
        c_month = current_time.month
        c_day = current_time.day
        c_hour = current_time.hour
        c_minutes = current_time.minute
        c_seconds = current_time.second
        format_time = str(c_year) + str(c_month) + str(c_day) + str(c_hour) + str(c_minutes) + str(c_seconds)
        return format_time

if __name__ == "__main__":
    format_date = Common_Tools()
    date_new = format_date.format_date()
    print(type(date_new))
    print(format_date.format_date())
