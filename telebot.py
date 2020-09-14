import telepot
token='1302764251:AAFK-t2r9xGxy0a0O5OcLs_5H7akNNuwHg'
TelegramBot=telepot.Bot(token)
print(TelegramBot.getMe())
def handle(msg):
  content_type,chat_type,chat_id=telepot.galnce(msg)
  print(content_type,chat_type,chat_id)
  
  if content_type=='text':
    TelegramBot.sendMessage(chat_id,"you said'{}'".format(msg["text"]))
    
TelegramBot.message_loop(handle)
