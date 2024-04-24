#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 02:12:13 2024

@author: jeremiahvelez_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS, HOST, PORT, DB, COL):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'AACUSER'
        #PASS = 'SNHU1234'
        #HOST = 'nv-desktop-services.apporto.com'
        #PORT = 30913
        #DB = 'AAC'
        #COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print ("CONNECTION SUCCESSFUL")

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary  
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            result = self.database.animals.find(data)
            return result
        else:
            return []
            raise Exception("Nothing to save, because data parameter is empty")
            
    def update (self, data, newData):
        total = self.database.animals.find(data).count()
        if data is not None:
            if total == 1:
                self.database.animals.update_one(data, newData)
            if total > 1:
                self.database.animals.update_many(data, newData)
            return total
    
    def delete(self, data):
        total = self.database.animals.find(data).count()
        if data is not None:
                if total == 1:
                     self.database.animals.delete_one(data)
                     return 1
                if total > 1:
                    self.database.animals.delete_many(data)
                    return total
            
            
            