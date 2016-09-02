#!/usr/bin/env python
"""
Write an aggregation query to answer this question:

Of the users in the "Brasilia" timezone who have tweeted 100 times or more,
who has the largest number of followers?

The following hints will help you solve this problem:
- Time zone is found in the "time_zone" field of the user object in each tweet.
- The number of tweets for each user is found in the "statuses_count" field.
  To access these fields you will need to use dot notation (from Lesson 4)
- Your aggregation query should return something like the following:
{u'ok': 1.0,
 u'result': [{u'_id': ObjectId('52fd2490bac3fa1975477702'),
                  u'followers': 2597,
                  u'screen_name': u'marbles',
                  u'tweets': 12334}]}
Note that you will need to create the fields 'followers', 'screen_name' and 'tweets'.

Please modify only the 'make_pipeline' function so that it creates and returns an aggregation
pipeline that can be passed to the MongoDB aggregate function. As in our examples in this lesson,
the aggregation pipeline should be a list of one or more dictionary objects.
Please review the lesson examples if you are unsure of the syntax.

Your code will be run against a MongoDB instance that we have provided. If you want to run this code
locally on your machine, you have to install MongoDB, download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials.

Please note that the dataset you are using here is a smaller version of the twitter dataset used
in examples in this lesson. If you attempt some of the same queries that we looked at in the lesson
examples, your results will be different.
"""


def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db


def make_pipeline():
    # complete the aggregation pipeline
    pipeline = []
    match = {'$match': {'user.time_zone': 'Brasilia',
                        'user.statuses_count': {'$gt': 100}}}
    pipeline.append(match)

    project = {'$project': {'followers': '$user.followers_count',
                            'screen_name': '$user.screen_name',
                            'tweets': '$user.statuses_count'}}
    pipeline.append(project)

    sort = {'$sort': {'followers': -1}}
    pipeline.append(sort)

    limit = {'$limit': 1}
    pipeline.append(limit)

    return pipeline


def aggregate(db, pipeline):
    return [doc for doc in db.tweets.aggregate(pipeline)]


if __name__ == '__main__':
    db = get_db('twitter')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint

    pprint.pprint(result)
    assert len(result) == 1
    assert result[0]["followers"] == 17209

