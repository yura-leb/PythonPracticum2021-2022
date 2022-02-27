import ipsedixit
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('number', type=int, help='Number of paragraphs')
parser.add_argument('dict', type=str, nargs='?', help='Dictionary to get words from')
args = parser.parse_args()
if not args.dict:
    generator = ipsedixit.Generator()
elif args.dict in ('caesar', 'tacitus'):
    generator = ipsedixit.Generator(args.dict)
else:
    try:
        with open(args.dict, 'r') as text_file:
            text = text_file.read()
        generator = ipsedixit.Generator(text)
    except FileNotFoundError:
        print(f'File {args.dict} not found')
paragraphs = generator.paragraphs(args.number)
print('\n\n'.join(paragraphs))
