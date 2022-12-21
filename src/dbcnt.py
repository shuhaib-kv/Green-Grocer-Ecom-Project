def selectall(qry):
    import pymysql
    con=pymysql.connect(host='localhost',port=3306,user='root',password='',db='green grocer')
    cmd=con.cursor()
    cmd.execute(qry)
    res=cmd.fetchall()
    return res
def selectall2(qry,val):
    import pymysql
    con=pymysql.connect(host='localhost',port=3306,user='root',password='',db='green grocer')
    cmd=con.cursor()
    cmd.execute(qry,val)
    res=cmd.fetchall()
    return res
def selectone(qry,val):
    import pymysql
    con = pymysql.connect(host='localhost', port=3306, user='root', password='', db='green grocer')
    cmd = con.cursor()
    cmd.execute(qry,val)
    res = cmd.fetchone()
    return res
def iud(qry,val):
    import pymysql
    con = pymysql.connect(host='localhost', port=3306, user='root', password='', db='green grocer')
    cmd = con.cursor()
    cmd.execute(qry, val)
    res = cmd.lastrowid
    con.commit()
    return res