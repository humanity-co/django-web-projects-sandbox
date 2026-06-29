"""
This is the place where url pathes of individual apps are collected.
Note that in a single app there will be multiple routers for multiple views.
"""
#this module from ninja is used to collect all routers.
#note that every root will have url paths.
#  So this means if one app has 3 views then there will be 3 routes.
from ninja import NinjaAPI
#import routers from all the views.
from avapp.views.apiBranch import branchRouter
#initialise the app url collector.
api = NinjaAPI()
#In case of multiple apps, it is recommended to group urls of one app together.
#adding the first root from the only available app.

api.add_router("/branch/",branchRouter)
#add employee and customer etc after those views  are created.