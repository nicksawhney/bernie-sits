# Bernie In Places
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

An app that accidentally went viral! [Read the story in WIRED here](https://www.wired.com/story/bernie-sanders-meme-street-view-site/)

## Install 

First, setup the project and create a topic branch using "git clone" and "git checkout". More details can be found at [GitHub- Contributing to a project](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project).

Next up, create a python virtual environment, and install all of the dependencies. 
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

If you plan on exceeding the rate limits or call cap, make sure to sign the url with `-s` or `--sign` (this also happens by default). If you're just doing this for fun, or want to look at a request url without the signature, you can use `-n` or `--no-sign`.


`Procfile` and `Aptfile` are required to deploy with [Heroku](https://heroku.com/)

## Contribute!
I'd like to make a self-sustaining version of this site that automatically tracks crowdfunding vs api/other site costs and pulls core functionality when funding dips below cost, bringing it back when funding returns. [Check out the idea and contribute to the discussion!](https://github.com/nicksawhney/bernie-sits/issues/25) 

Also join me in [Discussions](https://github.com/nicksawhney/bernie-sits/discussions) to discuss the future of the site. We'll be maintaining an aesthetically and functionally identical version of the original viral site, and another souped-up version with all the features requested. Backend optimizations like caching can go in the original version. Still trying to decide which version should be `main`

PRs and issues welcome!

Please don't deploy without permission! I'm working on figuring out the proper licensing and attributions for others to be able to deploy.

## Licensing
This site is licensed under the [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html)

## THANKS
This has been insane. 9,849,938 Bernie memes were created during the lifetime of this site! 
