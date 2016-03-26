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

def alreadyInCollection(text):
    if db.twitter_query.find({'query': text}).count() > 0:
        return True
    else:
        return False

def getCommunityInfo(text):
    results_cursor = db.twitter_community.find({'query': text})
    for document in results_cursor:
        return document

def communityInfo(text,i):
    raw_result = getCommunityInfo(text)
    community_i = raw_result['communities'][i]
    result = {}
    result['size'] = len(community_i['screen_names'])
    result['words'] = community_i['words']
    return result

def communitySize(text, i):
    raw_result = getCommunityInfo(text)
    community_i = raw_result['communities'][i]
    result = len(community_i['screen_names'])
    return result

def communitySizePercent(text, i):
    comSize = communitySize(text, i)
    totalSize = communitySize(text, 0) + communitySize(text, 1) + communitySize(text, 2) + communitySize(text, 3)
    return format(comSize/float(totalSize) * 100, '.2f')

def communityWords(text, i):
    raw_result = getCommunityInfo(text)
    community_i = raw_result['communities'][i]
    return community_i['words'][:30]

#Download query result from Mongolab (replace collection by collection name before running)
#def downloadFromMongolab():
#    results = db.collection.find()
#    for result in results:
        #do whatever you need

#uploadJsonToMongolab("president2.json")
client.close()