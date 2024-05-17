# spacy-rerank
Rank phrases and text based on query by leveraging hugging-face models. Currently, we are only leveraging tiny-bert model.

## Installation and Implementation

- Install the package using the below
```bash
pip install spacyrerank
```

- Code for simple implementation

```python
from spacyrerank.rerank import Reranker

query = "done effort is wasted"
texts = ["work done", "valuable man", "effort wasted", "Great work", "great work mate"]

reranker = Reranker(query, texts=texts)
reranker()

[{'rank': 2, 'text': 'effort wasted', 'similarity-score': 0.877},
 {'rank': 0, 'text': 'work done', 'similarity-score': 0.86},
 {'rank': 3, 'text': 'Great work', 'similarity-score': 0.773},
 {'rank': 4, 'text': 'great work mate', 'similarity-score': 0.757},
 {'rank': 1, 'text': 'valuable man', 'similarity-score': 0.719}]

CPU times: user 331 ms, sys: 76 ms, total: 407 ms
Wall time: 564 ms
```

