#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Filename @  model.py
# Author   @  Tian
# Date     @  2016-08-21 01:28:03
# Email    @  qiaotian@me.com

import csv as csv
import numpy as np

csv_file_object = csv.reader(open('train.csv', 'rb'))
header = csv_file_object.next()

# create a list to hold all data 
data = []
for row in csv_file_object:
    data.append(row[0:])

# convert the list to numpy array
data = np.array(data)


