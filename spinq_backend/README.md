# Backend

App Django / Python 3


## Crear la base de datos 

Dar de alta la base con postgis
```
sudo su - postgres
psql
```

``` sql
CREATE USER spinq WITH PASSWORD 'spinq';
ALTER ROLE spinq SUPERUSER;
CREATE EXTENSION postgis;
CREATE DATABASE spinq OWNER spinq;
```
