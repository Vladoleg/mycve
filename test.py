from pprint import pprint
from flask import Flask, render_template, url_for
from pymongo import MongoClient
import datetime as dt

# connecting to mongo db
client = MongoClient("mongodb://185.250.21.34:56454/?compressors=disabled&gssapiServiceName=mongodb")
my_db = client.cvedb
collection = my_db.cves


#static variables for tables and menu
fields = ['id', 'assigner', 'Published', 'Modified', 'last-modified', 'summary', 'impactScore', 'impactScore3', 
        'expoitabilityScore', 'expoitabilityScore3', 'references', 'vendors', 'cwe', 'vulnerable_configuration_cpe_2_2']
vendors = [
    {'name': 'huawei', 'url': 'huawei'},
    {'name': 'dell', 'url': 'dell'},
    {'name': 'redhat', 'url': 'redhat'},
    {'name': 'vmware', 'url': 'vmware'},
    {'name': 'veeam', 'url': 'veeam'},
    {'name': 'netapp', 'url': 'netapp'},
    {'name': 'lenovo', 'url': 'lenovo'},
    {'name': 'fujitsu', 'url': 'fujitsu'},
    {'name': 'juniper', 'url': 'juniper'},
    {'name': 'mikrotik', 'url': 'mikrotik'},
    {'name': 'intel', 'url': 'intel'}
]
params = ['Last 20', 'week', 'month', 'year']

#static variables for timelimits
now = dt.datetime.today()
week = now - dt.timedelta(days=7)
month = now - dt.timedelta(days=30)
year = now - dt.timedelta(days=365)
t = [week, month, year]



#app function
app = Flask(__name__)
elem=[]
li={'id':1, 'Published':1, 'vendors':1, 'last-modified':1,'_id':0}
'''for i in collection.find({'vendors': 'fujitsu'}, li).limit(15):
    elem.append(i)
    pprint (elem)
'''
def count_20(vendor):
    x = 0
    for i in collection.find({'vendors': vendor}, li).limit(20):
        elem.append(i)
        x = x+1
    pprint (elem)
    print (x)


chas = input('Enter a number  :')

def my_all(vendor, chas):
    x = 0
    if chas=='week': c=0
    elif chas=='month': c=1
    elif chas=='year': c=2
    for i in collection.find({'$and':[{'last-modified':{'$gt':t[c]}}, {'vendors': vendor}]}, li):
        elem.append(i)
        x = x+1
    pprint(elem)
    print (x)



my_all('huawei', chas)

'''count_20('huawei')'''

'''my_year('redhat')'''

'''
@app.route("/")
def index():
    return render_template("index.html", vendors=vendors, params=params)

if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port=5001)
'''