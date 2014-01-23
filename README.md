# Search Engine Backend Bootstrap

## Full Stack
### Solr: indexing + search
> pysolr: python interface for solr

### Django: backend API serving
> djangorestframework: Restful API
> fabric: automation

## Instructions
### Setup (for the first time)
1. Create a new collection (for the first time)
> fab create_core collection1

### Start Server
1. Start solr server
> fab start_solr

2. Start django server
> fab run_django

3. Feed the data (for the first time)
> fab feed_data

4. Enjoy the API

Example dataset:
http://data.gov.tw/node/7731
http://nrchbms.culture.tw/OpenData/API/iCultureAPI.aspx?type=26&radius=100&format=json

