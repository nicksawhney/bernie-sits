import requests 
from typing import Union
import cv2
import numpy as np
from io import BytesIO
from sign import sign_url
import os
import argparse


BERNIE = cv2.imread('bernie.png', -1)

API_URL = 'https://maps.googleapis.com/maps/api/streetview'
KEY = os.environ['KEY']
SECRET = os.environ['SECRET']

def get_image(location : Union[str, tuple, int], sign=True):
	'''
	Gets image from `location` in the google street view API
	
	returns: bytesarray representing google maps jpg
	'''

	if type(location) is int:
		loc_param = 'pano'

	else:
		loc_param = 'location'

	s = requests.Session()
	r = requests.Request('GET', API_URL, params={loc_param: location, 'size': '640x640', 'key': KEY}).prepare()

	print(f'requesting from {r.url}')

	if sign:
		url = sign_url(input_url=r.url, secret=SECRET)

	else:
		url = r.url

	resp = requests.get(url)

	print(resp.status_code)

	return resp.content


def add_bernie(img_bytes, y_off=330, x_off=400):
	'''
	adds bernie to an image (defaults to offset in original bernie-sits app)
	params:
		img_bytes: a bytearray representing a jpg image of sixe 
		x_off: bernie's x offset from left
		y_off: bernie's y offset from top 

	returns: 
	'''
	l_img = np.asarray(bytearray(img_bytes), dtype='uint8')
	l_img = cv2.imdecode(l_img, cv2.IMREAD_COLOR)

	y_offset = y_off
	x_offset = x_off

	s_img = BERNIE

	y1, y2 = y_offset, y_offset + s_img.shape[0]
	x1, x2 = x_offset, x_offset + s_img.shape[1]

	alpha_s = s_img[:, :, 3] / 255.0
	alpha_l = 1.0 - alpha_s

	for c in range(0, 3):
	    l_img[y1:y2, x1:x2, c] = (alpha_s * s_img[:, :, c] +
	                              alpha_l * l_img[y1:y2, x1:x2, c])

	is_success, encoded_bytes = cv2.imencode('.jpeg', l_img)

	img_buf = BytesIO(encoded_bytes)
	img_buf.seek(0)

	return img_buf


if __name__ == '__main__':
	parser = argparse.ArgumentParser(
		description='Adds bernie to a google maps address, as seen in bernie sits'
		'Ensure API_URL, KEY, and if needed SECRET are environment variables')

	parser.add_argument('fname', type=str, help='The filename for the bernie image (jpeg)')
	parser.add_argument('location', type=str, help='The address to put bernie in front of')
	parser.add_argument('-s', '--sign', type=bool, default=True, help='Whether or not to sign the url')

	args = parser.parse_args()

	
	maps_image = get_image(args.location, sign=args.sign)
	bernie_image = add_bernie(maps_image)

	with open(args.fname, 'wb+') as f:
		f.write(bernie_image.read())
