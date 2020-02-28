#!/bin/bash

echo "Starting Scrapping ****************"
python3.5  RedditScrapper.py
sleep(5)
echo " Scrapping Ends****************"
echo "Starting Data versioning****************"
python3.5  schema_version_check.py
sleep(5)
echo " Ends****************"
export GOOGLE_APPLICATION_CREDENTIALS="/home/san/Calloubroup/My First Project-43426c37fb15.json"

echo "Loading to GCP Buket ****************"
python3.5  Bucketloader.py
sleep(5)
echo " Loading Ends****************"
echo "Load data to BQ table ****************"
python3.5 LoadBuckettoBQ.py
sleep(5)
echo " Scrapping Ends****************"


