import requests
from api_url import URL

def post_user(user):
    return requests.post(f"{URL}/usuarios", json=user)

def get_users(id=None, cpf=None):
    if id:
        return requests.get(f"{URL}/usuarios/{id}").json()
    users = requests.get(f"{URL}/usuarios").json()
    if cpf:
        id = [user["id"] for user in users if user["cpf"] == cpf][0]
        return requests.get(f"{URL}/usuarios/{id}").json()
    return users

def delete_user(id):
    return requests.delete(f"{URL}/usuarios/{id}")

def update_user(id, user):
    return requests.put(f"{URL}/usuarios/{id}", json=user)

def get_bikes(id=None):
    if id:
        return requests.get(f"{URL}/bikes/{id}").json()
    return requests.get(f"{URL}/bikes").json()

def post_bikes(bike):
    return requests.post(f"{URL}/bikes", json=bike)

def delete_bikes(id):
    return requests.delete(f"{URL}/bikes/{id}")

def update_bikes(id, bike):
    return  requests.put(f"{URL}/bikes/{id}", json=bike)

def get_emp(id=None, id_user=None, id_bike=None):
    if id:
        return requests.get(f"{URL}/emprestimos/{id}").json()
    emps = requests.get(f"{URL}/emprestimos").json()
    if id_user:
       emps = [emp for emp in emps if emp['usuario_id'] == id_user]
    if id_bike:
       emps = [emp for emp in emps if emp['bicicleta_id'] == id_bike]
    return emps

def delete_emp(id):
    return requests.delete(f"{URL}/emprestimos/{id}")

def post_emp(id_user, id_bike):
    return requests.post(f"{URL}/emprestimos/usuarios/{id_user}/bikes/{id_bike}")

    