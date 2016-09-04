#!/usr/bin/python

"""
Find the time and value of max load for each of the regions
COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
and write the result out in a csv file, using pipe character | as the delimiter.

An example output can be seen in the "example.csv" file.
"""

import xlrd
import csv
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data"
outfile = "2013_Max_Loads.csv"


def open_zip(data_file):
    with ZipFile('{0}.zip'.format(data_file), 'r') as myzip:
        myzip.extractall()


def parse_file(data_file):
    workbook = xlrd.open_workbook('{0}.xls'.format(data_file))
    sheet = workbook.sheet_by_index(0)
    data = []
    # YOUR CODE HERE
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)
    header = ['Station', 'Year', 'Month', 'Day', 'Hour', 'Max Load']
    data.append(header)
    stations = sheet.row_values(0, start_colx=1, end_colx=9)
    for i in range(len(stations)):
        station_values = sheet.col_values(i + 1, start_rowx=1)
        max_row = station_values.index(max(station_values)) + 1
        Year, Month, Day, Hour, Minute, Second = xlrd.xldate_as_tuple(sheet.cell_value(max_row, 0), 0)
        data.append([stations[i], Year, Month, Day, Hour, max(station_values)])

    return data


def save_file(data, filename):
    # YOUR CODE HERE
    with open(filename, 'wb') as of:
        writer = csv.writer(of, delimiter='|')
        for row in data:
            writer.writerow(row)


def test():
    open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']

    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            station = line['Station']
            if station == 'FAR_WEST':
                for field in fields:
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        assert max_answer == max_line

                    # Otherwise check for equality
                    else:
                        assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        # Output should be 8 lines not including header
        assert number_of_rows == 8

        # Check Station Names
        assert set(stations) == set(correct_stations)


if __name__ == "__main__":
    test()
