from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "ACb3c8970fd8a9760050e39830d967949f" 
AUTH_TOKEN = "f05e2bc697862123ccf6a684c7b73a42" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
def sendMessage(to_number, message):
    to_number = "+91" + to_number
    print(to_number)
    client.messages.create(
	to=to_number, 
	from_="+15403181521", 
	body=message,  
)
