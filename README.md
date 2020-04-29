# TD Reply Engineer Take Home challenge Solution

I have provided two distinct solutions for the task
- Scraping AWS s3 website to get the api url link and implement the ETL pipelines to store the data in the database
- Scraping Public API website to get the api url link for Covid19 data and make the API call to get the data in json
- The CovidApi data was choosen because of the insightful impact of businesses accross the globe 


### The Docker-based Database part:
- Ensure that docker(docker-compose or docker desktop) is installed on your system
- Go into the `/dags` directory and run `runs.sh` to install the required packages
- Go into the solution directory and run `start.sh` to spin up the containers
- Postgres Database Instance is used.
- Go to `localhost:5050` to access the pgadmin page
- pgamin `username`: samuelolle@yahoo.com
- pgadmin `password`: leicester


### Database Configuration Include using pgadmin:
- `hostname`: sourcedb
- `Maintenance Database`: sourcedb
- `username`: sourcedb
- `password`: solution
- `port`: 5432


### The Python part:
- Ensure that docker(docker-compose or docker desktop) is installed on your system
- Go into the `/dags` directory and run `etl_for_s3_data.py`, `test_scraper.py`,`test_Covid19APICall.py` for the testcases
- run only each function in `etl_for_s3_data.py` not to wait too long for result.
- `test_scraper.py` is a basic web crawler
- The `config.py` contains the basic variable configurations. Alternative is `environs` package


### Solution contains Nine python files:
- `main_etl_for_s3_data.py`,  `etl_for_s3_data.py`, `test_etl_for_s3_data.py`
- `main_scraper.py`, `scraper.py`, `test_scraper.py`, 
- `covid19apicall.py`,`test_Covid19APICall.py`, 
- `config.py`


