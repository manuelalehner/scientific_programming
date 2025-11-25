""" Scintific Programming - Assignmnt 04

    Manuela Lehner, University of Innsbruck
"""

import os
import sys
from datetime import datetime

import requests
import pandas as pd
import matplotlib.pyplot as plt
from ipdb import set_trace as bp

# GeoSphere Austria Data Hub API endpoint
# <host>/<version>/<type>/<mode>/<resource_id>
host = 'https://dataset.api.hub.geosphere.at'
version = 'v1'
datatype = 'station'
resource_id = 'tawes-v1-10min'


def download_tawes(param, station_id, start=None, end=None):
    ''' download data from GeoSphere Austria Data Hub

    Parameters
    ----------
    param: str
        parameter to extract
    station_id: integer
        station ID (synop station id)
    start: str
        start date and time for historical data (YYYY-mm-ddTHH:MM)
    end: str
        end date and time for historical data (YYYY-mm-ddTHH:MM)

    Returns
    -------
    response.json(): dict
        json object containing retrieved data
    '''

    try:
        # if start date is provided download historical data, otherwise current
        if start is None:
            endpoint = f'{host}/{version}/{datatype}/current/{resource_id}'
            response = requests.get(
                endpoint, params={'parameters':param, 'station_ids':station_id})
        else:
            endpoint = f'{host}/{version}/{datatype}/historical/{resource_id}'
            response = requests.get(
                endpoint, params={'parameters':param, 'station_ids':station_id,
                'start':start, 'end':end})

        # status code 200 means that the download was succssful
        if response.status_code == 200:
            print('Data downloaded successfully')
        else:
            print(f'Data download error {data.status_code}')
    except:
        raise RuntimeError('Data download failed')

    return response.json()


def print_to_terminal(data):
    ''' print current data point to the terminal

    Parameters
    ----------
    data: dict
        json object downloaded from the API
    '''
    
    # extract information from the nested json object
    station = data['features'][0]['properties']['station']
    coords = data['features'][0]['geometry']['coordinates']
    time = datetime.fromisoformat(data['timestamps'][0])
    param = list(data['features'][0]['properties']['parameters'].keys())[0]
    name = data['features'][0]['properties']['parameters'][param]['name']
    value = data['features'][0]['properties']['parameters'][param]['data'][0]
    units = data['features'][0]['properties']['parameters'][param]['unit']

    # print current value to the terminal
    print('\n')
    print(f'Current ({time:%d %b %Y %H:%M} UTC) {name} at station ' +
          f'{station} ({coords[0]:.2f} E, {coords[1]:.2f} N):')
    print(f'{value} {units}')


def save_to_csv(data, output_dir):
    ''' save time series to csv file

    Parameters
    ----------
    data: dict
        json object downloaded from the API
    output_dir: str
        directory where csv file will be stored

    Returns
    -------
    ds: pandas series
        data timeseries
    '''

    # extract information from the nested json object
    station = data['features'][0]['properties']['station']
    time = data['timestamps']
    param = list(data['features'][0]['properties']['parameters'].keys())[0]
    value = data['features'][0]['properties']['parameters'][param]['data']

    # save timeseries to csv file (using pandas dataframe)
    datafile = os.path.join(output_dir, f'{param}_{station}.csv')
    ds = pd.Series(index=time, name=param, data=value)
    ds.to_csv(datafile, header=False)
    print(f'Data saved successfully to {datafile}')

    return ds


def plot_timeseries(data, output_dir):
    ''' plot timeseries and save plot

    Parameters
    ----------
    data: pandas series
        data timeseries to be plotted
    output_dir: str
        directory where plot will be saved (png)
    '''
    
    fig, ax = plt.subplots(figsize=(15,4), nrows=1, ncols=1)
    ax.plot(pd.to_datetime(data.index), data)
    ax.set_ylabel(data.name)

    plotfile = os.path.join(output_dir, f'{data.name}.png')
    fig.savefig(plotfile)
    plt.close()
    print(f'Plot saved successfully to {plotfile}')
   

def check_date_time(datestrings):
    '''check that the provided datestrings have the format YYYY-mm-dd HH:MM'''

    for datestring in datestrings:
        if ((datestring[4] != '-') or (datestring[7] != '-') or 
            (datestring[10] != ' ') or (datestring[13] != ':')):
            raise ValueError('Start and end dates must conform to the format YYYY-mm-dd HH:MM')


# ----- MAIN FUNCTION -----
def main(api_args, *, output_dir='./', create_plot=False):
    ''' download current or historical TAWES data from the GeoSphere Austria Data Hub
        and print data to screen or save to file

    Parameters
    ----------
    api_args: list (str)
        mandatory: parameter to download, station id
        optional: start and end date/time
    output_dir: str
        directory for saving historical data file and plot
    create_plot: bool
    '''

    # check that start and end date/time are formatted correctly
    if len(api_args) == 4:
        check_date_time(api_args[2:])

    # download TAWES data from the Data Hub
    data = download_tawes(*api_args)

    # print current data point to the terminal
    if len(api_args) == 2:
        print_to_terminal(data)
    # save time series to file
    else:
        ds = save_to_csv(data, output_dir)
        if create_plot:
            plot_timeseries(ds, output_dir)


if __name__ == '__main__':
    args = sys.argv[1:]

    # default output directory: './'
    if '--output_dir' in args:
        output_dir = args.pop(args.index('--output_dir') + 1)
        if not os.path.isdir(output_dir):
            raise NotADirectoryError('Output directory does not exist. Exiting')
        args.remove('--output_dir')
    else:
        output_dir = './'

    # default: no plot
    if '--create_plot' in args:
        create_plot = True
        args.remove('--create_plot')
    else:
        create_plot = False

    if len(args) not in (2, 4):
        print('Correct use of download_geosphere_tawes: \n')
        print('Download current data:')
        print('download_geosphere_tawes parameter station_id \n')
        print('Download historical time series:')
        print('download_geosphere_tawes parameter station_id ' +
              'start (YYYY-MM-DDThh:mm) end (YYYY-MM-DDThh:mm)')
        sys.exit()

    main(args, output_dir=output_dir, create_plot=create_plot)
