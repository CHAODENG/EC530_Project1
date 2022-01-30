import string
import numpy as np
import matplotlib.pyplot as plt
import PyPDF2

# Open the file in read mode
#text = open("/Users/dc/Desktop/sample.txt", "r")
def pdf_convert_txt(pdfFileObj):
    # creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
    # printing number of pages in pdf file 
    # print(pdfReader.numPages) 
        
    # creating a page object 
    pageObj = pdfReader.getPage(0) 
        
    # extracting text from page 
    text = pageObj.extractText()
    return text

def word_analysis(text):
# Create an empty dictionary
    d = dict()
# Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Convert the characters in line to
        # lowercase to avoid case mismatch
        line = line.lower()

        # Remove the punctuation marks from the line
        line = line.translate(line.maketrans("", "", string.punctuation))

        # Split the line into words
        words = line.split(" ")

    
        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
            # Remove NLTK stop words from the line
            if word not in stopwords:
                if word in d:
                    # Increment count of word by 1
                    d[word] = d[word] + 1
                else:
                    # Add the word to dictionary with count 1
                    d[word] = 1

    #Test to print the contents of dictionary
    for key in list(d.keys()):
        print(key, ":", d[key])
    
    return d

def create_histogram(d):
    labels, values = zip(*d.items())

    # sort your values in descending order
    indSort = np.argsort(values)[::-1]

    # rearrange your data
    labels = np.array(labels)[indSort]
    values = np.array(values)[indSort]

    indexes = np.arange(len(labels))

    bar_width = 0.35

    plt.bar(indexes, values)

    # add labels
    plt.xticks(indexes + bar_width, labels)
    plt.show()




if __name__ == "__main__":
    # Open the file in read mode
    # pdfFileObj = open('/Users/dc/Desktop/sample2.pdf', 'rb')
    # text = pdf_convert_txt(pdfFileObj)
    text = open("/Users/dc/Desktop/sample.txt", "r")
    #print(text)
    dic = word_analysis(text)
    create_histogram(dic)
