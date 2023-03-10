import os
import spacy

def get_entities(text, language_code):
        
    if language_code.lower() in ['ca', 'hr', 'da', 'nl', 'fi', 'fr', 'de',
                        'el','it', 'ja', 'ko', 'lt', 'mk','nb',
                        'pl','pt','ro','ru','es','sv','uk']:
        model = f"{language_code}_core_news_sm"
    elif language_code.lower() in ['zh', 'en']:
        model = f"{language_code}_core_web_sm"
    else:
        model = f"xx_ent_wiki_sm"
    
    print(f"The Language chosen is {language_code}")
    print(f"The corresponding model is {model} \n")
    
   # Installing the model if not already installed
    try:
        spacy.load(model)
    except:
        print("The package is not installed, so installing")
        install_str = 'python3 -m spacy download ' + model
        os.system(install_str)    
    else:
        print("The package is installed")

    # Loading the spacy model
    NER = spacy.load(model)
    
    # Load the text to NER model
    text = NER(text)

    # Initialize a emtpy entity list
    entity_list = []
    for word in text.ents:

        # Initialize a emtpy entity dict
        entity_dict = {}
        entity_dict['text'] = word.text
        entity_dict['type'] = word.label_
        entity_dict['start_pos'] = word.start_char
        entity_dict['end_pos'] = word.end_char

        entity_list.append(entity_dict)
        
    return entity_list


Sentence = "I work at Amazon for a very long time and Im from India"
get_entities(text=Sentence, language_code="en")
