# -*- coding: utf-8 -*-
"""
Created on Fri Sep 02 22:57:09 2016

@author: Oleksandr
"""
#import MySQLdb
import mysql.connector   
 
from mysql.connector import errorcode
import pymysql

class Database:
    
    def __init__(self):
        self.user = 'DBuser';
        self.password = '';
        self.host = '10.0.0.1';
        self.database = 'kmlserver';
        self.connection_open = False;
        self.cnx = "";
        self.cursor = "";
        self.ConnectToDB();
        self.started_tr = False;

    def CloseDB(self):
        if self.connection_open:       
            self.cursor.close();
            self.cnx.close();
            
    def ConnectToDB(self):
        if not self.connection_open:
            try :
                self.cnx = pymysql.connect(host=self.host,    # your host, usually localhost
                         user=self.user,         # your username
                         passwd= self.password,  # your password
                         db=self.database)        # name of the data base
                self.connection_open = True;
                self.cursor = self.cnx.cursor();
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                    return -1
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exists")
                    return -1
                else:
                    print(err)
                    return -1
                                        
    def LoadData(self, str_query): 
        check_query = str(str_query.upper());
        try:
            if "ROLLBACK" in check_query:
                if self.started_tr:
                    self.cnx.rollback();
                    self.cursor.close();
                    self.cursor = self.cnx.cursor();
                    self.started_tr = False;
                    print "TRANSACTION rollback"
                else:
                    print " transaction was not started";
                self.cursor = self.cnx.cursor();
            elif "START TRANSACTION" in check_query:
                if self.started_tr:
                    "print Transaction is already started";
                else:
                    self.cursor.close();
                    self.cursor = self.cnx.cursor();
                    self.started_tr = True;
                    print "TRANSACTION started"
            elif "COMMIT" in check_query:
                if self.started_tr:
                    self.cnx.commit();       
                    self.cursor.close();
                    self.cursor = self.cnx.cursor();
                    self.started_tr = False;
                    print "TRANSACTION commited";
                else:
                    "print Transaction was not started";
            elif "UPDATE" in check_query or "INSERT" in check_query:
                if self.started_tr:
                    self.cursor.execute(str_query);
                else:
                    self.cursor.execute(str_query);
                    self.cnx.commit();

            elif "SELECT" in check_query:

                self.cursor.execute(str_query);    
                result = []   
		num_fields = len(self.cursor.description)
		field_names = [i[0] for i in self.cursor.description]
                #print str(field_names);
                for value in self.cursor.fetchall():
                    #print value;
                    tmp = {};
		    		jj = 0;
                    for (index,column) in enumerate(value):                
                        #tmp['columns'[index][0]] = column
                        tmp[field_names[jj]] = column
						jj = jj + 1;
                        #print column;
                    result.append(tmp)
            else: 
                #print "something else called";
                self.cursor.execute(str_query);
                result = 1;
        except mysql.connector.Error as err:
            print "Except called";
            print "MySQL Error message:", err.msg       # error message
            result = - 1
        

        finally:
            #print "finally called";
            if 'result' in locals():
                return result
            else :
                return []
                
                
