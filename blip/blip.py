import argparse

parser = argparse.ArgumentParser(description='B(itf)lip a string to all its variants, for science.')
parser.add_argument('-s', required=True, type=str, help='String you want to blip')
parser.add_argument('--ascii', action='store_true', help='Print ASCII strings only')
parser.add_argument('--no-caps', action='store_true', help='Remove case by lowering, remember all caps when you spell the man name')

"""
Converts a binary string of 0s and 1s
back to its character
"""
def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

"""
Have to do a deep copy here with list(s) so we dont
edit s accidentally
"""
def replace_char_at(s, index, char):
    s_list = list(s)
    s_list[index] = char
    return ''.join(s_list)

"""
Shamelessly stolen from a few answers on SO
and constructed here for science
"""
def get_blips(s):
    flip_dict = {
        '0': '1',
        '1': '0'
    }
    blips = []
    binary = [format(ord(x), '08b') for x in s]
    blips.append(binary)
    for i,byte in enumerate(binary):
        for n,bit in enumerate(byte):
            temp_binary = binary[:]
            temp_byte = replace_char_at(byte, n, flip_dict[bit])
            temp_binary[i] = temp_byte
            blips.append(temp_binary)
    return blips

"""
Returns ASCII only strings, useful for
attack scenarios where you can only use ASCII
characters (like package managers)
"""
def get_ascii(l):
    return [
        blip for blip in l if blip.isascii()
    ]

"""
Lowercase all blips
"""
def scrub_nocap(l):
    lowered = [blip.lower() for blip in l]
    return list(set(lowered))

"""
Take each blip, join them and remove the space
between bytes and then decode back to a string
"""
def get_string_blips(l):
    return [
        decode_binary_string(''.join(blip)) for blip in l
    ]

def main():
    args = parser.parse_args()
    target_string = args.s
    print_ascii = args.ascii
    no_caps = args.no_caps
    binary_blips = get_blips(target_string)
    blips = get_string_blips(binary_blips)
    if print_ascii:
        blips = get_ascii(blips)
    if no_caps:
        blips = scrub_nocap(blips)
    for blip in blips:
        print('%s' % (blip))

if __name__ == '__main__':
    main()
