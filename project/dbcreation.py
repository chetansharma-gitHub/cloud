#!/usr/bin/python
import os
import MySQLdb as mariadb
mariadb_connection=mariadb.connect(user='root')
cursor=mariadb_connection.cursor()
a=[]
cursor.execute("create database cloudlogin")
cursor.execute("use cloudlogin")
cursor.execute("create table login(sno int(10) AUTO_INCREMENT ,name varchar(20) not null,userid varchar(30) not null,gender varchar(6) not null,email varchar(30) not null unique ,password varchar(30) not null ,phone_no varchar(10) not null UNIQUE,address varchar(50) not null,usertype varchar(10) not null, primary key(sno,userid) );")
cursor.execute("desc login")

for dbs in cursor:
	a=dbs
	print a



