# Django N + 1

`N+1` is the common way to reference a database performance issue that Django is susceptible to, when using certain database calls in certain ways.

This repository aims to be a collection of examples of theses mistakes, as many as possible, and also of the solution(s) to those performance loses.

For convenience of testing, a basic Django project named `n_plus_one` is available.

Each app will focus on one given type of problem, group of problems or alternative solutions.

Some apps will illustrate the use of tools to find these problems

## Table of Contents

- [Requirements](#requirements)
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
- Docker (for Postgres server instance)

To install the required Python modules: `pip install -r requirements.txt`

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

To create extra instances there's a management command:

```bash
python manage.py create_example_1_data 100
```

## Examples

Collection of examples of different ways in which the N+1 problem can arise in Django.


### Example 0

`N+1` by direct `ForeingKey` relationship.

To create extra instances for this app, execute: `python manage.py create_example_0_data $INT`
To load the data fixture: `python manage.py loaddata --app example_0 example_0_dump.json`


### Example 1

`N+1` by reverse `ForeignKey` relationship.

This is an implementation of the example used on [this](https://blog.sentry.io/2020/09/14/finding-and-fixing-django-n-1-problems) very good explanation of the `n+1` issue in Django. 

To create extra instances for this app, execute: `python manage.py create_example_1_data $INT`
To load the data fixture: `python manage.py loaddata --app example_1 example_1_dump.json`

In this example we explore:

- N+1 issues of accesing data from a `ForeignKeyField`
- Optimizations using database functions instead of Python code


### Example 2

`2N+1` issues with double-nested model access through `ForeighKeyField`

Inspired by the `2N+1` explanation on [https://scoutapm.com/blog/django-and-the-n1-queries-problem]()

To create extra instances for this app, execute: `python manage.py create_example_2_data $INT`
To load the data fixture: `python manage.py loaddata --app example_2 example_2_dump.json`


### Example 3

Exploration of N+1 issues when using `ManyToManyField` in your models.

To create extra instances for this app, execute: `python manage.py create_example_3_data $INT`
To load the data fixture: `python manage.py loaddata --app example_3 example_3_dump.json`


### REST

In this case we explore the N+1 issues when developing REST endpoints with `DjangoRESTFramework`

To create extra instances for this app, execute: `python manage.py create_rest_data $INT`
To load the data fixture: `python manage.py loaddata --app rest rest_dump.json`


### GraphQL

This example ios inspired by the tutorial at [https://apirobot.me/posts/django-graphql-solving-n-1-problem-using-dataloaders]()



## Profiling

There are a number of modules to help us with this

### Nplusone

To enable `nplusone`: 
```bash
python manage.py migrate --settings=nplus1_nomore.settings.nplusone
python manage.py runserver --settings=nplus1_nomore.settings.nplusone
```

#### [https://github.com/jmcarp/nplusone]()

`nplusone` is a library for detecting the n+1 queries problem in Python ORMs, including SQLAlchemy, Peewee, and the Django ORM.

Note: `nplusone` should only be used for development and should not be deployed to production environments.

Add:

- `'nplusone.ext.django',` to `INSTALLED_APPS`
- `'nplusone.ext.django.NPlusOneMiddleware',` to `MIDDLEWARE`

Config logging in settings:

```python
NPLUSONE_LOGGER = logging.getLogger('nplusone')
NPLUSONE_LOG_LEVEL = logging.WARN
```

Warning messages:

- When lazily loading data: `Potential n+1 query detected on <model>.<field>`
- When eagerly loading without using: `Potential unnecessary eager load detected on <model>.<field>`

To throw an error instead of a warning message, add `NPLUSONE_RAISE = True` to settings.


### Django Silk

To enable`django-silk`: 
```bash

python manage.py migrate --settings=nplus1_nomore.settings.silk
python manage.py runserver --settings=nplus1_nomore.settings.silk

```

Note: you'll need to uncomment the views to enable profiling

#### [https://github.com/jazzband/django-silk]()

Silk is a live profiling and inspection tool for the Django framework. Silk intercepts and stores HTTP requests and database queries before presenting them in a user interface for further inspection

Add to settings:

- MIDDLEWARE: `'silk.middleware.SilkyMiddleware',`
- INSTALLED_APPS: `'silk',`

To access reports add the following to URLconf:

```python
urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
```

To activate profiling:

- add to settings: `SILKY_PYTHON_PROFILER = True`
- decorate views:
```python
from silk.profiling.profiler import silk_profile

@silk_profile(name='View Blog Post')
def post(request, post_id):
    ...

```

### Django Postgres Metrics

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

#### [https://github.com/django-postgres-metrics/django-postgres-metrics]()

A Django application that exposes a bunch of PostgreSQL database metrics.

Add: 
- `'postgres_metrics.apps.PostgresMetrics',` to the top of INSTALLED_APPS
- `path('admin/postgres-metrics/', include('postgres_metrics.urls')),` to URLconf

TODO: the URL doesn't WORK ???


### Django cProfile Middleware

To enable `cprofile`:
```bash
# start server
python manage.py runserver --settings=nplus1_nomore.settings.cprofile

```

#### [https://github.com/omarish/django-cprofile-middleware/]()

This is a simple profiling middleware for Django applications.

- Add to MIDDLEWARE: `'django_cprofile_middleware.middleware.ProfilerMiddleware',`

Only available when `DEBUG=True` and user by staff.

To disable user creds: `DJANGO_CPROFILE_MIDDLEWARE_REQUIRE_STAFF = False`

To use add `?prof` or `&prof` at the end of your query to see the results of the query analysis.


### Django Debug Toolbar

To enable `debug_toolbar`:

```bash
# start server
python manage.py runserver --settings=nplus1_nomore.settings.debug

```

#### [https://django-debug-toolbar.readthedocs.io/en/latest/]()

The Django Debug Toolbar is a configurable set of panels that display various debug information about the current request/response and when clicked, display more details about the panel’s content.

Add `'debug_toolbar',` to INSTALLED_APPS
Add `'debug_toolbar.middleware.DebugToolbarMiddleware',` to MIDDLEWARE, as high as possible
Add `path('__debug__/', include('debug_toolbar.urls')),` to URLconf
Add to seetings:

```python

INTERNAL_IPS = [
    '127.0.0.1',
]
```

### Django-health-check

To enable `django-health-check`:

```bash

python manage.py migrate --settings=nplus1_nomore.settings.health

# start server
python manage.py runserver --settings=nplus1_nomore.settings.health

```

[https://github.com/KristianOellegaard/django-health-check]()

Checks for various conditions and provides reports when anomalous behavior is detected.

Add to URLconf: `path('health/', include('health_check.urls')),`

Add required apps to INSTALLED_APPS:
```python
INSTALLED_APPS = [
    # ...
    'health_check',                             # required
    'health_check.db',                          # stock Django health checkers
    'health_check.cache',
    'health_check.storage',
    'health_check.contrib.migrations',
    'health_check.contrib.celery',              # requires celery
    'health_check.contrib.celery_ping',         # requires celery
    'health_check.contrib.psutil',              # disk and memory utilization; requires psutil
    'health_check.contrib.s3boto3_storage',     # requires boto3 and S3BotoStorage backend
    'health_check.contrib.rabbitmq',            # requires RabbitMQ broker
    'health_check.contrib.redis',               # requires Redis broker
]
```

### Django Auto Prefetch

To load the data for `django-auto-prefetch`: `python manage.py loaddata --app autopre autopre_dump.json`

An example page can be reached at `/autopre/`


[https://github.com/tolomea/django-auto-prefetch]()

Automatically prefetch foreign key values as needed.

To enable, change:

```python
from django.db import models


class Book(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE)

```

for: 

```python
import auto_prefetch
from django.db import models


class Book(auto_prefetch.Model):
    author = auto_prefetch.ForeignKey("Author", on_delete=models.CASCADE)

```


### Outdated

- django-live-profiler


