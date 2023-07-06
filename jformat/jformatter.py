import os
import sys
import json
import argparse

def formatter(string, sort_keys=True, indent=4):
    #load incoming string inot JSON
    loaded_json = json.loads(string)
    #dum as string
    return json.dumps(string, sort_keys=sort_keys, indent=indent)
    
def main(path, no_sort):
    if no_sort: 
        sort_keys = False
    else:
        sort_keys = True
    with open(path, 'r') as f:
        print(formatter(f.read(), sort_keys=sort_keys))

#ensures that the code block following the condition is executed only when the script is executed directly in the cli
if __name__ == '__main__':
    parser = argparse.ArgumentParser("This is the J format tool")
    #allow us to say by default this is going to be a True boolean when it is being used
    parser.add_argument("--sort", action="store_true", help="set the sorting") 
    args = parser.parse_args()
    main(sys.argv[-1], no_sort=False)