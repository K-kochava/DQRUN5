from datetime import date, datetime


class Feed:
    def __init__(self):
        self.today = date.today()

    def input_text(self):
        text = input("Please enter your text: ")
        return text

    def input_city(self):
        city = input("Please enter your city: ")
        return city

    def input_date(self):
        expiration_date = input("Please enter your ad's expiration date in YYYY-MM-DD format: ")
        return expiration_date

    def diff_count(self, expiration):
        date_object = datetime.strptime(expiration, '%Y-%m-%d').date()
        diff = date_object - self.today
        diff = diff.days
        return diff


class News(Feed):
    def createfeed(self):
        news = str("News:" + '\n' + str(self.input_text()) + '\n' + str(self.input_city()) + ', ' + str(self.today) + '\n' + '\n')
        return news


class Ad(Feed):
    def createfeed(self):
        expiration_date = self.input_date()
        ad = str("Ad:" + '\n' + str(self.input_text()) + '\n' + 'Actual until: ' + str(expiration_date) + ', ' + (
                    str(self.diff_count(expiration_date)) + ' day(s) left.') + '\n' + '\n')
        return ad


class Forecast(Feed):
    def createfeed(self):
        text = 'The weather forecast is not available for selected region.'
        forecast = str("Forecast:" + '\n' + text + '\n' + str(self.input_city()) + ', ' + str(self.today) + '\n' + '\n')
        return forecast
