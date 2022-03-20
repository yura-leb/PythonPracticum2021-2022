import argparse
import ast
import re
import textdistance
import difflib

def get_pill(text):
    tokens = re.findall(r'[A-Z][\w_]*\(|,|\)', ast.dump(ast.parse(text)))
    for token in tokens:
        if len(token) > 1:
            token = token[0] + token[-1]
    return ''.join(tokens)


parser = argparse.ArgumentParser()
parser.add_argument("filename1", type=str, help='First input file')
parser.add_argument("filename2", type=str, help='Second input file')
args = parser.parse_args()
with open(args.filename1) as file_1:
    with open(args.filename2) as file_2:
        text1 = file_1.read()
        text2 = file_2.read()
        pill1 = get_pill(text1)
        pill2 = get_pill(text2)
        if textdistance.damerau_levenshtein.normalized_distance(pill1, pill2) <= 0.1:
            print("Plagiarism detected")
            diff = difflib.HtmlDiff(tabsize=4)
            no_comments1 = ast.unparse(ast.parse(text1))
            no_comments2 = ast.unparse(ast.parse(text2))
            diff_html = diff.make_file(no_comments1.split('\n'), no_comments2.split('\n'), args.filename1, args.filename2)
            with open('diff.html', 'w') as html:
                html.write(diff_html)
        

