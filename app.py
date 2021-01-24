from flask import Flask, render_template, url_for, request, Response
import base64
import cv2
import io
import os

from images import *


app = Flask(__name__)

@app.route('/', methods=['post', 'get'])
def login():
	location = ''
	if request.method == 'POST':
		location = request.form.get('address/location')
		img_bytes = get_image(location)
		image = add_bernie(img_bytes)

	if not location:
		return render_template('index.html', image=False, location=False)

	img_url = base64.b64encode(image.getvalue())

	return render_template('index.html', image=img_url.decode('utf-8'), location=location)

@app.route('/api', methods=['post'])
def post():
  location = request.form.get('address/location')
  image = get_image(location)

  return Response(image, mimetype='image/jpeg')

if __name__ == '__main__':
	app.run(debug=True)
