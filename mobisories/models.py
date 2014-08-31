from django.db import models

# Create your models here.



class Product(models.Model):
	
	name = models.CharField(max_length=128)
	sku = models.CharField(max_length=128,null = True)
	quantity = models.IntegerField(max_length=128,null = True)
	picture = models.ImageField(upload_to='product_images', blank=True)


	def __unicode__(self):
		return self.name

ACTION_STATUS = (
	(1,'Post'),
	(2,'Like'),
	(3,'Share'),
	(4,'Reshare'),

)




class Entity(models.Model):
	name = models.CharField(max_length=128,null = True)
	username = models.CharField(max_length=128,null = True)
	password = models.CharField(max_length=128,null = True)
	email = models.CharField(max_length=128,null = True)
	no_follower = models.IntegerField(default=0,null = True)
	no_following = models.IntegerField(default=0,null = True)
	collections = models.ManyToManyField(Product, through = "Collection", related_name = "belongs_to",null = True)
	#followers = models.ForeignKey("self",related_name= "follower_list",null = True)
	relationships = models.ManyToManyField("self", through = "Relationship",related_name= "related_to",null = True,
											symmetrical=False)


	def __unicode__(self):
		return self.name

	#class Meta:
	#	abstract = True
RELATIONSHIP_FOLLOWING = 1
RELATIONSHIP_BLOCKED = 2
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_FOLLOWING, 'Following'),
    (RELATIONSHIP_BLOCKED, 'Blocked'),
)


class User(Entity):
	pass 

class Shop(Entity):
	
	url = models.URLField()
	address = models.CharField(max_length=128)


class Collection(models.Model):
	entity = models.ForeignKey(Entity,related_name = "entities")
	product = models.ForeignKey(Product,related_name = "products")
	action = models.IntegerField(choices = ACTION_STATUS)

class Relationship(models.Model):
	from_entity = models.ForeignKey(Entity,related_name = 'from_entities')
	to_entity = models.ForeignKey(Entity,related_name = 'to_entities')
	status = models.IntegerField(choices= RELATIONSHIP_STATUSES)





#class ProductAttributes(models.Model)	
#	attribute_category = models.CharField(max_length=128)
#	attribute_value = models.IntegerField(max_length=128)
