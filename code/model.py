
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.svm import SVC 

def model_evaluation(x, y):
   
    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(x)

    #train test split 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42 )

    #Model
    model = SVC(kernel="linear")
    model.fit(X_train, y_train)


    y_pred = model.predict(X_test)


    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print("Confusion Matrics\n",confusion_matrix(y_test,y_pred))