# This python3 script takes in a list of file names
# e.g. python script.py file.jpg file2.jpg
# e.g. python3 script.py *.jpg # all files in directory
# it pads out those photos, to match the closest of a list of aspect ratios
# then saves the output
# I haven't tried it with formats other than jpg, but it should work

from PIL import Image
import sys
import pprint as pp
from math import ceil

# pass in a file name
# the new file will be saved at newFname(fname)
# ratios is a list of aspect ratios (floats)
def fixImage(fname,ratios):
    print("Fixing image %s" % fname)
    original_im = Image.open(fname)
    original = {
        'width': original_im.size[0],
        'height': original_im.size[1],
    }
    original['big'] = max(original['width'],original['height'])
    original['small'] = min(original['width'],original['height'])
    original['ratio'] = original['big'] / original['small']
    print("original")
    pp.pprint(original)

    flip = lambda r: r if r >= 1 else 1/r
    ratios = [flip(r) for r in ratios]
    deltas = [abs(r - original['ratio']) for r in ratios]
    chosen_ratio = [r for (r,d) in zip(ratios,deltas) if d == min(deltas)][0]


    new = {'ratio':  chosen_ratio}

    if original['ratio'] > new['ratio'] :
        # we need to extend the shortest dimension
        new['big'] = original['big']
        new['small'] = ceil(new['big'] / new['ratio'])
    else:
        # we need to extend the longest dimension
        new['small'] = original['small']
        new['big'] = ceil(new['small'] * new['ratio'])

    for x in ['big','small']:
        assert(new[x] >= original[x])

    if original['width'] == original['big']:
        new['width'] = new['big']
        new['height'] = new['small']
    else:
        new['width'] = new['small']
        new['height'] = new['big']

    print("new")
    pp.pprint(new)

    new_im = Image.new('RGB',
                       (new['width'], new['height']),   
                       (255, 255, 255))  # White

    new_im.paste(original_im, original_im.getbbox())
    new_im.save(newFname(fname))

def newFname(fname):
    return(fname.replace('.','-padded.')) # assumes there is only 1 dot in the file name

if __name__ == '__main__':
    paper_sizes = [(10,13.5),(10,15)] # standard photo paper sizes (cm)
    ratios = [max(s)/min(s) for s in paper_sizes]
    for fname in sys.argv[1:]:
        print("arg: " + fname)
        fixImage(fname,ratios)
