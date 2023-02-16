import spacy

def get_entities(text, language_code):
    
    Sentence = text
    
    if language_code in ['ca', 'hr', 'da', 'nl', 'fi', 'fr', 'de',
                        'el','it', 'ja', 'ko', 'lt', 'mk','nb',
                        'pl','pt','ro','ru','es','sv','uk']:
        model = f"{language_code}_core_news_sm"
    elif language_code in ['zh', 'en']:
        model = f"{language_code}_core_web_sm"
    else:
        model = f"xx_ent_wiki_sm"
    
    
    NER = spacy.load(model)
    text = NER(Sentence)

    entity_list = []
    for word in text.ents:
        print(word.text, word.label_, word.start_char,word.end_char)

        entity_dict = {}
        entity_dict['text'] = word.text
        entity_dict['type'] = word.label_
        entity_dict['start_pos'] = word.start_char
        entity_dict['end_pos'] = word.end_char

        entity_list.append(entity_dict)
        
    return entity_list
  
  
  
Sentence = "I work at Google for a very long time"
get_entities(text=Sentence, language_code="en")
