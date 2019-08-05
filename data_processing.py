from flask_table import Table, Col
import locale
from utils import get_config


locale.setlocale(locale.LC_NUMERIC, "german")


class UserRunningDataTable(Table):

    user = Col('')
    day1_d = Col('Montag')
    day2_d = Col('Dienstag')
    day3_d = Col('Mittwoch')
    day4_d = Col('Donnerstag')
    day5_d = Col('Freitag')
    day6_d = Col('Samstag')
    day7_d = Col('Sonntag')
    sum = Col('Gesamt')
    progress = Col('Fortschritt')

    def sort_url(self, col_id, reverse=False):
        pass


class UserRunningDataItem(object):

    def __init__(self, user, days_d):
        self.user = user
        self.progress = str(round(((sum(days_d) / 1000) / int(get_config()['CHALLENGE']['start_kilometers'])) * 100, 2)) + '%'
        self.sum = locale.format_string("%.3f", round(sum(days_d)) / 1000, grouping=True) + 'km'
        days_d = [locale.format_string("%.3f", d / 1000, grouping=True) + 'km' for d in days_d]
        self.day1_d = days_d[0]
        self.day2_d = days_d[1]
        self.day3_d = days_d[2]
        self.day4_d = days_d[3]
        self.day5_d = days_d[4]
        self.day6_d = days_d[5]
        self.day7_d = days_d[5]


def create_table(data):

    items = [UserRunningDataItem(row['user'], [day['distance'] for day in row['days']]) for row in data]
    return UserRunningDataTable(items)
