import re

def parse_phone_number(text:str):
    '''
    please add here your regular expression function that catches Dutch phone numbers in international format
    and returns them as a list (e.g., ['+3112345689', '+31987654321']).
    '''

    # using this regular expression find phone number in text
    # start with +31, optionally followed by (0)
    # and contain digits, spaces, or dashes
    # with at least 9 characters after +31
    find_phone_number= r'\+31(?:\(0\))?[\d\s-]{9,}'

    # find all possible phone number in text
    results = re.findall(find_phone_number, text)
    #return final phone numbers as a list
    final_numbers = []

    for result in results:
        # delete (0) if there is
        cleaned_number = re.sub(r'\(0\)', '', result)
        # check every phone number's format and if right add it into the list
        if re.match(r'^\+31[\d\s-]{9,}$', cleaned_number):
            final_numbers.append(result)
        else:
            print(f"invalid phone number format: {result}")

    return final_numbers

def parse_url(text:str):
    '''
    please add here your regular expression function that catches web links (url's)
    and returns them as a list (e.g., ['rug.nl', 'www.google.com']).
   '''
    #start with "https://"
    #followed by website name and a dot and then a domain name
    #then followed by path name as optionally part
    find_url = r'(https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[\w./?&=%#-]*)?|[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[\w./?&=%#-]*)?)'

    # find all possible url in text
    raw_results = re.findall(find_url, text)
    #Delete punctuation at the end
    results = [re.sub(r'[.,!?;:]+$', '', url) for url in raw_results]
    return results
