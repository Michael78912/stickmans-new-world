import argparse
parser = argparse.ArgumentParser()
parser.add_argument('echo', help='output the string specified')
args=parser.parse_args()
print(args.echo)
