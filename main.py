from pyrogram import Client, idle


app = Client("tracemoepy")

if __name__ == '__main__':
    app.start()
    idle()
