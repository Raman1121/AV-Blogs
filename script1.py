
from twilio.rest import Client 
   
account_sid = '<YOUR-ACC-ID-HERE>8' # Obtained from Step-3 
auth_token = 'your_auth_token' # Obtained from Step-3 
   
Your_whatsapp_number = ‘+911234567899’ # Include the country code 
From_number = ‘+1488*****’ # Obtained from Step 2 
   
client = Client(account_sid, auth_token) 
   
message = client.messages.create( 
                             body ='Hello there !', 
                             from_= From_number, 
                             to = Your_whatsapp_number 
                         ) 
print(message.sid) 