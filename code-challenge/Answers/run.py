import time
from utils import *
from sql_queries import sql_strings

if __name__ == "__main__":
    start_time = time.time()

    # create database schema and tables if not yet exist.
    db_create_schema()

    tables = ['table1', 'table2', 'table3', 'table4']
    for table in tables:
        # import csv files 
        csv_data = csv_parse('../Data/' + table + '.csv')
        
        if table == 'table3':
            new_data = []
            for t in csv_data:
                tlist = list(t)
                tlist[1] = date_format(tlist[1])
                new_data.append(tuple(tlist))
            csv_data = new_data

        # insert csv data into database tables
        db_insert(sql_strings.get(table + '_sql_insert'), csv_data)
        print("\nSUCCESS: %s rows inserted into %s" % (len(csv_data), table))

    print("\n\n---Runtime: %s seconds ---" % (time.time() - start_time))