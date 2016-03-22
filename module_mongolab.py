from pymongo import MongoClient
#import json

#import module_twitterscraping as twscrap

#Ouverture de la connexion Mongolab
client = MongoClient("mongodb://Thibaut:EnsaeTwitter16@ds055865.mlab.com:55865/ensae_twitter")
db = client.ensae_twitter

#Upload json file to the collection in MongoLab (replace collection by collection name before running)
def uploadToMongolab(text):
    line = {'query' : text, 'collected': False, 'community': False}
    if line != "\n":
      db.twitter_query.insert_one(line)

#Download query result from Mongolab (replace collection by collection name before running)
#def downloadFromMongolab():
#    results = db.collection.find()
#    for result in results:
        #do whatever you need

#uploadJsonToMongolab("president2.json")
client.close()