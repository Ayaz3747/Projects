from urllib.request import urlopen 
from urllib.parse import urlencode
from re import search
import sys
import datetime
import time
def h():
    
    html = urlopen("http://cbseresults.nic.in/")
    find = html.read().decode()
    match = search (r'<b>Likely to be announced on 30<sup>th</sup> May 2019</B></font></font>',find)
    if match:
        res="Not declared"
    else:
        
            res= "Result declared"
    rees="Checking result status..."
    sys.stdout.write("\r[*]"+rees)

    time.sleep(5)
    sys.stdout.flush()
    sys.stdout.write("\rStatus on "+str(datetime.datetime.now())+" : "+res)
    sys.stdout.flush()
    print("")
    h()
h()