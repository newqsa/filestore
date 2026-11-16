import logging
from logging.handlers import RotatingFileHandler

# Bot Configuration
LOG_FILE_NAME = "bot.log"
PORT = '8080'
OWNER_ID = 6390511215

MSG_EFFECT = 5046509860389126442

SHORT_URL = "" # shortner url 
SHORT_API = "" 
SHORT_TUT = ""

# Bot Configuration
SESSION = "yato"
TOKEN = "642712"
API_ID = ""
API_HASH = ""
WORKERS = 5

DB_URI = "mongodb"
DB_NAME = "addafilez"

FSUBS = [[-1003016571084, True, 10]] # Force Subscription Channels [channel_id, request_enabled, timer_in_minutes]
# Database Channel (Primary)
DB_CHANNEL =    # just put channel id dont add ""
# Multiple Database Channels (can be set via bot settings)
# DB_CHANNELS = {
#     "-1002595092736": {"name": "Primary DB", "is_primary": True, "is_active": True},
#     "-1001234567890": {"name": "Secondary DB", "is_primary": False, "is_active": True}
# }
# Auto Delete Timer (seconds)
AUTO_DEL = 300
# Admin IDs
ADMINS = [6390511215, 862418425]
# Bot Settings
DISABLE_BTN = True
PROTECT = False

# Messages Configuration
MESSAGES = {
    "START": "<b>›› ʜᴇʏ!!, {first} ~ <blockquote>ನಮಸ್ತೆ..ನಮ್ಮ ಮೂವಿಗಳನ್ನ save ಮಾಡಿ ಇಟ್ಕೊಂಡಿರಿತಿನೇ.</blockquote></b>",
    "FSUB": "<b><blockquote>›› ʜᴇʏ ×</blockquote>\n  ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️ ನೀವು ಇನ್ನೂ ನಮ್ಮ ಚಾನೆಲ್‌ಗಳಿಗೆ ಸಬ್‌ಸ್ಕ್ರೈಬ್ ಮಾಡಿಲ್ಲ ಎಂದು ಕಾಣುತ್ತಿದೆ. ನಿಮ್ಮ ಫೈಲ್‌ಗಳನ್ನು ಪಡೆಯಲು ಈಗಲೇ ನಮ್ಮ ಚಾನೆಲ್‌ಗಳನ್ನು ಸಬ್‌ಸ್ಕ್ರೈಬ್ ಮಾಡಿ!</b>",
    "ABOUT": "<b>›› ғᴏʀ ᴍᴏʀᴇ: @AddaFileZ\n <blockquote expandable>›› ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/AddaFileZ'>Cʟɪᴄᴋ ʜᴇʀᴇ</a> \n›› ᴏᴡɴᴇʀ: @Contact_AddaFileZ_bot \n›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @AddaFileZ</b></blockquote>",
    "REPLY": "<b>For More Join - @AddaFileZ</b>",
    "SHORT_MSG": "<b>📊 ʜᴇʏ {first}, \n\n‼️ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇꜱ ɪɴ ᴀ ꜱɪɴɢʟᴇ ʟɪɴᴋ ‼️\n\n ⌯ ʏᴏᴜʀ ʟɪɴᴋ ɪꜱ ʀᴇᴀᴅʏ, ᴋɪɴᴅʟʏ ᴄʟɪᴄᴋ ᴏɴ ᴏᴘᴇɴ ʟɪɴᴋ ʙᴜᴛᴛᴏɴ..</b>",
    "START_PHOTO": "https://graph.org/file/510affa3d4b6c911c12e3.jpg",
    "FSUB_PHOTO": "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg",
    "SHORT_PIC": "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg",
    "SHORT": "https://telegra.ph/file/8aaf4df8c138c6685dcee-05d3b183d4978ec347.jpg"
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
