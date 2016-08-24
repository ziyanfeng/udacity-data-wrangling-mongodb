#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up.

If you look at the full city data, you will notice that there are couple of
values that seem to provide the same information in different formats: "point"
seems to be the combination of "wgs84_pos#lat" and "wgs84_pos#long". However,
we do not know if that is the case and should check if they are equivalent.

Finish the function check_loc(). It will recieve 3 strings: first, the combined
value of "point" followed by the separate "wgs84_pos#" values. You have to
extract the lat and long values from the "point" argument and compare them to
the "wgs84_pos# values, returning True or False.

Note that you do not have to fix the values, only determine if they are
consistent. To fix them in this case you would need more information. Feel free
to discuss possible strategies for fixing this on the discussion forum.

The rest of the code is just an example on how this function can be used.
Changes to "process_file" function will not be taken into account for grading.
"""

import csv

CITIES = 'cities.csv'


def check_loc(point, lat, longi):
    # YOUR CODE HERE
    coordinates = point.split(' ')
    return coordinates[0] == lat and coordinates[1] == longi


def process_file(filename):
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        # skipping the extra matadata
        for i in range(3):
            reader.next()
        # processing file
        for line in reader:
            # calling your function to check the location
            result = check_loc(line["point"], line["wgs84_pos#lat"], line["wgs84_pos#long"])
            if not result:
                print "{}: {} != {} {}".format(line["name"], line["point"], line["wgs84_pos#lat"],
                                               line["wgs84_pos#long"])
            data.append(line)

    return data


def test():
    assert check_loc("33.08 75.28", "33.08", "75.28") is True
    assert check_loc("44.57833333333333 -91.21833333333333", "44.5783", "-91.2183") is False


if __name__ == "__main__":
    test()
