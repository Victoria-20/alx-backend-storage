#!/usr/bin/env python3
""" 8. List all documents in Python"""
import pymongo


def list_all(mongo_collection):
    """ lists all collections in mongoDB """
    if mongo_collection is None:
        return []
    list_doc = list(mongo_collection.find())
    return list_doc
