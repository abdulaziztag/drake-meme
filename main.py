from PIL import Image, ImageDraw, ImageFont
from telethon import TelegramClient, events
import os
api_id = 901989
api_hash = '9a188355878585bb2237201d1a3b7ce5'
client = TelegramClient('anon', api_id, api_hash)

def wrap(str):
    txtArr = list(str)
    if (len(str) >= 24):
        txtArr.insert(25, '\n')
        str = ''.join(txtArr)
    if (len(str) >= 12):
        txtArr.insert(13, '\n')
        str = ''.join(txtArr)
    if (len(str) >= 36):
        txtArr.insert(37, '\n')
        str = ''.join(txtArr)
    if (len(str) >= 48):
        txtArr.insert(49, '\n')
        str = ''.join(txtArr)
    return str

@client.on(events.InlineQuery)
async def handler(event):
    builder = event.builder
    try:
        textArr = event.text.split('|')
        drake = Image.open('drake.jpg')
        #r"C:\Windows\Fonts\SEGUIEMJ.ttf"
        font = ImageFont.truetype("arial.ttf", 60)
        font2 = ImageFont.truetype("arial.ttf", 30)
        d = ImageDraw.Draw(drake)
        d.text((550, 110), wrap(textArr[0]), fill="black", font=font, embedded_color=True)
        if (len(textArr) >= 2):
            d.text((550, 610), wrap(textArr[1]), fill="black", font=font, embedded_color=True)
        if (len(textArr) >= 3):
            d.text((150, 50), textArr[2], fill="white", font=font, embedded_color=True)
        d.text((720, 930), "@drake_memebot", fill="black", font=font2)
        basewidth = 300
        wpercent = (basewidth / float(drake.size[0]))
        hsize = int((float(drake.size[1]) * float(wpercent)))
        img = drake.resize((basewidth, hsize), Image.ANTIALIAS)
        img.save('sompic' + str(event.id) + '.jpg')
    except Exception as e:
        print(e)
    await event.answer([
        builder.photo('./sompic' + str(event.id) + '.jpg')
    ])
    os.remove('./sompic' + str(event.id) + '.jpg')

client.start()
client.run_until_disconnected()
