import re

replacement_dict = {
    r'a\\': 'ă',
    r'i\\': 'ĭ',
    r'o\\': 'ŏ',
    r'e\\': 'ĕ',
    r'u\\': 'ŭ',
    r'ơ\\': 'ơ̆',
    r'ư\\': 'ư̆',
    r'a\|': 'Ă',
    r'i\|': 'Ĭ',
    r'o\|': 'Ŏ',
    r'e\|': 'Ĕ',
    r'u\|': 'Ŭ',
    r'ơ\|': 'Ơ̆',
    r'ư\|': 'Ư̆',
    r'e#': 'ê̆',
    r'o#': 'ô̆',
    '`': 'ñ',
    '~': 'Ñ',
    r'\^': 'ĭ',
    r'&': 'Ĭ',
    r'\[': 'ƀ',
    r'\{': 'Ƀ',
    r'\]': 'č',
    r'\}': 'Č'
}

# Function to replace all special character escape sequences
def replace_special_characters(text, replacement_dict):
    for key, value in replacement_dict.items():
        text = re.sub(key, value, text)
    return text

def convert_special_characters(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    new_content = replace_special_characters(content, replacement_dict)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(new_content)

# Example usage
convert_special_characters('bahnar.txt', 'bahnar-converted.txt')



