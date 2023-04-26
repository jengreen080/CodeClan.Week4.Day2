import psycopg2
import psycopg2.extras as ext 

def run_sql(sql, values = None):
    conn = None # connection to database
    results = []
    try:
        conn = psycopg2.connect(dbname = 'music_collection')
        cur = conn.cursor(cursor_factory = ext.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall() # wouldn't do this if you had loads of data. But it's fine for us
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("We messed up:", error)
    finally:
        if conn is not None:
            conn.close()
            
    # return some data
    # in python form
    return results