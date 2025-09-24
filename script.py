from twilio.rest import Client
import hadith
import idsDoNotGit

account_sid = idsDoNotGit.get_accountsid()
auth_token = idsDoNotGit.get_auth_token()
hadith_api_key = idsDoNotGit.get_hadith_api_key()

client = Client(account_sid, auth_token)

english, number, bookName, status = hadith.get_hadith(hadith_api_key)

message = client.messages.create(
  from_=idsDoNotGit.get_sender(),
  body= f"{english}\n\n{bookName}: {number}\nGrade: {status}",
  to=idsDoNotGit.get_reciever()
)

#print(english)
#print(number)
#print(bookName)
#print(status)