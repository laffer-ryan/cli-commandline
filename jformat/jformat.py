import os
import sys
import json
import argparse
import click


def formatter(string, sort_keys=True, indent=4):
    #load incoming string inot JSON
    loaded_json = json.loads(string)
    #dum as string
    return json.dumps(string, sort_keys=sort_keys, indent=indent)


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option("--sort", "-s", is_flag=True)
def main(path, sort):
    with open(path, 'r') as _f:
        print(formatter(_f.read(), sort_keys=sort))

#ensures that the code block following the condition is executed only when the script is executed directly in the cli
if __name__ == '__main__':
    main()