# SQL-Django-Models-and-Migrations @CS50 Harvard
SQL, Django Models and Migrations

This repository is about using SQL and Django Models/Migrations to efficiently store and access data.
As an exercise example, I have developed a Flights mangement system web app; https://www.youtube.com/watch?v=juKiaHTV--M

1. SQL, or Structured Query Language, is a programming language that allows us to update and query databases.
How our data is stored ?. When using SQL, we’ll work with a relational database where we can find all of our data stored in a number of tables. Each of these tables is made up of a set number of columns and a flexible number of rows.
There are several different relational database management systems (DBMSs) that are commonly used to store information, and that can easily interact with SQL commands;
-MySQL
-PostgreSQL
-SQLite
-etc.…
The first two, MySQL and PostgreSQL, are heavier-duty database management systems that are typically run on servers separate from those running a website. SQLite, on the other hand, is a lighter-weight system that can store all of its data in a single file. We’ll be using SQLite throughout this course, as it is the default system used by Django.
There are several commands in order to manage SQL databases; create tables, Select, Update, Join, Indexing, etc.

2. Django Models are a level of abstraction on top of SQL that allow us to work with databases using Python classes and objects rather than direct SQL queries.

3. Migration; once created a model, we do not yet have a database to store this information. To create a database from our Django models its necessary to run the commands "python manage.py makemigrations" and "python manage.py migrate". This command creates some Python files that will create or edit our database to be able to store what we have in our models.

4. Django Admin; since it is so common for developers to have to create new objects, Django comes with a default admin interface that allows us to do this more easily.

5. Users; the last important thing is the idea of "authentication", or allowing users to log in and log out of a website. Fortunately, Django makes this very easy for us.
