# Overview

I am trying to create a database with satellite information that can easily be retrieved and organized. I learned how to protect current data, wrote code to make sure the data is up-to-date, and found different ways to manipulate the data.

I created a database that allows for users to retreive up-to-date data on satellites from the Celestrak API. Satellites can also be added to this database. The users are provided a menu to select what data they want and if they want to enter data, then the database is updated and closed on command.

I wanted to create a beginner database that I can one day use to pridct the locations of satellites in the sky and eventually turn it into visual data using GIS.

[Software Demo Video](https://ooo.mmhmm.app/watch/z_neWae8jpztomASJqxqQn)

# Relational Database

The database is called starstats.db, and it is updated daily. It is a single table that users can pull satellite data from. 

I created a table for the satellites in the API, including the current date of the data, the name of the satellite, the epoch of each satellite, the number of rotations, the tilt and position of the satellite, and how fast the satellite was moving, which ended up requiring ten columns. The table has a row for each satellite. 

# Development Environment

{Describe the tools that you used to develop the software}
I used the Visual Studio Code IDE and the Celestrek Starlink satellites' API.

{Describe the programming language that you used and any libraries.}

I used python and sqlite and json libraries. 

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [ChatGPT](https://chat.openai.com/c/3b2684a4-6579-40bf-be9d-9f5e3c07d783)
- [FreeCodeCamp SQLite Tutorial ](https://www.bing.com/ck/a?!&&p=a97f58ebc91a7ec5JmltdHM9MTcwODkwNTYwMCZpZ3VpZD0xNmZhZjM4OC1jZGIxLTY1YWUtMTI1Yi1lN2JhY2M5YzY0OTgmaW5zaWQ9NTI1MQ&ptn=3&ver=2&hsh=3&fclid=16faf388-cdb1-65ae-125b-e7bacc9c6498&psq=sqlite+tutorial+youtube&u=a1aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g_dj1ieUhjWVJwTWdJNA&ntb=1)

# Future Work
- I want to add another table for space stations. 
- I want to add a row that contains a prediction for the future location of each satellite.
- Using GIS, I would like to create a visualization of the data in the database.