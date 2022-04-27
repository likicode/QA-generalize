# Challenges in Generalization in Open Domain Question Answering

[Challenges in Generalization in Open Domain Question Answering](https://arxiv.org/pdf/2109.01156.pdf). 
In NAACL Findings, 2022.

```
@article{liu2021challenges,
  title={Challenges in Generalization in Open Domain Question Answering},
  author={Liu, Linqing and Lewis, Patrick and Riedel, Sebastian and Stenetorp, Pontus},
  journal={arXiv preprint arXiv:2109.01156},
  year={2021}
}
```

This repository contains the annotated data and evaluation script to reproduce our evaluation methods.


## Resources and Data Format
**decomposed_questions**: Each question is decomposed into the following atoms. We initially depend on these atoms to select candidates for the overlap,
comp-gen, and novel-entity categories based on their definitions.
```
{'id': 0,
 'text': 'who got the first nobel prize in physics',
 'wiki_entities': [['Nobel Prize in Physics', 'nobel prize in physics']],
 'wiki_entities_pos': [('26650', 4, 8)],
 'verb': 'got',
 'other_args': ['first'],
 'answers': ['Wilhelm Conrad Röntgen'],
 'question_word': 'who'}
 
```
**annotations**: Each question is paired with a human verified label ('overlap', 'comp_gen', 'novel_entity'). The evaluations should be made according to these labels.

**open_domain_qa_data**: Test set with reference answers for each dataset.

**predictions**: Sample predictions from [DPR](https://github.com/facebookresearch/DPR) model on NaturalQuestions Test set.

## Run evaluations
Please run the commmand below to evaluate your modes' predictions:

```
$ python evaluate.py --dataset naturalquestions --predictions predictions/test.dpr.nq.txt
--------------------
label: total
Exact Match Score: 0.41274238227146814
--------------------
label: overlap
Exact Match Score: 0.7132616487455197
--------------------
label: comp_gen
Exact Match Score: 0.25882352941176473
--------------------
label: novel_entity
Exact Match Score: 0.33835845896147404
```
