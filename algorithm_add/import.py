#!/usr/bin/env python3

import argparse
import os
import glob
import urllib
import re


import requests

# Define API Endpoints for Algorithms and Files
URL_ALGORITHMS = '/api/algorithms/store_file'
URL_INPUTFILE = '/api/file-inputs/store_file'

def send(file,url):
        # Check if url is valid (includes http)
        if not re.match(r'http(s?)\:', url):
            url = 'http://' + url


        print("File {0} uploaded using URL {1}\n".format(file,url))
        m = { 'file': open(file,'rb')}

        r = requests.post(url, files=m)
        print("Returned Status code: {0}\n".format(r.status_code))


def main():
    parser = argparse.ArgumentParser(description='Uploads Algorithm Jars or InputFiles to the Metanome platform')
    parser.add_argument('-s','--source', required=True,
                    help='File or Directory to be uploaded to Metanome')
    parser.add_argument('-ip','--ip',  required=True,
                    help='IP and Port of Metanome Backend')
    parser.add_argument('-type','--type',required=True, choices=['algorithm', 'inputfile'],help='Type of the files uploaded can be algorithm or inputfile')
    args = parser.parse_args()

    if args.type == 'algorithm':
        api_endpoint = URL_ALGORITHMS
    else:
        api_endpoint = URL_INPUTFILE

    if os.path.isdir(args.source):
        print("Sending file(s) in directory {0} to IP {1}".format(args.source,args.ip))
        for file in array_filter(glob(args.source), 'is_file'):
            send(file,args.ip + api_endpoint)

    else:
        print("Sending file {0} to IP {1}".format(args.source,args.ip))
        send(args.source,args.ip + api_endpoint)

if __name__ == "__main__":
    main()
