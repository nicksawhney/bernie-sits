from flask import Flask, render_template, url_for, request
from flask.json import jsonify
import base64
import cv2
import io


from images import *


app = Flask(__name__)

@app.route('/', methods=['post', 'get'])
def login():
	location = ''
	if request.method == 'POST':
		location = request.form.get('address/location')

		if not location:
			return render_template('index.html', image=False, location = False)

		img_bytes = get_image(location)
		image = add_bernie(img_bytes)

	if not image:
		return render_template('index.html', image=None, location=None)
		
	with open('img.jpeg', 'wb+') as f:
		f.write(image.read())
		image.seek(0)

	img_url = base64.b64encode(image.getvalue())

	return render_template('index.html', image=img_url.decode('utf-8'), location=location)

if __name__ == '__main__':
	app.run()