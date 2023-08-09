from pathlib import Path 
from dotenv import load_dotenv  
import requests 
import json
import os  
import requests
load_dotenv() 



api_key = os.environ.get('api_key') 


file_data = open('sample_gpt.pdf', 'rb') 
    
headers = {
    'x-api-key': api_key
}


#------------------ upload your document 
 
response = requests.post('https://api.askyourpdf.com/v1/api/upload', headers=headers,
 files={'file': file_data})

if response.status_code == 201:
    print(response.json())
else:
    print('Error:', response.status_code)




#------------------ chat with document 



headers = {
    'Content-Type': 'application/json',
    'x-api-key': api_key
}

data = [
    {
        "sender": "User",
        "message": "What does this document say?"
    }
]
docid = {"docId":"b8b9b60f-1243-45fc-9686-f46e152e07fb"}
response = requests.post('https://api.askyourpdf.com/v1/chat/b8b9b60f-1243-45fc-9686-f46e152e07fb', 
headers=headers, data=json.dumps(data))

if response.status_code == 200:
    res = response.json() 
    print(res['answer']['message'])
else:
    print('Error:', response.status_code) 

 


