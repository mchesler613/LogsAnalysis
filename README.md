
# INTRODUCTION

The Logs Analysis Project is a database-driven project that stores interesting information about authors, their articles and the popularity of their articles based on Web access.

My task is to provide a reporting tool that generates a project-supplied text output format based on three questions:
1.  What are the most popular three articles of all time?
2.  Who are the most popular article authors of all time?
3.  On which days did more than 1% of requests lead to errors?

I implemented the reporting tool using the Python programming language which accesses a PostgreSQL database.


# DESIGN

I design this reporting tool referencing the **Python3** environment and using **"psycopg2"** to access the PostgreSQL database.

The main function calls 2 other functions, **runquery()** and **printresult()** 3 times, one for each of the 3 unique questions.

I provided 3 sets of "question-SQL query-output format" triple global variables, based on the 3 questions asked.  Each variable set is then passed on to the runquery() and printresult() functions to answer its unique question and produce its unique answer in the project-supplied text output format.

The generic runquery(query) function connects to the "news" database via psycopg2, executes the unique SQL query supplied to it, saves the query results in a variable, closes the database connection and then returns the results variable.

The generic printresult(results,question,format) function prints the unique question on the terminal and then prints each result in the results variable in the supplied text format on the terminal.

The source code to this design is implemented in the **logsanalysis.py** file. This file has been checked to conform to the Python style guide via the **pycodestyle** tool without generating any warnings.


# INSTALLATION

This project requires that the following packages be already installed and running:

+ Install [Virtual Box](https://www.virtualbox.org/)
+ Install [Vagrant](https://www.vagrantup.com/)
+ Run vagrant, via `vagrant up` command
+ Access vagrant via ssh with the `vagrant ssh` command
+ Install PostgreSQL database and make sure we can access it via psql
+ Download newsdata.sql supplied by Udacity
+ Create the database tables and data via the `psql -d news -f newsdata.sql` command
+ Explore the news database inside psql via the `\dt`, `\d` commands
+ The "news" database should contain 3 tables: authors, articles, and log
+ To answer the 3rd question, I created 2 views in the "news" database.
```
CREATE VIEW totalhits AS
SELECT to_char("time",'Month DD, YYYY') AS date, count(*) AS num
FROM log
GROUP by date
ORDER by date;

CREATE VIEW badhits AS
SELECT to_char("time",'Month DD, YYYY') AS date, count(*) AS num
FROM log
WHERE status not like '%2%'
GROUP by date
ORDER by date;
```
# USAGE

To run this project, simply execute this command on the terminal: ```./logsanalysis.py```

# OUTPUT

The output from running `./logsanalysis.py` is contained in the **logsanalysis.txt** text file.


# AUTHOR BIO

Merilyn Chesler is a student at the Udacity Fullstack Development Nanodegree Degree Program from December 2018-April 2019.
