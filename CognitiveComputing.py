import nltk
from textblob import TextBlob
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Receber o texto digitado

	texto = input("Digite o texto a ser analisado: ")

# Tokenizar as palavras do texto
	tokens = word_tokenize(texto)

# Remover as stopwords
	stop_words = set(stopwords.words('portuguese'))
	tokens = [w for w in tokens if not w in stop_words]

# Fazer a normalização das palavras
	stemmer = PorterStemmer()
	tokens = [stemmer.stem(w) for w in tokens]

# Juntar as palavras novamente em um texto
	texto = ' '.join(tokens)

# Criar um objeto TextBlob
	blob = TextBlob(texto)

# Imprimir o sentimento
	sentimento = blob.sentiment.polarity
	print("Sentimento: ", sentimento)

# Juntar as palavras novamente em um texto
	texto = ' '.join(tokens)

# Criar um objeto TextBlob
	blob = TextBlob(texto)

# Imprimir o sentimento
	sentimento = blob.sentiment.polarity
	print("Sentimento: ", sentimento)

		if sentimento > 0:
		    print("O paciente apresenta um sentimento positivo.")
			elif sentimento < 0:
		    print("O paciente apresenta um sentimento negativo.")
			else:
		    print("O paciente apresenta um sentimento neutro.")

		if sentimento > 0.2:
		    print("O paciente apresenta uma tendência a superestimar a situação.")
			elif sentimento < -0.2:
		    print("O paciente apresenta uma tendência a subestimar a situação.")
			else:
		    print("O paciente apresenta uma tendência a ser realista.")



