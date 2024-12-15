
LANGUAGES = {
    "English": ["hello", "world", "good", "morning", "night", "friend", "love"],
    "Spanish": ["hola", "mundo", "buenos", "dias", "noche", "amigo", "amor"],
    "French": ["bonjour", "monde", "bon", "nuit", "ami", "amour"],
    "German": ["hallo", "welt", "guten", "morgen", "nacht", "freund", "liebe"]
}

def detect_language(text):
    """
    Detects the language of the input text by matching keywords.
    """
    text = text.lower()  
    word_list = text.split() 
    
    language_scores = {}
    
   
    for language, keywords in LANGUAGES.items():
        count = sum(1 for word in word_list if word in keywords)
        language_scores[language] = count
    
 
    detected_language = max(language_scores, key=language_scores.get)
    
   
    if language_scores[detected_language] > 0:
        print(f"Detected Language: {detected_language}")
    else:
        print("Language could not be detected.")

def main():
    print("=== Simple Language Detector ===")
    print("Supported Languages: English, Spanish, French, German")
   
    text = input("Enter a sentence or text: ")
    detect_language(text)
if __name__ == "__main__":
    main()
