import os


def get_path(dirname):
	files = os.listdir(dirname)
	for file in files:
		fullpath = os.path.abspath(os.path.join(dirname, file))
		print(fullpath)

get_path("/home/megazoid/Videos/")