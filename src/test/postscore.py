import requests

response = requests.post(url="http://127.0.0.1:5000/postscore",
                         json={
                               "idea_pitch":"6", 
                               "feature_value":"8",
                               "future_scope":"8",
                               "working_model":"6",
                               "presentation":"9",
                               "comment":"",
                               
                               "id":"1",
                               "judge_uid":"2iuj7e1247g1TYSJ0TicqO2WaM73"
                              },
                         headers={"Content-Type":"application/json"})

print(response.status_code)
print(response.json())


