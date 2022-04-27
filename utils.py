import json
import json_lines
import pickle
import string
import re


def read_reference(data_path):
    data = []
    with open(data_path, 'rb') as f:
        for line in json_lines.reader(f):
            data.append(line)
    return [line['answers'] for line in data]


def read_predictions(data_path):
    data = open(data_path).readlines()
    return [line.rstrip('\n') for line in data]


def read_pickle(data_path):
    with open(data_path, 'rb') as f:
        data = pickle.load(f)
    return data


def read_json(data_path):
    with open(data_path, 'rb') as f:
        data = json.load(f)
    return data


def normalize_answer(s):
    def remove_articles(text):
        return re.sub(r'\b(a|an|the)\b', ' ', text)

    def white_space_fix(text):
        return ' '.join(text.split())

    def remove_punc(text):
        exclude = set(string.punctuation)
        return ''.join(ch for ch in text if ch not in exclude)

    def lower(text):
        return text.lower()

    return white_space_fix(remove_articles(remove_punc(lower(s))))


def exact_match_score(prediction, ground_truth):
    return normalize_answer(prediction) == normalize_answer(ground_truth)