import sys
import pymysql
import json
import requests


def _connect_db(host, port, user, password, db):
    return pymysql.connect(host=host,
                           port=port,
                           user=user,
                           password=password,
                           db=db,
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

def _cursor_execute(conn, *sql):
    rcount, cursor = (-1, None)
    try:
        cursor = conn.cursor()
        rcount = cursor.execute(*sql)
        conn.commit()
    except Exception, e:
        print("[*] Error when executing sql %s, %s" % (sql, e))
    return rcount, cursor

def main():
    es_url = "http://localhost:9200"
    session = requests.Session()
    session.headers.update({'content-type': 'application/json'})
    db_name = "test"
    conn = _connect_db("localhost", 3306, "root", "", db_name)
    tables = ["test1", "test2"]
    for table in tables:
        print("[*] copy data for %s" % table)
        sql = "select * from {}".format(table)
        count, cursor = _cursor_execute(conn, sql)
        total = 0
        error = 0
        for d in cursor.fetchall():
            r = session.post(es_url+"/"+db_name+"_"+"table"+"/data", data=json.dumps(d))
            if r.status_code == requests.codes.created:
                total += 1
            else:
                print(json.dumps(d, indent=2))
                print(r.text)
                error += 1
        print("[*] %d records copied, %d records failed to copy" % (total, error))


if __name__=="__main__":
    sys.exit(main())