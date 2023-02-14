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

#app function
app = Flask(__name__)

for i in collection.find({'vendors': 'redhat'}).limit(15):
    pprint (i['id'])


'''
@app.route("/")
def index():
    return render_template("index.html", vendors=vendors, params=params)

if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port=5001)
'''