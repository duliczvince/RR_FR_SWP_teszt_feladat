# RR_FR_SWP_teszt_feladat

***

Választott API: python-restcountries https://pypi.org/project/python-restcountries/ - több mint 8 adat kellett és ez volt a második api ami ennek a kritériumnak megfelel

Program nyelv: Python

PostgreSQL virtuális gépen fut - minden teszt feladatra virtuális gépet használok

Kezelt országadatok: name, latlng, demonym, borders, capital, population, region, top_level_domain

***

# SQL


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
	
	latlng VARCHAR NOT NULL,
	
	demonym VARCHAR NOT NULL,
	
	borders VARCHAR NOT NULL,
	
	capital VARCHAR NOT NULL,
	
	population NUMERIC NOT NULL,
	
	region VARCHAR NOT NULL,
	
	top_level_domain VARCHAR NOT NULL
	
);


