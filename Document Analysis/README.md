# Document Analyzer
Designing a analyzer which can extract the words from txt file(or pdf file) and compute their frequency. Then creating the histogram based on the frequency to show the result directly.  
## 1. The Package used by the project
![image](https://user-images.githubusercontent.com/90479627/151717328-37500974-ce44-4e0c-8ba3-0330f8a0b323.png)  
1) String is used to process the content we extract from txt or pdf.    
2) Numpy and matplot is used to draw the histogram.
3) PyPDF2 is used to convert the pdf to txt.  

## 2. The Module
In order to reuse each part of the code, we use a modular design to complete the project. So some module would be shown as below:  
### 2.1 Converter  
Based on the PyPDF2 API,this is how I use its API to convert pdf file to txt file.  

![image](https://user-images.githubusercontent.com/90479627/151717573-fa3ae161-d92d-4f6c-9073-16e22d94947f.png)  
### 2.2 Word Frequency Analysis
First, we compute the words in each line and convert the words in lowercase so that we can avoid case mismatch. Then removing all the punctuation marks from the line.  

![image](https://user-images.githubusercontent.com/90479627/151717739-5f661ac3-67e5-42ee-b3f1-a3fad2184da4.png)

According to analyzing each line, we can then use the dictionary to record the frequency of different word. At the same time, we should remove all NLTK stop words from the line.   

![image](https://user-images.githubusercontent.com/90479627/151717899-fb45dfc1-fa5c-4f9a-bd63-93722776df2a.png)  
### 2.3 Draw the histogram  
This part is how to process the key-value and set up the parameters that could be shown in the graph later.  

![image](https://user-images.githubusercontent.com/90479627/151718048-d2c12953-44e5-4050-9cfe-ac118fe62710.png)  

## 3. Results 
The result shows that the word frequency we could get from the sample.txt. The txt file has been provided in the same directory.  
The x-axis lists all the word except for the NLTK stop words from the content in the txt file and the y-axis lists the word frequency respectively for each word.  

![image](https://user-images.githubusercontent.com/90479627/151718211-aa1c4a1f-8551-45b1-94b0-99d39f774fb4.png)




