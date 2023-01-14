## English data

There are two corpora for English: FCE and REALEC

### FCE

| Source corpus |  Split                 | Proportion | Nr sentences | Nr tokens | Nr errors | Error rate |
|:--------------|:-----------------------|:-----------|:-------------|:----------|:----------|:-----------|
| FCE           | Total                  | 1.0        | 33,236       |561,416    | 53,607    | 0.101      |
|               | • train                | 0.805      | 28,350       |454,736    | 45,183    | 0.099      |
|               | • dev                  | 0.062      | 2,191        |34,748     | 3,678     | 0.106      |
|               | • test                 | 0.074      | 2,695        |41,932     | 4,746     | 0.113      |

The FCE Corpus ([Yannakoudakis et al., 2011](https://aclanthology.org/P11-1019/)) consists of essays written by candidates for the First Certificate in English (FCE) exam (now "B2 First") designed by Cambridge English to certify learners of English at CEFR level B2. It is part of the larger Cambridge Learner Corpus that was annotated for grammatical errors ([Nicholls, 2003](https://www.academia.edu/download/43303478/CL2003_Nicholls.pdf)). The FCE Corpus has been used in grammatical error detection (and correction) experiments on numerous occasions, as summarised [here](https://paperswithcode.com/dataset/fce).

### REALEC

| Source corpus |  Split                    | Proportion | Nr sentences | Nr tokens | Nr errors | Error rate |
|:--------------|:--------------------------|:-----------|:-------------|:----------|:----------|:-----------|
| REALEC        | Total                     | 1.0        | 200,432      | 4,218,265  | 290,289   | 0.069      |
|               | • train                   | 0.980      | 196,365      | 4,131,899  | 284,278   | 0.069      |
|               | • dev                     | 0.010      | 2,049       | 44,086    | 3,053    | 0.069      |
|               | • test                    | 0.010      | 2,018       | 42,280    | 2,958    | 0.070      |

The [Russian Error-Annotated Learner English Corpus (REALEC)](https://realec.org/index.xhtml#/exam/) is an open access corpus available from HSE university. It contains approximately 18,700 texts written by HSE students in the Independent English Language Test between 2014-2020 in response to two types of tasks (approximately 4,336,000 words). A team of specially trained Linguistics undergraduate students proficient in English annotated about 6,000 essays between 2014 and 2019, but when a much larger volume of texts began to be submitted to REALEC in 2020, manual annotation was replaced with a BERT-transformer-type neural network for both identification and correction of errors.

Since REALEC is much larger than the other corpora in MultiGED-2023, we decided upon a 98/1/1 train/dev/text split in order to create a development and test set that was similar in size to other corpora. Note also that because of its size, the REALEC training set is compressed to bring it below GitHub's maximum file size limit (25MB). 


