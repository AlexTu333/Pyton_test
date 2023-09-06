import requests

resp = requests.get("http://mobizon.ua/")
#print(resp.status_code)
#print(resp.content)
#print(type(resp))
#print(resp.text)            # Передает уже в закодированном виде
#print(repr(resp.content))  # Возвращает литеральное представление контента (с полным синтаксисом)
#print(resp.headers)
#print(resp.request)
#print(resp.request.headers)
print(resp.url)





