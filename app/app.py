import streamlit as st
from WordFP import WordFP
from texts import Texts
from PIL import Image
import pandas as pd
import os

ABSOLUT_PATH = os.path.dirname(os.path.realpath(__file__))

class BackEnd:
    def __init__(self):
        self.base_matrix, self.complete_base, self.wfp = BackEnd.__load_dataset(self)
    
    @st.cache(allow_output_mutation=True)
    def __load_dataset(self):
        wfp = WordFP()
        
        return wfp.getbase_wordFP(), wfp.getbase_wordFP_full(), wfp

class FrontEnd(BackEnd):
    def __init__(self):
        super().__init__()
        texts_markdown = Texts()
        self.tex_home = texts_markdown.textHome()     
        self.text_contribute = texts_markdown.textContribute()
        FrontEnd.main(self)

    def main(self):
        nav = FrontEnd.navbar(self)
        if nav == 'HOME':
            st.title('Word FingerPrints')
            st.markdown('{}'.format(self.tex_home))

            pil_img = Image.open(ABSOLUT_PATH+'/figs/illustration.png')
            st.image(pil_img)            
        
        if nav == 'Search Words':
            st.title('Search Words by Similarity')
            col1,col2 = st.columns(2)
            word_inputed = str(col1.text_input('Type a word:', 'animal'))
            method_inputed = col2.selectbox('Select a similarity method:', ('geometric','arithmetic','tanimoto','tversky'))
            alpha = 1
            beta = 1
            if method_inputed == 'tversky':
                col1_, col2_, col3_, col4_ = st.columns(4)
                alpha = float(col3_.text_input('Type alpha value:', 1.5))
                beta = float(col4_.text_input('Type beta value:', 1))

            threshold_inputed = st.slider('Threshold', 0.0, 1.0, 0.75)
            
            
            btn_run = st.button('Search')
            if btn_run:
                words_similarity = self.wfp.fit_similarity(
                    base_wordFP=self.base_matrix,
                    wordFP=word_inputed,
                    complete_base=self.complete_base, #dataframe with first column of words
                    similarity_metric=method_inputed, alpha=alpha, beta=beta,
                    threshold=threshold_inputed)                
                
                st.table(pd.DataFrame({'Words':words_similarity.keys(), 'Similarity':words_similarity.values()}),)
                #st.dataframe({'Words':words_similarity.keys(), 'Similarity':words_similarity.values()})
    def navbar(self):
        nav = st.sidebar.radio('Go to:', ['HOME', 'Search Words'])
        st.sidebar.markdown('# Contribute')
        st.sidebar.info('{}'.format(self.text_contribute))##
        return nav
    

if __name__ == '__main__':
    run_app = FrontEnd()