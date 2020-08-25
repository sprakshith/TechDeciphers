import datetime

def getMonthvalue(month):
    if month == 'January':
        return '01'
    elif month == 'February':
        return '02'
    elif month == 'March':
        return '03'
    elif month == 'April':
        return '04'
    elif month == 'May':
        return '05'
    elif month == 'June':
        return '06'
    elif month == 'July':
        return '07'
    elif month == 'August':
        return '08'
    elif month == 'September':
        return '09'
    elif month == 'October':
        return '10'
    elif month == 'November':
        return '11'
    elif month == 'December':
        return '12'
    else:
        return '01'

def getArticleDate(rawHtmlDate):
    actualDate = rawHtmlDate.split(",")[1]
    actualDate = actualDate.strip()
    actualDate = actualDate.split(' ')
    print("actualDate ::::: {}".format(actualDate))

    dateFormat = "2000-12-12"
    dateObject = ""

    if len(actualDate) >= 3:
        dateFormat = "{}-{}-{}".format(actualDate[2],getMonthvalue(actualDate[1]),actualDate[0])

    dateObject = datetime.datetime.strptime(dateFormat,'%Y-%m-%d').date()

    return dateObject
