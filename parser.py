import nltk
import ssl
from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords                       
from nltk.tokenize import word_tokenize, sent_tokenize                             
from image_gen import imageGen

import json             

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("slauw87/bart_summarisation")
model = AutoModelForSeq2SeqLM.from_pretrained("slauw87/bart_summarisation")


try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# nltk.download('stopwords')

def pos_tag(sentences):
    pos_tagged_sentences = []
    for sentence in sentences:
        words = word_tokenize(sentence[0].replace(',', ''))
        pos_tagged = nltk.pos_tag(words)
        pos_tagged_sentences.append((pos_tagged, sentence[1]))

    return pos_tagged_sentences

# def ner(sentences):
#     ner_tagged_sentences = []
#     for sentence in sentences:
#         words = word_tokenize(sentence[0])
#         pos_tagged = nltk.pos_tag(words)
#         ner_tagged = nltk.ne_chunk(pos_tagged)
#         ner_tagged_sentences.append(ner_tagged)

#     return ner_tagged_sentences

# Define functions
def main():
    template = '''In a [adj1] world, where [plu1] roam freely and [adj2] [plu2] sing in harmony, there lived a [adj3] [noun1] who dreamed of [vering] to the top of the tallest [noun2].At the top, it turned around looked down'''
    # parse file formData.json
    with open('formData.json') as f:
        data = json.load(f)
        print(data)

    sentences = []
    for sentence in template.split("."):
        # print(sentence)
        insertedIndices = []
        sentence = sentence.replace(",", "").split(" ")
        for wordIndex in range(len(sentence)):
            if sentence[wordIndex][1:-1] in data:
                insertedIndices.append(wordIndex + 1)
                sentence[wordIndex] = data[sentence[wordIndex][1:-1]].lower()

        sentences.append((" ".join(sentence) + " .", insertedIndices))
    
    print(sentences)
    # sentences = []


    # sentences = [
    # ("I decided to go on a vacation to Australia with a ball.", [11]),
    # ("We got to the airport 32 hours early.", [6]),
    # ("When we went through security, I got stopped because I forgot to take pillow out of my pocket.", [14]),
    # ("We got some pizza for the flight and arrived at the gate.", [4]),
    # ("Once we boarded the plane, I was sitting next to a very old man.", [13]),
    # ("He spent the entire flight swimming and talking about his job doing chores.", [6, 13]),
    # ("Whenever I tried to sleep, he would step around me to go to the pool.", [15]),
    # ("I was so jittery.", [4])
    # ("Since I couldn't sleep, I decided to fly and run instead.", [8, 10]),
    # ("Finally, we arrived in Australia.", [])
