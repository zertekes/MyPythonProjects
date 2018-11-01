from facepy import GraphAPI
import datetime
import random

api_token = 'EAAKcVSj3FnoBANGMG6lQCsGCDvFNaxopDzZAxgraqEyZBy7omzE8tQN6Mx9uFZBomOFiGoBKe4jExPhfwvwuO3WJLTaClgsCukz5hK1bVG3hG3ygOl9Sw1YrNWhBT4xOhYDIHET1c6319uJuDSA0Magmy78mJZAuX7ZBiebZCXf440UM7ZBXqPjTZBwyVMsxtGGSywllq46bEgZDZD'
graph = GraphAPI(api_token)
friend_list = graph.get("me/friends?fields=birthday,name")
birthday_wishes = ("Happy Birthday")

#Get today's day and month
now = datetime.datetime.now().strftime("%m-%d")
month_day = now.split('-')

#Iterate through friend list birthday's and wish a random message
for friend in friend_list['data']:
    if friend.has_key('birthday'):
        bday_array = friend['birthday'].split('/')
        if bday_array[0] == month_day[0] and bday_array[1] == month_day[1]:
            graph.post(friend['id']+ '/feed', 0, message = birthday_wishes)
            print ("Wished " + friend['name'])

