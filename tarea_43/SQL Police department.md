#  SQL Police department

## Submit all users' details


`SELECT * FROM users;`

Con **SELECT** se realiza una consulta de selección u obtención de datos.

**FROM** users indica que se obtengan los datos de la tabla **"users"**

`*` indica que se obtengan todas las columnas de la tabla.

## Submit all suscribers' details

`SELECT * FROM subscribers`

Con **SELECT** se realiza una consulta de selección u obtención de datos.

**FROM** users indica que se obtengan los datos de la tabla **"subscribers"**

`*` indica que se obtengan todas las columnas de la tabla.

## Submit all users first names, email addresses and last access times' details

`SELECT FirstName, EmailAddress, LastAccess FROM users;`

Con **SELECT** se realiza una consulta de selección u obtención de datos.

**FROM** users indica que se obtengan los datos de la tabla **"users"**

Se especifica el nombre de las columnas concretas de las que se quieren obtener los datos:  **"FirstName, EmailAddress y LastAccess"**


## Submit all sucribers subscription dates and password hashes' details

`SELET SubscriptionDate, PasswordHash FROM subscribers;`


Con **SELECT** se realiza una consulta de selección u obtención de datos.

**FROM** users indica que se obtengan los datos de la tabla **"subscribers"**

Se especifica el nombre de las columnas concretas de las que se quieren obtener los datos:  **"SubscriptionDate y PasswordHash"**


## Submit all entries number of promotions sent' details. Please make sure there are no duplicates

`SELECT DISTINCT PromotionsSent FROM mailing_list;`

Con **SELECT** se realiza una consulta de selección u obtención de datos.

**FROM** users indica que se obtengan los datos de la tabla **"mailing_list"**

Se especifica que **PromotionsSet** es la columna de la que se quieren obtener datos y se añade la palabra clave **DISTINCT** para indicar que se eliminen los valores duplicados.


## Submit all members' details sorted by number of purchases in ascending order

`SELECT * FROM membars ORDER BY NumberOfPurchases ASC;`

Con **SELECT** se realiza una consulta de selección u obtención de datos.

**FROM** users indica que se obtengan los datos de la tabla **"members"**

`*` indica que se obtengan todas las columnas de la tabla.

**ORDER BY** indica que se quieren obtener los datos ordenados por los datos de la columna **NumberOfPurchases** y la palabra clave **ASC** indica que la ordenación debe ser ascendente.


## Submit all subscribers' details sorted by addresses in descending order

`SELECT * FROM subscribers ORDER BY Address DESC;`

Con **SELECT** se realiza una consulta de selección u obtención de datos.

**FROM** users indica que se obtengan los datos de la tabla **"subscribers"**

`*` indica que se obtengan todas las columnas de la tabla.

**ORDER BY** indica que se quieren obtener los datos ordenados por los datos de la columna **Address** y la palabra clave **DESC** indica que la ordenación debe ser descendente.


## Submit all subscribers number of purchases and usernames details sorted by usernames in descending order. No duplicates.

`SELECT DISTINCT Username, Purchases FROM subscribers ORDER BY Username DESC;`

Con **SELECT** se realiza una consulta de selección u obtención de datos.

**FROM** users indica que se obtengan los datos de la tabla **"subscribers"**

Se especifica que **Username y Purchases** son las columnas de las que se quieren obtener datos y se añade la palabra clave **DISTINCT** para indicar que se eliminen los valores duplicados.

**ORDER BY** indica que se quieren obtener los datos ordenados por los datos de la columna **Username** y la palabra clave **DESC** indica que la ordenación debe ser descendente.


## Submit all users last access times, email addresses and number of posts' details sorted by last access times in descendig order an then by number of post in descending order.

`SELECT LastAccess, EmailAddress, NumberOfPosts FROM users ORDER BY LastAccess DESC, NumberOfPosts DESC;`

Con **SELECT** se realiza una consulta de selección u obtención de datos.

**FROM** users indica que se obtengan los datos de la tabla **"users"**

Se especifica que **LastAccess, EmailAddress y NumberOfPosts** son las columnas de las que se quieren obtener datos.

**ORDER BY** indica que se quieren obtener los datos ordenados por los datos de la columna **LastAccess** y después ordenados por los datos de la columna **NumberOfPosts** 

La palabra clave **DESC** indica que la ordenación debe ser descendente.


## Submit the top 10 records' details when soreted by number of promotions sent in descending order and then by given names in descending order.

`SELECT * FROM mailing_list ORDER BY PromotionsSent DESC, GivenName DESC LIMIT 10;`

Con **SELECT** se realiza una consulta de selección u obtención de datos.

**FROM** users indica que se obtengan los datos de la tabla **"mailing_list"**

`*` indica que se obtengan todas las columnas de la tabla.

**ORDER BY** indica que se quieren obtener los datos ordenados por los datos de la columna **PromotionsSent** y después ordenados por los datos de la columna **GivenName** 

La palabra clave **DESC** indica que la ordenación debe ser descendente.

**LIMIT 10** limita el número de resultados obtenidos a 10

## Submit top 10 users surnames, access times and email addresses' details when sorted by surnames in ascending order and then by access times in ascending order. No duplicates.

`SELECT DISTINCT Surname, AccessTime, EmailAddress FROM users ORDER BY Surname ASC AccessTime ASC LIMIT 10`

Con **SELECT** se realiza una consulta de selección u obtención de datos.

**FROM** users indica que se obtengan los datos de la tabla **"users"**

Se especifica que **Surname, AccessTime yEmailAddress** son las columnas de las que se quieren obtener datos y se añade la palabra clave **DISTINCT** para indicar que se eliminen los valores duplicados.

**ORDER BY** indica que se quieren obtener los datos ordenados por los datos de la columna **Surname** y después ordenados por los datos de la columna **AccessTime** 

La palabra clave **ASC** indica que la ordenación debe ser ascendente.

**LIMIT 10** limita el número de resultados obtenidos a 10
