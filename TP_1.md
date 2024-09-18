# TP Spacy 
Utilisation modèles pré-entraînés
(séances 1)

## Étape 1
### récupérer modèle et données

- création d'un venv si besoin 
    - avec python 
    - `python -m venv [nom_du_dossier]`
    - `cd [nom_du_dossier]`
    - avec conda 
        - `conda create -n [nom_du_venv] python=3.9.18`
        - `conda activate [nom_du_venv]`
    - `pip install spacy`
    - `python -m spacy download fr_core_news_sm`
    - trouver du corpus:
    - `wget https://github.com/UniversalDependencies/UD_French-Sequoia/raw/master/fr_sequoia-ud-test.conllu`
    - version texte brute: 
        - `cat fr_sequoia-ud-test.conllu | grep "# text" | sed 's/# text = //'` 
    - mettre la sortie dans un fichier txt: 
        - `cat fr_sequoia-ud-test.conllu | grep "# text" | sed 's/# text = //' > fr_sequoia_test.txt`
        

## Étape 2
### être capable de lire le corpus, et l'analyser
- Comment est structuré le corpus ? (Regardez le format, le type d'annotation, les colonnes ...) 
- Combien d'énoncés ?
    - `cat fr_sequoia-ud-test.conllu | grep -c "# text"`
    - ou `wc -l fr_sequoia_test.txt`
- Combien de label ? (Regardez seulement la colonne 4)
    - `cat fr_sequoia-ud-test.conllu | grep -v "#" | grep . | cut -f4| sort | uniq -c | sort -n`

## Étape 3 
### reproduire la tokenization du corpus
Essayer d'utiliser `typing` et des `dataclass` en python pour structurer votre code

- partir du texte brut (fr_sequoia_test.txt) 
- imposer la tokenisation de sequoia
    - cf. https://spacy.io/usage/linguistic-features#own-annotations
    - ou cf. https://spacy.io/api/doc
    - Quelles différences ?

## Étape 4 
### charger les objets Doc de Spacy et appliquer un modèle
Essayer d'utiliser plusieurs modèles 
 
- cf. https://spacy.io/usage/linguistic-features
