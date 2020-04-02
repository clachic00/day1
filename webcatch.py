import requests

from bs4 import BeautifulSoup


def getData():

    result = []

    print("getData.....")


    url='https://bbs.ruliweb.com/market/board/1020'


    req = requests.get(url)
    html = req.text

    #print(html)

    soup = BeautifulSoup(html, 'html.parser')

    items = soup.select(".subject")

    for item in items:
        #print(item.text)

        #print(items)
        result.append(item.text)

    return result



    #