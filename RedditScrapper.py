import praw
import time
from datetime import datetime, timedelta
import csv
import sys
from genson import SchemaBuilder
import json


def schema_generator():
	 
        builder = SchemaBuilder()
	
        builder.add_schema({ "properties": {"Title": {"type": "string"},"Created": {"type": "date"},"Autor" : {"type": "string"}, "Score" : {"type": "integer"}, "id" : {"type": "string"},"Name" : {"type": "string"},"Comments" : {"type": "integer"},"votes" : {"type": "float"}}})
        builder.to_schema()
        #print(builder.to_json(indent=2))
        t= builder.to_json(indent=2)
        with open('versions/new_schema.json', 'w') as outfile:
            	json.dump(t,outfile)
        
      
def write_csv(data):
	with open("versions/Reddit_data.csv","w",newline="") as csv_file:
		writer=csv.writer(csv_file)
		writer.writerows(data)




def connect_reddit():

	reddit = praw.Reddit(client_id='p5j4n4TmOgoSZA',
                     client_secret='nYM3EikKA3Y0fpwQVUHxeabVeIE',
                     user_agent='my user agent',
                     username='AntiqueProject8',
                     password='786125qw')

	return reddit
        
def get_subredit(reddit ,reddit_subscribe,first):  
	output=[]      
	subreddit = reddit.subreddit(reddit_subscribe)

	print(subreddit.display_name)  
	output.append(["Title","Created","Autor","Score","id","Name","Comments","votes"])

  	# Output: redditdev
	'''
	for submission in subreddit.top(limit=10):
    		print(submission.title)  # Output: the submission's title
    		print(submission.score)  # Output: the submission's score
    		print(submission.id)     # Output: the submission's ID
    		print(submission.url)
	
	'''


	t=reddit.subreddit(reddit_subscribe).top('month')
	

	for i in t:
		#sprint(dir(i))
		print("Title",i.title)
		print("Created", datetime.utcfromtimestamp(int(i.created)).strftime('%Y-%m-%d'))
	
		print("Autor",i.author)
		print("Score",i.score)
		print("id",i.id)
		print("Name",i.name)
		print("Comments",i.num_comments)
		print("votes",i.upvote_ratio)
		output.append([i.title,datetime.utcfromtimestamp(int(i.created)).strftime('%Y-%m-%d'),i.author,i.score,i.id,i.name,i.num_comments,i.upvote_ratio])
		break
	
	return output




if __name__=="__main__":
	
	reddit=connect_reddit()

	t=get_subredit(reddit ,'dubai','first')
	print(t)
	schema_generator()
	write_csv(t)	
