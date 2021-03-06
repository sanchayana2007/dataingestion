import praw
import time
from datetime import datetime, timedelta
import csv
import sys
from genson import SchemaBuilder
import json

from configparser import ConfigParser
parser= ConfigParser()
parser.read('Config.ini')


#TODO : The schema definatiomn should have been agregated to a single place or file 
def schema_generator():
	 
        builder = SchemaBuilder()
		
        builder.add_schema({ "properties": {"Title": {"type": "string"},"Created": {"type": "date"},"Autor" : {"type": "string"}, "Score" : {"type": "integer"}, "id" : {"type": "string"},"Name" : {"type": "string"},"Comments" : {"type": "integer"},"votes" : {"type": "float"}}})
        builder.to_schema()
        #print(builder.to_json(indent=2))
        t= builder.to_json(indent=2)
        with open('versions/current_schema.json', 'w') as outfile:
            	json.dump(t,outfile)
                
#TODO : The schema definatiomn for BQ needs to pulled from  
        builderbq = SchemaBuilder()

        builderbq.add_schema({ "properties": {"Title": {"type": "STRING"},"Created": {"type": "DATE"},"Autor" : {"type": "STRING"}, "Score" : {"type": "INTEGER"}, "id" : {"type": "STRING"},"Name" : {"type": "STRING"},"Comments" : {"type": "INTEGER"},"votes" : {"type": "FLOAT"}}})
        

        builderbq.add_schema({ "order": {"Title": {"type": "1"},"Created": {"type": "2"},"Autor" : {"type": "3"}, "Score" : {"type": "4"}, "id" : {"type": "5"},"Name" : {"type": "6"},"Comments" : {"type": "7"},"votes" : {"type": "8"}}})

        builderbq.to_schema()
        #print(builder.to_json(indent=2))
        t= builderbq.to_json(indent=2)
        with open('versions/current_BQschema.json', 'w') as outfile:
                json.dump(t,outfile)
 
def write_csv(data):
	with open("versions/Reddit_data.csv","w",newline="") as csv_file:
		writer=csv.writer(csv_file)
		writer.writerows(data)




def connect_reddit():
	reddit = praw.Reddit(client_id=parser.get('REDDIT_DATA','client_id'),
                     client_secret=parser.get('REDDIT_DATA','client_secret'),
                     user_agent=parser.get('REDDIT_DATA','user_agent'),
                     username=parser.get('REDDIT_DATA','username'),
                     password=parser.get('REDDIT_DATA','password'))
                     		

	return reddit
        
def get_subredit(reddit ,reddit_subscribe,first=None):  
	output=[]      
	subreddit = reddit.subreddit(reddit_subscribe)

	print(subreddit.display_name)  
	output.append(["Title","Created","Autor","Score","id","Name","Comments","votes"])
	
  	# Output: redditdev
	if not first:
		print("Running the secondtime")	
		for  j,i in enumerate(subreddit.top('day')):
			print("Title",i.title)
			print("Created", datetime.utcfromtimestamp(int(i.created)).strftime('%Y-%m-%d'))
			print("Autor",i.author)
			print("Score",i.score)
			print("id",i.id)
			print("Name",i.name)
			print("Comments",i.num_comments)
			print("votes",i.upvote_ratio)
			output.append([i.title,datetime.utcfromtimestamp(int(i.created)).strftime('%Y-%m-%d'),i.author,i.score,i.id,i.name,i.num_comments,i.upvote_ratio])
			#Taken the first 10 items only 
			if j==9:
				break
		
							
	elif first=='first':


		t=reddit.subreddit(reddit_subscribe).top('month')
		#reddit.subreddit(reddit_subscribe).top('week')
		#t=reddit.redditor('dubai').top('month')
        	
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
		#break
	return output




if __name__=="__main__":
	
	reddit=connect_reddit()

	t=get_subredit(reddit ,'dubai')
	print(t)
	schema_generator()
	write_csv(t)	
