#!/usr/bin/python3
"""
MIT License

Copyright (c) 2019 Guiral Lacotte

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# imports
import re
import glob
import argparse
import webbrowser
from folium import Map, PolyLine, Marker
from folium.plugins import HeatMap

# constants

# functions

def build_map(data, segments):
    #Build and display Folium map
    html_file = args.output
    # color map for heatmap plugin 
    heatmap_grad = \
    {0.0: '#000004',
     0.1: '#160b39',
     0.2: '#420a68',
     0.3: '#6a176e',
     0.4: '#932667',
     0.5: '#bc3754',
     0.6: '#dd513a',
     0.7: '#f37819',
     0.8: '#fca50a',
     0.9: '#f6d746',
     1.0: '#fcffa4'}

    fmap = Map(tiles = 'CartoDB dark_matter', prefer_canvas = True, max_zoom = 16)

    # Individual coordonate as heatmap 
    HeatMap(data, radius = 5, blur = 5, gradient = heatmap_grad, max_zoom = 19).add_to(fmap)
    
    # Trace the trip as polyline 
    for segment in segments:
        PolyLine(locations=segment, weight=5, color = '#FFC300', opacity = 0.6).add_to(fmap)

    # Set map bounds 
    fmap.fit_bounds(fmap.get_bounds())

    # save map to HTML file and open with browser
    print('writing '+html_file+'...')
    fmap.save(html_file)
    webbrowser.open(html_file, new = 2, autoraise = True)
    print('done')
    return (None)

def open_csv_files(files):
	# open gpx files and extract tracks
	# Done with RegEx, dirty but 3 times faster than Lxml 
    data = []
    segments = []
    for file in files:
        print('reading :'+file+'...')
        with open(file, 'r') as filehandler:
            # Open a file 
            for line in filehandler:
                #Search for coordonates
                tmp = re.findall('[-]*[0-9]{1,2}[.][0-9]{4,}',line)
                if tmp:
                    if len(tmp) == 2: # 1 coordonate it is point  
                        data.append([float(tmp[0]), float(tmp[1])])
                    if len(tmp) == 4: # 2 coordonate it is a trip
                        segments.append([[float(tmp[0]), float(tmp[1])],[float(tmp[2]), float(tmp[3])]])     
    print('Trackpoints:', len(data), 'trackpoints')
    print('Segments:', len(segments), 'trips')
    return(data, segments)

def main(args):
    # arguments
    csv_dir = args.dir
    csv_filter = args.filter
    html_file = args.output

    # output file must be html
    if not html_file[-5:] == '.html':
        print('ERROR output file must be .html')
        quit()
    # parse GPX and Exiffiles
    csv_files = glob.glob(csv_dir+'/'+csv_filter)
    if not csv_files:
        print('ERROR no GPX files in '+csv_dir)
        quit()

    # We should be good with user input, now 
    data, segments = open_csv_files(csv_files)
    build_map(data, segments)
    return(None)

if __name__ == '__main__':
    # command line parameters
    parser = argparse.ArgumentParser(description = 'Generate a map based on Uber csv files')
    parser.add_argument('--csv-dir', dest = 'dir', default = 'uber', help = 'directory containing the csv files (default: uber)')
    parser.add_argument('--csv-filter', dest = 'filter', default = '*.csv', help = 'glob filter for the csv files (default: *.csv)')
    parser.add_argument('--output', dest = 'output', default = 'uber_map.html', help = 'output HTML file (default: uber_map.html)')
    args = parser.parse_args()
    # Main function 
    main(args)