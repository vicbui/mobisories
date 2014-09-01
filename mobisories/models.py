from django.db import models

# Create your models here.



class Product(models.Model):
	
	name = models.CharField(max_length=128)
	sku = models.CharField(max_length=128,null = True)
	quantity = models.IntegerField(max_length=128,null = True)
	picture = models.ImageField(upload_to='product_images', blank=True)


	def get_collectors(self,action):
		r = self.belongs_to.filter(entities__action = action)
		return r 

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

	def add_relationship(self,entity,status):
		r = Relationship.objects.get_or_create(from_entity = self,to_entity= entity,status = status)[0]
		return r

	def remove_relationship(self,entity,status):
		r = Relationship.objects.get(from_entity = self,to_entity= entity,status = status)
		r.delete()
		return True 

	def get_following(self,status):
		r = self.relationships.filter(to_entities__status = status)
		return r 

	def get_follower(self,status):
		r = self.related_to.filter(from_entities__status = status)
		return r

	def add_collection(self,product,action):
		r = Collection.objects.get_or_create(entity = self, product = product,action = action)[0]
		return r 
	def remove_collection(self,product,status):
		r = Collection.objects.get_or_create(entity = self, product = product,action = action)[0]		
		r.delete()
		return True 

	def get_collection(self,status):
		r = self.collections.filter(products__action = status)
		return r 

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



