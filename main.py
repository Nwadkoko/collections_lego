import csv
import os
import requests

from bottle import route, run, view, request, static_file, redirect

from dotenv import load_dotenv

load_dotenv()

collections_path = os.getcwd() + '/data'


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')


@route('/')
@view('index')
def view_collection():
    """Index."""


@route('/sets')
@view('sets')
def view_collection():
    """View owned sets."""

    items = []

    with open(collections_path + "/lego.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            if row[3] != "Collectable Minifigures":
                items.append(row)

    return locals()


@route('/minifigures')
@view('minifigures')
def view_collection():
    """View owned minifigures."""

    items = {}

    with open(collections_path + "/lego.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:

            if row[3] == "Collectable Minifigures":
                if row[7] in items.keys():
                    newArray = items[row[7]]
                    newArray.append(row)
                    items[row[7]] = newArray
                else:
                    items[row[7]] = [row]

    items = items.items()

    return locals()


@route('/add', method='POST')
def add_new_item():
    """Add a new item to the collection."""

    item = request.forms.get("item")

    already_exist = False

    api_endpoint = os.getenv('API_ENDPOINT')
    api_key = os.getenv('API_KEY')
    api_username = os.getenv('API_USERNAME')
    api_password = os.getenv('API_PASSWORD')

    params = {'apiKey': api_key, 'username': api_username,
              'password': api_password}

    r = requests.get(url=api_endpoint + '/login', params=params)

    user_hash = r.json()['hash']

    with open(collections_path + "/lego.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            if row[0] == item:
                already_exist = True

    if not already_exist:
        params_id = "{'setNumber':'" + item + "'}"
        params = {'apiKey': api_key,
                  'userHash': user_hash, 'params': params_id}

        r1 = requests.get(url=api_endpoint + '/getSets', params=params)
        response = r1.json()
        print(response)
        if response['status'] == 'success' and response['matches'] == 1:

            rows = [[item, response["sets"][0]["name"], response["sets"][0]["year"], response["sets"][0]["theme"],
                     response["sets"][0]["pieces"], response["sets"][0]["image"]["imageURL"],
                     response["sets"][0]["bricksetURL"], response["sets"][0]["subtheme"]]]
            with open(collections_path + "/lego.csv", 'a+', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(rows)

    redirect('/')


@route('/<collection>/remove/<item>')
def remove_item(collection="none", item="none", method="POST"):
    """Remove an entry in a collection"""

    if collection == 'lego.csv':

        rows = []

        with open(collections_path + "/" + collection, 'r') as csvfile:
            csvreader = csv.reader(csvfile)

            for row in csvreader:
                if row[0] != item:
                    rows.append(row)

        with open(collections_path + "/" + collection, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(rows)

    redirect('/')


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
