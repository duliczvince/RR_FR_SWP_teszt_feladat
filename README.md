# RR_FR_SWP_teszt_feladat

Választott API: python-restcountries https://pypi.org/project/python-restcountries/
Program nyelv: Python

PostgreSQL virtuális gépen fut

Kezelt országadatok: name, languages, flag, currencies, capital, population, region, top_level_domain

SQL:
***

CREATE DATABASE country_datas
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Hungarian_Hungary.1250'
    LC_CTYPE = 'Hungarian_Hungary.1250'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

CREATE TABLE country(
	name VARCHAR PRIMARY KEY,
	languages VARCHAR NOT NULL,
	flag VARCHAR NOT NULL,
	currencies VARCHAR NOT NULL,
	capital VARCHAR NOT NULL,
	population NUMERIC NOT NULL,
	region VARCHAR NOT NULL,
	top_level_domain VARCHAR NOT NULL
);


