# Shared task on Multilingual Grammatical Error Detection (MultiGED-2023)

[Computational SLA](https://spraakbanken.gu.se/en/compsla) working group invites you to participate in the first shared task on Multilingual Grammatical Error Detection, **MultiGED**, where five languages are included: Czech, English, German, Italian and Swedish.

The results will be presented on May, 22, 2023, at NLP4CALL workshop, colocated with [NODALIDA conference](https://www.nodalida2023.fo/) to be held in Faroe Island. 

To register, fill in [this form](https://forms.gle/DgwTNmTCQhsmrbxq6).

## Task description

In this shared task your goal is to detect tokens in need of correction, labeling them as either correct (**"c"**) or incorrect (**"i"**), i.e. performing binary classification on a token level, as shown in the example below.

| Running nr |  Token   | Label |
|:-----------|:---------|:------|
| 1          |  I       | c     |
| 2          |  saws    | **i** |
| 3          |  the     | c     |
| 4          |  show    | c     |
| 5          |  's      | c     |
| 6          |  advertisement | c     |
| 7          |  hanging | c     |
| 8          |  up      | c     |
| 9          |  of      | **i** |
| 10         |  a       | c     |
| 11         |  wall    | c     |
| 12         |  in      | c     |
| 13         |  London  | c     |


## Tracks

There is one track only, although results will be collected and compared by each individual language. When submitting your results, please use ISO 639‑1 **language prefixes**. 

* **cs-** for Czech
* **en-** for English
* **de-** for German
* **it-** for Italian
* **sv-** for Swedish

It is possible, but not mandotary, to develop systems for each of the included languages. 


## Data

For each of the languages we use a corpus of second language learner essays as a source. For datasets that have been previously used for similar tasks (GED/GEC), we follow the same data splits (e.g. Czech, English-FCE, German, **Italian???** ).

Two new datasets are introduced in this shared task: one for Swedish (based on SweLL-gold corpus) and another for English (based on REALEC corpus). **--Any others that are new?**

The data is organized in columns, with one token per line; each sentence is separated by an empty line. **IS THIS TRUE? Andrew?**

You are welcome to use the provided datasets across languages and mix them as you see fit **(any better way of saying that?)**

You can download the datasets from the links below. **--Should we link the datasets to the file names in the tables below (except text, of course)?**

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

The SweLL-gold corpus is described in [Volodina et al. (2019)](https://nejlt.ep.liu.se/article/view/1374) with statistics and metadata provided [here](https://spraakbanken.github.io/swell-release-v1/Metadata-SweLL). 


## Use of external data

We encourage you to use ay external data of your choice, provided you describe it and - where possible - share with the community for potential replication studies.

You can also prepare your own synthetic datasets, which we also encourage you to share with the community. 

Besides, you are welcome to report any errors/problems with the datasets using "issues"/"pull requests" **-- SHOULD we allow this???**

## Test data

The final model will be evaluated on a hidden test set. We will release test files per language to the registered participants by the end of February 2023. Please fill in [this form](https://forms.gle/DgwTNmTCQhsmrbxq6) to register for participation.

**IS THIS CORRECT, Orphee?**

## Evaluation 

### Evaluation script

**Chris, could you please add some intformation here?** 

You will be able to test your models tuned on validation datasets using the evaluation script through [CodaLab](). **Orphee, please add here the link to the CodaLab**

### Evaluation metrics

We are using M2 metrics described in [Bryant et al (2022)](https://arxiv.org/abs/2211.05166), section 6.1 ...

The script should give you an output that looks like this: **BLA-BLA-BLA ***

**Chris, could you please add some intformation here?** 

## Submissions

All system submissions will be administered through CodaLab.

Further insructions .... **Orphee?**

## Publication

You are welcome to submit a paper with your system description to the NLP4CALL workshop special track. All papers will be reviewed. **Is this right?**
Accepted papers will be published in the workshop proceedings through NEALT Proceedings Series and ACL anthology.  


## Timeline

* approx mid-Januarry 2022 - first call for participation. Training data released, CodaLab opens for team registrations.
* approx mid-February 2023 - validation server released online
* approx end of February 2023 - test data released
* approx 5 March 2023 - system submission deadline (system output, models, code, fact sheets, extra data, etc)
* approx mid-March 2023 - results announced
* approx 8-10 April 2023 - paper submission deadline (system descriptions)
* approx end April 2023 - paper reviews sent to the authors
* approx 10 May 2023 - camera-ready deadline
* 22(-24) May 2023 - presentations of the systems at workshop NLP4CALL

## Registration for the task

Teams that intend to participate, are requested to fill in [this form](https://forms.gle/DgwTNmTCQhsmrbxq6). 

## Organizers

* [Elena Volodina](https://spraakbanken.gu.se/en/about/staff/elena), Sweden/University of Gothenburg (main organizer)
* [Cris Bryant](https://www.cst.cam.ac.uk/people/cjb255), Great Britain/Reverso & University of Cambridge
* [Andew Caines](https://www.cl.cam.ac.uk/~apc38/), Great Britain/University of Cambridge
* [Orphee DeClerq](https://research.flw.ugent.be/nl/orphee.declercq), Belgium/Gent university
* [Jennifer Carmen Frey](https://www.eurac.edu/en/people/jennifer-carmen-frey), Italy/EURAC
* Elizaveta Ershova, Cyprus/JetBrains
* [Alexandr Rosen](http://utkl.ff.cuni.cz/~rosen/), Czech Republic/Charles university
* Olga Vinogradova, Israel 

## Contact information

Mail to: < multiged - 2023 @ googlegroups . com >
