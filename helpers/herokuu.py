import heroku3
from sample_config import Config

"""
    Appending each value to the list
    So even if app vars not in order,
    it will be appended to the list XD

    Copy paste this code to make more apps :)

"""


app = []
try:
    app.append(Config.APP_NAME0)
except AttributeError:
    app.append(None)
    pass
try:
    app.append(Config.APP_NAME1)
except AttributeError:
    app.append(None)
    pass
try:
    app.append(Config.APP_NAME2)
except AttributeError:
    app.append(None)
    pass
try:
    app.append(Config.APP_NAME3)
except AttributeError:
    app.append(None)
    pass
try:
    app.append(Config.APP_NAME4)
except AttributeError:
    app.append(None)
    pass
try:
    app.append(Config.APP_NAME5)
except AttributeError:
    app.append(None)
    pass
try:
    app.append(Config.APP_NAME6)
except AttributeError:
    app.append(None)
    pass
try:
    app.append(Config.APP_NAME7)
except AttributeError:
    app.append(None)
    pass
try:
    app.append(Config.APP_NAME8)
except AttributeError:
    app.append(None)
    pass
try:
    app.append(Config.APP_NAME9)
except AttributeError:
    app.append(None)
    pass

# Always for safety XD
app.append(None)



h_conn = []
try:
    h_conn.append(heroku3.from_key(Config.API_KEY0))
except AttributeError:
    pass
try:
    h_conn.append(heroku3.from_key(Config.API_KEY1))
except AttributeError:
    pass
try:
    h_conn.append(heroku3.from_key(Config.API_KEY2))
except AttributeError:
    pass
try:
    h_conn.append(heroku3.from_key(Config.API_KEY3))
except AttributeError:
    pass
try:
    h_conn.append(heroku3.from_key(Config.API_KEY4))
except AttributeError:
    pass
try:
    h_conn.append(heroku3.from_key(Config.API_KEY5))
except AttributeError:
    pass
try:
    h_conn.append(heroku3.from_key(Config.API_KEY6))
except AttributeError:
    pass
try:
    h_conn.append(heroku3.from_key(Config.API_KEY7))
except AttributeError:
    pass
try:
    h_conn.append(heroku3.from_key(Config.API_KEY8))
except AttributeError:
    pass
try:
    h_conn.append(heroku3.from_key(Config.API_KEY9))
except AttributeError:
    pass

# Always for safety XD
h_conn.append(None) 