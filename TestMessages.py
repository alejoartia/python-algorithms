"""This is an exaple about how to use Twilio rest to send messages"""
# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import os
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
#TWILIO_ACCOUNT_SID = 'ACbf277416bd2a67ba415d7cf20d0f6ea0'
#TWILIO_AUTH_TOKEN = '28ba348947f6f1969c6209316a702e3a'

#account_sid = os.environ['TWILIO_ACCOUNT_SID']
#auth_token = os.environ['TWILIO_AUTH_TOKEN']


account_sid = 'ACbf277416bd2a67ba415d7cf20d0f6ea0'
auth_token = '28ba348947f6f1969c6209316a702e3a'


client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+573133114059",
    from_="+13253088674",
    body="Funciono y te amo julieth")
