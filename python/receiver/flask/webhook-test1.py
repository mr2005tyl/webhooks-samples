from flask import Flask, request
#from OpenSSL import SSL
import os
import json

filename = 'C:\\webhook\\webhookPayloads.json' #file that webhook payloads will be written

if os.path.exists(filename):
    append_write = 'a' # append if already exists
else:
    append_write = 'w' # make a new file if not

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        f = open(filename, 'r')
        read = f.read()
        f.close()
        return read

@app.route('/post', methods=['POST'])
def index1():
    if 'alert' in request.args:
        alert = str(request.args['alert'])
        f = open(filename,append_write)
        #req_data = request.get_json()
        #str_obj = json.dumps(req_data)
        f.write(alert+'\n')
        f.close()
        #return '{"success":"true"}'
        return alert

if __name__ == "__main__":   
    #context = ('ssl.cert', 'ssl.key') # certificate and key file. Cannot be self signed certs    
    app.run(host='0.0.0.0', port=5000, threaded=True) # will listen on port 5000
