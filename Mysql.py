import mysql.connector

conn = mysql.connector.connect(
    user='utp'
    , password='utp'
    , host='100.84.72.40'
    , port='3301'
    , database='utp_dsp'
    , use_unicode=False
    , charset='utf8')

cur = conn.cursor();
cur.execute("SET NAMES utf8");
cur.execute("select * from utp_content_asset limit 2")

print cur.column_names
print cur.rowcount
for i in cur:
    print i
    for j in i:
        print j,
    print "\n"

cur.close()
conn.close()