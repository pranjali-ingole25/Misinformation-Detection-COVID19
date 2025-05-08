
from sklearn.feature_extraction.text import TfidfVectorizer  # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix # type: ignore
from sklearn.svm import SVC # type: ignore
'''from sklearn.linear_model import LogisticRegression # type: ignore
from sklearn.naive_bayes import MultinomialNB # type: ignore
from sklearn.ensemble import RandomForestClassifier # type: ignore'''

def model_evaluation(x, y):
   
    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(x)


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42 )


    # model = LogisticRegression()
    # model = MultinomialNB()
    # model = RandomForestClassifier()
    model = SVC(kernel="linear")
    model.fit(X_train, y_train)


    y_pred = model.predict(X_test)


    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print("Confusion Matrics\n",confusion_matrix(y_test,y_pred))