from datetime import datetime, date


class feedCreator:
    def create_feed(var):
        output = ''
        if var:
            for k in var.split('\n\n'):
                if k[0:4].find('news') != -1:
                    text = k.split('\n')[1]
                    city = k.split('\n')[2]
                    news = str("News:" + '\n' + text + '\n' + city + ', ' + str(date.today()) + '\n' + '\n')
                    output = output + news
                if k[0:2].find('ad') != -1:
                    text_ad = k.split('\n')[1]
                    expiration_date = k.split('\n')[2]
                    today = date.today()
                    date_object = datetime.strptime(expiration_date, '%Y-%m-%d').date()
                    diff = date_object - today
                    ad = str("Ad:" + '\n' + text_ad + '\n' + 'Actual until: ' + str(date_object) + ', ' + (
                            str(diff.days) + ' day(s) left.') + '\n' + '\n')
                    output = output + ad
                if k[0:8].find('forecast') != -1:
                    location = k.split('\n')[1]
                    text = 'The weather forecast is not available for selected region.'
                    forecast = str("Forecast:" + '\n' + text + '\n' + location + ', ' + str(date.today()) + '\n' + '\n')
                    output = output + forecast
            return output