# Shared task on Multilingual Grammatical Error Detection (MultiGED-2023)

Computational SLA working group invites you to participate in the first shared task on Multilingual Grammatical Error Detection, _MultiGED_, where five languages are included: Czech, English, German, Italian and Swedish.

## Task description

In this shared task your goal is to detect tokens in need of correction, labeling them as either correct ("c") or incorrect ("i") for each token, i.e. binary classification.

| Running nr |  Token   | Label |
|:-----------|:---------|:------|
| 1          |  I       | c     |
| 2          |  saws    | i     |
| 3          |  the     | c     |
| 4          |  show    | c     |
| 5          |  's      | c     |
| 6          |  advertisement | c     |
| 7          |  hanging | c     |
| 8          |  up      | c     |
| 9          |  of      | i     |
| 10         |  a       | c     |
| 11         |  wall    | c     |
| 12         |  in      | c     |
| 13         |  London  | c     |


## Tracks

There is one track only, although results are reported for each language individually using ISO 639‑1 language prefixes for submissions. 

* cs- for Czech
* en- for English
* de- for German
* it- for Italian
* sv- for Swedish

It is possible, but not mandotary to develop systems for each of the participating languages. 

## Data

For each of the languages we use a corpus of second language learner essays as a source. For corpora that have been previously used for shared tasks, we follow the same data splits (Czech, English-FCE, German, Italian).

Two new datasets are introduced in this shared task: one for Swedish (based on SweLL corpus) and another for English (based on REALEC corpus).

You can download the datasets from the links below.

_Should we link the datasets to the file names in the tables below (except text, of course)?_

### Czech

| Source corpus |  Split             | Proportion | Nr sentences | Nr tokens | Nr errors | Error rate |
|:--------------|:-------------------|:-----------|:-------------|:----------|:----------|:-----------|
| GECCC         | Total              | 1.0        | 35,443       |365,033    | 88,148    | 0.242      |
|               | • [cs-train.tsv]() | 0.758      | 29,786       |303,703    | 70,993    | 0.234      |
|               | • [cs-dev.tsv]()   | 0.073      | 2,779        |29,221     | 8,301     | 0.284      |
|               | • cs-test.tsv      | 0.080      | 2,878        |32,109     | 8,854     | 0.276      |

_Describe the corpus? Link to an article about the corpus?_ 

### English

There are two corpora for English: FCE and REALEC

| Source corpus |  Split                 | Proportion | Nr sentences | Nr tokens | Nr errors | Error rate |
|:--------------|:-----------------------|:-----------|:-------------|:----------|:----------|:-----------|
| FCE           | Total                  | 1.0        | 33,236       |561,416    | 53,607    | 0.101      |
|               | • [en-train-fce.tsv]() | 0.805      | 28,350       |454,736    | 45,183    | 0.099      |
|               | • [en-dev-fce.tsv]()   | 0.062      | 2,191        |34,748     | 3,678     | 0.106      |
|               | • en-test-fce.tsv      | 0.074      | 2,695        |41,932     | 4,746     | 0.113      |

_Describe the corpus? Link to an article about the corpus?_ 

| Source corpus |  Split                    | Proportion | Nr sentences | Nr tokens | Nr errors | Error rate |
|:--------------|:--------------------------|:-----------|:-------------|:----------|:----------|:-----------|
| REALEC        | Total                     | 1.0        | 200,432      |4,418,696  | 290,289   | 0.069      |
|               | • [en-train-realec.tsv]() | 0.764      | 160,594      |3,377,609  | 232,290   | 0.069      |
|               | • [en-dev-realec.tsv]()   | 0.095      | 19,883       |419,161    | 28,995    | 0.069      |
|               | • en-test-realec.tsv      | 0.095      | 19,955       |421,495    | 29,004    | 0.069      |


_Describe the corpus? Link to an article about the corpus?_ 

### German

| Source corpus |  Split             | Proportion | Nr sentences | Nr tokens | Nr errors | Error rate |
|:--------------|:-------------------|:-----------|:-------------|:----------|:----------|:-----------|
| Falko-Merlin  | Total              | 1.0        | 24,077       |381,134    | 64,054    | 0.168      |
|               | • [de-train.tsv]() | 0.800      | 19,237       |305,113    | 51,143    | 0.168      |
|               | • [de-dev.tsv]()   | 0.104      | 2,503        |39,444     | 6,709     | 0.170      |
|               | • de-test.tsv      | 0.096      | 2,337        |36,577     | 6,202     | 0.170      |


_Describe the corpus? Link to an article about the corpus?_ 


### Italian

| Source corpus |  Split             | Proportion | Nr sentences | Nr tokens | Nr errors | Error rate |
|:--------------|:-------------------|:-----------|:-------------|:----------|:----------|:-----------|
| Merlin        | Total              | 1.0        | 8,061        |99,693     | 13,251    | 0.133      |
|               | • [it-train.tsv]() | 0.789      | 6,393        |78,638     | 10,376    | 0.132      |
|               | • [it-dev.tsv]()   | 0.110      | 2,503        |11,038     | 1,429     | 0.130      |
|               | • it-test.tsv      | 0.101      | 2,337        |10,017     | 1,446     | 0.144      |


_Describe the corpus? Link to an article about the corpus?_ 


### Swedish

| Source corpus |  Split             | Proportion | Nr sentences | Nr tokens | Nr errors | Error rate |
|:--------------|:-------------------|:-----------|:-------------|:----------|:----------|:-----------|
| SweLL-gold    | Total              | 1.0        |         |     |     |       |
|               | • [sv-train.tsv]() |       |         |     |      |       |
|               | • [sv-dev.tsv]()   |       |         |     |      |       |
|               | • sv-test.tsv      |       |         |     |      |       |

The corpus is described in [Volodina et al. (2019)](https://nejlt.ep.liu.se/article/view/1374) with statistics and metadata provided [here](https://spraakbanken.github.io/swell-release-v1/Metadata-SweLL). 


##



