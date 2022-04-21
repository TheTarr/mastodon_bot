# Python program to demonstrate
# command line arguments
 
import sys
import requests

# Post a request and get response
def requests_form(url, text):
    data = {'language': 'en-US', 'text': text}
    response = requests.post(url, data)
    return response


# Get the 'matches' field of the response
def process_response(response):
    raw_res = response.json()
    res = raw_res['matches']
    return res


def compare_text(text, res):
    compare = ''
    pre = 0
    after = 0
    for i in range(len(res)):
        after = res[i]['length'] + res[i]['offset']
        compare += text[pre:after]
        if res[i]['replacements'] and res[i]['rule']["id"] != "WRONG_APOSTROPHE":
            temp = '[' + str(res[i]['replacements'][0]['value']) + ']'
            compare += temp
        else:
            compare += '[NO SUGGEST VALUE]'
        pre = after
    compare += text[after:]
    return compare

if __name__ == "__main__":
    url = "https://api.languagetoolplus.com/v2/check"
    text = sys.argv[1]
    # text = '<p><span class="h-card"><a href[ref]="https://bgme.me/@ciao" class="u-url[usual] mention">@<span>ciao</span></ a></span> Check the grammar for me. she and I go to school.</p >'
    clean_text = text[107:]
    clean_text = clean_text[:-4]
    response = requests_form(url, clean_text)
    try:
        res = process_response(response)
        compared_text = compare_text(clean_text, res)
        print(compared_text)
    except:
        print("=============================problem==========================")
        print(text)