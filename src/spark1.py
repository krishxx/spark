# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 19:03:33 2018

@author: Srikrishna.Sadula
"""

from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf = conf)

textFile = sc.read.text("readme.txt")
textFile.count()
textFile.first()
linesWithSpark = textFile.filter(textFile.value.contains("Spark"))
textFile.filter(textFile.value.contains("Spark")).count()  # How many lines contain "Spark"?
