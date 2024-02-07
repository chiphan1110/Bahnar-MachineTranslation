import re

def remove_header_footer(text):
    text = re.sub(r'LUẬT TỤC BAHNAR\s*', '', text)
    text = re.sub(r'BUÔN KRÔNG THỊ TUYẾT NHUNG \n+\d*','', text)
    return text

def sentence_concat(text):
    lines = text.split('\n')
    concat = []
    for i, line in enumerate(lines):
        if line[0].isdigit() or line[0].isupper():
            if concat == []:
                last_idx = i
            else: 
                lines[last_idx] += ''.join(concat)
                concat.clear()
        else:
            concat.append(line)
            lines[i] = ''
                

    text = '\n'.join(line for line in lines if line != '')
    return text

def remove_empty(text):
    non_empty_lines = [line.lstrip() for line in text.split('\n') if line.strip() != '']
    empty_removed = '\n'.join(non_empty_lines)
    return empty_removed

def separate_language(text):
    bahnar = []
    vietnamese = []
    lines = text.split('\n')

    for i, line in enumerate(lines):
        # if line.startswith('CHƯƠNG') or line.startswith('APĂNG'):
            # continue
        if line.startswith('Điều'):
            processing_bahnar = True 
            bahnar.append(line)
            
        elif re.match(r'^\d+\.', line): 
            if processing_bahnar:
                bahnar.append(line)
            else:
                vietnamese.append(line)
        else:
            processing_bahnar = False
            vietnamese.append(line)
    bahnar = '\n'.join(bahnar)
    vietnamese = '\n'.join(vietnamese)
    return bahnar, vietnamese
       
            

