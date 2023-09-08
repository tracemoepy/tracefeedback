from pyrogram import Client, idle
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
app = Client("john_bot",
             api_id=config.get('pyrogram', 'api_id'),
             api_hash=config.get('pyrogram', 'api_hash'),
             bot_token=config.get('pyrogram', 'bot_token'),
             plugins=dict(root="plugins"),
)
if __name__ == '__main__':
    app.start()
    idle()
    
