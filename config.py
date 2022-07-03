import sys
import os 
import configparser 

parser = configparser.ConfigParser(interpolation=None) 
fullpath = os.path.expanduser("~/.config/kaizoku.conf") 

def parse_conf(): 

    if os.path.exists(fullpath): 
        parser.read(fullpath) 
        session_id = parser.get('kaizoku', 'session_id') 

        return session_id 

    session_id = input("Enter instagram session id: ") 

    if session_id: 
        parser['kaizoku'] = { 
                'session_id': session_id,
                }

    with open(fullpath,'w') as f: 
        parser.write(f) 

    return session_id 
