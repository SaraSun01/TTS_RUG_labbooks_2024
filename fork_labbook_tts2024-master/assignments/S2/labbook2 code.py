import re

#That's the test_data phone numbers from labbook1
phone_numbers = [
    "+31123456789",
    "+31 50-363-80-04",
    "+31503638004",
    "+31 50 363 80 04",
    "+31(0)58 2055 009"
]

English_number_dic= {
    '0': 'OH',
    '1': 'ONE',
    '2': 'TWO',
    '3': 'THREE',
    '4': 'FOUR',
    '5': 'FIVE',
    '6': 'SIX',
    '7': 'SEVEN',
    '8': 'EIGHT',
    '9': 'NINE',
    '+31': 'PLUS THIRTY ONE'
}
Dutch_number_dic= {
    '0': 'NUL',
    '1': 'ÉÉN',
    '2': 'TWEE',
    '3': 'DRIE',
    '4': 'VIER',
    '5': 'VIJF',
    '6': 'ZES',
    '7': 'ZEVEN',
    '8': 'ACHT',
    '9': 'NEGEN',
    '+31': 'PLUS DERTIG ÉÉN'
}
def verbalize_phone_number(phone_numbers):

    results=[]
    for number in phone_numbers:
        #Making phone numbers only include numbers and '+'
        cleaned_phone_numbers = re.sub(r'[^\d+]', '', number)
        phone_result={'Phone number':cleaned_phone_numbers}

        #Verbalize numbers into English
        #Verbaize '+31' as a whole
        if cleaned_phone_numbers.startswith('+31'):
            process_phone = English_number_dic['+31'] + ' '
            #Processing of numbers after +31
            for digit in cleaned_phone_numbers[3:]:
                process_phone += English_number_dic[digit]+ ' '
            phone_result['English']=process_phone.strip()

        else:
            process_phone = ''
            #If it doesn't start with ‘+31’, then converts the whole number directly
            for digit in cleaned_phone_numbers:
                process_phone+=English_number_dic.get(digit,digit)+' '
            phone_result['English']=process_phone.strip()

        #Same way to verbalize numbers into Dutch
        if cleaned_phone_numbers.startswith('+31'):
            process_phone = Dutch_number_dic['+31'] + ' '
            #Processing of numbers after +31
            for digit in cleaned_phone_numbers[3:]:
                process_phone += Dutch_number_dic[digit] + ' '
            phone_result['Dutch'] = process_phone.strip()

        else:
            process_phone = ''
            # If it doesn't start with ‘+31’, then convert the whole number directly
            for digit in cleaned_phone_numbers:
                process_phone += Dutch_number_dic.get(digit, digit)+' '
            phone_result['Dutch'] = process_phone.strip()

        results.append(phone_result)

    return results

results=verbalize_phone_number(phone_numbers)

for r in results:
    print(r)

def add_pau_and_br(phrase):
    #Separate phrases into words
    words = phrase.split()
    new_phrase = []
    # Check and handle the "+31" prefix in English
    # +31 as an whole for grouping of country codes, followed by a <PAU> tag.
    if words[0]=='PLUS' and words[1]=='THIRTY' and words[2]=='ONE':
        new_phrase.append("PLUS THIRTY ONE <PAU>")
        words=words[3:]
    # Check and handle the "+31" prefix in Dutch
    if words[0]=='PLUS' and words[1]=='DERTIG' and words[2]=='ÉÉN':
        new_phrase.append("PLUS DERTIG ÉÉN <PAU>")
        words=words[3:]
    # Group digits and add <BR> every 3 words
    # Referring the example of digit groupings in AE phone numbers
    for i in range(0,len(words),3):
        new_phrase.append(' '.join(words[i:i+3]))
        if i+3<len(words):
            new_phrase.append('<BR>')

    return ' '.join(new_phrase)
#Process the results in verbalize_phone_number
grouping_results=[]
for result in results:
    #Process the English and Dutch phrases
    english_phrase=result['English']
    dutch_phrase=result['Dutch']
    #Apply 'def add_pau_and_br' to both the English and Dutch phrases
    formatted_english=add_pau_and_br(english_phrase)
    formatted_dutch=add_pau_and_br(dutch_phrase)
    #Append formatted results to grouping results
    grouping_results.append({
        'Phone number':result['Phone number'],
        'English':formatted_english,
        'Dutch':formatted_dutch
    })

#Print all formatted results
for gr in grouping_results:
    print(gr)