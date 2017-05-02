import torndb

def get_db():
    return torndb.Connection(host="localhost", database="alex", user="root", password="11111111", time_zone='+8:00')