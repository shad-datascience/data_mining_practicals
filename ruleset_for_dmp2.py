# [iii] Ruleset definition

def DirtyIrisRuleset(row):
    errorlist = []

    #rule 1
    if row['Species'] not in ['setosa','versicolor','virginica']:
        errorlist.append("species must be 'setosa' or 'versicolor' or 'virginica'")
    
    #rule 2
    if (row['Sepal.Length'] <= 0) or (row['Sepal.Width'] <= 0):
        errorlist.append('numerical properties cannot be zero')
    elif (row['Petal.Length'] <= 0) or (row['Petal.Length'] <= 0):
        errorlist.append('numerical properties cannot be zero')
    else:
        pass

    #rule 3
    if row['Sepal.Length'] < row['Petal.Width']:
        errorlist.append('sepal length must be atleast 2x petal width')
    
    #rule 4
    if row['Sepal.Length'] > 30:
        errorlist.append("sepal length must not be > 30")

    #rule 5
    if row['Sepal.Length'] <= row['Petal.Length']:
        errorlist.append("sepal length must be longer than petal length")

    return errorlist