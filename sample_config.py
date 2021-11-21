import os

class Config(object):
    
    # Telegram Vars
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    ADMINS = set(int(x) for x in os.environ.get("ADMINS", "").split())
    
    #Bot Stuff
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    if BOT_USERNAME.startswith("@"):
        BOT_USERNAME = BOT_USERNAME[1:]


    # Heroku API Vars
    # Copy Paste the below vars and rename it with correct
    # numbers if you need to add more apps
    API_KEY0 = os.environ.get("API_KEY0", None)
    API_KEY1 = os.environ.get("API_KEY1", None)
    API_KEY2 = os.environ.get("API_KEY2", None)
    API_KEY3 = os.environ.get("API_KEY3", None)
    API_KEY4 = os.environ.get("API_KEY4", None)
    API_KEY5 = os.environ.get("API_KEY5", None)
    API_KEY6 = os.environ.get("API_KEY6", None)
    API_KEY7 = os.environ.get("API_KEY7", None)
    API_KEY8 = os.environ.get("API_KEY8", None)
    API_KEY9 = os.environ.get("API_KEY9", None)
    # Heroku APP Vars
    APP_NAME0 = os.environ.get("APP_NAME0", None)
    APP_NAME1 = os.environ.get("APP_NAME1", None)
    APP_NAME2 = os.environ.get("APP_NAME2", None)
    APP_NAME3 = os.environ.get("APP_NAME3", None)
    APP_NAME4 = os.environ.get("APP_NAME4", None)
    APP_NAME5 = os.environ.get("APP_NAME5", None)
    APP_NAME6 = os.environ.get("APP_NAME6", None)
    APP_NAME7 = os.environ.get("APP_NAME7", None)
    APP_NAME8 = os.environ.get("APP_NAME8", None)
    APP_NAME9 = os.environ.get("APP_NAME9", None)
    
   
