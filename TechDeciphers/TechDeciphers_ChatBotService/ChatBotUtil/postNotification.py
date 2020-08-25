from twilio.rest import Client
import topNewGadgets

def getNewsMethod():
    account_sid = 'AC9357105f5b4b1f8affe58951c64d5f99'
    auth_token = '6952b1b2a154522e6e367d16714ae76e'
    client = Client(account_sid, auth_token)

    whatsAppMessage = topNewGadgets.getTopNewsGadget("")

    print(whatsAppMessage)

    message = client.messages.create(
                                  body = whatsAppMessage,
                                  from_ = 'whatsapp:+14155238886',
                                  to = 'whatsapp:+919742538349'
                              )

    print(message.sid)
