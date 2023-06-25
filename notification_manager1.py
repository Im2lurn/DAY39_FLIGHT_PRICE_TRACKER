import requests
from details import bot_token1, bot_chatID1
class NotificationManager:
    def send_sms(self,message):
        bot_token = bot_token1
        bot_chatID = bot_chatID1
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + message

        response = requests.get(send_text)
        return response.json()


