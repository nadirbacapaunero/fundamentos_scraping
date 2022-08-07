import requests
import lxml.html as html
import os
import datetime





home_url = 'https://www.larepublica.co/'
xpath_link_to_article='//text-fill[not(@class)]/a/@href'           #'//div[@class="container"]//a/@href' #cambie el div por el text-fill
xpath_title='//div[@class="mb-auto"]/text-fill/span/text()'  #cambie el h2 por el text-fill
xpath_summary='//div[@class="lead"]/p//text()'
xpath_body = '//div[@class ="html-content"]/p[not(@class)]//text()'

def parse_notice(link, today):
    try:
      response = requests.get(link)
      if response.status_code == 200:
        notice = response.content.decode('utf-8')
        parsed = html.fromstring(notice)

        try:
            title = parsed.xpath(xpath_title)[0]
            title = title.replace('\"', '')
            summary = parsed.xpath(xpath_summary)[0]
            body = parsed.xpath(xpath_body)
        except IndexError:
            return
        with open('{}\{}.txt'.format(today,title),'w', encoding='utf-8') as f:
            f.write(title)
            f.write('\n\n')
            f.write(summary)
            f.write('\n\n')  
            for p in body:
                f.write(p)
                f.write('\n')
      else:
        raise ValueError(response.status_code)
    except ValueError as ve:
        print(ve)


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
            raise ValueError(response.status_code)


    except ValueError as ve:
        print(ve)



def run():
    parse_home()    


if __name__ =='__main__':
    run()