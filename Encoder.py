import argparse
import base64

parser = argparse.ArgumentParser(description='Convert python script to multilevel base64 encoded script')
parser.add_argument('code', nargs='?', type=argparse.FileType('r'))
parser.add_argument('-o','--output', nargs='?', type=argparse.FileType('w'))
parser.add_argument('level', type=int, help='Number of levels of encoding')

args = parser.parse_args()
level = args.level
code = args.code.read()

def encodeCode(c):
    c = str.encode(c)
    ce = base64.b64encode(c)
    return ce.decode('UTF-8')

snip="""
eval(compile(base64.b64decode(b'{}'), "<string>", 'exec'))"""


for i in range(level):
    print('Completed {0:.2f}%'.format((i+1)*100/level))
    code = snip.format(encodeCode(code))

code = 'import base64'+code
if args.output:
    if '.py' == args.output.name[-3:]:
        args.output.write(code)
    else:
        print('Invalid file')
else:
    f = open('.'.join(args.code.name.split('.')[:-1])+'_encoded.py','w')
    print('New file saved in '+'.'.join(args.code.name.split('.')[:-1])+'_encoded.py')
    f.write(code)
    f.close()