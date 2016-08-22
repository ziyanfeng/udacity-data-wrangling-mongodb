#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Complete the 'extract_airports' function so that it returns a list of airport
codes, excluding any combinations like "All".
"""

from bs4 import BeautifulSoup
html_page = "options.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        for airport in soup.find(id="AirportList").find_all("option"):
            if len(airport['value']) == 3:
                if airport['value'] != 'All':
                    data.append(airport['value'])

    return data


def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

test()
