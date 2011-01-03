#!/opt/local/bin/python

import md5
import urllib
from xml.dom.minidom import parseString

api_key = "5e4b6063e4d98e5d017b6b043d840f6f"
secret = "1634a38450eb6d7383d5883a59b16e0f"

def gen_api_sig(args):
    sig_str = ""
    sig_str = ''.join([x + args[x] for x in sorted(args)])
    api_sig = md5.new(sig_str + secret).hexdigest()
    return api_sig

def call_method(args):
    args['format=json'] = api_key
    api_sig = gen_api_sig(args)
    args['api_sig'] = api_sig
    params = urllib.urlencode(args)
    f = urllib.urlopen("http://ws.audioscrobbler.com/2.0/", params)
    return f.read()
    
token_xml = call_method({'method' : 'auth.getToken'})
token_dom = parseString(token_xml)
token = token_dom.childNodes[0].childNodes[1].childNodes[0].nodeValue

# open up
# http://www.last.fm/api/auth?api_key=5e4b6063e4d98e5d017b6b043d840f6f&token=INSERTTOKENHERE

session_xml = call_method({'method' : 'auth.getSession', 'token' : token})
sesson_dom = parseString(session_xml)
key = \
    session_dom.childNodes[0].childNodes[1].childNodes[3].childNodes[0].nodeValue

tracks_2010 = call_method({'method' : 'user.getRecentTracks',
			   'sk' : key,
			   'user' : 'uberjoe',
			   'from' : str(time.mktime(start_of_2010)),
			   'to' : str(time.mktime(end_of_2010)),
			   'format' : 'json',
			   'limit' : '10000'}) 

json_2010 = json.loads(tracks_2010)


for track in json_2010['recenttracks']['track']:
    artist = track['artist']['#text']
    if artist in artist_2010:
            artist_2010[artist] += 1
    else:
            artist_2010[artist] = 1
