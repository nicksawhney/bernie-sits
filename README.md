I'll flesh this out once i'm done stopping the site from crashing lol

## Install 

First, create a pythin virtual environment, and install all of the depenedencies. 
```
python3 -m venv ve
source ve/bin/activate
pip install -r requirements.txt
```

Next, create a google cloud platform project with Street View Static API access (you will need a credit card to set this up)

https://console.cloud.google.com/apis/library/street-view-image-backend.googleapis.com

To run, set the following environment variables
```
API_URL = 'https://maps.googleapis.com/maps/api/streetview'
KEY = 'YOUR-MAPS-STREETVIEW-KEY'
SECRET = 'YOUR-GOOGLE-SECRET'
```

You might wanna rename the variables to not conflict with existing ones.

Since the site is down now, you can also use `images.py` as a command-line bernie meme creation tool with:
```
python images.py 'FILENAME.jpg' 'LOCATION'
```

Or, bring up the web application locally, and visit http://localhost:5000
```
flask run
```

## Contribute!
PRs and issues welcome!

Please do not deploy without my permission!

## Licensing
This project will be licensed under the GNU General Public License (TODO: add licensing details)

## THANKS
This has been insane. 9,849,938 Bernie memes were created during the lifetime of this site! 
