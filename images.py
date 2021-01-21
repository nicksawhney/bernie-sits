import requests 
from typing import Union
import cv2
import numpy as np
from io import BytesIO
from sign import sign_url
import os
# from config import *

BERNIE = cv2.imread('bernie.png', -1)

API_URL = os.environ['API_URL']
KEY = os.environ['KEY']
SECRET = os.environ['SECRET']

def get_image(location : Union[str, tuple, int]):
	'''
	Gets image from `location` in the google street view API
	'''

	if type(location) is int:
		loc_param = 'pano'

	else:
		loc_param = 'location'

	s = requests.Session()
	r = requests.Request('GET', API_URL, params={loc_param: location, 'size': '640x640', 'key': KEY}).prepare()
	print(r.url)

	# print(r.status_code)

	signed_url = sign_url(input_url = r.url, secret=SECRET)
	print(signed_url)

	resp = requests.get(signed_url)

	print(resp.status_code)

	return resp.content


def add_bernie(img_bytes):
	l_img = np.asarray(bytearray(img_bytes), dtype='uint8')
	l_img = cv2.imdecode(l_img, cv2.IMREAD_COLOR)

	y_offset = 330
	x_offset = 400

	s_img = BERNIE

	y1, y2 = y_offset, y_offset + s_img.shape[0]
	x1, x2 = x_offset, x_offset + s_img.shape[1]

	alpha_s = s_img[:, :, 3] / 255.0
	alpha_l = 1.0 - alpha_s

	for c in range(0, 3):
	    l_img[y1:y2, x1:x2, c] = (alpha_s * s_img[:, :, c] +
	                              alpha_l * l_img[y1:y2, x1:x2, c])

	is_success, encoded_bytes = cv2.imencode('.jpeg', l_img)

	print(is_success)

	img_buf = BytesIO(encoded_bytes)
	img_buf.seek(0)

	return img_buf

# filename = 'pikachu.png'
# ironman = Image.open(filename, 'r')
# filename1 = 'bg.png'
# bg = Image.open(filename1, 'r')
# text_img = Image.new('RGBA', (600,320), (0, 0, 0, 0))
# text_img.paste(bg, (0,0))
# text_img.paste(ironman, (0,0), mask=ironman)
# text_img.save("ball.png", format="png")

if __name__ == '__main__':
	loc = input('Enter an Address: ')

	get_image(loc)