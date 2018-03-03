# fullstack_nanodegree_project3
This file contains all the information about the project.
It explains that how you can run this project and what can you do with it.
# Project Overview
In this project, you'll work with data that could have come from a real-world web application,
with fields representing information that a web server would record, such as HTTP status codes and URL paths.
The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

# How to Run?

## PreRequisites:
  * [Python3](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)

## Setup Project:
  1. Install Vagrant and VirtualBox
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here.
  4. Unzip this file after downloading it. The file inside is called newsdata.sql.
  5. Copy the newsdata.sql file and content of this current repository, by either downloading or cloning it from
  [Here](https://github.com/maandeep98/fullstack_nanodegree_project3)
  
## Launching the Virtual Machine:
  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  
  ```
    $ vagrant up
  ```
  2. Then Log into this using command:
  
  ```
    $ vagrant ssh
  ```
  3. Change directory to /vagrant and look around with ls.
  
## Setting up the database and Creating Views:

  1. Load the data in local database using the command:
  
  ```
    psql -d news -f newsdata.sql
  ```
  The database includes three tables:
  * The authors table includes information about the authors of articles.
  * The articles table includes the articles themselves.
  * The log table includes one entry for each time a user has accessed the site.
  
  2. Use `psql -d news` to connect to database and now you are ready for the application of queries.
  
  3. Create view count_views using:
  ```
    create view count_views as select title,author,count(*) as views from articles,log where 
    log.path like concat('%',articles.slug) group by articles.title,articles.author 
    order by views desc;
  ```
  | Column  | Type    |
  | :-------| :-------|
  | title   | text    |
  | author  | text    |
  | views   | Integer |
  
  4. Create view view_error using the command:
  ```
    create view view_error as select date(time),round(100.0*sum(case log.status when '200 OK' 
    then 0 else 1 end)/count(log.status),2) as "Percentage Error" from log group by date(time) 
    order by "Percentage Error" desc;
  ```
  | Column        | Type    |
  | :-------      | :-------|
  | date          | date    |
  | Percentage Error | float   |
  
## Running the queries:
  1. From the vagrant directory inside the virtual machine,run log.py using:
  ```
    $ python3 log.py
  ```
  
###FAQ's: [here](https://classroom.udacity.com/nanodegrees/nd004-intr1/parts/e400b41b-7a81-4598-ae2a-d2ab41c5b42d/modules/bbd71bf2-7490-4679-a943-ca6ef9e376cb/lessons/129df784-18b7-47a3-b482-cb1edb7faac9/concepts/b2ff9cba-210e-463e-9321-2605f65491a9)