# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 00:10:04 2016

@author: Oleksandr
"""
path = "/var/www/localhost/htdocs/";

def fopen(file_name, type_write):
    data = []
    data.append(path+file_name)
    data.append(type_write)
    return data
    
def fwrite(file_data, str_to_write):
    file_name = file_data[0]
    type_write = file_data[1]
    f = open(file_name, type_write)
    f.write(str_to_write)
    f.close()