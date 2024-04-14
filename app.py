import requests
from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/aviationweather/<airport>')
def index(airport):
    re = requests.get("https://aviationweather.gov/cgi-bin/data/metar.php?ids=" + escape(airport))
    restext = re.text
    
    re1 = requests.get("https://aviationweather.gov/cgi-bin/data/taf.php?ids=" + escape(airport))
    restext1 = re1.text
    
    ret = restext + restext1;
    
    if len(restext) < 5:
        ret = "err"
    else:
        ret = restext + restext1
        
    return ret
