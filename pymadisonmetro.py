#/usr/bin/env python3
import urllib.request
import urllib.error
import json

API_BASE = "http://api.smsmybus.com/"
API_VERSION = "v1"
REQ_URL = API_BASE + API_VERSION + "/"

def GetRoutes(key):
    req_str = "getroutes?key={0}".format(key)
    url = REQ_URL + req_str
    data = _get_json(url)

    routes = None
    if data['status'] != 0:
        errorMsg = data['description']
        raise ValueError(errorMsg)
    else:
        routes = data['routes']

    return routes

def GetArrivals(key, stopID=None, routeID=None, vehicleID=None):
    req_str = "getarrivals?key={0}".format(key)
    if stopID is not None:
        req_str += "&stopID={:04d}".format(stopID)
    if routeID is not None:
        req_str += "&routeID={:02d}".format(routeID)
    if vehicleID is not None:
        req_str += "&vehicleID={:03d}".format(vehicleID)

    url = REQ_URL + req_str
    print(url)
    data = _get_json(url)

    return data

def GetStops(key, routeID, dest):
    pass

def _get_json(url):
    #request = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(url)
    except urllib.error.URLError as error:
        if hasattr(error, 'reason'):
            print("Error: failed to reach the SMSMyBus server.")
            print("Reason: ", error.reason)
        elif hasattr(error, 'code'):
            print("Error: the server couldn\'t fulfill the request.")
            print("Error code: ", error.code)

    #data = _parse_response(response)
    #return data
    return _parse_response(response)

def _parse_response(response):
    response_text = response.read().decode()
    return json.loads(response_text)
