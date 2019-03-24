
## Gun Violence Data Preparation

1. **gun_violence_data_preparation.ipynb**

> Used for feature engineering and data cleanup

_Input:_
* Gun Violence Dataset from [Kaggle](https://www.kaggle.com/jameslko/gun-violence-data) 
* lat_long.csv 

_Output_
* gun-violence-data_01-2013_03-2018_cleaned.csv

_Note_
* Las Vegas shoting incident is added with incident_id "000000"
* Missing latitude and longitude information are updated using Geocoder.

2. **lat_long.csv**

> Contains latitude and longitude information fetched using [Geocoder using LocationIQ API](https://geocoder.readthedocs.io/providers/LocationIQ.html)

_Note_
* LOCATIONIQ_API_KEY is needed to fetch missing latitude and longitude information (if any). 
* LOCATIONIQ API has a limit of 10000 requests per day.

3. **app_choropleth.py**

> Dash app for generating choropleth across years.

_Input:_
* gun-violence-data_choropleth.csv

4. **app_scatter.py**

> Dash app for generating scatter plot across years.

_Input:_
* gun-violence-data_01-2013_03-2018_cleaned.csv

5. **gun_violence_data_preparation2.ipynb**

> Used for feature engineering needed for generating choropleth.

_Input:_
* gun-violence-data_01-2013_03-2018_cleaned.csv
* statecode.csv

_Output:_
gun-violence-data_choropleth.csv

6. **statecode.csv**

> Contains mapping information of state names to its correponding abbreviations.

Files from the DS side, visualizations, and zip files containing html articles and analysis with .png images
for static needs, with html images for interactive national level analysis

