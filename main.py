#!/usr/bin/env python3
#coding: utf-8

from datetime import datetime
import MySQLdb
import bme280
import config

if __name__ == '__main__':
    temp, pres, hum = bme280.getData()

    query = """INSERT INTO environment_data
            (time_at, temperature, humidity, pressure)
            VALUES ('{time:}', {temp:}, {hum:}, {pres:})"""

    connection = MySQLdb.connect(
            host=config.DB_ADDR,
            port=config.DB_PORT,
            user=config.DB_USER,
            passwd=config.DB_PASSWD),
            db=config.DB_NAME,
            charset='utf8')
    cursor = connection.cursor()
    cursor.execute(query.format(
        time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        temp=temp, hum=hum, pres=pres))
    connection.commit()
    connection.close()

