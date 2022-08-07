import requests
import lxml.html as html
import os
import datetime





home_url = 'https://www.larepublica.co/'
xpath_link_to_article= '//div[@class="container"]//a/@href'
xpath_title='//div[@class="mb-auto"]/h2/span/text()'
xpath_summary='//div[@class="lead"]/p//text()'
xpath_body = '//div[@class ="html-content"]/p[not(@class)]//text()'

def parse_notice(links, today):
    try:
        pass
    except


def parse_home():
    try:
        response =requests.get(home_url)
        if response.status_code == 200:
           home = response.content.decode('utf-8')
           parsed = html.fromstring(home)
           links_to_notices = parsed.xpath(xpath_link_to_article)
           #print(links_to_notices)

           today = datetime.date.today().strftime('%d-%m-%Y') #guardamos las fechas
           if not os.path.isdir(today):
            os.mkdir(today)

           for link in links_to_notices:
            parse_notice(link, today)  


        else:
            raise ValueError(f'Error: {response.status_code}')


    except ValueError as ve:
        print(ve)



def run():
    parse_home()    


if __name__ =='__main__':
    run()