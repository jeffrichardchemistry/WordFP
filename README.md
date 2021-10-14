# WordFP
This application consists of a python package made to encode words and compare them through similarity calculation.
The words are encoded in a matrix of 0's and 1's called "WordFP", where the first column refers to all the letters
present in a word and the second column to the last refers to the position of a certain letter in a word.
The search for similar words is calculated based on the metrics: geometric, arithmetic, tanimoto and tversky.
A jupyter-notebook with an example of using this package is in the examples/how_to_use.ipynb directory

<p align="center"><img src="/examples/illustration.png?raw=true" width=500 align="middle"></p>

Another way to use this package is through of web app [WordFP](https://github.com/jeffrichardchemistry/WordFP).
It is possible to run locally too following the steps below.

<p align="center"><img src="/examples/wordfp_app.gif?raw=true" align="middle"></p>

## Install
<b>Via pip</b>
```
$ pip install wordfp
```
or

<b>Via github</b>
```
$ git clone https://github.com/jeffrichardchemistry/WordFP
$ cd WordFP
$ python3 setup.py install
```

## Install and Run WebAPP Locally
The web application is in the "app/app.py" folder. Install dependencies:
```
$ pip install streamlit wordfp
```
To run:
```
$ cd .../app/
$ streamlit run app.py
```

## Considerations
This project was an idea I came up with at a random moment while studying my PhD work,
I hope it can help someone someday in areas like natural language processing (NLP).
