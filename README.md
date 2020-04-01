# Uber_map.py

Python script to reproduce the Strava Global Heatmap ([www.strava.com/heatmap](https://www.strava.com/heatmap)) with Uber GDPR data.
Fork of https://github.com/remisalmon/Strava-local-heatmap-browser modify to display Uber trips.

## Features

* Minimal Python dependencies ([folium](https://github.com/python-visualization/folium))
* Fast and dirty (3x faster than `gpxpy.parse()`)

## Usage

* Download your CSV files from Uber and add them to the `uber` folder  
(see https://support.strava.com/hc/en-us/articles/216918437-Exporting-your-Data-and-Bulk-Export)
* Run `python3 uber_map.py`

### Command-line options

```
usage: uber_map.py [-h] [--csv-dir DIR]
                                       [--csv-filter FILTER] [--output OUTPUT]

optional arguments:
  -h, --help           show this help message and exit
  --csv-dir DIR        directory containing the csv files (default: csv)
  --csv-filter FILTER  glob filter for the csv files (default: *.csv)
  --output OUTPUT      output HTML file (default: strava_local_heatmap.html)
```

## Python dependencies

```
folium==0.10.0

```