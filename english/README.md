## English data

There are two corpora for English: FCE and REALEC. Note that for REALEC we are releasing a dev and test set only (no train set).

### FCE

| Source corpus |  Split                 | Proportion | Nr sentences | Nr tokens | Nr errors | Error rate |
|:--------------|:-----------------------|:-----------|:-------------|:----------|:----------|:-----------|
| FCE           | Total                  | 1.0        | 33,237       |531,416    | 50,860    | 0.096      |
|               | • train                | 0.855      | 28,351       |454,736    | 42,899    | 0.094      |
|               | • dev                  | 0.065      | 2,191        |34,748     | 3,460     | 0.100      |
|               | • test                 | 0.079      | 2,695        |41,932     | 4,501     | 0.107      |

The FCE Corpus ([Yannakoudakis et al., 2011](https://aclanthology.org/P11-1019/)) consists of essays written by candidates for the First Certificate in English (FCE) exam (now "B2 First") designed by Cambridge English to certify learners of English at CEFR level B2. It is part of the larger Cambridge Learner Corpus that was annotated for grammatical errors ([Nicholls, 2003](https://www.academia.edu/download/43303478/CL2003_Nicholls.pdf)). The FCE Corpus has been used in grammatical error detection (and correction) experiments on numerous occasions, as summarised [here](https://paperswithcode.com/dataset/fce).

### REALEC

| Source corpus |  Split                 | Proportion | Nr sentences | Nr tokens | Nr errors | Error rate |
|:--------------|:-----------------------|:-----------|:-------------|:----------|:----------|:-----------|
| REALEC        | Total                  | 1.0        | 8136         |177,769    | 16,608    | 0.093      |
|               | • train                | n/a        | n/a          |n/a        | n/a       | n/a      |
|               | • dev                  | 0.5        | 4067         |88,008     | 8103      | 0.092      |
|               | • test                 | 0.5        | 4069         |89,761     | 8505    | 0.095      |

The [Russian Error-Annotated Learner English Corpus (REALEC)](https://realec.org/index.xhtml#/exam/) is an open access corpus available from HSE university. It contains approximately 18,700 texts written by HSE students in the Independent English Language Test between 2014-2020 in response to two types of tasks (approximately 4,336,000 words). A team of specially trained Linguistics undergraduate students proficient in English annotated about 6,000 essays between 2014 and 2019, and when a much larger volume of texts began to be submitted to REALEC in 2020, manual annotation was replaced with a BERT-transformer-type neural network for both identification and correction of errors. In this shared task, we are releasing only the manually annotated essays.
