import requests
from TechDeciphers_ChatBotService.ChatBotUtil.dateTimeUtil import getArticleDate
from bs4 import BeautifulSoup
from datetime import date

def getTopNewsGadget(messageFormat):

    for i in range(1,6):
        URL = "https://gadgets.ndtv.com/news/page-" + str(i)
        r = requests.get(URL)

        soup = BeautifulSoup(r.content, 'html5lib')

        table = soup.find('div', attrs = {'class' : 'story_list'})
        tableData = table.find_all_next('li');

        myList = []
        for data in tableData:
            captionData = data.find('span', attrs = {'class' : 'news_listing'})
            dateData = data.find('div', attrs = {'class' : 'dateline'})
            articleDictionary = {}
            if dateData != None and captionData != None:
                myDate = getArticleDate(dateData.text)
                myArticle = captionData.text
                todayDate = date.today()
                if(myDate == date.today()):
                    myList.append(myArticle)

        for i in range(len(myList)):
            messageFormat += "{}. {}\n".format(i+1, myList[i])

        return messageFormat
