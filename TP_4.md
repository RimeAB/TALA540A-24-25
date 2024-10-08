# TP Spacy POS tagging
Entraînement


## Étape 1: préparation du corpus

cf https://spacy.io/api/cli#convert

Option simple: convertir des fichiers conllu en corpus d'entraînement. Par exemple avec sequoia:

- à faire pour les train, dev et test
- à faire pour d'autres (sous-)corpus


## Étape 2: configuration de la pipeline


cf. https://spacy.io/usage/training#quickstart

Pendant la séance, configurer un modèle: 
-  pour le français
-  uniquement un tagger
-  optimisé vitesse ('efficiency')

télécharger le `base_config.cfg` correspondant et executer

`python -m spacy init fill-config base_config.cfg config.cfg`

On peut ensuite modifier base.cfg
pour l'instant:
- batch_size
- max_steps
- max_epochs

pour accélérer l'entraînement et voir que tout fonctionne.

(Chez vous, vous pourrez relancer des entraînements plus longs pour obtenir de meilleurs scores).


## Étape 3: Entraînement

cf. https://spacy.io/api/cli#train

Commande:
`python -m spacy train config.cfg --output ./spacy_model2/ --paths.train ./spacy_sequoia/fr_sequoia-ud-train.spacy --paths.dev ./spacy_sequoia/fr_sequoia-ud-dev.spacy `

(adapter les chemins en fonction de votre environement)

## Étape 4: Évaluation (cf. TP précédent)


## Étape 5: refaire la même chose sur un autre langue/d'autres corpus
