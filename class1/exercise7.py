import pprint
import json
import yaml


def read_json():
    with open('data.json', 'r') as fp:
       data = json.load(fp)
       print 'json data is:'       
       pprint.pprint(data, width=4)


def read_yaml():
    with open('data.yaml', 'r') as fp:
       data = yaml.load(fp)
       print 'yaml data is:'
       pprint.pprint(data, width=4)
       

def main():
    print '\n'
    read_json()
    print '\n'
    read_yaml()
    

if __name__ == '__main__':
    main()