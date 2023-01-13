## English data

There are two corpora for English: FCE and REALEC

### FCE

| Source corpus |  Split                 | Proportion | Nr sentences | Nr tokens | Nr errors | Error rate |
|:--------------|:-----------------------|:-----------|:-------------|:----------|:----------|:-----------|
| FCE           | Total                  | 1.0        | 33,236       |561,416    | 53,607    | 0.101      |
|               | • train                | 0.805      | 28,350       |454,736    | 45,183    | 0.099      |
|               | • dev                  | 0.062      | 2,191        |34,748     | 3,678     | 0.106      |
|               | • test                 | 0.074      | 2,695        |41,932     | 4,746     | 0.113      |

The FCE Corpus was released in 2011 along with [this ACL publication](https://aclanthology.org/P11-1019/) by Yannakoudakis et al.
It contains essays by candidates for the First Certificate in English (FCE) exam (now "B2 First") designed by Cambridge English to certify learners of English at CEFR level B2.
It is part of the larger Cambridge Learner Corpus and was annotated for grammatical errors as described in [Nicholls (2003)](https://www.academia.edu/download/43303478/CL2003_Nicholls.pdf). The FCE Corpus has been used in grammatical error detection (and correction) experiments on numerous occasions, as summarised [here](https://paperswithcode.com/dataset/fce).

### REALEC


| Source corpus |  Split                    | Proportion | Nr sentences | Nr tokens | Nr errors | Error rate |
|:--------------|:--------------------------|:-----------|:-------------|:----------|:----------|:-----------|
| REALEC        | Total                     | 1.0        | 200,432      | 4,218,265  | 290,289   | 0.069      |
|               | • train                   | 0.980      | 196,365      | 4,131,899  | 284,278   | 0.069      |
|               | • dev                     | 0.010      | 2,049       | 44,086    | 3,053    | 0.069      |
|               | • test                    | 0.010      | 2,018       | 42,280    | 2,958    | 0.070      |

Note that the training set is compressed to bring it down under GitHub's current file size limit (25MB).


