import numpy as np


class WordFP():
    def __init__(self, max_word_length=25):        
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.n_alphabet_letters = len(self.alphabet)
        self.max_word_length = max_word_length
        
    def __getAlphabetWord_index(self, word):
        word_list = list(word.lower())
        
        #positions of each letter in alphabet
        word_index = [self.alphabet.find(word) for word in word_list]
        #print(word_index)
        #position of each letter in word
        column_index = np.arange(0, len(word_index), 1)
        #get positions of 1 in matrix (tuple (line,column))
        matrix_positions = [(word_ind, column_ind) for word_ind, column_ind in zip(word_index, column_index)]
        
        return word_index,np.array(matrix_positions) #return as matrix 
    
    def fit(self, word, engine='F', matrix_dtype='uint32'):
        #get letter index in alphabet (first column) and indexes of letters position in matrix
        alphabet_index , indexes_1s = WordFP.__getAlphabetWord_index(self, word=word)
        
        word_FP = np.zeros(self.n_alphabet_letters, dtype=matrix_dtype, order=engine)#array of 0s to first column
        matrix_FP = np.zeros((self.n_alphabet_letters,self.max_word_length), dtype=matrix_dtype, order=engine)#matrix of 0s
        
        word_FP[alphabet_index] = 1 #substitute by 1 in positions get before
        matrix_FP[indexes_1s[:,0],indexes_1s[:,1]] = 1 #substitute by 1 in positions get before
        
        #put array fingerprint of letters in alphabet in first position of matrix
        word_FP = np.insert(matrix_FP, 0,values=word_FP,axis=1) 
        
        return word_FP
