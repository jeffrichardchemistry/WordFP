import numpy as np
import pandas as pd
import os
from .fastsimilarity import getOnematch #to package
#from fastsimilarity import getOnematch #run locally

ABSOLUT_PATH = os.path.dirname(os.path.realpath(__file__))

class WordFP():
    """
    Class to run word fingerprint (wordFP).
    This package considers ASCII encoding, with all accents and diacritics removed. 
    
    Arguments
    ---------------------
    max_word_length: default: 23
        Set the largest word in the database. In PT-BR case the largest word 
        in our database has 23 letters.
    """
    def __init__(self, max_word_length=23):        
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.n_alphabet_letters = len(self.alphabet)
        self.max_word_length = max_word_length
        self._path_database = ABSOLUT_PATH+'/data/wordFP_full.pkl'        
        
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
    
    def getbase_wordFP(self):
        """
        Matrix of wordFP in uint8 type. This matrix has 261797 word in fingerprint form.
        Each matrix of wordFP was transformed into 1D form by the numpy ravel() function.
        Each line represents a word, to see the complete dataframe run the function "getbase_wordFP_full"
        """
        return pd.read_pickle(self._path_database, compression='zip').iloc[:, 2:].values.astype('uint8')
    
    def getbase_wordFP_full(self):
        """
        Full dataframe with words and wordFPs. The fingerprints are in 1D form (numpy ravel function).
        """
        return pd.read_pickle(self._path_database, compression='zip')
        
    def fit(self, word, engine='F', matrix_dtype='uint8'):
        """
        This function returns a matrix of zeros and ones, wherer
        1's means presence of a letter in a certain position and 0's absence.
        The first column of matrix indicate the letters belonging to the word
        in alphabet order.
        
        Arguments
        ---------------------                
        wordFP
            word as a string
        
        engine: {‘C’, ‘F’}, default: ‘F’
            Whether to store multi-dimensional data in row-major (C-style)
            or column-major (Fortran-style) order in memory.
        
        matrix_dtype
            Array type, same numpy.
        """
        
        #get letter index in alphabet (first column) and indexes of letters position in matrix
        alphabet_index , indexes_1s = WordFP.__getAlphabetWord_index(self, word=word)
        
        word_FP = np.zeros(self.n_alphabet_letters, dtype=matrix_dtype, order=engine)#array of 0s to first column
        matrix_FP = np.zeros((self.n_alphabet_letters,self.max_word_length), dtype=matrix_dtype, order=engine)#matrix of 0s
        
        word_FP[alphabet_index] = 1 #substitute by 1 in positions get before
        matrix_FP[indexes_1s[:,0],indexes_1s[:,1]] = 1 #substitute by 1 in positions get before
        
        #put array fingerprint of letters in alphabet in first position of matrix
        word_FP = np.insert(matrix_FP, 0,values=word_FP,axis=1) 
        
        return word_FP
    
    def fit_similarity(self,
                       base_wordFP,
                       wordFP,
                       complete_base,
                       similarity_metric='geometric', alpha=1, beta=1,
                       threshold=0.75):
        """
        This function returns the words in a dictionary
        with similarity value of matches.
        Alpha and beta is just for tversky similarity method.
        
        Arguments
        ---------------------
        base_wordFP
            This argument is the matrix of only word fingerprints.
            Run function "getbase_wordFP()" to get database of 261797 PT-BR words (max_word_length=23)
        
        wordFP
            word as a string
        
        complete_base
            This argument is the matrix of word fingerprints and their names (word string)
        
        similarity_metric
            Is the way to calculate the similarity. The options are: 'tanimoto', 'tversky',
            'geometric', 'arithmetic', 'euclidian' and 'manhattan'.
        
        threshold
            Returns words just above similarity (min=0, max=1)
        """
        
        wordFP = WordFP.fit(self, word=wordFP, engine='F').ravel().reshape(1,-1).astype('uint8')
        #print(wordFP)
        output = getOnematch(base_train=base_wordFP,
                             base_test=wordFP,
                             complete_base=complete_base,
                             similarity_metric=similarity_metric, alpha=alpha, beta=beta,
                             threshold=threshold)
        #print(output)
        return output
    

"""if __name__ == '__main__':
    df_full = pd.read_pickle('/dados/GoogleDrive/rotinas_python/github_projects/WordFP/data/wordFP_full.pkl', compression='zip')
    xi_train = df_full.iloc[:, 2:].values.astype('uint8')
    
        
    wfp = WordFP()
    wfp.fit_similarity(base_wordFP=xi_train, wordFP='açucar', complete_base=df_full, similarity_metric='geometric', threshold=0.75)"""
   