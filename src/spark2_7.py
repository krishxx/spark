# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 19:03:33 2018

@author: Srikrishna.Sadula
"""

from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf = conf)

lines = sc.textFile("D:\\projects\\machinelearning\\mltutor\\spark\\src\\readme.txt")
lines.first()
pythonLines = lines.filter(lambda line: "Python" in line)
pythonLines.first()

sc.stop()