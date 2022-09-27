import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text = text = """
I. Introduction
In 2000, Raina decided to play cricket and subsequently moved from his hometown Muradnagar, Ghaziabad district to Lucknow, to attend the Guru Gobind Singh Sports College, Lucknow.[16] He rose to become the captain of the Uttar Pradesh U-16s and came to prominence amongst Indian selectors in 2002 when he was selected at the age of 15 and a half years for the U-19 tour to England, where he made a pair of half-centuries in the U-19 Test matches.[18] He toured Sri Lanka later that year with the U-17 team.

He made his Ranji Trophy debut for Uttar Pradesh against Assam in February 2003 at the age of 16 but did not play another match until the following season. He debuted in List A Cricket against Madhya Pradesh at Indore in 2005 and scored 16 runs.[19] He played for India green, UP under 16, India Blue, India Red, Rest of India, India under 19, Indian board's president's XI, Rajasthan Cricket association's president's XI, India seniors, Central zone.[20] In Ranji trophy 2005-06 season he scored 620 in 6 games.[21] In 2018 Akshdeep Nath replaced him as UP's Ranji trophy captain due to poor performance of scoring 105 runs in 9 innings averaging 11.66.[22]

In late 2003, he toured Pakistan for the U-19 Asian ODI Championship before being selected for the 2004 U-19 World Cup, where he scored three half-centuries, including a 90 scored off only 38 balls. He was then awarded a Border-Gavaskar scholarship to train at the Australian Cricket Academy and in early 2005, he made his first-class limited overs debut, and scored 645 runs that season at an average of 53.75.[23]"""             
stopwords = list(STOP_WORDS)
    
nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
tokens = [token.text for token in doc]
    
word_frequencies = {}
    
for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1
                    
                    
max_frequency = max(word_frequencies.values())
    
for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency
    
sentence_tokens = [sent for sent in doc.sents]
    
sentence_scores = {}
for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.text.lower()]
                    
from heapq import nlargest
select_length = int(len(sentence_tokens)*0.3)
    
summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)

final_summary = [word.text for word in summary]
summary = ' '.join(final_summary)
print(summary)