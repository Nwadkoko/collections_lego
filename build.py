import csv
import os
import shutil

collections_path = os.getcwd() + '/data'

htmlHead = """
    <!DOCTYPE html>
        <html lang='fr-FR'>
            <head>
                <meta charset='UTF-8'>
                <meta http-equiv='X-UA-Compatible' content='IE=edge'>
                <meta name='viewport' content='width=device-width, initial-scale=1.0'>
                <title>Les LEGO</title>
                <link rel='stylesheet' href='styles.css'>
                <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'>
            </head>
            <body>
                <header>
                    <h1>My LEGO's Collection</h1>
                </header>
    """

htmlFooter = """
            </body>
        </html>
    """


def generate_index():

    htmlBody = """
    <main>
        <nav>
            <a href="/sets">Sets</a>
            <a href="/minifigures">Minifigures</a>
        </nav>
    </main>
    """

    htmlfile = open("public/index.html", "w")
    a = htmlfile.write(htmlHead + htmlBody + htmlFooter)
    htmlfile.close()

    source = "static/styles.css"
    destination = "public/styles.css"
    shutil.copy(source, destination)


def generate_sets_list():

    items = []

    htmlBody = """<main><ol>"""

    with open(collections_path + "/lego.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        for item in csvreader:

            if item[3] != "Collectable Minifigures":

                htmlBody += "<li><div class='img-container'><img src='" + \
                    item[5] + "'></div>"
                htmlBody += "<div class='text-btn-container'><h2>" + \
                    item[1] + "</h2>"
                htmlBody += "<div class='btn-container'><a href='https://brickset.com/sets/" + \
                    item[0]
                htmlBody += "' target='_blank'><i class='fa fa-link'></i></a></div></div></li>"

                items.append(item)

    htmlBody += "</ol></main></body>"

    htmlfile = open("public/sets.html", "w")
    a = htmlfile.write(htmlHead + htmlBody + htmlFooter)
    htmlfile.close()


def generate_minifig_list():

    items = {}
    itemsToReturn = []

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

    htmlBody = """<main><ol>"""

    for item in items:

        htmlBody += "<h2 class='minifig-collection-heading'>" + \
            item[0] + "</h2>"

        for minifig in item[1]:

            htmlBody += "<li><div class='img-container'><img src='" + \
                minifig[5] + "'></div>"
            htmlBody += "<div class='text-btn-container'><h2>" + \
                minifig[1] + "</h2>"
            htmlBody += "<div class='btn-container'><a href='https://brickset.com/sets/" + \
                minifig[0]
            htmlBody += "' target='_blank'><i class='fa fa-link'></i></a></div></div></li>"

            itemsToReturn.append(item)

    htmlBody += """</ol></main>"""

    htmlfile = open("public/minifigures.html", "w")
    a = htmlfile.write(htmlHead + htmlBody + htmlFooter)
    htmlfile.close()


generate_index()
generate_sets_list()
generate_minifig_list()
