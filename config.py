import sys
import os 
import configparser 
import browser_cookie3 

parser = configparser.ConfigParser(interpolation=None) 
fullpath = os.path.expanduser("~/.config/kaizoku.conf") 

def parse_conf(): 

    if os.path.exists(fullpath): 
        parser.read(fullpath) 
        session_id = parser.get('kaizoku', 'session_id') 

        return session_id 
    
    print("Manually enter session id or import using --cookies-from-browser") 
    session_id = input("Enter instagram session id: ") 

    if session_id: 
        parser['kaizoku'] = { 
                'session_id': session_id,
                }

    with open(fullpath,'w') as f: 
        parser.write(f) 

    return session_id 

def get_cookies(browser):
    
    if browser == "chrome": 
        cookies = browser_cookie3.chrome(domain_name='.instagram.com')
    
    elif browser == "vivaldi": 
        cookies = browser_cookie3.vivaldi(domain_name='.instagram.com')

    elif browser == "firefox": 
        cookies = browser_cookie3.firefox(domain_name='.instagram.com')
        
        session_id = "" 

        for cookie in cookies:
            if cookie.name == "sessionid":
                session_id = cookie.value
                
        if session_id: 
            parser['kaizoku'] = { 
                    'session_id': session_id,
                    }

        with open(fullpath,'w') as f: 
            parser.write(f) 

        return session_id 

