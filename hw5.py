from collections import Counter
import csv
import json
import pickle
import string


def main(filename):
    all_words = []

    for line in open(filename):
        line = line.strip()
        if not line:
            continue
        for word in line.split():
            word = word.strip(string.punctuation)
            if word:
                all_words.append(word)

    counter = Counter(all_words)

    with open("wordcount.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['word', 'count'])
        writer.writerows(counter.most_common())

    json.dump(list(counter.most_common()), open("wordcount.json", "w"))

    pickle.dump(counter, open("wordcount.pkl", "wb"))


if __name__ == '__main__':
    main("i_have_a_dream.txt")
