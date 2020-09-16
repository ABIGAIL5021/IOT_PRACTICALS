import telepot
token='your token from botfather'
TelegramBot=telepot.Bot(token)
print(TelegramBot.getMe())
def handle(msg):
  content_type,chat_type,chat_id=telepot.galnce(msg)
  print(content_type,chat_type,chat_id)
  
  if content_type=='text':
    TelegramBot.sendMessage(chat_id,"you said'{}'".format(msg["text"]))
    
TelegramBot.message_loop(handle)
