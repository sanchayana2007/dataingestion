from google.cloud import bigquery
import pprint
import json
client = bigquery.Client()
from datetime import datetime, timedelta
from genson import SchemaBuilder
types={"string":"STRING","integer":"INT64","date":"DATE","float":"FLOAT64"}
def get_BQtable_schema(dataset_id, table_id):
    """Get BigQuery Table Schema."""
    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset(dataset_id)
    bg_tableref = bigquery.table.TableReference(dataset_ref, table_id)
    bg_table = bigquery_client.get_table(bg_tableref)
    # Print Schema to Console
    pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(bg_table.schema)
    return bg_table.schema


def get_table_schema(schema):
    with open(schema) as json_file:
        json1_str = json_file.read()
        print("INtesr ",type(json1_str))
        data = json.loads(json1_str)
        data = json.loads(data)
        print("INtesr ",type(data))
        return data["properties"]

def match_schemas(BQschema,TablleSchema):
    #print(BQschema)
    for i in BQschema:
        print("ColumnName",i._name,"BQ SCHEMA",i.field_type,"Table type",str(TablleSchema[i._name]['type']))
        if str(i.field_type)==str(TablleSchema[i._name]['type']): 
            print("Matched")
        else:
            print("Not Matched")
#eastern-dream-261104:redditdata
bigqueryTableSchema = get_BQtable_schema("redditdata","data")	
tableschema=get_table_schema("versions/current_BQschema.json")
#eastern-dream-261104:redditdata.data
match_schemas(bigqueryTableSchema,tableschema)


#Implement rowise cjehecks 

