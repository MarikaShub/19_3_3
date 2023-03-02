import requests
import json

# POST
user = {
    "id": 123456789,
    "username": "maruSh",
    "firstName": "maru",
    "lastName": "Shun",
    "email": "sdf@fgfg.ru",
    "password": "123457899",
    "phone": "1234667887987",
    "userStatus": 0
  }
res_create_user = requests.post('https://petstore.swagger.io/v2/user', data=json.dumps(user, ensure_ascii=False), headers={'accept': 'application/json', 'Content-Type': 'application/json'})

print(f'Статус кода POST: {res_create_user}')
print(res_create_user.json())


# GET
get_username = 'maruSh'
res_username = requests.get(f"https://petstore.swagger.io/v2/user/{get_username}", headers={'accept': 'application/json'})

print(f"Статус кода get: {res_username}")
print(res_username.json())

# PUT
put_username = 'maruSh'
put_user = {
  "id": 9223372036854744308,
  "username": "maruSh",
  "firstName": "Marina",
  "lastName": "Shubina",
  "email": "123@asdf.ru",
  "password": "123457890-9",
  "phone": "12356",
  "userStatus": 0
}
res_put_user = requests.put(f'https://petstore.swagger.io/v2/user/{put_username}', data=json.dumps(put_user, ensure_ascii=False),
                            headers={'accept': 'application/json', 'Content-Type': 'application/json'})


print(f'Статус кода PUT: {res_put_user}')
print(res_put_user.json())


# DELETE
del_user = 'maruSh'
res_del_user = requests.delete(f'https://petstore.swagger.io/v2/user/{del_user}', headers={'accept': 'application/json'})
print(f'Статус кода DELETE: {res_del_user}')
print(res_del_user.json())
