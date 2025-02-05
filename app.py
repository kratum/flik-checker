from flask import Flask, request, jsonify, render_template
import requests
from xml.etree import ElementTree as ET

app = Flask(__name__)

def check_flik_in_wfs(flik):
    wfs_url = "https://www.wfs.nrw.de/umwelt/elwas-duengeverordnung_wfs"
    typename = "elwas_duengeverordnung_wfs:nitratbelastete_gebiete_feldbloecke"

    params = {
        "service": "WFS",
        "version": "1.1.0",
        "request": "GetFeature",
        "typename": typename,
        "filter": f"<Filter><PropertyIsEqualTo><PropertyName>FLIK</PropertyName><Literal>{flik}</Literal></PropertyIsEqualTo></Filter>"
    }

    try:
        response = requests.get(wfs_url, params=params)
        response.raise_for_status()
        
        tree = ET.fromstring(response.content)
        features = tree.findall(".//{http://www.opengis.net/gml}featureMember")
        return {"success": True, "result": len(features) > 0}
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_flik', methods=['POST'])
def check_flik():
    data = request.get_json()
    flik = data.get('flik')
    
    if not flik:
        return jsonify({"success": False, "error": "No FLIK provided"})
    
    result = check_flik_in_wfs(flik)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
