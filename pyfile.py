import nltk
from nltk.corpus import stopwords 
nltk.download('stopwords')


f1 = open("Beyond the wall of sleep.txt", "r",errors='ignore')
words1=f1.read().lower()
words1.strip('\n')
words1=words1.split()

f2= open("The Project Gutenberg eBook of Pride and Prejudice.txt", "r",errors='ignore')
words2=f2.read().lower()
words2=words2.strip('\n')
words2=words2.split()


remove_list=stopwords.words('english')
clean_words1=[word for word in words1 if not word in remove_list]


remove_list=stopwords.words('english')
clean_words2=[word for word in words2 if not word in remove_list]


result=set(clean_words1)& set(clean_words2)

print("number of common words: ", len(result)) 
print(result)