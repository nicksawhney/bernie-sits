# Bernie In Places

An app that accidentally went viral! [Read the story in WIRED here](https://www.wired.com/story/bernie-sanders-meme-street-view-site/)

## Install 

First, create a pythin virtual environment, and install all of the depenedencies. 
```
python3 -m venv ve
source ve/bin/activate
pip install -r requirements.txt
```

Next, create a google cloud platform project with Street View Static API access (you will need a credit card to set this up)

https://console.cloud.google.com/apis/library/street-view-image-backend.googleapis.com

Set the following environment variables by adding the following lines to your `.bash_profile`, `.zshrc`, etc:
```
export API_URL='https://maps.googleapis.com/maps/api/streetview'
export KEY='YOUR-MAPS-STREETVIEW-KEY'
export SECRET='YOUR-GOOGLE-SECRET'
```

You might want to rename the variables to not conflict with existing ones.

## Running 

To run the web application locally
```
flask run
```
and, visit http://localhost:5000

For production deployment, I used [gunicorn](https://gunicorn.org/). 

Since the site is down now, you can also use `images.py` as a command-line bernie meme creation tool with
```
python images.py 'FILENAME.jpg' 'LOCATION'
```

`Procfile` and `Aptfile` are required to deploy with [Heroku](https://heroku.com/)

## Contribute!
PRs and issues welcome!

Please do not deploy without my permission!

## Licensing
This project will be licensed under the GNU General Public License (TODO: add licensing details)

## THANKS
This has been insane. 9,849,938 Bernie memes were created during the lifetime of this site! 