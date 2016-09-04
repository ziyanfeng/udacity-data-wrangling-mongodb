# -*- coding: utf-8 -*-

"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data"


def open_zip(data_file):
    with ZipFile('{0}.zip'.format(data_file), 'r') as myzip:
        myzip.extractall()


def parse_file(data_file):
    workbook = xlrd.open_workbook('{0}.xls'.format(data_file))
    sheet = workbook.sheet_by_index(0)

    # example on how you can get the data
    sheet_data = [[sheet.cell_value(rowi, coli) for coli in range(sheet.ncols)] for rowi in range(sheet.nrows)]

    # other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    # print "Number of rows in the sheet:",
    # print sheet.nrows
    # print "Type of data in cell (row 3, col 2):",
    # print sheet.cell_type(3, 2)
    # print "Value in cell (row 3, col 2):",
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3, from rows 1-3:"
    # print sheet.col_values(3, start_rowx=1, end_rowx=4)

    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):",
    # print sheet.cell_type(1, 0)
    # exceltime = sheet.cell_value(1, 0)
    # print "Time in Excel format:",
    # print exceltime
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)

    data = {
            'maxvalue': 0,
            'minvalue': 0,
            'avgcoast': 0,
            'maxtime': (0, 0, 0, 0, 0, 0),
            'mintime': (0, 0, 0, 0, 0, 0)
    }

    coastvalues = [sheet_data[r][1] for r in range(1, len(sheet_data))]  # COAST value is in column 1
    data["maxvalue"] = max(coastvalues)
    data["minvalue"] = min(coastvalues)
    data["avgcoast"] = sum(coastvalues) / float(len(coastvalues))

    exceltimes = [sheet_data[r][0] for r in range(1, len(sheet_data))]  # time value is in column 0
    data["maxtime"] = xlrd.xldate_as_tuple(exceltimes[coastvalues.index(max(coastvalues))], 0)
    data["mintime"] = xlrd.xldate_as_tuple(exceltimes[coastvalues.index(min(coastvalues))], 0)

    return data


def test():
    open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()
