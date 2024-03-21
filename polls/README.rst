{\rtf1\ansi\ansicpg950\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 ============\
django-polls\
============\
\
django-polls is a Django app to conduct web-based polls. For each\
question, visitors can choose between a fixed number of answers.\
\
Detailed documentation is in the "docs" directory.\
\
Quick start\
-----------\
\
1. Add "polls" to your INSTALLED_APPS setting like this::\
\
    INSTALLED_APPS = [\
        ...,\
        "django_polls",\
    ]\
\
2. Include the polls URLconf in your project urls.py like this::\
\
    path("polls/", include("django_polls.urls")),\
\
3. Run ``python manage.py migrate`` to create the models.\
\
4. Start the development server and visit the admin to create a poll.\
\
5. Visit the ``/polls/`` URL to participate in the poll.}