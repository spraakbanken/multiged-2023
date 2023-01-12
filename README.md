# Shared task on Multilingual Grammatical Error Detection (MultiGED-2023)

The [Computational SLA](https://spraakbanken.gu.se/en/compsla) working group invites you to participate in the first shared task on Multilingual Grammatical Error Detection, **MultiGED**, where five languages are included: Czech, English, German, Italian and Swedish.

The results will be presented on May, 22, 2023, at the NLP4CALL workshop, colocated with the [NODALIDA conference](https://www.nodalida2023.fo/) to be held in the Faroe Islands. 

To register, fill in [this form](https://forms.gle/DgwTNmTCQhsmrbxq6).

## Task description

In this shared task your goal is to detect tokens in need of correction, labeling them as either correct (**"c"**) or incorrect (**"i"**), i.e. performing binary classification at the token level, as shown in the example below.

| Token ID |  Token   | Label |
|:---------|:---------|:------|
| 1        |  I       | c     |
| 2        |  saws    | **i** |
| 3        |  the     | c     |
| 4        |  show    | c     |
| 5        |  's      | c     |
| 6        |  advertisement | c  |
| 7        |  hanging | c     |
| 8        |  up      | c     |
| 9        |  of      | **i** |
| 10       |  a       | c     |
| 11       |  wall    | c     |
| 12       |  in      | c     |
| 13       |  London  | c     |


## Tracks

There is one track only, although results will be collected and compared by each individual language. When submitting your results, please use ISO 639‑1 **language prefixes** to indicate which language your system was developed for and should be tested on. 

* **cs-** for Czech
* **en-** for English
* **de-** for German
* **it-** for Italian
* **sv-** for Swedish

It is possible, but not mandatory, to develop systems for each of the included languages. 


## Data

For each of the languages we use a corpus of second language learner essays as a source. For datasets that have been previously used for similar tasks (GED/GEC), we follow the same data splits (e.g. Czech, English-FCE, German).

Two new datasets are introduced in this shared task: one for Swedish (based on SweLL-gold corpus) and another for English (based on REALEC corpus). **--Any others that are new?**

The data is organized in tab-separated columns, with one token per line; each sentence is separated by an empty line. The first column contains the tokens, the second column contains the grammatical error label (c or i). Note that there are no column headers.

You are welcome to use the provided datasets across languages and mix them as you see fit **(any better way of saying that?)**

You can download the datasets from the links below. **--Should we link the datasets to the file names in the tables below (except text, of course)?** AC: I would say that there are training and validation (or 'dev' if we rename it) folders in this repository. So the easiest thing is for people to clone the whole repo.


### Data licenses

| Language |  Corpus name | Corpus license | MultiGED license | 
|:---------|:-------------|:---------------|:------------------|
| Czech    | GECCC        | CC BY-SA 4.0   |                   |
| English  | FCE          | [custom](https://ilexir.co.uk/datasets/index.html)  |                   |
|          | REALEC       |                |                   |
| German   | Falko        | CC BY-SA 4.0   |                   |
|          | MERLIN       | CC BY 3.0      |                   |
| Italian  | MERLIN       | CC BY 3.0      |                   |
| Swedish  | SweLL-gold   |                |                   |


### Czech

| Source corpus |  Split             | Proportion | Nr sentences | Nr tokens | Nr errors | Error rate |
|:--------------|:-------------------|:-----------|:-------------|:----------|:----------|:-----------|
| GECCC         | Total              | 1.0        | 35,443       |365,033    | 88,148    | 0.242      |
|               | • [cs-train.tsv]() | 0.758      | 29,786       |303,703    | 70,993    | 0.234      |
|               | • [cs-dev.tsv]()   | 0.073      | 2,779        |29,221     | 8,301     | 0.284      |
|               | • cs-test.tsv      | 0.080      | 2,878        |32,109     | 8,854     | 0.276      |

Grammar Error Correction Corpus for Czech ([GECCC](https://arxiv.org/pdf/2201.05590.pdf)) consists of 83 058 sentences and covers four diverse domains, including essays written by native students, informal website texts, essays written by Romani ethnic minority children and teenagers and essays written by nonnative speakers. All domains are professionally annotated for GEC errors in a unified manner, and errors were automatically categorized with a Czech-specific version of the ERRor ANnotation Toolkit ([ERRANT](https://github.com/chrisjbryant/errant)), released [here](https://github.com/ufal/errant_czech). For more details see [Naplava et al. (2022)](https://arxiv.org/pdf/2201.05590.pdf).


### English

There are two corpora for English: FCE and REALEC

| Source corpus |  Split                 | Proportion | Nr sentences | Nr tokens | Nr errors | Error rate |
|:--------------|:-----------------------|:-----------|:-------------|:----------|:----------|:-----------|
| FCE           | Total                  | 1.0        | 33,236       |561,416    | 53,607    | 0.101      |
|               | • [en-train-fce.tsv]() | 0.805      | 28,350       |454,736    | 45,183    | 0.099      |
|               | • [en-dev-fce.tsv]()   | 0.062      | 2,191        |34,748     | 3,678     | 0.106      |
|               | • en-test-fce.tsv      | 0.074      | 2,695        |41,932     | 4,746     | 0.113      |

The FCE Corpus was released in 2011 along with [this ACL publication](https://aclanthology.org/P11-1019/) by Yannakoudakis et al.
It contains essays by candidates for the First Certificate in English (FCE) exam (now "B2 First") designed by Cambridge English to certify learners of English at CEFR level B2.
It is part of the larger Cambridge Learner Corpus and was annotated for grammatical errors as described in [Nicholls (2003)](https://www.academia.edu/download/43303478/CL2003_Nicholls.pdf). The FCE Corpus has been used in grammatical error detection (and correction) experiments on numerous occasions, as summarised [here](https://paperswithcode.com/dataset/fce).


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


The dataset split used here is described in [Boyd (2018)](https://aclanthology.org/W18-6111.pdf) and has been published [here](https://github.com/adrianeboyd/boyd-wnut2018).

Further information on Merlin can be found in [Boyd et al. (2014)](http://www.lrec-conf.org/proceedings/lrec2014/pdf/606_Paper.pdf) and  on the [Merlin platform](https://www.merlin-platform.eu/). For Falko, please refer to the Falko website [here](https://hu-berlin.de/falko).

Note that tokens transcribed as entirely "-unreadable-" in the Merlin corpus have been omitted (partially unreadable tokens, such as "ver-unreadable-" have been retained).


### Italian

| Source corpus |  Split             | Proportion | Nr sentences | Nr tokens | Nr errors | Error rate |
|:--------------|:-------------------|:-----------|:-------------|:----------|:----------|:-----------|
| Merlin        | Total              | 1.0        | 8,061        |99,693     | 13,251    | 0.133      |
|               | • [it-train.tsv]() | 0.789      | 6,393        |78,638     | 10,376    | 0.132      |
|               | • [it-dev.tsv]()   | 0.110      | 2,503        |11,038     | 1,429     | 0.130      |
|               | • it-test.tsv      | 0.101      | 2,337        |10,017     | 1,446     | 0.144      |


The Merlin corpus is described in [Boyd et al. (2014)](http://www.lrec-conf.org/proceedings/lrec2014/pdf/606_Paper.pdf). Further documentation can be found on the [Merlin platform](https://www.merlin-platform.eu/).

Note that tokens transcribed as entirely "-unreadable-" in the Merlin corpus have been omitted (partially unreadable tokens, such as "lem-unreadable-" have been retained).


### Swedish

| Source corpus |  Split             | Proportion | Nr sentences | Nr tokens | Nr errors | Error rate |
|:--------------|:-------------------|:-----------|:-------------|:----------|:----------|:-----------|
| SweLL-gold    | Total              | 1.0        |         |     |     |       |
|               | • [sv-train.tsv]() |       |         |     |      |       |
|               | • [sv-dev.tsv]()   |       |         |     |      |       |
|               | • sv-test.tsv      |       |         |     |      |       |

The SweLL-gold corpus is described in [Volodina et al. (2019)](https://nejlt.ep.liu.se/article/view/1374) with statistics and metadata provided [here](https://spraakbanken.github.io/swell-release-v1/Metadata-SweLL). 


## Use of external data

We encourage you to use any external data of your choice, provided you describe it and - where possible - share with the community for potential replication studies.  **CB: I would say participants can use any data they wish, provided it is publicly available for research purposes.**

You can also prepare your own synthetic datasets, which we also encourage you to share with the community. 

Besides, you are welcome to report any errors/problems with the datasets using "issues"/"pull requests" **-- SHOULD we allow this???** AC: yes good idea; if people find any data problems we'll need to remember to announce it on the google group (that there's a new version of the data).


## Test data

The final model will be evaluated on a hidden test set. We will release test files per language to the registered participants by the end of February 2023. Please fill in [this form](https://forms.gle/DgwTNmTCQhsmrbxq6) to register for participation.

**IS THIS CORRECT, Orphee?**


## Evaluation 

### Evaluation metric

Evaluation will be carried out in terms of token-based Precision, Recall and F0.5 to be consistent with previous work on error detection ([Bell et al., 2019](https://aclanthology.org/W19-4410/); [Kaneko and Komachi, 2019](https://arxiv.org/pdf/1904.07334.pdf); [Yuan et al., 2021](https://aclanthology.org/2021.emnlp-main.687/).)

Example:  

| Token ID |  Token   | Reference | Hypothesis | Meaning
|:---------|:---------|:----------|:-----------|:--------|
| 1        |  I       | c         | c          |         |
| 2        |  saws    | i         | i          | True Positive |
| 3        |  the     | c         | c          |         |
| 4        |  show    | c         | i          | False Positive |
| 5        |  last    | c         | c          |         |
| 6        |  nigt    | i         | c          | False Negative |
| 7        |  .       | c         | c          |         |

F0.5 is used instead of F1 because humans judge false positives more harshly than false negatives and so precision is more important than recall.  


### Evaluation script

The provided `eval.py` script calculates system performance from input CoNLL-format Hypothesis and Reference tab-separated files. This script is used to evaluate any output submitted to [Codalab]() (development/test data), but you can also download it and use it independently. The script is run from the command line as follows:  **Orphee to add Codalab link!**

`python3 eval.py -hyp <hyp_tsv> -ref <ref_tsv>`

It is assumed that the `hyp_tsv` file is in the same format as the equivlanet `ref_tsv` file provided in this shared task. The script processes a single language at a time, so you will need to call it several times to evaluate multiple languages.  


## System submissions

All system submissions will be administered through CodaLab.

Further insructions .... **Orphee?**


## Publication

We encourage you to submit a paper with your system description to the NLP4CALL workshop special track. All papers will be reviewed by the organizing committee. **Is this right?** AC: yes we'll have to review them fairly quickly as a group effort, unlikely we'll reject any papers, but we should be clear what we expect in terms of minimum requirements for a decent paper in this context.

Accepted papers will be published in the workshop proceedings through NEALT Proceedings Series and double-published through the ACL anthology. 

Further instructions on this will follow.


## Timeline

* ≈ mid-January 2022 - first call for participation. Training data released, CodaLab opens for team registrations.
* ≈ mid-February 2023 - validation server released online
* ≈ end of February 2023 - test data released
* ≈ 5 March 2023 - system submission deadline (system output, models, code, fact sheets, extra data, etc)
* ≈ mid-March 2023 - results announced
* ≈ 8-10 April 2023 - paper submission deadline (system descriptions)
* ≈ end April 2023 - paper reviews sent to the authors
* ≈ 10 May 2023 - camera-ready deadline
* 22 May 2023 - presentations of the systems at NLP4CALL workshop 

## Registration for the task

Teams that intend to participate, are requested to fill in [this form](https://forms.gle/DgwTNmTCQhsmrbxq6). 

## Organizers

* [Elena Volodina](https://spraakbanken.gu.se/en/about/staff/elena), University of Gothenburg, Sweden
* [Chris Bryant](https://www.cst.cam.ac.uk/people/cjb255), University of Cambridge, UK
* [Andrew Caines](https://www.cl.cam.ac.uk/~apc38/), University of Cambridge, UK
* [Orphee De Clercq](https://research.flw.ugent.be/nl/orphee.declercq), Ghent University, Belgium
* [Jennifer-Carmen Frey](https://www.eurac.edu/en/people/jennifer-carmen-frey), EURAC Research, Italy
* Elizaveta Ershova, JetBrains, Cyprus
* [Alexandr Rosen](http://utkl.ff.cuni.cz/~rosen/), Charles University, Czech Republic
* Olga Vinogradova, Israel 

## Contact information and forum for discussions

Mail your questions to: < multiged - 2023 @ googlegroups . com >

This is a google group which you can join, ask questions, hold discussions and browse for already answered questions.

## References

* Elena Volodina, Lena Granstedt, Arild Matsson, Beáta Megyesi, Ildikó Pilán, Julia Prentice, Dan Rosén, Lisa Rudebeck, Carl-Johan Schenström, Gunlög Sundberg and Mats Wirén (2019). The SweLL Language Learner Corpus: From Design to Annotation. Northern European Journal of Language Technology, Special Issue.
* Adriane Boyd, Jirka Hana, Lionel Nicolas, Detmar Meurers, Katrin Wisniewski, Andrea Abel, Karin Schöne, Barbora Štindlová, and Chiara Vettori (2014). The MERLIN corpus: Learner language and the CEFR. Proceedings of the Ninth International Conference on Language Resources and Evaluation (LREC'14), pp. 1281-1288.
* Adriane Boyd (2018). Using Wikipedia edits in low resource grammatical error correction. Proceedings of the 2018 EMNLP Workshop W-NUT: The 4th Workshop on Noisy User-generated Text, pp. 79-84. 
* Jakub Náplava, Milan Straka, Jana Straková and Alexandr Rosen (2022). Czech Grammar Error Correction with a Large and Diverse Corpus. Transactions of the Association for Computational Linguistics 10 (2022), pp. 452–467.
* Helen Yannakoudakis, Ted Briscoe, and Ben Medlock (2011). A New Dataset and Method for Automatically Grading ESOL Texts. In Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies, pages 180–189.

