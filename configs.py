# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "0")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3]

📚 **Library:** [Pyrogram]

📢 **Main channel:** [HD Dᴜʙ Hᴜʙ 4ᴜ](https://t.me/hddubhub4u)

🧑🏻‍💻 **Developer:** @robo_glitch

👥 **Support Group:** [Movie Req Group](https://t.me/dubbedweb)

😈 **Other Bots:** [Future Backups](https://t.me/futurebackups)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻**Notice from Developer: @robo_glitch**

ᴛʜɪs ɪs ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ ꜰɪʟᴇsᴛᴏʀᴇ ʙᴏᴛ.

ʜᴏᴡ ᴛᴏ ᴜsᴇ ?❓

📁 sᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ & ɪᴛ ᴡɪʟʟ ʙᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ & ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴇ ʟɪɴᴋ.

❤ ʙᴇɴᴇꜰɪᴛs: ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ ᴏʀ ᴀɴʏ ᴄᴏᴘʏʀɪɢʜᴛ ᴄʜᴀɴɴᴇʟ, ᴛʜᴇɴ ɪᴛs ᴜsᴇꜰᴜʟ ꜰᴏʀ ᴅᴀɪʟʏ ᴜsᴀɢᴇ, ʏᴏᴜ ᴄᴀɴ sᴇɴᴅ ᴍᴇ ʏᴏᴜʀ ꜰɪʟᴇ & ɪ ᴡɪʟʟ sᴇɴᴅ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ᴛᴏ ʏᴏᴜ & ᴄʜᴀɴɴᴇʟ ᴡɪʟʟ ʙᴇ sᴀꜰᴇ ꜰʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ɪɴꜰʀɪɴɢᴇᴍᴇɴᴛ ɪssᴜᴇ. ɪ sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ ᴀʟsᴏ ʏᴏᴜ ᴄᴀɴ ᴄʜᴇᴄᴋ ᴀʙᴏᴜᴛ ʙᴏᴛ.

⚠ ᴘᴏʀɴᴏɢʀᴀᴘʜʏ ᴄᴏɴᴛᴇɴᴛs ᴀʀᴇ sᴛʀɪᴄᴛʟʏ ᴘʀᴏʜɪʙɪᴛᴇᴅ & ɢᴇᴛ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ.
ᴀʟsᴏ ʀᴇᴍᴇᴍʙᴇʀ ᴛʜᴀᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴡɪʟʟ ᴅᴇʟᴇᴛᴇ ᴀᴅᴜʟᴛ ᴄᴏɴᴛᴇɴᴛs ꜰʀᴏᴍ ᴅᴀᴛᴀʙᴀsᴇ. sᴏ ʙᴇᴛᴛᴇʀ ᴅᴏɴ'ᴛ sᴛᴏʀᴇ ᴛʜᴏsᴇ ᴋɪɴᴅ ᴏꜰ ᴛʜɪɴɢs 🙂

[Donate Me 💰](https://t.me/robo_glitch) (❤ Any Amount ❤)
"""
	HOME_TEXT = """
Hi ❤ [{}](tg://user?id={})\n\n**This is Permanent File Store Bot**

sᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ ɪ ᴡɪʟʟ sᴀᴠᴇ ɪᴛ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ. ᴀʟsᴏ ᴡᴏʀᴋs ꜰᴏʀ ᴄʜᴀɴɴᴇʟ. ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴄʜᴀɴɴᴇʟ ᴀs ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴇᴅɪᴛ ᴘᴇʀᴍɪssɪᴏɴ, ɪ ᴡɪʟʟ ᴀᴅᴅ sᴀᴠᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ꜰɪʟᴇ ɪɴ ᴄʜᴀɴɴᴇʟ & ᴀᴅᴅ sʜᴀʀᴀʙʟᴇ ʙᴜᴛᴛᴏɴ ʟɪɴᴋ.ᴀʟsᴏ! ᴄʜᴇᴄᴋ  **ᴅᴇᴠᴇʟᴏᴘᴇʀ ɴᴏᴛɪᴄᴇ ʙᴜᴛᴛᴏɴ** 🛠
"""
