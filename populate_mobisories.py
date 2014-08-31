import os 
def populate():
	print "test file first"

#def add_user
#
#def add_shop
#
#def add_product 
#
#def like_product 
#
#def post_product 


if __name__ == '__main__' : 
	print "Starting Mobisories Poulation script..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'm_project.settings')
	from mobisories.models import *
	populate()  