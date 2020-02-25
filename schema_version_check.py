from datetime import datetime, timedelta
from genson import SchemaBuilder
import json
import os
from os import path
import shutil
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
	
	oldschema="versions/old_schema.json"
	newschema="versions/new_schema.json"
	result=compare_schema(oldschema,newschema)
	if result:
		print("Same Schema")
		print("stating as Old schema version")
		 
	else:
		print("New schema version")
		print("Creating a new  schema version")
		# get the path to the file in the current directory
		
		# rename the original file
		versioned_schema="versions/schema" + datetime.now().strftime("%m_%d_%Y") + '.json'
		shutil.copy('versions/old_schema.json',versioned_schema) 
		shutil.copy('versions/new_schema.json','versions/old_schema.json') 

