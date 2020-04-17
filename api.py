import requests

params = {'ll': '58.601003,49.674041',
          'size': '450,450',
          'l': 'sat',
          'z': '17'
         }
url = 'https://static-maps.yandex.ru/1.x'
r = requests.get(url, params=params)

f = open('title.jpg', mode='wb')
f.write(r.content)
f.close()