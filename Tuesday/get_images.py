# for downloadding images
import requests
import shutil

# for parsing the csv file
import csv


# convert coordinates from csv in hh:mm:ss.ms format to degrees
def time_to_deg(t):
    (h, m, s) = t.split(':')
    mult = 1
    if h[0] == "-": mult = -1
    return int(h) + mult * int(m) / 60. + mult * float(s) / 3600.


# convert right ascension from hh:mm:ss.ms to degrees
def get_ra(t):
    return time_to_deg(t) * 15


def download_image(name, ra, dec):
    image_url = "http://skyservice.pha.jhu.edu/DR7/ImgCutout/getjpeg.aspx?ra=" + ra + "&dec=" + dec + "&scale=0.2&width=120&height=120"
    # print ra, dec, image_url
    resp = requests.get(image_url, stream=True)
    local_file = open('GalaxyZoo/' + name + '.jpg', 'wb')
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, local_file)
    del resp


# read in csv
hnd = open("GalaxyZoo/training_data.txt", "w+")
hnd.write("[\n")
with open('GalaxyZoo/GalaxyZoo1_DR_table2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    entry = 0
    max_number = 100000
    for row in csv_reader:
        if entry % 100 == 0:
            print entry
        if entry == 0:  # skip header
            entry += 1
            continue
        elif entry > max_number:
            break
        else:
            ra, dec = str(get_ra(row[1])), str(time_to_deg(row[2]))
            download_image(row[0], ra, dec)
            training_row = [row[0], int(row[13]), int(row[14]), int(row[15])]
            hnd.write(str(training_row))
            if entry <= max_number: hnd.write(",\n")
            entry += 1

hnd.write("]\n")
hnd.close()