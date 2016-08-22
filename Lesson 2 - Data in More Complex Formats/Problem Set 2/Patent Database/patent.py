#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This and the following exercise are using US Patent database. The patent.data
file is a small excerpt of much larger datafiles that are available for
download from US Patent website. These files are pretty large ( >100 MB each).
The original file is ~600MB large, you might not be able to open it in a text
editor.

The data itself is in XML, however there is a problem with how it's formatted.
Please run this script and observe the error. Then find the line that is
causing the error. You can do that by just looking at the datafile in the web
UI, or programmatically. For quiz purposes it does not matter, but as an
exercise we suggest that you try to do it programmatically.

NOTE: You do not need to correct the error - for now, just find where the error
is occurring.
"""

import xml.etree.ElementTree as ET

PATENTS = 'patent.data'


def get_root(fname):

    tree = ET.parse(fname)
    return tree.getroot()


get_root(PATENTS)


# Quiz: Result of Parsing the Datafile
# Please enter content of the line that is causing the error:
# line 657
# <?xml version="1.0" encoding="UTF-8"?>

# What do you think is the problem?
# multiple xml schema in the same file
