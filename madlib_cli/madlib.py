import re

print("""Hello, you should enter a series of words depending on the type of word (can be adgective, verb, noun etc..), and the algroithm will place those words in a text and will show the super funny output on the screen\n""")

def read_template(filename: str):
    try:
        with open(filename, 'r') as file:
            file_content = file.read()
        return file_content
    except:
        FileNotFoundError

madlib_text = read_template('assets/madlib.txt')

print(madlib_text + "\n")

def parse_template(string):
    words = re.findall(r'{.+?}', string)
    all_words = []
    for word in words:
        all_words.append(word[1:-1])
    new_string = re.sub(r'{.+?}',r'{}', string)
    return new_string, all_words

parsed_string, all_words = parse_template(madlib_text)

list_word_input = []
for i in range(0,len(all_words)):
    word = input('Please write the words you want to fill ')
    list_word_input.append(word)

def merge(string,list):
    new_string = string.format(*list)
    print(new_string)
    return new_string

print(merge(parsed_string,list_word_input))

