from flask import Flask, jsonify
from flask_cors import CORS
import pymysql

app=Flask(__name__)
CORS(app)

def connect():
    con=pymysql.connect(host='localhost',user='root',password='',db='fortinet',cursorclass=pymysql.cursors.DictCursor)
    return con

@app.route("/getall", methods=['GET'])
def getall():
    con=connect()
    cur=con.cursor()
    cur.execute("SELECT a.*,b.Address FROM fortinet.restaurants a,fortinet.restaurant_address b where a.`Restaurant ID`=b.`Restaurant ID`;")
    res=cur.fetchall()
    k=[]
    cui=[]
    for i in res:
        cui=cui+str(i['Cuisines']).split(", ")
        i['Rating color']=str(i['Rating color']).replace(" ","")
        i['Cuisines']=str(i['Cuisines']).split(", ")
        k.append(i)
    cui=list(set(cui))
    cui.sort()
    cui.remove("")
    return jsonify({'res':k,'cui':cui})


if __name__=='__main__':
    app.run(debug=True)