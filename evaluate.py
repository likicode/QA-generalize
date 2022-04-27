import os
import argparse

from utils import *

DIRNAME = os.path.dirname(os.path.abspath(__file__))
REFERENCE_PATHS = {
    'triviaqa': os.path.join(DIRNAME, 'open_domain_qa_data/triviaqa_test.jsonl'),
    'naturalquestions': os.path.join(DIRNAME, 'open_domain_qa_data/nq_test.jsonl'),
    'webquestions': os.path.join(DIRNAME, 'open_domain_qa_data/webquestions_test.jsonl'),
}
ANNOTATION_PATHS = {
    'triviaqa': os.path.join(DIRNAME, 'annotations/tqa_test_subset.json'),
    'naturalquestions': os.path.join(DIRNAME, 'annotations/nq_test.json'),
    'webquestions': os.path.join(DIRNAME, 'annotations/webq_test.json'),
}

ANNOTATIONS = [
    'total',
    'overlap',
    'comp_gen',
    'novel_entity'
]


def get_score(select_idx, predictions, references):
    labels = []
    assert len(predictions) == len(references)
    for i in select_idx:
        if max([exact_match_score(predictions[i], ga) for ga in references[i]]):
            labels.append(True)
        else:
            labels.append(False)

    em_score = sum(labels) / len(labels)
    return labels, em_score


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--predictions', type=str, default='predictions/test.dpr.nq.txt')
    parser.add_argument('--dataset', type=str, default='naturalquestions')

    args = parser.parse_args()

    answer_predictions = read_predictions(args.predictions)
    references = read_reference(REFERENCE_PATHS[args.dataset])
    annotated_data = read_json(ANNOTATION_PATHS[args.dataset])

    for annotation_label in ANNOTATIONS:
        if annotation_label == 'total':
            _, em_score = get_score(range(len(answer_predictions)), answer_predictions, references)
        else:
            select_idx = [item['id'] for item in annotated_data if item['labels'] == [annotation_label]]
            _, em_score = get_score(select_idx, answer_predictions, references)

        print('-' * 20)
        print('label:', annotation_label)
        print('Exact Match Score:', em_score)
