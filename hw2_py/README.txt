Homework 2: Descriptive Modeling and Unsupervised Learning of Textual Data


Files in Use: (remove before submitting hw)
main2.py
preprocessor.py
docmatrix.py
kmeans.py
evaluation.py
visualization.py
similarity.py


Built with:
Python 3
Jupyter IDE
PyCharm IDE


Installation:

The follow libraries were installed in a Python virtual environment.

1. NLTK
2. spaCy
3. gensim

$ pip install -U <name of library>

The spaCy library extension ‘en_core_web_sm’ is also used and can be installed as a package.

$ python -m spacy download en_core_web_sm


User Guide:

Files: main.py, preprocessor.py, preprocessing&lda.py, src folder (contains all text documents and stopwords.txt)

This program runs by typing "python main.py" at the command line. Main.py opens a file, data.txt, reads each
file name, and executes the file against the program. Main.py also calls preprocessor.py, which
contains all the classes that we have written. After running the preprocessor, a list of the most frequently
occuring topics in the corpus is output to topics.txt, which is located in the same directory as main.py.

The LDA program runs separately in preprocessing&lda.py.

More information about the libraries at:
https://www.nltk.org/install.html
https://spacy.io/usage/
https://spacy.io/usage/models
https://pypi.org/project/gensim/