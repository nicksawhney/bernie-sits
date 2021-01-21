from flask import Flask, render_template, url_for, request
from flask.json import jsonify
import base64
import cv2
import io
import os

from images import *


app = Flask(__name__)

@app.route('/', methods=['post', 'get'])
def login():
	if request.method == 'POST':
		location = request.form.get('address/location')
		if location.strip() != '':
			img_bytes = get_image(location)
			if not img_bytes:
				return render_template('index.html', image=False, location = False)

			image = add_bernie(img_bytes)
		else:
			return render_template('index.html', image=False, location = False)

		with open('img.jpeg', 'wb+') as f:
			f.write(image.read())
			image.seek(0)

		print(type(image))
		img_url = base64.b64encode(image.getvalue())

		# print(img_url)
		return render_template('index.html', image=img_url.decode('utf-8'), location=location)

	#GET Request Response
	return render_template('index.html', image=False, location = False)

if __name__ == '__main__':
	app.run(debug=True)