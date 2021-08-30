# Django N+1 No More!!!

This project aims to be an exhaustive collection of examples of theses mistakes, as many as possible, and also of the solution(s) to these performance loses caused by `N+1` issues.

`N+1` is the common way to reference a database performance issue that Django is susceptible to, when using certain database calls, in certain ways.

For convenience of poking and proding, a basic Django project named `nplus1_nomore` is available.

Each app focuses on one given type of problem, group of problems or alternative solutions.


## Table of Contents

- [Requirements](#requirements)
- [Resources](#resources)
- [Project Setup](#project-setup)
- [Examples](#examples)
  - [Example 0](#example-0)
  - [Example 1](#example-1)
  - [Example 2](#example-2)
  - [Example 3](#example-3)
  - [REST API](#rest-api)
  - [GraphQl](#graphql)
- [Profiling Tools](#profiling)
  - [nplusone](#nplusone)
  - [Django Silk](#django-silk)
  - [Django Postgres Metrics](#django-postgres-metrics)
  - [Django cProfile Middleware](#django-cprofile-middleware)
  - [Django Debug Toolbar](#django-debug-toolbar)
  - [Django Health Check](#django-health-check)
  - [Django Auto Prefetch](#django-auto-prefetch)
  - [Outdated](#outdated)



## Requirements

- Python 3.6
- Django 2.2

Optional:

- Docker (for use with Postgres metrics module)

To install the required Python modules: 
```bash
pip install -r requirements.txt
```


## Resources

I have used a number of online resources when researching this topic.
Here are some of them:

- [https://blog.sentry.io/2020/09/14/finding-and-fixing-django-n-1-problems]()
- [https://scoutapm.com/blog/django-and-the-n1-queries-problem]()
- [https://www.valentinog.com/blog/n-plus-one/]()
- [https://apirobot.me/posts/django-graphql-solving-n-1-problem-using-dataloaders]()


## Project Setup

From the folder containing this README file, and from an appropiate `virtualenv`, execute the following:

```bash
# install requirements
pip install -r requirements.txt
# go to project folder
cd n_plus_one
# migrations
python manage.py makemigrations autopre example_0 example_1 example_2 example_3 rest graph
python manage.py migrate

```

Model instances can be created using the custom management commands provided, or by loading the included fixtures.


## Examples

Collection of examples of different ways in which the N+1 problem can arise in Django.


### Example 0

`N+1` by direct `ForeingKey` relationship.

To create extra instances for this app, execute: 
```bash
python manage.py create_example_0_data $INT
```

To load the data fixture: 
```bash
python manage.py loaddata --app example_0 example_0_dump.json
```


### Example 1

`N+1` by reverse `ForeignKey` relationship.

This is an implementation of the example used on [this](https://blog.sentry.io/2020/09/14/finding-and-fixing-django-n-1-problems) very good explanation of the `n+1` issue in Django. 

To create extra instances for this app, execute: 
```bash
python manage.py create_example_1_data $INT
```
To load the data fixture: 
```bash
python manage.py loaddata --app example_1 example_1_dump.json
```

In this example we explore:

- N+1 issues of accesing data from a `ForeignKeyField`
- Optimizations using database functions instead of Python code


### Example 2

`2N+1` issues with double-nested model access through `ForeighKeyField`

Inspired by the `2N+1` explanation on [https://scoutapm.com/blog/django-and-the-n1-queries-problem]()

To create extra instances for this app, execute: 
```bash
python manage.py create_example_2_data $INT
```
To load the data fixture: 
```bash
python manage.py loaddata --app example_2 example_2_dump.json
```


### Example 3

Exploration of N+1 issues when using `ManyToManyField` in your models.

To create extra instances for this app, execute: 
```bash
python manage.py create_example_3_data $INT
```
To load the data fixture: 
```bash
python manage.py loaddata --app example_3 example_3_dump.json
```


### REST

In this case we explore the N+1 issues when developing REST endpoints with `DjangoRESTFramework`

To create extra instances for this app, execute: 
```bash
python manage.py create_rest_data $INT
```
To load the data fixture: 
```bash
python manage.py loaddata --app rest rest_dump.json
```


### GraphQL

This example is inspired by the tutorial at [https://apirobot.me/posts/django-graphql-solving-n-1-problem-using-dataloaders]()



## Profiling

There are a number of modules to help us with this as well as keep an eye on the overall performance of our project.

To enable any module, start the server with the appropiate settings.

Links to disabled modules will return an error.


### Nplusone

`nplusone` is a library for detecting the n+1 queries problem in Python ORMs, including SQLAlchemy, Peewee, and the Django ORM.

To enable `nplusone`:

```bash
python manage.py migrate --settings=nplus1_nomore.settings.nplusone
python manage.py runserver --settings=nplus1_nomore.settings.nplusone
```

For more details: [https://github.com/jmcarp/nplusone]()


### Django Silk

Silk is a live profiling and inspection tool for the Django framework. Silk intercepts and stores HTTP requests and database queries before presenting them in a user interface for further inspection.

To enable`django-silk`:

```bash

python manage.py migrate --settings=nplus1_nomore.settings.silk
python manage.py runserver --settings=nplus1_nomore.settings.silk

```

Note: you'll need to uncomment the decorators and the `import` statement on views to enable profiling

For more details: [https://github.com/jazzband/django-silk]()


### Django Postgres Metrics

A Django application that exposes a bunch of PostgreSQL database metrics.

To enable `django-postgres-metrics`:

```bash
# start local docker PG server
./start_pg.sh   
python manage.py migrate --settings=nplus1_nomore.settings.pg_metrics
# create superuser (requires admin access)
python manage.py createsuperuser --settings=nplus1_nomore.settings.pg_metrics
# create some instances
python manage.py loaddata --app example_1 example_1_dump.json --settings=nplus1_nomore.settings.pg_metrics
# start server
python manage.py runserver --settings=nplus1_nomore.settings.pg_metrics

```

Remember to create the `.env` file from `.env_example`, and fill the required data.

For more details: [https://github.com/django-postgres-metrics/django-postgres-metrics]()


### Django cProfile Middleware

This is a simple profiling middleware for Django applications.

To use add `?prof` or `&prof` at the end of your query to see the results of the query analysis.

To enable `cprofile`:
```bash
# start server
python manage.py runserver --settings=nplus1_nomore.settings.cprofile

```


### Django Debug Toolbar

The Django Debug Toolbar is a configurable set of panels that display various debug information about the current request/response and when clicked, display more details about the panel’s content.

To enable `debug_toolbar`:

```bash
# start server
python manage.py runserver --settings=nplus1_nomore.settings.debug

```

For more details: [https://django-debug-toolbar.readthedocs.io/en/latest/]()


### Django-health-check

Checks for various conditions and provides reports when anomalous behavior is detected.

To enable `django-health-check`:

```bash

python manage.py migrate --settings=nplus1_nomore.settings.health

# start server
python manage.py runserver --settings=nplus1_nomore.settings.health

```

For more details: [https://github.com/KristianOellegaard/django-health-check]()


### Django Auto Prefetch

To load the data for `django-auto-prefetch`: `python manage.py loaddata --app autopre autopre_dump.json`

An example page can be reached at `/autopre/`


For more details: [https://github.com/tolomea/django-auto-prefetch]()


### Outdated

- django-live-profiler


