from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Function for a nice visualisation of the predicted results (confusion matrix) and important scores

def vis_results(y_test, y_pred, model, savefig = True):
    '''Takes an array ytest and an array ypred and returns a confusion matrix,
       as well as a classification report. 

       savefig: if True the confusion matrix is saved in the images folder.
       model: str used as prefix for the confusion matrix file and title for the confusion matrix plot
    '''

    print('----------'*6)
    print('Classification report:')
    print(classification_report(y_test,y_pred))
    print('----------'*6)
    print('Confusion matrix:')
    conf_mat = sns.heatmap(confusion_matrix(y_test,y_pred), annot=True, fmt='d', cmap='Blues')
    plt.title(model)
    if savefig: 
        conf_mat.figure.savefig('images/Confusion_Matrices/'+model+'_confusion_matrix.png',dpi=600)
    print('----------'*6)

    return

# Function for a pairplot 

def make_pairplot(df, target):

    sns.pairplot(df, hue=target)
    
    return