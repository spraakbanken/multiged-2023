# Shared task on Multilingual Grammatical Error Detection (MultiGED-2023)

The [Computational SLA](https://spraakbanken.gu.se/en/compsla) working group invites you to participate in the first shared task on Multilingual Grammatical Error Detection, **MultiGED**, which includes five languages: Czech, English, German, Italian and Swedish.

The results will be presented on 22nd May, 2023, at the [NLP4CALL workshop](https://spraakbanken.gu.se/en/research/themes/icall/nlp4call-workshop-series/nlp4call2023), colocated with the [NoDaLiDa conference](https://www.nodalida2023.fo/) to be held in the Faroe Islands. 

To register for/express interest in the shared task, please fill in [this form](https://forms.gle/DgwTNmTCQhsmrbxq6).   
To get important information and updates about the shared task, please join the [MultiGED-2023 Google Group](https://groups.google.com/g/multiged-2023).   
Official system evaluation will be carried out on [CodaLab](https://codalab.lisn.upsaclay.fr/competitions/9784).  

## Task description

The aim of this shared task is to detect tokens in need of correction across five different languages, labeling them as either correct (**"c"**) or incorrect (**"i"**), i.e. performing binary classification at the token level, as shown in the example below.

|  Token   | Label |
|:---------|:------|
|  I       | c     |
|  saws    | **i** |
|  the     | c     |
|  show    | c     |
|  last    | c     |
|  nigt    | **i** |
|  .       | c     |

We particularly encourage development of multilingual systems that can process all languages using a single model, but this is not a mandatory requirement to participate in the task. 

## Data

We provide training, development and test data for each of the five languages: Czech, English, German, Italian and Swedish. The training and development datasets are already available in the [MultiGED-2023 Github repository](https://github.com/spraakbanken/multiged-2023), and test sets will be released during the test phase. More information about each corpus is available below. 

* [Czech - GECCC](https://github.com/spraakbanken/multiged-2023/tree/main/czech)
* [English - FCE and REALEC](https://github.com/spraakbanken/multiged-2023/tree/main/english)
* [German - Falko-MERLIN](https://github.com/spraakbanken/multiged-2023/tree/main/german)
* [Italian - MERLIN](https://github.com/spraakbanken/multiged-2023/tree/main/italian)
* [Swedish - SweLL-gold](https://github.com/spraakbanken/multiged-2023/tree/main/swedish)

Some of these datasets are already used in Grammatical Error Detection/Correction (GED/GEC) research, but we also release two new datasets: REALEC (English) and SweLL-gold (Swedish). Where possible, we use the same train/dev/test split as previous work (GECCC, FCE, Falko-MERLIN), and only create new splits when necessary (REALEC, MERLIN, SweLL). All datasets are derived from annotated second language learner essays.  

Please let us know if you find any errors/inconsistencies in a dataset by submitting an Issue/Pull Request on the Github repo. Any changes to the data will be announced via the [MultiGED-2023 Google Group](https://groups.google.com/g/multiged-2023) (so please join it!).


| Source corpus | Language | Split             | Nr sentences | Nr tokens | Nr errors | Error rate |
|:--------------|:---------|:-------------------|:-------------|:----------|:----------|:-----------|
| GECCC         | Czech    | Total              | 35,453       | 399,742   | 84,041    | 0.210      |
| FCE           | English  |  Total             | 33,243      | 531,416   | 50,860    | 0.096      |
| REALEC*       | English  | Total              | 8,136        | 177,769   | 16,608    | 0.093      |
| Falko-MERLIN  | German   | Total              | 24,079       | 381,134   | 57,897    | 0.152      |
| MERLIN        | Italian  | Total              | 7949        | 99,698   | 14,893    | 0.149      |
| SweLL-gold    | Swedish  | Total              | 8,553        | 145,507   | 27,274    | 0.187      |

\* dev and test sets only


### Data Format

Data is provided in a tab-separated format consisting of two columns: the first column contains the token and the second column contains the label (c or i), as in the Task Description. Note that there are no column headers, each sentence is separated by an empty line, and double quotes are escaped (`\"`). *It is expected that system output is generated in the same format*.

### External Data

Participants may use additional resources to build their systems *provided that the resource is publicly available for research purposes*. This includes monolingual data, artificial data, pretrained models, syntactic parsers, etc. After the shared task, we encourage participants to share any newly created resources with the community. 

### Data Licenses

| Language |  Corpus name | Corpus license | MultiGED license | 
|:---------|:-------------|:---------------|:------------------|
| Czech    | GECCC        | CC BY-SA 4.0   | CC BY-SA 4.0      |
| English  | FCE          | [custom](https://ilexir.co.uk/datasets/index.html)  | [custom](https://ilexir.co.uk/datasets/index.html) |
|          | REALEC       | CC BY-SA 4.0   | CC BY-SA 4.0      |
| German   | Falko        | CC BY-SA 4.0   | CC BY-SA 4.0      |
|          | MERLIN       | CC BY-SA 4.0      | CC BY-SA 4.0         |
| Italian  | MERLIN       | CC BY-SA 4.0      | CC BY-SA 4.0         |
| Swedish  | SweLL-gold   | [CLARIN-ID, -PRIV, -NORED, -BY](https://www.kielipankki.fi/support/clarin-eula/#res)| CC BY 4.0   |

## Evaluation 

Evaluation will be carried out in terms of token-based Precision, Recall and F0.5 to be consistent with previous work on error detection ([Bell et al., 2019](https://aclanthology.org/W19-4410/); [Kaneko and Komachi, 2019](https://arxiv.org/pdf/1904.07334.pdf); [Yuan et al., 2021](https://aclanthology.org/2021.emnlp-main.687/).)

Example:  

<table>
<tr><th>Hypothesis</th><th>Reference</th><th>Meaning</th></tr>
<tr><td>

|  Token   | Label |
|:---------|:------|
|  I       | c     |
|  saws    | i     |
|  the     | c     |
|  show    | i     |
|  last    | c     |
|  nigt    | c     |
|  .       | c     |

</td><td>

|  Token   | Label |
|:---------|:------|
|  I       | c     |
|  saws    | i     |
|  the     | c     |
|  show    | c     |
|  last    | c     |
|  nigt    | i     |
|  .       | c     |

</td><td>

|  Meaning   |
|:---------|
| - |
|  True Positive   |
| - |
|  False Positive  |
| - |
|  False Negative  |
| - |

</td></tr></table>

F0.5 is used instead of F1 because humans judge false positives more harshly than false negatives and so precision is more important than recall.  

Although official evaluation will be carried out on [CodaLab](https://codalab.lisn.upsaclay.fr/competitions/9784), we include our evaluation script in this repository, `eval.py`, which can be used to evaluate system performance independently. This script can be run from the command line as follows:

`python3 eval.py -hyp <hyp_tsv> -ref <ref_tsv>`

It is assumed that the `hyp_tsv` and `ref_tsv` files are in the same two-column tab-separated format as the data provided in this shared taskk. Note that the script processes a single language at a time, so you will need to call it several times to evaluate multiple languages.  

## Publication

We encourage you to submit a paper with your system description to the [NLP4CALL workshop](https://spraakbanken.gu.se/en/research/themes/icall/nlp4call-workshop-series/nlp4call2023) special track. We follow the same requirements for paper submissions as the [NLP4CALL workshop](https://spraakbanken.gu.se/en/research/themes/icall/nlp4call-workshop-series/nlp4call2023), i.e. we use the same template and apply the same page limit. All papers will be reviewed by the organizing committee. 

Accepted papers will be published in the workshop proceedings through NEALT Proceedings Series and double-published through the ACL anthology. 

Further instructions on this will follow.

## Timeline

* 23 January, 2023 - first call for participation. Training and validation data released, CodaLab opens for team registrations.
* 14 February, 2023 - second call/reminder
* ~~27 February~~ 06 March, 2023 - test data released
* ~~03 March~~ 13 March, 2023 - system submission deadline (system output)
* ~~10 March~~ 15 March, 2023 - results announced
* 03 April, 2023 - paper submission deadline with system descriptions. We encourage you to share models, code, fact sheets, extra data, etc. with the community through github or other repositories on paper publication.
* 21 April, 2023 - paper reviews sent to the authors
* 01 May, 2023 - camera-ready deadline
* 22 May, 2023 - presentations of the systems at NLP4CALL workshop 

## Organizers

* [Elena Volodina](https://spraakbanken.gu.se/en/about/staff/elena), University of Gothenburg, Sweden
* [Chris Bryant](https://www.cst.cam.ac.uk/people/cjb255), University of Cambridge, UK
* [Andrew Caines](https://www.cl.cam.ac.uk/~apc38/), University of Cambridge, UK
* [Orphee De Clercq](https://research.flw.ugent.be/nl/orphee.declercq), Ghent University, Belgium
* [Jennifer-Carmen Frey](https://www.eurac.edu/en/people/jennifer-carmen-frey), EURAC Research, Italy
* Elizaveta Ershova, JetBrains, Cyprus
* [Alexandr Rosen](http://utkl.ff.cuni.cz/~rosen/), Charles University, Czech Republic
* Olga Vinogradova, Independent researcher, Israel 

## Contact information and forum for discussions

Please join the [MultiGED-2023 google group](https://groups.google.com/g/multiged-2023) in order to ask questions, hold discussions and browse for already answered questions.
