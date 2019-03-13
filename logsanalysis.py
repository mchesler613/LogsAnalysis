#!/usr/bin/env python3
# Python source code for the Logs Analysis Project from Udacity
# Author: Merilyn Chesler
# Date: 1/30/2019
# Course: Udacity Nanodegree Full Stack Program

import psycopg2


"""
    Settings for Question 1
"""


question1 = "1. What are the most popular three articles of all time?\n"
query1 = """select articles.title, count(*) as views
    from log, articles
    where log.path='/article/'||articles.slug
    group by articles.title
    order by views desc
    limit 3;"""
format1 = "\"{}\" -- {} views"


"""
    Settings for Question 2
"""


question2 = "2. Who are the most popular article authors all time?\n"
query2 = """select authors.name, count(*) as views
    from authors, articles, log
    where log.path='/article/'||articles.slug and authors.id = articles.author
    group by authors.name
    order by views desc;"""
format2 = "{} -- {} views"


"""
    Settings for Question 3
"""


question3 = "3. On which days did more than 1% of requests lead to errors?\n"
query3 = """select regexp_replace(totalhits.date, '\\s+', ' ', 'g'),
    to_char(100.0*badhits.num/totalhits.num,'9D99%') as errors
    from totalhits, badhits
    where totalhits.date=badhits.date and badhits.num > 0.01*totalhits.num;"""
format3 = "{} -- {} errors"

"""
    A generic function to run a preformatted SQL query from the news database
    Argument: SQL query
    Output: query results
"""


def runquery(query):
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


"""
    A generic function to print the results from runquery() in pretty format
    Arguments: results string, preformatted question, print format
    Output: n/a
"""


def printresult(results, question, format):
    print(question)
    for result in results:
        print(format.format(result[0], result[1]))
    print("\n")


"""
    The main function calls each of the 3 database queries
"""


if __name__ == '__main__':
    result1 = runquery(query1)
    printresult(result1, question1, format1)

    result2 = runquery(query2)
    printresult(result2, question2, format2)

    result3 = runquery(query3)
    printresult(result3, question3, format3)
