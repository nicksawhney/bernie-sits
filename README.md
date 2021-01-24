I'll flesh this out once i'm done stopping the site from crashing lol

To run, set the following environment variables
```
API_URL = 'https://maps.googleapis.com/maps/api/streetview'
KEY = 'YOUR-MAPS-STREETVIEW-KEY'
SECRET = 'YOUR-GOOGLE-SECRET'
```

You might wanna rename the variables to not conflict with existing ones.

## Running

Make sure to `pip install -r requirements.txt`

Use `python app.py` to run the flask application on `localhost:5000`to debug. 

For a production deployment. I used [gunicorn](https://gunicorn.org/). 


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