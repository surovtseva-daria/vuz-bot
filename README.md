# Прокси к сайту Калькулятор баллов ЕГЭ

https://tabiturient.ru/calculator/

Прокси принимает запрос по адресу /vuzes/

С параметрами по баллам, например 

`http://127.0.0.1:5000/vuzes/?math=90&rus=90&fiz=90&inform=90&region=1001&limit=10`

в ответ возвращает список вузов и специальностей в формате json:

```json
[
  {
    "about_link": "https://tabiturient.ru/vuzu/kosygin/about", 
    "napravlenie": "Конструирование изделий легкой промышленности", 
    "vuz_id": "4864", 
    "vuz_name": "РГУ им. А.Н. Косыгина"
  }, 
  {
    "about_link": "https://tabiturient.ru/vuzu/kosygin/about", 
    "napravlenie": "Технология художественной обработки материалов", 
    "vuz_id": "17729", 
    "vuz_name": "РГУ им. А.Н. Косыгина"
  }, 
  {
    "about_link": "https://tabiturient.ru/vuzu/kosygin/about", 
    "napravlenie": "Технология художественной обработки материалов", 
    "vuz_id": "4912", 
    "vuz_name": "РГУ им. А.Н. Косыгина"
  }, 
  {
    "about_link": "https://tabiturient.ru/vuzu/kosygin/about", 
    "napravlenie": "Технологии и проектирование текстильных изделий", 
    "vuz_id": "4861", 
    "vuz_name": "РГУ им. А.Н. Косыгина"
  }, 
  {
    "about_link": "https://tabiturient.ru/vuzu/mgu/about", 
    "napravlenie": "Прикладная математика и информатика", 
    "vuz_id": "579", 
    "vuz_name": "МГУ им. Ломоносова"
  }, 
  {
    "about_link": "https://tabiturient.ru/vuzu/mgu/about", 
    "napravlenie": "Фундаментальная информатика и информационные технологии", 
    "vuz_id": "580", 
    "vuz_name": "МГУ им. Ломоносова"
  }, 
  {
    "about_link": "https://tabiturient.ru/vuzu/mgu/about", 
    "napravlenie": "Экономика", 
    "vuz_id": "624", 
    "vuz_name": "МГУ им. Ломоносова"
  }, 
  {
    "about_link": "https://tabiturient.ru/vuzu/mgu/about", 
    "napravlenie": "Фундаментальные математика и механика", 
    "vuz_id": "3766", 
    "vuz_name": "МГУ им. Ломоносова"
  }, 
  {
    "about_link": "https://tabiturient.ru/vuzu/mgu/about", 
    "napravlenie": "Фундаментальная и прикладная физика", 
    "vuz_id": "612", 
    "vuz_name": "МГУ им. Ломоносова"
  }, 
  {
    "about_link": "https://tabiturient.ru/vuzu/mgu/about", 
    "napravlenie": "Фундаментальные математика и механика", 
    "vuz_id": "573", 
    "vuz_name": "МГУ им. Ломоносова"
  }
]
```

Параметры предметов:

* math - Математика
* rus - Русский
* obsh - Обществознание
* foreg - Иностранный язык
* inform - ИКТ
* biolog - Биология
* geog - География
* xim - Химия 
* fiz - Физика
* lit- Литература
* hist - История

Параметр region может быть пустым или соответсвовать значению в файле `./regions.csv`

# Запуск локально 

`pip install`

`python app.py`

