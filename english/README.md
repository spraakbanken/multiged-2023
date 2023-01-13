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

Russian Error-Annotated Learner English Corpus (REALEC) is in the open access at the HSE university [portal](https://realec.org/index.xhtml#/exam/). Essays written by HSE students in the Independent English Language Test over the years 2014-2020 by 2022 make up about 18,700 texts written in answer to two types of tasks (approximately 4,336,000 words). Initially, we were able to annotate errors in those essays manually. A team of specially trained Linguistics undergraduate students proficient in English annotated about 6,000 essays between 2014 and 2019. However, later, REALEC started receiving a much larger number of texts, so in 2020 manual annotation was replaced with a BERT-transformer-type neural network for both identification and correction of errors.


Note that the training set is compressed to bring it down under GitHub's current file size limit (25MB).


