# Schema for Song Play Analysis
Using the song and log datasets, you'll need to create a star schema optimized for queries on song play analysis. This includes the following tables.

**Table Description**
1. Fact Table
- songplays - records in log data associated with song plays i.e. records with page NextSong
`songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent`

2. Dimension Tables
- users - users in the app
`user_id, first_name, last_name, gender, level`
- songs - songs in music database
`song_id, title, artist_id, year, duration`
- artists - artists in music database
`artist_id, name, location, latitude, longitude`
- time - timestamps of records in songplays broken down into specific units
`start_time, hour, day, week, month, year, weekday`

**Project Template**

To get started with the project, go to the workspace on the next page, where you'll find the project template files. You can work on your project and submit your work through this workspace. Alternatively, you can download the project template files from the Resources folder if you'd like to develop your project locally.

In addition to the data files, the project workspace includes _six files_:

`test.ipynb` displays the first few rows of each table to let you check your database.
`create_tables.py` drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
`etl.ipynb` reads and processes a single file from `song_data` and `log_data` and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
`etl.py` reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
`sql_queries.py` contains all your sql queries, and is imported into the last three files above.
`README.md `provides discussion on your project.

**Project Steps**
NOTE: You will not be able to run `test.ipynb`,`etl.ipynb`, or `etl.py` until you have run `create_tables.py` at least once to create the sparkifydb database, which these other files connect to.

**_Below are steps you can follow to complete the project_⬇️**

1. Create Tables
- [x] Write CREATE statements in `sql_queries.py` to create each table.
- [] Write DROP statements in `sql_queries.py` to drop each table if it exists.
- [] Run `create_tables.py` to create your database and tables.
- [] Run `test.ipynb` to confirm the creation of your tables with the correct columns. Make sure to click "Restart kernel" to close the connection to the database after running this notebook.

2. Build ETL Processes
- [] Follow instructions in the `etl.ipynb` notebook to develop ETL processes for each table. At the end of each table section, or at the end of the notebook, run `test.ipynb` to confirm that records were successfully inserted into each table. Remember to rerun `create_tables.py` to reset your tables before each time you run this notebook.

3. Build ETL Pipeline
- [] Use what you've completed in `etl.ipynb` to complete `etl.py`, where you'll process the entire datasets. Remember to `run create_tables.py` before running `etl.py` to reset your tables. Run `test.ipynb` to confirm your records were successfully inserted into each table.

4. Run Sanity Tests
- [] When you are satisfied with your work, run the cell under the Sanity Tests section in the `test.ipynb` notebook. The cells contain some basic tests that will evaluate your work and catch any silly mistakes. We test column data types, primary key constraints and not-null constraints as well look for on-conflict clauses wherever required. If any of the test cases catches a problem, you will see a warning message printed in Orange that looks like this:

[WARNING] The songplays table does not have a primary key!
You may want to make appropriate changes to your code to make these warning messages go away. The tests below are only meant to help you make your work foolproof. The submission will still be graded by a human grader against the project rubric.

**Document Process**
Do the following steps in your README.md file.
- [x] Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.
- [] How to run the Python scripts
- [] An explanation of the files in the repository
- [] State and justify your database schema design and ETL pipeline.
- [] [Optional] Provide example queries and results for song play analysis.
- [] Here's a [Guide] (https://www.markdownguide.org/basic-syntax/guide) on Markdown Syntax.*
- [] Provide DOCSTRING statement in each function implementation to describe what each function does.
