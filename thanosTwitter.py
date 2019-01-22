import tweepy
import random

# Enter the details from Twitter Dev Account
screen_name = 'xxxxxxxx'
consumer_key = 'xxxxxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxx'
access_token = 'xxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# List of people who follow me
friends =  api.friends_ids(screen_name)
noFriends = len(friends)

noToSnap = int(noFriends)/2

# Set a list for people getting snap
thanosSnap = []
counter = 0 

# Bring the number of people to snap to a full number
# so there isn't an error 
if noToSnap / 2 == 0:
    pass
else:
    noToSnap += .5

# Choose randomly from the friends list
# and add them to the snap list. At the
# same time removing the friend from the
# friends list so it doesn't double up
while counter != noToSnap: 
    snap = random.choice(friends)
    thanosSnap.append(snap)
    friends.remove(snap)
    counter += 1

# And then finally send the call to Twitter
# and remove the people you have followed
for i in thanosSnap:
    print("Unfollowing {0}".format(api.get_user(i).screen_name))
    api.destroy_friendship(i)
