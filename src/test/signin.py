import requests

response = requests.post(url="http://127.0.0.1:5000/signin",
                         json={
                               "email":"viv@gmail.com", 
                               "password":"P@$$w0rd"
                              },
                         headers={"Content-Type":"application/json"})

print(response.status_code)
print(response.json())