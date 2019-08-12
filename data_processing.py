from flask_table import Table, Col
import locale
from utils import get_config, get_week_kilometers

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
        self.progress = str(round(((sum(days_d) / 1000) / get_week_kilometers()) * 100, 2)) + '%'
        self.sum = locale.format_string("%.3f", round(sum(days_d)) / 1000, grouping=True) + 'km'
        # days_d = [locale.format_string("%.3f", d / 1000, grouping=True) + 'km' for d in days_d]
        self.day1_d = self.format(days_d[0])
        self.day2_d = self.format(days_d[1])
        self.day3_d = self.format(days_d[2])
        self.day4_d = self.format(days_d[3])
        self.day5_d = self.format(days_d[4])
        self.day6_d = self.format(days_d[5])
        self.day7_d = self.format(days_d[6])
        
    @staticmethod
    def format(day_d):
        """
        generates the display string for a day distance
        :param day_d: days distance
        :return: string
        """
        return '-' if day_d == 0 else locale.format_string("%.3f", day_d / 1000, grouping=True) + 'km'


def create_table(data):
    """
    creates a flask table with the given data
    :param data: distance data per user and day
    :return: table
    """
    items = [UserRunningDataItem(row['user'], [day['distance'] for day in row['days']]) for row in data]
    return UserRunningDataTable(items)
