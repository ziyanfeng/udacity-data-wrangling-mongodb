# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with another type of infobox data, audit it,
clean it, come up with a data model, insert it into MongoDB and then run some
queries against your database. The set contains data about Arachnid class.

For this exercise, the arachnid data is already in the database. You have been
given the task of including 'binomialAuthority' information in the records.
You will do this by processing the arachnid.csv to extract binomial authority
data and then using this data to update the corresponding data base records.

The following things should be done in the function add_field:
- process the csv file and extract 2 fields - 'rdf-schema#label' and
  'binomialAuthority_label'
- clean up the 'rdf-schema#label' the same way as in the first exercise,
  removing redundant "(spider)" suffixes
- return a dictionary with the cleaned 'rdf-schema#label' field values as keys,
  and 'binomialAuthority_label' field values as values
- if 'binomialAuthority_label' is "NULL" for a row in the csv, skip the item

The following should be done in the function update_db:
- query the 'label' field in the database using rdf-schema#label keys from the
  data dictionary
- update the documents by adding a new item under 'classification' with the key
  'binomialAuthority' and the binomialAuthority_label value from the data
  dictionary as the value

For item {'Argiope': 'Jill Ward'} in the data dictionary, the resulting document structure
should look like this:

{ 'label': 'Argiope',
  'uri': 'http://dbpedia.org/resource/Argiope_(spider)',
  'description': 'The genus Argiope includes rather large and spectacular spiders that often ...',
  'name': 'Argiope',
  'synonym': ["One", "Two"],
  'classification': {
                    'binomialAuthority' : 'Jill Ward'
                    'family': 'Orb-weaver spider',
                    'class': 'Arachnid',
                    'phylum': 'Arthropod',
                    'order': 'Spider',
                    'kingdom': 'Animal',
                    'genus': None
                    }
}

Note that the value in the 'binomialAuthority' field is a placeholder; this is only to
demonstrate the output structure form, for the entries that require updating.
"""
import csv
import pprint
import re

DATAFILE = 'arachnid.csv'
FIELDS = {'rdf-schema#label': 'label',
          'binomialAuthority_label': 'binomialAuthority'}


def add_field(filename, fields):
    """
    Complete this function to set up a dictionary for adding binomialAuthority
    information to the database.
    """
    process_fields = fields.keys()
    data = {}
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for i in range(3):
            reader.next()
        # YOUR CODE HERE
        for line in reader:
            if line['binomialAuthority_label'] != 'NULL':
                label = re.sub('\(.*?\)', '', line['rdf-schema#label']).strip()
                value = line['binomialAuthority_label']
                data[label] = value
    return data


def update_db(data, db):
    """
    Use the dictionary you generated from add_field to update the database.
    """
    # YOUR CODE HERE
    for key in data:
        db.arachnid.update({'label': key},
                           {"$set": {'classification.binomialAuthority':data[key]}}, multi=True)


def test():
    # Please change only the add_field and update_db functions!
    # Changes done to this function will not be taken into account
    # when doing a Test Run or Submit, they are just for your own reference
    # and as an example for running this code locally!

    data = add_field(DATAFILE, FIELDS)
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    update_db(data, db)

    updated = db.arachnid.find_one({'label': 'Opisthoncana'})
    assert updated['classification']['binomialAuthority'] == 'Embrik Strand'
    pprint.pprint(data)


if __name__ == "__main__":
    test()