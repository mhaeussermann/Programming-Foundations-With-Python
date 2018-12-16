import urllib

def read_text():
    quotes = open("/PATH/TO/FILE")
    contents_file = quotes.read()
    quotes.close()
    check_profanity(contents_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity found!")
    elif "false" in output:
        print("No profanity found!")
    else:
        print("There was a error in reading the file")
read_text()
