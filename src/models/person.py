#!/usr/bin/python
# -*- coding: utf-8 -*-

from orator import Model
from orator.orm import has_many_through
from models.tweets_person import TweetsPerson
from models.tweet import Tweet

class Person(Model):
    pass

    #SELECT "tweets".*, "tweets_people"."PERSON_ID", "tweets".*, "tweets_people"."PERSON_ID" FROM
    #"tweets" INNER JOIN "tweets_people" ON "tweets_people"."TWEET_ID" = "tweets"."ID" WHERE "tweets_people"."PERSON_ID" = %s ([7]))
    @has_many_through(TweetsPerson, 'person_id', 'tweet_id')
    def tweets(self):
        return Tweet