# ]
    # sentences = [
    #                 ("Sticky day, so I decided to go to the zoo.", [1]),
    #                 ("As soon as I arrived, I saw a Monkey cooking slowly in its enclosure.", [9, 10, 11]),
    #                 ("Next, I headed to the cake exhibit and watched them run crazy.", [6, 11, 12]),
    #                 ("Suddenly, a scared worm appeared out of nowhere and coded after me.", [3, 4, 10, 11])   
    #             ]
    # sentences = [
    #                 ("Bats are so cool!", []),
    #                 ("They are BLUE, NOISY animals which have wings.", [3, 4]),
    #                 ("They like to fly around at NOON which makes some people scared of them.", [7]),
    #                 ("But bats are HAPPY, and they don't want to hurt people.", [4]),
    #                 ("I have a pet bat that lives in ZOO.", [9]),
    #                 ("I like to feed the bat CAKE and PIZZA.", [6, 8]),
    #                 ("He likes to PLAY.", [4]),
    #                 ("I am his favorite person, but he also likes FIDDLE.", [10])
    #             ]

    # sentences = [
    #                 ("Coffeehouses are in!", []),
    #                 ("Gone are the local corner CHINO and the neighborhood ice-cream INVITE.", [6, 11]),
    #                 ("It doesn't matter if you live in a/an HOT city or a/an RARE town; there is bound to be a coffee COTTAGE in your FLIPPED-OUT neighborhood.", [9, 13, 22, 25]),
    #                 ("Coffeehouses have become the place where RICH friends gather, sit, and chew the WATERSPOUT, remembering the good old RAVEN as they sip their steaming cups of coffee.", [7, 14, 19]),
    #                 ("Coffeehouses cater to busy business people, who use them to PUMP million-dollar deals.", [11]),
    #                 ("Coffeehouses are also favorite spots for single men and EASEL artists, who love to linger over their mugs of coffee as they watch the attractive go by, hoping to catch his or her eye, and maybe even FETCH a date.", [38])
    #             ]
    
    # total_text = ""
    # for sentence in sentences:
    #     total_text += (sentence[0]) + " "

    # named entity recognition
    # ner_tagged_sentences = ner(sentences)

    # print(ner_tagged_sentences)

    # Part of Speech Tagging code
    # pos_tagged_sentences = pos_tag(sentences)

    # print(pos_tagged_sentences)

    # posProcessed = []
    # unwantedPos = ["CC", "DT", "EX", "IN", "MD", "PDT", "PRP", "PRP$", "TO", "UH", "WDT", "WP", "WP$", "WRB"]
    # for (sentence, focus_words_indices) in pos_tagged_sentences:
    #     cleanedSentence = ""
    #     focusWords = ""
    #     for i in range(len(sentence)):
    #         pos = sentence[i][1]
    #         if (pos in unwantedPos) and ((i+1) not in focus_words_indices):
    #             continue
    #         else:
    #             cleanedSentence += sentence[i][0] + " "
    #             if (i+1) in focus_words_indices:
    #                 focusWords += sentence[i][0] + "," 
                
    #     posProcessed.append((cleanedSentence, focusWords))

    # condensed = []
    # for i in range(0, len(posProcessed), 2):
    #     newSentences = posProcessed[i][0] + ' ' + posProcessed[i+1][0]
    #     newFocusWords = posProcessed[i][1] + "," + posProcessed[i+1][1]
    #     condensed.append((newSentences, newFocusWords))

    # i = 0
    # for (text, focus_words) in condensed:
    #     imageGen(text, i, focus_words)
    #     i += 1

    # Summarization code
    condensed = []
    for i in range(0, len(sentences), 2):
        focus_words = ""
        cleanedSentence = sentences[i][0].replace(',', '').split(' ')
        for j in sentences[i][1]:
            focus_words += cleanedSentence[j-1].strip(".") + ","

        cleanedSentence = sentences[i+1][0].replace(',', '').split(' ')
        for j in sentences[i+1][1]:
            focus_words += cleanedSentence[j-1].strip(".") + ","

        condensed.append((sentences[i][0] + ' ' + sentences[i+1][0], focus_words))

    print(condensed)

    k = 0
    for i in range(len(condensed)):
        (text, focus_words) = condensed[i]
        prompt1 = f"Summarize the text, focusing on {focus_words}: {text}"
        input_ids1 = tokenizer.encode(prompt1, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids1 = model.generate(input_ids1, max_length=50, min_length=10, length_penalty=2.0, num_beams=5, early_stopping=True)
        summary1 = tokenizer.decode(summary_ids1[0], skip_special_tokens=True)

        if i == 0:
            summary2 = summary1
        else:
            totalContext = ""
            for j in range(i):
                totalContext += condensed[j][0] + " "
            prompt2 = f"Summarize the text: {totalContext}"
            input_ids2 = tokenizer.encode(prompt2, return_tensors="pt", max_length=1024, truncation=True)
            summary_ids2 = model.generate(input_ids2, max_length=50, min_length=10, length_penalty=2.0, num_beams=5, early_stopping=True)
            summary2 = tokenizer.decode(summary_ids2[0], skip_special_tokens=True)


        print(summary1, summary2)
        imageGen(summary1, k, summary2)
        k += 1
        # print("Summary of the text:", summary)

# Main execution
if __name__ == '__main__':
    main()