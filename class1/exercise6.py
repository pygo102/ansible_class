import yaml
import json




def output_yaml(data):
    with open('data.yaml', 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
    
    
def output_json(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)




def main():
    sample_data = [
        1, 'two', 3,
        {'a': 1, 'b': 2}
    ]

    output_yaml(sample_data)
    output_json(sample_data)



if __name__ == '__main__':
    main()
