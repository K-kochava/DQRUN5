from Feed import News, Forecast, Ad

var = input("Please enter type of task (news, ad, forecast): ")

class CreateFeed:
    def createfeed(var):
        output = ''
        for k in var.split(','):
            if k.strip() in ('news', 'ad', 'forecast'):
                if k == 'news':
                    output = output + News().createfeed()
                else:
                    if k.strip() == 'ad':
                        output = output + Ad().createfeed()
                    else:
                        if k.strip() == 'forecast':
                            output = output + Forecast().createfeed()
                        else:
                            print("Nothing to output" + '\n')
            else:
                print("This is unexpected type of task. Select news, ad or forecast.")
        return output


def main(var):
    f = open("task5.txt", "w")
    f.write(CreateFeed.createfeed(var))
    f.close()


main(var)
