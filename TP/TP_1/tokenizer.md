## Tokenisation du corpus

- Tokenisation du corpus avec l'outil Bonsai.
- Travail manuel et automatique pour identifier les mots composés (par exemple, "aux" = "à + les", "revenons-en" = "revenons + -en").
- Vérification manuelle après la tokenisation.

## Tokenisation avec Spacy - Proposition d'Algo

- Comparaison entre la tokenisation par défaut de Spacy et celle du corpus :
    - **Méthode 1** (Python): Écrire un script Python qui parcourt les deux fichiers ligne par ligne et qui ajoute les différences dans une liste.
    - **Méthode 2** (Bash): Extraire les tokens avec Spacy, mettre les tokens du corpus dans un autre fichier, puis comparer avec `vimdiff`.
        - Exemple de commande : `vimdiff output-tokenized-with-spacy.txt sequoia-tokens.txt`
        - Voir `https://vim.rtorr.com` ou exécuter `vim --help` pour comprendre comment utiliser `vim` dans le terminal.
- Gestion des cas particuliers :
    - Utilisation de `add_special_cases` ou des règles dans les `prefix-infix-suffix  patterns`.

## Exécution du code

- `python tokenizer.py`


