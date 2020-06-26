from restcountries import RestCountryApiV2 as rapi
import psycopg2

#konstansok
USER = "postgres"
PASSWORD = "asddsa123A"
HOST = "127.0.0.1"
PORT = "5432"
DATABASE = "country_datas"

def connectToDB():
    connection = None

    try:
        connection = psycopg2.connect(user = USER,
                                      password = PASSWORD,
                                      host = HOST,
                                      port = PORT,
                                      database = DATABASE)

        cursor = connection.cursor()
        clearCountryDB(cursor)
        connection.commit()


        #adat kigyűjtés + írás
        country_list = rapi.get_all()
        sumCountry = 0
        countryRowList = []
       
        while sumCountry < countCountry():
            country = country_list[sumCountry]
            countryRowList.clear()
            INSERT_QUERY = "INSERT INTO country (name, latlng, demonym, borders, capital, population, region, top_level_domain) VALUES ("
            
            countryRowList.extend([
                removeChars(country.name),
                removeChars(country.latlng),
                removeChars(country.demonym),
                removeChars(country.borders),
                removeChars(country.capital),
                removeChars(country.population),
                removeChars(country.region),
                removeChars(country.top_level_domain)])
            
            for x in countryRowList:
                INSERT_QUERY += " '"+str(x)+"',"

            INSERT_QUERY = INSERT_QUERY[:-1]
            cursor.execute(INSERT_QUERY + ")")
            connection.commit()
            
            sumCountry+=1
    
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to SQL", error)
        
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("SQL connection is closed")

def countCountry():
    return len(rapi.get_all())

#eltávolítandó dolgok a str-ből
def removeChars(text):
    text = str(text)
    removeChars = ['[', ']', "'", '.']
    for i in removeChars : 
        text = text.replace(i, '')
    return text

def clearCountryDB(cursor):
    return cursor.execute("truncate table country")

def main():
    print("Ország szám: ", countCountry())
    connectToDB()
    
main()
