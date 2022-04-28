import requests
from bs4 import BeautifulSoup

root_site = 'https://tabiturient.ru'


def calculator(rus='', math='', obsh='', foreg='', inform='', biolog='', geog='', xim='', fiz='', lit='', hist=''):
    headers = {
        'accept': 'text/html, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
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
        'city': '',
        'dopex': '1',
        'medal': '0',
        'gto': '0',
        'volont': '0',
        'form1': '1',
        'form2': '0',
        'form3': '0',
        'limit': '10',
        'limmore': '0'
    }
    page = requests.post(root_site + '/ajax/ajcalculator.php', headers=headers, data=body)
    soup = BeautifulSoup(page.text, "html.parser")
    vuzes = soup.select('div.mobpadd20-3')

    response = []
    for vuz in vuzes:
        vuz_id = vuz['id'].lstrip("vuz")
        vuz_name = vuz.select('td.vuzlistlogo')[0].text
        napravlenie = vuz.select('td.vuzlistcontent > div > div > div:nth-child(1) > div > span')[0].text
        about_link = vuz.select('table.dopvuzlist * a')[0]['href']
        vuz_obj = {'vuz_id': vuz_id,
                   'vuz_name': vuz_name,
                   'napravlenie': napravlenie,
                   'about_link': about_link
                   }
        response.append(vuz_obj)
        # vuz_name=vuz.center.b.text
    return response


if __name__ == '__main__':
    calculator(rus='90', math='90', inform='90', fiz='90')
