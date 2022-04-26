from datetime import date, datetime


class Feed:
    def createfeed(var):
        pass

class News(Feed):
    def createfeed(var):
        text = input("Please enter your news' text: ")
        city = input("Please enter your city: ")
        news = str("News:" + '\n' + text + '\n' + city + ', ' + str(date.today()) + '\n' + '\n')
        return news

class Ad(Feed):
    def createfeed(var):
        text_ad = input("Please enter your text_ad: ")
        expiration_date = input("Please enter your ad's expiration date in YYYY-MM-DD format: ")
        today = date.today()
        date_object = datetime.strptime(expiration_date, '%Y-%m-%d').date()
        diff = date_object - today
        ad = str("Ad:" + '\n' + text_ad + '\n' + 'Actual until: ' + str(date_object) + ', ' + (
                    str(diff.days) + ' day(s) left.') + '\n' + '\n')
        return ad

class Forecast(Feed):
    def createfeed(var):
        location = input("Please enter your location: ")
        text = 'The weather forecast is not available for selected region.'
        forecast = str("Forecast:" + '\n' + text + '\n' + location + ', ' + str(date.today()) + '\n' + '\n')
        return forecast