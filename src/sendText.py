from distutils.log import info
from twilio.rest import Client
from Reminder import *
 
account_sid = 'ACd90ea0d83723b9818ae2936efcc9c1ff' 
auth_token = 'd7af2043a0fd6ac621ce8a3e842d2217' 
client = Client(account_sid, auth_token) 

def send(text: str):    
    message = client.messages.create(  
        messaging_service_sid='MG984de57a10f516460cf8a1e48bef2fe0', 
        body=text,      
        to='+17326668590' 
    ) 


    print(message.sid)

send(getInfo())