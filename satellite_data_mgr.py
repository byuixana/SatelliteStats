"""Datatypes:
1. BLOB
2. TEXT
3. INTEGER
4. NULL
4. REAL"""

import sqlite3
import requests
from datetime import datetime
import json

connection = sqlite3.connect("starstats.db")

cursor = connection.cursor()

#ChatGPT taught me how to format the table creation.

cursor.execute("CREATE TABLE IF NOT EXISTS starlink_satellites("
               "date TEXT, "
               "name TEXT, "
               "epoch REAL, " 
               "mean_motion REAL, "
               "eccentricity REAL, "
               "inclination REAL, "
               "ra_of_aacending_node REAL, "
                "mm_rate_of_change REAL, "
                "mean_anomaly REAL, "
                "revolutions INTEGER)")

#Check if the table is empty.
cursor.execute(f"SELECT COUNT(*) FROM starlink_satellites")

current_rowcount = cursor.fetchone()[0]

#Check if the data has not been updated or the table is empty.
if current_rowcount <= 1:
    
        url = "https://celestrak.org/NORAD/elements/gp.php?INTDES=2020-025&FORMAT=JSON-PRETTY"

        response = requests.get(url)

        if response.status_code == 200:
            satellite_data = response.json()   
            for object in satellite_data:
                satellite_values = (datetime.now().date().strftime("%Y-%j"), object["OBJECT_NAME"], object["EPOCH"], object["MEAN_MOTION"], object["ECCENTRICITY"], object["INCLINATION"], object["RA_OF_ASC_NODE"], object["ARG_OF_PERICENTER"], object["MEAN_ANOMALY"], object["REV_AT_EPOCH"])

                cursor.execute("INSERT INTO starlink_satellites VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", satellite_values)

                connection.commit()
            
        #Updates cursor
        cursor.execute(f"SELECT COUNT(*) FROM starlink_satellites")
        current_rowcount = cursor.fetchone()[0]

        #How to select from a specific column
        #SELECT column_name FROM table_name WHERE condition;

if current_rowcount > 1:
    cursor.execute("SELECT date FROM starlink_satellites ORDER BY date DESC")

    most_recent_date = cursor.fetchone()

    if most_recent_date[0] != datetime.now().date().strftime("%Y-%j"):
        if response.status_code == 200:
            satellite_data = response.json()    
            for object in satellite_data:
                #name TEXT, epoch REAL, inclination REAL, ra_of_aacending_node REAL, mm_rate_of_change REAL, revolutions INTEGER, mean_motion REAL, mean_anomaly REAL, bstar REAL, eccentricity REAL
                satellite_values = (datetime.now().date().strftime("%Y-%j"), object["OBJECT_NAME"], object["EPOCH"], object["MEAN_MOTION"], object["ECCENTRICITY"], object["INCLINATION"], object["RA_OF_ASC_NODE"], object["ARG_OF_PERICENTER"], object["MEAN_ANOMALY"], object["REV_AT_EPOCH"],)

                cursor.execute("INSERT INTO starlink_satellites VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", satellite_values)

                connection.commit()

        else:
            print("Error")
    else: 
        print("Data is current.")

user_selection = 0

while user_selection != 6:

    menu = """Welcome to the Starlink Satellites Database! What would you like to do?
    1) Find a specific satellite
    2) Display all satellites
    3) Remove data
    4) Add a satellite
    5) List satellite epochs
    6) Close databse"""
    
    print(menu)

    user_selection = int(input("Selection:"))
    if user_selection != 6:

        if user_selection == 1:

            satellite_name = input("Satellite selection:")

            values = (satellite_name,)

            cursor.execute("SELECT * FROM starlink_satellites WHERE name = ?", values)

            satellite_record = cursor.fetchone()

            print(f"Title: {satellite_record[1]}, Epoch: {satellite_record[2]}, Revolution at Epoch: {satellite_record[9]}, Mean Motion: {satellite_record[4]}")

        elif user_selection == 2:

            cursor.execute("SELECT * FROM starlink_satellites ORDER BY name")

            records = cursor.fetchall()

            for satellite_record in records:
                print(f"Title: {satellite_record[1]}, Epoch: {satellite_record[2]}, Revolution at Epoch: {satellite_record[9]}, Mean Motion: {satellite_record[3]}")

        elif user_selection == 3:
            satellite_name = input("Enter satellite to remove: ")

            if cursor.rowcount == 0:
                print("ERROR! Satellite not in database.")

            values = (satellite_name,)

            cursor.execute("DELETE FROM starlink_satellites WHERE name = ?", values)

            connection.commit()

        elif user_selection == 4:
            #I asked for ChatGPT to autofll some values for user input.
            object = {
                "OBJECT_NAME": "STARLINK-1398",
                "EPOCH": "2024-02-25 12:00:00",  # Update with the desired epoch time
                "MEAN_MOTION": 14.342535,         # Update with the desired mean motion
                "ECCENTRICITY": 0.001234,         # Update with the desired eccentricity
                "INCLINATION": 53.245,            # Update with the desired inclination
                "RA_OF_ASC_NODE": 125.678,        # Update with the desired RA of Ascending Node
                "ARG_OF_PERICENTER": 34.567,      # Update with the desired Argument of Pericenter
                "MEAN_ANOMALY": 23.456,           # Update with the desired Mean Anomaly
                "REV_AT_EPOCH": 12345,            # Update with the desired Revolutions at Epoch
                "DRAG": 0.0 
            }

            #name TEXT, epoch REAL, inclination REAL, ra_of_aacending_node REAL, mm_rate_of_change REAL, revolutions INTEGER, mean_motion REAL, mean_anomaly REAL, bstar REAL, eccentricity REAL
            name_input = input("Satellite name:")
            epoch = input("Current epoch: ")
            mean_motion = float(input("Mean Motion: "))
            eccentricity = float(input("Eccentricity: "))
            inclination = float(input("Inclination: "))
            right_ascenscion = float(input("Right Ascension of Asecnding Node: "))
            arg_of_pericenter = float(input("Argument of pericenter: "))
            mean_anomaly = float(input("Mean Anomaly: "))
            rev_at_epoch = float(input("Revolution at epoch: "))
            drag = float(input("Drag: "))
            values = (datetime.now().date().strftime("%Y-%j"), name_input, epoch, eccentricity, mean_motion, inclination, right_ascenscion, arg_of_pericenter, mean_anomaly, rev_at_epoch)
            cursor.execute("INSERT INTO starlink_satellites VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values)
            connection.commit()

        elif user_selection == 5:
            cursor.execute("SELECT GROUP_CONCAT(epoch) FROM starlink_satellites")

            #Get the string from the function with the data.
            epoch_data = cursor.fetchall()[0][0]

            #Split the data into a list
            epoch_list = epoch_data.split(",")

            #Print out each epoch
            for epoch in epoch_list:
                print(f"{epoch}")

        else:
            #Commit all connections once program has ended.
            connection.commit()
            connection.close()
