# Misinformation-Detection-COVID19
A machine learning project to detect misinformation related to COVID-19 using Support Vector Machine (SVM) with 91% accuracy.The goal of this project is to classify news articles or social media posts as either fake or real using machine learning techniques. 

# Key Features
1.Fake vs Real News Detection: Classify news articles into fake and real categories based on their content.

2.Natural Language Processing (NLP): Utilizes NLP techniques to process and clean textual data.

3.Machine Learning Model: A Support Vector Machine (SVM) classifier is used to detect fake news with high accuracy.

4.Evaluation: The model is evaluated using metrics like accuracy, precision, recall, f1-score, and confusion matrix.

# Features
The project uses the following features for detecting misinformation related to COVID-19:

Text Data Preprocessing: Removal of punctuation, special characters, and stopwords.Text lowercasing and tokenization.Lemmatization to reduce words to their base form.

Feature Extraction:  TF-IDF Vectorizer to convert text into numerical features by measuring the importance of words in the dataset.

Machine Learning Model: Support Vector Machine (SVM) with a linear kernel.

# Evaluation
The model is evaluated using the following metrics:

Accuracy: The model achieved 91% accuracy.
Confusion Matrix: Displays the count of true positives, false positives, true negatives, and false negatives.
Precision, Recall, and F1-Score: Detailed performance metrics to assess how well the model is detecting fake vs. real news.

# Evaluation Metrics
The model performance is evaluated using the following metrics:

Accuracy: 91%
Precision (Real News): 0.89
Recall (Real News): 0.94
Precision (Fake News): 0.93
Recall (Fake News): 0.88
F1-Score: 0.91

# Dataset
The dataset used in this project is sourced from:IEEE DataPort 
Covid-19 Fake News Infodemic Research Dataset (CoVID19-FNIR Dataset) - Julio A. Saenz (University of Wyoming)
Sindhu Reddy Kalathur Gopal (University of Wyoming)
Diksha Shukla (University of Wyoming)

Citation:
Julio A. Saenz, Sindhu Reddy Kalathur Gopal, Diksha Shukla, June 12, 2021, "Covid-19 Fake News Infodemic Research Dataset (CoVID19-FNIR Dataset)", IEEE Dataport, doi: https://dx.doi.org/10.21227/b5bt-5244.



# **Misinformation Detection - COVID-19**

A machine learning project to detect misinformation related to **COVID-19** using a **Support Vector Machine (SVM)** model with **91% accuracy**. The goal of this project is to classify news articles or social media posts as either **fake or real** using machine learning techniques.


## **Key Features**

1. **Fake vs Real News Detection:** Classifies news articles into **fake and real categories** based on their content.
2. **Natural Language Processing (NLP):** Utilizes NLP techniques to **process and clean textual data**.
3. **Machine Learning Model:** Employs a **Support Vector Machine (SVM)** classifier to detect fake news with high accuracy.
4. **Evaluation Metrics:** The model is evaluated using metrics like **accuracy, precision, recall, f1-score, and confusion matrix**.


## **Features**

The project uses the following features for detecting misinformation related to COVID-19:

* **Text Data Preprocessing:**

  * Removal of punctuation, special characters, and stopwords.
  * Text lowercasing and tokenization.
  * Lemmatization to reduce words to their base form.

* **Feature Extraction:**

  * **TF-IDF Vectorizer** to convert text into numerical features by measuring the importance of words in the dataset.

* **Machine Learning Model:**

  * **Support Vector Machine (SVM)** with a linear kernel for effective classification.


## **Evaluation**

The model performance is evaluated using the following metrics:

* **Accuracy:** Achieved **91% accuracy** on the test dataset.
* **Confusion Matrix:** Displays the count of true positives, false positives, true negatives, and false negatives.
* **Precision, Recall, and F1-Score:** Detailed metrics to assess the model’s performance in detecting fake vs. real news.

### **Evaluation Metrics**

| Metric        | Real News (1) | Fake News (0) | Overall |
| ------------- | ------------- | ------------- | ------- |
| **Precision** | 0.89          | 0.93          | -       |
| **Recall**    | 0.94          | 0.88          | -       |
| **F1-Score**  | 0.92          | 0.90          | 0.91    |
| **Accuracy**  | -             | -             | 91%     |


## **Dataset**

The dataset used in this project is sourced from **IEEE DataPort**:

**Dataset Title:** Covid-19 Fake News Infodemic Research Dataset (CoVID19-FNIR Dataset)

**Authors:**

* Julio A. Saenz, University of Wyoming
* Sindhu Reddy Kalathur Gopal, University of Wyoming
* Diksha Shukla, University of Wyoming

**Citation:**

> Saenz, J. A., Kalathur Gopal, S. R., & Shukla, D. (2021). Covid-19 Fake News Infodemic Research Dataset (CoVID19-FNIR Dataset). IEEE DataPort. [https://dx.doi.org/10.21227/b5bt-5244](https://dx.doi.org/10.21227/b5bt-5244)


