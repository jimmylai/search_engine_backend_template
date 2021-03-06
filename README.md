## LDSP: Search Engine Backend API Solution for fast prototyping
## LDSP = Linux + Django + Solr + Python

## Full Stack
### Solr: indexing + search
* pysolr: python interface for solr

### Django: backend API serving
* djangorestframework: Restful API
* fabric: automation

## Instructions
### Setup (for the first time)
1. Prepare Solr program and install Python packages
> fab setup_env

2. Create a new core in Solr (for the first time)
> fab create_core CORENAME

### Start Server
1. Start solr server
> fab run_solr

2. Start django server
> fab run_django

3. Feed the data (for the first time)
> fab feed_data

4. Enjoy the API!

### Tutorial:
* Example Dataset: Taiwan movie dataset http://data.gov.tw/node/7731
* Data source http://nrchbms.culture.tw/OpenData/API/iCultureAPI.aspx?type=26&radius=100&format=json
* The preprocessed data is in data/movie.json

>1. fab setup_env
>2. fab create_core movie
>3. fab run_solr
>4. fab feed_data:movie,data/movie
>5. fab run_django
