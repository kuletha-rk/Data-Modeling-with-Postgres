"""
Part 1 - Create Tables
Dropping tables, if exist and creating fact & dimension tables
in sql.py file, before running create_tables.py.

"""
# Dropping tables

"""
Fact Table:
- songplays - records in log data associated with song plays i.e. records with page NextSong
`songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent`
"""

songplay_table_drop = "DROP table IF EXISTS songplays"

"""
Dimension Table:
- users - users in the app
`user_id, first_name, last_name, gender, level`
- songs - songs in music database
`song_id, title, artist_id, year, duration`
- artists - artists in music database
`artist_id, name, location, latitude, longitude`
- time - timestamps of records in songplays broken down into specific units
`start_time, hour, day, week, month, year, weekday`
"""

user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

# Creating tables
"""
Fact tables
"""
songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays
                         (songplay_id SERIAL PRIMARY KEY,
                         start_time timestamp,
                         user_id int NOT NULL REFERENCES users(user_id),
                         level varchar,
                         song_id varchar REFERENCES songs(song_id),
                         artist_id varchar REFERENCES artists(artist_id),
                         session_id int,
                         location varchar,
                         user_agent varchar)""")
"""
Dimension tables
"""
user_table_create = ("""CREATE TABLE IF NOT EXISTS users
                     (user_id int PRIMARY KEY,
                     first_name varchar,
                     last_name varchar,
                     gender varchar,
                     level varchar)""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs
                     (song_id varchar PRIMARY KEY,
                     title varchar,
                     artist_id varchar,
                     year numeric,
                     duration numeric)""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists
                       (artist_id varchar PRIMARY KEY,
                       artist_name varchar,
                       artist_location varchar,
                       artist_latitude decimal,
                       artist_longitude decimal)""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time
                     (start_time timestamp PRIMARY KEY,
                     hour int,
                     day int,
                     week int,
                     month int,
                     year int,
                     weekday int)""")
"""
Part 2-Inserting records

"""
songplay_table_insert = ("""INSERT INTO songplays (songplay_id, start_time,
                         user_id, level, song_id, artist_id, session_id,
                         location, user_agent)
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                         ON CONFLICT (songplay_id) DO NOTHING;
                         """)

user_table_insert = ("""INSERT INTO users (user_id, first_name,
                     last_name, gender, level)
                     VALUES (%s, %s, %s, %s, %s)
                     ON CONFLICT (user_id)
                     DO UPDATE SET level=excluded.level;
                     """)

song_table_insert = ("""INSERT INTO songs (song_id, title,
                     artist_id, year, duration)
                     VALUES (%s, %s, %s, %s, %s)
                     ON CONFLICT (song_id) DO NOTHING;
                     """)

artist_table_insert = ("""INSERT INTO artists (artist_id, artist_name,
                       artist_location,
                       artist_latitude, artist_longitude)
                       VALUES (%s, %s, %s, %s, %s)
                       ON CONFLICT (artist_id) DO NOTHING;
                       """)


time_table_insert = ("""INSERT INTO time (start_time, hour, day,
                     week, month, year, weekday)
                     VALUES (%s, %s, %s, %s, %s, %s, %s)
                     ON CONFLICT (start_time) DO NOTHING;
                     """)

"""
Part 3 - Finding Songs
"""
song_select = ("""SELECT songs.song_id, artists.artist_id
               FROM songs JOIN artists
               ON artists.artist_id = songs.artist_id
               WHERE songs.title = %s
                    AND artists.artist_name = %s
                    AND songs.duration = %s""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create,
                        time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop,
                      song_table_drop, artist_table_drop,
                      time_table_drop]
