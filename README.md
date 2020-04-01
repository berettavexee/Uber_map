# Uber_map.py

Python script that produces an activity map using the CSV files provided by Uber as part of the GDPR access requests.
Fork of https://github.com/remisalmon/Strava-local-heatmap-browser version, modified to display UBER data

## Features

* Minimal Python dependencies ([folium](https://github.com/python-visualization/folium))
* Fast and dirty (3x faster than `gpxpy.parse()`)

## Usage

* Download your CSV files from Uber and add them to the `uber` folder  
* Run `python3 uber_map.py`

### Command-line options

```
usage: uber_map.py [-h] [--csv-dir DIR] [--csv-filter FILTER] [--output OUTPUT]

optional arguments:
  -h, --help           show this help message and exit
  --csv-dir DIR        directory containing the csv files (default: uber)
  --csv-filter FILTER  glob filter for the csv files (default: *.csv)
  --output OUTPUT      output HTML file (default: strava_local_heatmap.html)
```

## Python dependencies

```
python 3
folium==0.10.0

```