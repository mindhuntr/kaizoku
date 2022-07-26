# kaizoku 

A command line tool which uses instagrapi to download instagram content 

## Dependencies
``` shell 
pip3 install -r requirements.txt 
``` 

## Installation 
``` shell 
git clone https://github.com/mindhuntr/kaizoku 
``` 

## Usage 

Display help: 
``` shell 
kaizoku --help 
``` 

Download video, image or caraousel: 
``` shell 
kaizoku https://instagram.com/p/Clpwjq
``` 

Download all stories from a user: 
``` shell 
kaizoku --get-all-stories lalo
``` 

Import cookies form browser (supports firefox,vivaldi,chrome) 
``` shell 
kaizoku --cookies-from-browser firefox 
``` 

Download first three posts from saved messages
``` shell 
kaizoku --saved 3 
``` 
