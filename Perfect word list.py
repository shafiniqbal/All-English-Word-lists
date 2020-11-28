from string import ascii_uppercase
k=''
with open ('Custom Words mid range.csv' , 'w') as wf:
    for i in ascii_uppercase:
        readfile = 'words csv\\'+i+'word.csv'
        with open (readfile , 'r') as rf:
            for i in rf:
                if ' ' in i.rstrip() or '-' in i or "'" in i or '"' in i or '#' in i:   
                    continue
                elif 6 < len(i) < 14 :             # length of words
                    if k == i:                     # to remove repeated ones
                        continue
                    else:
                        wf.write(i.rstrip()+'\n')
                        k=i
                        # nothong added
