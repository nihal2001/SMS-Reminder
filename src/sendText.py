from twilio.rest import Client
 
account_sid = 'ACd90ea0d83723b9818ae2936efcc9c1ff' 
auth_token = 'ed4a22bcdb3920c38fada1d100b11759' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
    messaging_service_sid='MG984de57a10f516460cf8a1e48bef2fe0', 
    body='This is a test',      
    to='+17326668590' 
) 

print(message.sid)