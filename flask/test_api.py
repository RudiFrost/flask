from requests import get, post, delete

# newses = get('http://localhost:5000/api/news').json()
#
# for nws in newses["news"]:
#     print(nws)
#     print("-------------------------------------")

# print(get('http://localhost:5000/api/news/1').json())
#
# print(get('http://localhost:5000/api/news/999').json())
# # новости с id = 999 нет в базе
#
# print(get('http://localhost:5000/api/news/q').json())
#
# print(post('http://localhost:5000/api/news').json())
#
# print(post('http://localhost:5000/api/news',
#            json={'title': 'Заголовок'}).json())
#
# print(post('http://localhost:5000/api/news',
#            json={'title': 'Новость API 1',
#                  'content': 'Эту новость мы тоже добавили с помощью API',
#                  'user_id': 1,
#                  'is_private': False}).json())

# newses = get('http://localhost:5000/api/news').json()
#
# for nws in newses["news"]:
#     print(nws)
#     print("-------------------------------------")

newses = get('http://localhost:5000/api/v2/news').json()

for nws in newses["news"]:
    print(nws)
    print("-------------------------------------")

print(post('http://localhost:5000/api/v2/news',
           json={'title': 'API v2 Новость 2 ',
                 'content': 'API v2 2v Эту новость мы тоже добавили с помощью API v2',
                 'user_id': 1,
                 'is_private': False}).json())

newses = get('http://localhost:5000/api/v2/news').json()

for nws in newses["news"]:
    print(nws)
    print("-------------------------------------")

# print(delete('http://localhost:5000/api/news/999').json())
# # новости с id = 999 нет в базе
#
# print(delete('http://localhost:5000/api/news/5').json())

# newses = get('http://localhost:5000/api/news').json()
#
# for nws in newses["news"]:
#     print(nws)
#     print("-------------------------------------")