from google.cloud import bigquery
import json
# Construct a BigQuery client object.

#create the Bigquery.dataset and dataset.table from the Bigquery webconsole dataset= 
#dataset.table= redditdata.data 


client = bigquery.Client()
def create_bq_schema():
    bqschema=[]
    bqtypes={"string":"STRING","integer":"INT64","date":"DATE","float":"FLOAT64"}
    with open("versions/new_schema.json") as json_file:
       json1_str = json_file.read()
       data = json.loads(json1_str)
       data = json.loads(data)
       print(data['properties'])
       for key,val in data['properties'].items():
          #print(key,val['type'])
          bqschema.append(bigquery.SchemaField(key, bqtypes[val['type']]))
       return bqschema  


# TODO(developer): Set table_id to the ID of the table to create.
table_id = "eastern-dream-261104.redditdata.data"
job_config = bigquery.LoadJobConfig()
#job_config.autodetect = True
#job_config.schema =create_bq_schema()
job_config.schema = [bigquery.SchemaField("Title", "STRING"),bigquery.SchemaField("Created", "DATE"),bigquery.SchemaField("Autor", "STRING"),bigquery.SchemaField("Score", "INT64"),bigquery.SchemaField("id", "STRING"),bigquery.SchemaField("Name", "STRING"),bigquery.SchemaField("Comments", "INT64"),bigquery.SchemaField("votes", "FLOAT64")]
job_config.skip_leading_rows = 1
job_config.source_format = bigquery.SourceFormat.CSV

uri = "gs://redditdubai-bucket-sanc/reddit_csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Wait for the job to complete.

table = client.get_table(table_id)
print("Loaded {} rows to table {}".format(table.num_rows, table_id))



