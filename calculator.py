import requests
from bs4 import BeautifulSoup

root_site = 'https://tabiturient.ru'


def calculator(rus='', math='', obsh='', foreg='', inform='', biolog='', geog='', xim='', fiz='', lit='', hist='',
               limit=100, region='',dopexam=0):
    headers = {
        'accept': 'text/html, */*; q=0.01',
        'accept-language': 'ru-RU,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'sec-ch-ua': '\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '\"Windows\"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'x-requested-with': 'XMLHttpRequest'
    }
    body = {
        'sumrus': rus,
        'summath': math,
        'sumobsh': obsh,
        'sumforeg': foreg,
        'suminform': inform,
        'sumbiolog': biolog,
        'sumgeog': geog,
        'sumxim': xim,
        'sumfiz': fiz,
        'sumlit': lit,
        'sumhist': hist,
        'sort': '1',
        'spec': '',
        'city': region + ' ',
        'dopex': dopexam,
        'medal': '0',
        'gto': '0',
        'volont': '0',
        'form1': '1',
        'form2': '0',
        'form3': '0',
        'limit': limit,
        'limmore': '0'
    }
    url = root_site + '/ajax/ajcalculator.php'
    page = requests.post(url, headers=headers, data=body)
    print(f'request to: {url}, with params: {body}')
    soup = BeautifulSoup(page.text, "html.parser")
    vuzes = soup.select('div.mobpadd20-3')

    response = []
    for vuz in vuzes:
        vuz_id = vuz['id'].lstrip("vuz")
        vuz_name = vuz.select('td.vuzlistlogo')[0].text.strip()
        napravlenie = vuz.select('td.vuzlistcontent > div > div > div:nth-child(1) > div > span')[0].text
        about_link = vuz.select('table.dopvuzlist * a')[0]['href']
        vuz_obj = {'vuz_id': vuz_id,
                   'vuz_name': vuz_name,
                   'napravlenie': napravlenie,
                   'about_link': about_link
                   }
        response.append(vuz_obj)
        # vuz_name=vuz.center.b.text
    print(f'response: {response}')
    return response


if __name__ == '__main__':
    print(calculator(rus='90', math='90', inform='90', fiz='90', limit=3, region='1020'))
