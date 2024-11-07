from typing import List
import spacy

#Modèle Spacy pour la tokenization
nlp = spacy.load("fr_core_news_sm")

#Personnaliser les cas particuliers 
def customize_tokenizer(nlp):
    special_cases = {
        "qu'": [{"ORTH": "qu'"}],   
        "l'": [{"ORTH": "l'"}],     
        "d'": [{"ORTH": "d'"}], 
        "c'": [{"ORTH": "c'"}],     
        "j'": [{"ORTH": "j'"}],     
        "m'": [{"ORTH": "m'"}],     
        "t'": [{"ORTH": "t'"}],     
        "là-bas": [{"ORTH": "là-bas"}],     
    }
    for case, token_data in special_cases.items():
        nlp.tokenizer.add_special_case(case, token_data)

#Appliquer les modifs
customize_tokenizer(nlp)

#Lire le texte 
def read_text(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

#Tokenization avec les nouvelles règles
def tokenize_text_spacy(text: str) -> List[str]:
    doc = nlp(text)
    tokens = [token.text.strip() for token in doc]
    return tokens

#Sauvegarder les tokens avec ID 
def save_tokens_with_range(tokens: List[str], output_file: str):
    with open(output_file, 'w', encoding='utf-8') as f:
        token_id = 1 
        
        for i, token in enumerate(tokens):
            if token in [".", "!", "?"]:  # Fin de phrase    
             
                f.write(f"{token_id}\t{token}\n")
                token_id = 0  
            elif token in ["au", "aux", "du"]:  # Si le token est un déterminant contracté
                # On génère une plage d'index pour ces cas particuliers
                token_range = f"{token_id}-{token_id + 1}"
                if token == "au":
                    sub_tokens = ["à", "le"]
                elif token == "aux":
                    sub_tokens = ["à", "les"]
                elif token == "du":
                    sub_tokens = ["de", "le"]
                #elif token == "des":
                    #sub_tokens = ["de", "les"]
                
              
                f.write(f"{token_range}\t{token}\n")
                f.write(f"{token_id}\t{sub_tokens[0]}\n")
                f.write(f"{token_id + 1}\t{sub_tokens[1]}\n")
                
                token_id += 2
            else:
                if token_id == 0:
                    f.write(f"{token}\n")
                else:
                    f.write(f"{token_id}\t{token}\n")
                token_id += 1

    print(f"Tokens saved to {output_file}")

def main(txt_file: str, output_file: str):
    text = read_text(txt_file)
    
    spacy_tokens = tokenize_text_spacy(text)
    
    save_tokens_with_range(spacy_tokens, output_file)

if __name__ == "__main__":
    txt_file = 'fr_sequoia_test.txt'
    output_file = 'tokenized_output.txt'  #Fichier de sortie
    main(txt_file, output_file)

