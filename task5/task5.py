from datetime import date, datetime
var = input("Please enter type of task (news, ad, forecast): ")


def createfeed(var):
    output = ''
    for k in var.split(','):
        if k.strip() in ('news', 'ad', 'forecast'):
            if k == 'news':
                text = input("Please enter your news' text: ")
                city = input("Please enter your city: ")
                today = datetime.today()
                news = str("News:" + '\n' + text + '\n' + city + ', ' + str(date.today()) + '\n' + '\n')
                output = output + news
            else:
                if k.strip() == 'ad':
                    text_ad = input("Please enter your text_ad: ")
                    expiration_date = input("Please enter your ad's expiration date in YYYY-MM-DD format: ")
                    today = date.today()
                    date_object = datetime.strptime(expiration_date, '%Y-%m-%d').date()
                    diff = date_object - today
                    ad = str("Ad:" + '\n' + text_ad + '\n' + 'Actual until: ' + str(date_object) + ', ' + (str(diff.days) + ' day(s) left.') + '\n' + '\n')
                    output = output + ad
                else:
                    if k.strip() == 'forecast':
                        location = input("Please enter your location: ")
                        text = 'The weather forecast is not available for selected region.'
                        forecast = str("Forecast:" + '\n' + text + '\n' + location + ', ' + str(date.today()) + '\n' + '\n')
                        output = output + forecast
                    else:
                        print("Nothing to output" + '\n')
        else:
            print("This is unexpected type of task. Select news, ad or forecast.")
    return output


def main(var):
    f = open("task5.txt", "w")
    f.write(createfeed(var))
    f.close()


main(var)
