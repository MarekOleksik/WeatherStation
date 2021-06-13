from __future__ import print_function

from mysql_connection import mydb
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
import mysql.connector
from bme280 import readBME280ID, readBME280All
import time


DB_NAME = 'SENSORS'

TABLES = {}
TABLES['PME280'] = (
    "CREATE TABLE `PME280` ("
    "  `Id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `date` datetime NOT NULL,"
    "  `sensor` varchar(8) NOT NULL,"
    "  `chipId` int(8) NOT NULL,"
    "  `version` int(4) NOT NULL,"
    "  `temperature` float(8) NOT NULL,"
    "  `pressure` float(8) NOT NULL,"
    "  `humidity` float(8) NOT NULL,"
    "  PRIMARY KEY (`Id`)"
    ") ENGINE=InnoDB")

cursor = mydb.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        mydb.database = DB_NAME
    else:
        print(err)
        exit(1)
        
for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()


def main():
    cursor = mydb.cursor()
  
    while True:
        timestamp = datetime.now()
        print("\n")
        print(timestamp)        

        (chip_id, chip_version) = readBME280ID()
        #print ("Chip ID     :", chip_id)
        #print ("Version     :", chip_version)

        temperature,pressure,humidity = readBME280All()

        print ("Temperature : ", temperature, "C")
        print ("Pressure : ", pressure, "hPa")
        print ("Humidity : ", humidity, "%")

        
        add_readings = ("INSERT INTO PME280 "
               "(date, sensor, chipId, version, temperature, pressure, humidity) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")
        readings = (timestamp, 'BME280', chip_id, chip_version, temperature, pressure, humidity)
  
        cursor.execute(add_readings, readings)
        mydb.commit()
        time.sleep(3600)


if __name__=="__main__":
   main()