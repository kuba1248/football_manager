from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserDetails(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	balance = models.DecimalField(max_digits=16, default=100000, decimal_places=2)
	cellphone = models.CharField(max_length=14)
	address = models.CharField(max_length=255)
	town = models.CharField(max_length=45)
	post_code = models.CharField(max_length=45)
	country = models.CharField(max_length=45)

	def __str__(self):
		user = User.objects.get(id=self.user_id)
		return "id=" + str(self.pk) + " username=" + user.username + " email=" + user.email

class Product(models.Model):
	CATEGORIES = (
		('LAP', 'Laptop'),
		('CON', 'Console'),
		('GAD', 'Gadget'),
		('GAM', 'Game'),
		('TEL', 'TV'),
		('legend', 'legend'),
		('superstar', 'superstar'),
		('young', 'young'),
		('prof', 'prof'),
		('quick', 'quick'),
		('strong', 'strong')
	)
	
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to='images/')
	description = models.CharField(max_length=500)
	quantity = models.IntegerField()
	category = models.CharField(
		max_length=20,
		choices=CATEGORIES
	)
	date_posted = models.DateTimeField(auto_now_add=True, blank=True)
	
	def __str__(self):
		return "ID:" + str(self.pk) + " " + self.title

class Auction(models.Model):
	product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
	number_of_bids = models.IntegerField()
	time_starting = models.DateTimeField()
	time_ending = models.DateTimeField()
	
	def __str__(self):
		return "ID:" + str(self.pk) + " PRODUCT_ID:" + str(self.product_id)

class Watchlist(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
	
	def __str__(self):
		return "USER_ID:" + str(self.user_id) + " AUCTION_ID:" + str(self.auction_id)

class Bid(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
	bid_time = models.DateTimeField()
	
	def __str__(self):
		return "USER_ID:" + str(self.user_id) + " AUCTION_ID:" + \
			str(self.auction_id) + " " + str(self.bid_time) 

class Chat(models.Model):
	auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	message = models.TextField()
	time_sent = models.DateTimeField()

	def __str__(self):
		return "AUCTION_ID:" + str(self.auction_id) + " USER_ID:" + str(self.user_id)

