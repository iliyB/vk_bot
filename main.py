import vk_api
from vk_api.longpoll import VkLongPoll,VkEventType

from bot import VkBot
import datetime
now=datetime.datetime.now()

token="2e206344c6f275c520ace5c8f856f61b4dc8f1833142dc767a7c6a96a42e44c4c252213434609c431cf13" 
N_message=1

def write_message(user_id,message):
	global N_message
	tim=now.hour*100 + now.minute+now.second
	if message=="Приезжай":
		vk.method('messages.send', {'user_id': user_id, 'message': message,'random_id': tim+N_message})
		N_message+=1
		vk.method('messages.send', {'user_id': user_id, 'message': message,'random_id':tim+N_message,'sticker_id':53})
		N_message+=1
	else:
		vk.method('messages.send', {'user_id': user_id, 'message': message,'random_id':tim+N_message})
		N_message+=1
	

vk=vk_api.VkApi(token=token)

longpoll=VkLongPoll(vk)

print("Server started")
for event in longpoll.listen():
	if event.to_me and event.type==VkEventType.MESSAGE_NEW:
		print('New message')
		print(f'For me by: {event.user_id}', end='')

		bot=VkBot(event.user_id)

		write_message(event.user_id,bot.new_message(event.text))

		print('Text: ', event.text)