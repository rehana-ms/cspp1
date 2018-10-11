'''
    Document Distance - A detailed description is given in the PDF
'''
import math
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF

    '''
    file1_data=read_content(dict1)
    file2_data=read_content(dict2)
  #  print("first file",file1_data)
  #  print("Second file",file2_data)
    stopwords=load_stopwords("stopwords.txt")
   # print(stopwords)
    word_freq=create_dictionary(file1_data,file2_data,stopwords)
   # print(word_freq)
    compute_distance(word_freq)

def compute_distance(word_freq):
	numerator=0
	sum1=0
	sum2=0
	for word in word_freq:
	#	print(word_freq[word])
	    freq=word_freq[word]
	    numerator=numerator+(freq[0]*freq[1])
	    sum1=sum1+freq[0]**2
	    sum2=sum2+freq[1]**2
	#print(numerator)
	denominator=Math.sqrt(sum1)*Math.sqrt(sum2)
	#print(denominator)
	print(round(numerator/denominator))



def create_dictionary(file1,file2,stopwords):
#    print(file)
    
    file1_words=file1.split(' ')
    file2_words=file2.split(' ')
    #print(file1_words)
    #print(file2_words)
    word_list=file1_words+file2_words
    
    dict={}
    for word in word_list:
        #print(word)
        if word not in stopwords:
            #print(file1_words.count(word),file2_words.count(word))
            dict[word]=(file1_words.count(word),file2_words.count(word))
    return dict

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = []
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords.append(line.strip())
    return stopwords

def read_content(filename):
    with open(filename, 'r') as filename:
        for line in filename:
            data="".join(line.rstrip())
            #print(data)
    return data.lower()
    filename.close()
    

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    
    #print(file1_data)
    #print(file2_data)
    
    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
