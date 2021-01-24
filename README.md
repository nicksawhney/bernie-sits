# Bernie In Places

An app that accidentally went viral! [Read the story in WIRED here](https://www.wired.com/story/bernie-sanders-meme-street-view-site/)


## Running
Set the following environment variables by adding the following lines to your `.bash_profile`, `.zshrc`, etc:
```
export API_URL='https://maps.googleapis.com/maps/api/streetview'
export KEY='YOUR-MAPS-STREETVIEW-KEY'
export SECRET='YOUR-GOOGLE-SECRET'
```

You might want to rename the variables to not conflict with existing ones.

Make sure to `pip install -r requirements.txt`

Use `python app.py` to run the flask application on `localhost:5000`to debug. 

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