{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python311\\python.exe' requires the ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/HP/AppData/Local/Programs/Python/Python311/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "# imoporting modules\n",
    "import pandas as pd      # its used for dataframe\n",
    "import numpy as np      # its used for n dimensional array\n",
    "import matplotlib.pyplot as plt     # its used for ploting the graph\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>v1</th>\n",
       "      <th>v2</th>\n",
       "      <th>Unnamed: 2</th>\n",
       "      <th>Unnamed: 3</th>\n",
       "      <th>Unnamed: 4</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ham</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ham</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>spam</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ham</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ham</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     v1                                                 v2 Unnamed: 2  \\\n",
       "0   ham  Go until jurong point, crazy.. Available only ...        NaN   \n",
       "1   ham                      Ok lar... Joking wif u oni...        NaN   \n",
       "2  spam  Free entry in 2 a wkly comp to win FA Cup fina...        NaN   \n",
       "3   ham  U dun say so early hor... U c already then say...        NaN   \n",
       "4   ham  Nah I don't think he goes to usf, he lives aro...        NaN   \n",
       "\n",
       "  Unnamed: 3 Unnamed: 4  \n",
       "0        NaN        NaN  \n",
       "1        NaN        NaN  \n",
       "2        NaN        NaN  \n",
       "3        NaN        NaN  \n",
       "4        NaN        NaN  "
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#read csv file\n",
    "data=pd.read_csv(\"spam.csv\",encoding=\"latin_1\")\n",
    "data.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5573, 5)"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#find no.of rows and columns\n",
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "v1               0\n",
       "v2               0\n",
       "Unnamed: 2    5523\n",
       "Unnamed: 3    5561\n",
       "Unnamed: 4    5567\n",
       "dtype: int64"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#find if any NaN numbers is there in data\n",
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Drop columns\n",
    "data = data.drop([\"Unnamed: 2\", \"Unnamed: 3\", \"Unnamed: 4\"], axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#column names rechange\n",
    "data = data.rename(columns={\"v1\":\"label\", \"v2\":\"text\"})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "ham     4826\n",
       "spam     747\n",
       "Name: label, dtype: int64"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Count observations in each label\n",
    "data.label.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# convert label to a numerical variable\n",
    "data['label_num'] = data.label.map({'ham':0, 'spam':1})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>label</th>\n",
       "      <th>text</th>\n",
       "      <th>label_num</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ham</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ham</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>spam</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ham</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ham</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  label                                               text  label_num\n",
       "0   ham  Go until jurong point, crazy.. Available only ...          0\n",
       "1   ham                      Ok lar... Joking wif u oni...          0\n",
       "2  spam  Free entry in 2 a wkly comp to win FA Cup fina...          1\n",
       "3   ham  U dun say so early hor... U c already then say...          0\n",
       "4   ham  Nah I don't think he goes to usf, he lives aro...          0"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>label</th>\n",
       "      <th>text</th>\n",
       "      <th>label_num</th>\n",
       "      <th>length</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ham</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "      <td>0</td>\n",
       "      <td>111</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ham</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "      <td>0</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>spam</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "      <td>1</td>\n",
       "      <td>155</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ham</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "      <td>0</td>\n",
       "      <td>49</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ham</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "      <td>0</td>\n",
       "      <td>61</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  label                                               text  label_num  length\n",
       "0   ham  Go until jurong point, crazy.. Available only ...          0     111\n",
       "1   ham                      Ok lar... Joking wif u oni...          0      29\n",
       "2  spam  Free entry in 2 a wkly comp to win FA Cup fina...          1     155\n",
       "3   ham  U dun say so early hor... U c already then say...          0      49\n",
       "4   ham  Nah I don't think he goes to usf, he lives aro...          0      61"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['length'] = data['text'].apply(len)\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5573, 4)"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x=np.array(data['text'])\n",
    "x\n",
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 0, 1, ..., 0, 0, 0], dtype=int64)"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y = np.array(data['label_num'])\n",
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x161059990b8>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import seaborn as sns\n",
    "sns.countplot(data[\"label\"])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x16105971630>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data[\"label\"].value_counts().plot(kind=\"pie\",autopct=\"%1.1f%%\")\n",
    "plt.axis(\"equal\")\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2     Free entry in 2 a wkly comp to win FA Cup fina...\n",
       "5     FreeMsg Hey there darling it's been 3 week's n...\n",
       "8     WINNER!! As a valued network customer you have...\n",
       "9     Had your mobile 11 months or more? U R entitle...\n",
       "11    SIX chances to win CASH! From 100 to 20,000 po...\n",
       "Name: text, dtype: object"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "spam1=data.loc[data['label']=='spam']\n",
    "spam1[\"text\"].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    Go until jurong point, crazy.. Available only ...\n",
       "1                        Ok lar... Joking wif u oni...\n",
       "3    U dun say so early hor... U c already then say...\n",
       "4    Nah I don't think he goes to usf, he lives aro...\n",
       "6    Even my brother is not like to speak with me. ...\n",
       "Name: text, dtype: object"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ham1=data.loc[data['label']=='ham']\n",
    "ham1[\"text\"].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(500,)"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_train=np.array(data.iloc[0:500,1])\n",
    "x_train.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['ham', 'ham', 'spam', 'ham', 'ham'], dtype=object)"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_train=np.array(data.iloc[0:500,0])\n",
    "y_train[0:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CountVectorizer(analyzer='word', binary=False, decode_error='strict',\n",
      "        dtype=<class 'numpy.int64'>, encoding='utf-8', input='content',\n",
      "        lowercase=True, max_df=1.0, max_features=None, min_df=1,\n",
      "        ngram_range=(1, 1), preprocessor=None, stop_words=None,\n",
      "        strip_accents=None, token_pattern='(?u)\\\\b\\\\w\\\\w+\\\\b',\n",
      "        tokenizer=None, vocabulary=None)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "count_vector = CountVectorizer()\n",
    "print(count_vector)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "train_data = count_vector.fit_transform(x_train)\n",
    "test_data = count_vector.transform(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from sklearn.naive_bayes import MultinomialNB\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model=MultinomialNB()\n",
    "model.fit(train_data,y_train)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 0, 0, ..., 0, 0, 0], dtype=int64)"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pred=model.predict(test_data)\n",
    "pred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.98385167464114831"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.score(test_data,y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "             precision    recall  f1-score   support\n",
      "\n",
      "          0       0.99      0.99      0.99      1450\n",
      "          1       0.95      0.92      0.94       222\n",
      "\n",
      "avg / total       0.98      0.98      0.98      1672\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import classification_report\n",
    "nbreport=classification_report(y_test, pred)\n",
    "print(nbreport)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from sklearn.metrics import f1_score\n",
    "from sklearn.metrics import recall_score\n",
    "from sklearn.metrics import precision_score\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "y=[f1_score(y_test,pred),recall_score(y_test,pred),precision_score(y_test,pred)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>x</th>\n",
       "      <th>y</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>f1score</td>\n",
       "      <td>0.938215</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>recall</td>\n",
       "      <td>0.923423</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>precision</td>\n",
       "      <td>0.953488</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           x         y\n",
       "0    f1score  0.938215\n",
       "1     recall  0.923423\n",
       "2  precision  0.953488"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x=[\"f1score\",\"recall\",\"precision\"]\n",
    "y=[f1_score(y_test,pred),recall_score(y_test,pred),precision_score(y_test,pred)]\n",
    "df = pd.DataFrame(dict(x=x, y=y))\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x16105aace10>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.factorplot(\"x\",\"y\", data=df,kind=\"bar\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x16105a390f0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(\"x\",\"y\", data=df)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x16105b374a8>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.pie(y,labels=x,autopct='%1.1f%%')\n",
    "plt.axis(\"equal\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#creating testing data\n",
    "x_test=[ \"hi how are you\",\n",
    "        \"Free entry in 2 a wkly comp to win FA Cup fina...\",\n",
    "        \"when will you go to home\",\n",
    "        \"i will call you back\",\n",
    "        \"are you busy now\"]\n",
    "                 \n",
    "                "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "x_test.append(\"goodmoring\")\n",
    "x_test.append(\"WINNER!! As a valued network customer you have...\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['hi how are you',\n",
       " 'Free entry in 2 a wkly comp to win FA Cup fina...',\n",
       " 'when will you go to home',\n",
       " 'i will call you back',\n",
       " 'are you busy now',\n",
       " 'goodmoring',\n",
       " 'WINNER!! As a valued network customer you have...']"
      ]
     },
     "execution_count": 138,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['hi how are you',\n",
       "       'Free entry in 2 a wkly comp to win FA Cup fina...',\n",
       "       'when will you go to home', 'i will call you back',\n",
       "       'are you busy now', 'goodmoring',\n",
       "       'WINNER!! As a valued network customer you have...'],\n",
       "      dtype='<U49')"
      ]
     },
     "execution_count": 139,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_test1=np.array(x_test)\n",
    "x_test1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    Go until jurong point, crazy.. Available only ...\n",
       "1                        Ok lar... Joking wif u oni...\n",
       "2    Free entry in 2 a wkly comp to win FA Cup fina...\n",
       "3    U dun say so early hor... U c already then say...\n",
       "4    Nah I don't think he goes to usf, he lives aro...\n",
       "5    FreeMsg Hey there darling it's been 3 week's n...\n",
       "Name: text, dtype: object"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train=data.iloc[0:200,1]\n",
    "X_train[0:6]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0     ham\n",
       "1     ham\n",
       "2    spam\n",
       "3     ham\n",
       "4     ham\n",
       "Name: label, dtype: object"
      ]
     },
     "execution_count": 141,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Y_train=data.iloc[0:200,0]\n",
    "Y_train[0:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CountVectorizer(analyzer='word', binary=False, decode_error='strict',\n",
      "        dtype=<class 'numpy.int64'>, encoding='utf-8', input='content',\n",
      "        lowercase=True, max_df=1.0, max_features=None, min_df=1,\n",
      "        ngram_range=(1, 1), preprocessor=None, stop_words=None,\n",
      "        strip_accents=None, token_pattern='(?u)\\\\b\\\\w\\\\w+\\\\b',\n",
      "        tokenizer=None, vocabulary=None)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "count_vector = CountVectorizer()\n",
    "print(count_vector)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "train_data = count_vector.fit_transform(X_train)\n",
    "test_data = count_vector.transform(x_test1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(200, 1159)"
      ]
     },
     "execution_count": 144,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(7, 1159)"
      ]
     },
     "execution_count": 145,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test_data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(200,)"
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Y_train.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from sklearn.naive_bayes import MultinomialNB\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)"
      ]
     },
     "execution_count": 148,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model=MultinomialNB()\n",
    "model.fit(train_data,Y_train)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['ham', 'spam', 'ham', 'ham', 'ham', 'ham', 'spam'],\n",
       "      dtype='<U4')"
      ]
     },
     "execution_count": 149,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pred=model.predict(test_data)\n",
    "pred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "y1=model.predict(test_data)               "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['ham', 'spam', 'ham', 'ham', 'ham', 'ham', 'spam'],\n",
       "      dtype='<U4')"
      ]
     },
     "execution_count": 151,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>INPUT</th>\n",
       "      <th>OUTPUT</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>hi how are you</td>\n",
       "      <td>ham</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "      <td>spam</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>when will you go to home</td>\n",
       "      <td>ham</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>i will call you back</td>\n",
       "      <td>ham</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>are you busy now</td>\n",
       "      <td>ham</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>goodmoring</td>\n",
       "      <td>ham</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>WINNER!! As a valued network customer you have...</td>\n",
       "      <td>spam</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                               INPUT OUTPUT\n",
       "0                                     hi how are you    ham\n",
       "1  Free entry in 2 a wkly comp to win FA Cup fina...   spam\n",
       "2                           when will you go to home    ham\n",
       "3                               i will call you back    ham\n",
       "4                                   are you busy now    ham\n",
       "5                                         goodmoring    ham\n",
       "6  WINNER!! As a valued network customer you have...   spam"
      ]
     },
     "execution_count": 152,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame(dict(INPUT=x_test1, OUTPUT=y1))\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>INPUT</th>\n",
       "      <th>OUTPUT</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>are you busy now</td>\n",
       "      <td>ham</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>goodmoring</td>\n",
       "      <td>ham</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>WINNER!! As a valued network customer you have...</td>\n",
       "      <td>spam</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                               INPUT OUTPUT\n",
       "4                                   are you busy now    ham\n",
       "5                                         goodmoring    ham\n",
       "6  WINNER!! As a valued network customer you have...   spam"
      ]
     },
     "execution_count": 153,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.iloc[4:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
