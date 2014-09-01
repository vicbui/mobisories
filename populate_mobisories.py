import os 
def populate():
	u1 = User.objects.get_or_create(name = 'vic')[0]
	u2 = User.objects.get_or_create(name = 'vicbui')[0]

	s1 = Shop.objects.get_or_create(name = 'nike')[0]
	s2 = Shop.objects.get_or_create(name = 'addidas')[0]

	p1 = Product.objects.get_or_create(name = 'nike1')[0]
	p2 = Product.objects.get_or_create(name = 'nike2')[0]

	p3 = Product.objects.get_or_create(name = 'addidas1')[0]
	p4 = Product.objects.get_or_create(name = 'addidas2')[0]


	# shop posted 2 products
	s1.add_collection(p1,1)
	s1.add_collection(p2,1)
	s2.add_collection(p3,1)
	s2.add_collection(p4,1)

	# user follow shops 
	u1.add_relationship(s1,1)
	u1.add_relationship(s2,1)
	s1.add_relationship(s2,1)

	# user like products 
	u1.add_collection(p1,2)
	u1.add_collection(p3,2)

	# print all user and the products likes 
	for u in User.objects.all():
		print "User : {0} likes the following : \n".format(str(u.name))
		for p in u.get_collection(2):
			print "Product : {0}".format(str(p.name))


	print "End of populating"		


if __name__ == '__main__' : 
	print "Starting Mobisories Poulation script..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'm_project.settings')
	from mobisories.models import *
	populate()