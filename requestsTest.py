import requests
import re 

url = 'https://movie.douban.com/top250'
header = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}



res = requests.post(url,headers=header)
content = res.text

print(content)