
def encode(char:str):
    characters = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F',
                    '6': 'G', '7': 'H','8':'I','9':'J','10':'K','11':'L',
                    '12':'M', '13':'N','14':'O','15':'P','16':'Q','17':'R',
                    '18':'S','19':'T','20':'U','21':'V','22':'W','23':'X',
                    '24':'Y','25':'Z','26':'2','27':'3','28':'4','29':'5',
                    '30':'6','31':'7','=':'='}
    result = []
    for texts in [char[i:i + 5] for i in range(0, len(char), 5)]:
        ascii_vals = [ord(s) for s in texts]
        binary_vals = ['{0:08b}'.format(s) for s in ascii_vals]
        group_five = [0,0,0,0,0]
        for i in range(5):
            try:
                group_five[i] = binary_vals[i]
            except IndexError:
                group_five[i] = 'xxxxxxxx'
        five_split = [''.join(group_five)[s:s+5] for s in range(0,40,5)]
        clean = []
        for s in five_split:
            if s:
                if '0' in s or '1' in s:
                    clean.append(s.replace('x','0'))
                else:
                    clean.append(s)
            else:
                clean.append(s)
        clean_with_pads = ['=' if s == 'xxxxx' else s for s in clean]
        decimal_vals = [int(s,2) if s.isdigit() else s for s in clean_with_pads]
        base_32_ify = ''.join([characters[str(s)] for s in decimal_vals])
        result.append(base_32_ify)
    return ''.join(result)


def decode(char:str):
    result = []
    for texts in [char[i:i + 8] for i in range(0, len(char), 8)]:
        characters = {'A': '0', 'B': '1', 'C': '2', 'D': '3', 'E': '4', 'F': '5',
                        'G': '6', 'H': '7', 'I': '8', 'J': '9', 'K': '10', 'L': '11',
                        'M': '12', 'N': '13', 'O': '14', 'P': '15', 'Q': '16', 'R': '17',
                        'S': '18', 'T': '19', 'U': '20', 'V': '21', 'W': '22', 'X': '23',
                        'Y': '24', 'Z': '25', '2': '26', '3': '27', '4': '28', '5': '29',
                        '6': '30', '7': '31', '=': '='}
        l = [s for s in texts]
        un_base_32 = [characters[s] for s in l]
        dec_to_bin = ['xxxxx' if s == '=' else '{0:05b}'.format(int(s)) for s in un_base_32]
        five_to_eight = [''.join(dec_to_bin)[i:i+8] for i in range(0,40,8)]
        clean = []
        for s in five_to_eight:
            if s:
                if 'x' in s:
                    clean.append(s.replace('0','x').replace('1','x'))
                else:
                    clean.append(s)
            else:
                clean.append(s)
        remove_x = [s for s in clean if s != "xxxxxxxx"]
        bin_to_dec = [int(s,2) for s in remove_x]
        dec_to_ascii = [chr(int(i)) for i in bin_to_dec]
        result.append(''.join(dec_to_ascii))
    return ''.join(result)
