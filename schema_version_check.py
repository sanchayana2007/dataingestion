from datetime import datetime, timedelta
from genson import SchemaBuilder
import json
import os
from os import path
import shutil

from configparser import ConfigParser
parser= ConfigParser()
parser.read('Config.ini')


def compare_schema(oldschema,newschema):  
	with open(oldschema) as json_file:
		json1_str = json_file.read()
		print("INtesr ",type(json1_str))
		data = json.loads(json1_str)
		data = json.loads(data)
		print("INtesr ",type(data))
		builder1 = SchemaBuilder()
		builder1.add_schema(data)
        
	with open(newschema) as json_file:
		json1_str = json_file.read()
		print("INtesr ",type(json1_str))
		data = json.loads(json1_str)
		data = json.loads(data)
		print("INtesr ",type(data))
		builder = SchemaBuilder()
		builder.add_schema(data)

		if builder1== builder:
			return True
		else:
			return False

if __name__=="__main__":
	

	
	old_ver=parser.get('VERSION','version')
	versioned_schema="versions/olderschema/schema_v" + old_ver + '.json'
	oldschema=versioned_schema
	
	bqversioned_schema="versions/olderschema/BQschema_v" + old_ver + '.json'
	bqoldschema=bqversioned_schema
	newschema="versions/current_schema.json"
	print(oldschema,newschema)
	result=compare_schema(oldschema,newschema)
	
	if result:
		print("Same Schema")
		print("stating as Old schema version")
		shutil.copy('versions/Reddit_data.csv','versions/olderdata/Reddit_data'+datetime.now().strftime("%m_%d_%Y")+'v'+old_ver+'.csv') 
		 
	else:
		print("New schema version")
		new_ver=str(int(old_ver)+1)
		print("Creating a new  schema version",new_ver)
		# get the path to the file in the current directory
		# rename the original file
		#Update the version Info
		parser.set('VERSION','version',new_ver)
		with open('Config.ini','w') as f:
			parser.write(f)
		new_schema="versions/olderschema/schema_v" + new_ver + '.json'
		shutil.copy('versions/current_schema.json',new_schema) 
		shutil.copy('versions/Reddit_data.csv','versions/olderdata/Reddit_data'+datetime.now().strftime("%m_%d_%Y")+'v'+new_ver+'.csv') 
		
		bqnew_schema="versions/olderschema/BQschema_v" + new_ver + '.json'
		shutil.copy('versions/current_BQschema.json',new_schema) 
