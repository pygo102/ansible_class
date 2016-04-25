from pprint import pprint
import json
import yaml


def display_json(filename):
    with open(filename, 'r') as fp:        
        data = json.load(fp)
        print 'json data is:'
        pprint(data)


def display_yaml(filename):
    with open(filename, 'r') as fp:        
        data = yaml.load(fp)
        print 'yaml data is:'
        pprint(data)


def main():
    display_json(filename='data.json')
    display_yaml(filename='data.yaml')    


if __name__ == '__main__':
    main()
