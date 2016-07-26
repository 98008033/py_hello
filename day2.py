import cx_Oracle

con = cx_Oracle.connect("pospay/123456@192.168.100.245/trfdb")
cursor = con.cursor ()
cursor.execute ("select count(*),TCPSCOD from stppayinf where ACTDAT between '20160218000000' and '20160418235959' group by TCPSCOD")
row = cursor.fetchall ()
# print(row[0])
for x in row:
    print(x)
cursor.close ()
con.close ()

123