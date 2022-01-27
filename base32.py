def base32(text):
    result = []
    for texts in [text[i:i + 5] for i in range(0, len(text), 5)]:
        characters = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F',
                      '6': 'G', '7': 'H','8':'I','9':'J','10':'K','11':'L',
                      '12':'M', '13':'N','14':'O','15':'P','16':'Q','17':'R',
                      '18':'S','19':'T','20':'U','21':'V','22':'W','23':'X',
                      '24':'Y','25':'Z','26':'2','27':'3','28':'4','29':'5',
                      '30':'6','31':'7','=':'='}
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
