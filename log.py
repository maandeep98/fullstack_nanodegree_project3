#!/usr/bin/env python3

import psycopg2

database_nm = "news"

# 1. Which are the three most popular articles of all time?
sol_1 = "select title,views from count_views limit 3"

# 2. Who are the most popular article authors of all time?
sol_2 = """select authors.name,sum(count_views.views) as views from
count_views,authors where authors.id = count_views.author
group by authors.name order by views desc"""

# 3. On which days did more than 1% of requests lead to an error?
sol_3 = "select * from view_error where \"Percentage Error\" > 1"


# Storing the results
sol_1_result = dict()
sol_1_result['title'] = "\n1. The 3 most popular articles of all time are:\n"

sol_2_result = dict()
sol_2_result['title'] = """\n2. The most popular article authors of
all time are:\n"""

sol_3_result = dict()
sol_3_result['title'] = """\n3. Days with more than 1% of request that
lead to an error:\n"""


# this function returns results of queries
def sol_result(query):
    db = psycopg2.connect(database=database_nm)
    data = db.cursor()
    data.execute(query)
    results = data.fetchall()
    db.close()
    return results


def print_results(query_result)
    print(query_result['title'])
    for result in query_result['results']:
        print('\t' + str(result[0]) + ' -----> ' + str(result[1]) + ' views')


def print_error_results(query_result):
    print(query_result['title'])
    for result in query_result['results']:
        print('\t' + str(result[0]) + ' -----> ' + str(result[1]) + ' %')


# stores query result
sol_1_result['results'] = sol_result(sol_1)
sol_2_result['results'] = sol_result(sol_2)
sol_3_result['results'] = sol_result(sol_3)

# print formatted output
print_results(sol_1_result)
print_results(sol_2_result)
print_error_results(sol_3_result)
