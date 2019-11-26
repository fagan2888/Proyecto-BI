import glob
import pandas as pd

DEFAULT_VALUE = "NE"

def merge(basis, merger):
	newDFModel = {}

	reference = basis.columns
	additions = merger.columns
	missingRef = []
	missingAdd = []
	for ref in reference:
		if ref not in additions:
			missingAdd.append(ref)
		newDFModel[ref] = []

	for add in additions:
		if add not in reference:
			missingRef.append(add)
			newDFModel[add] = []

	for index, row in basis.iterrows():
		for col in reference:
			newDFModel[col].append(row[col])
		for col in missingRef:
			newDFModel[col].append(DEFAULT_VALUE)

	for index, row in merger.iterrows():
		for col in additions:
			newDFModel[col].append(row[col])
		for col in missingAdd:
			newDFModel[col].append(DEFAULT_VALUE)
	
	return pd.DataFrame(newDFModel)



path = './Data/'

files = [f for f in glob.glob(path + "**/*.csv", recursive=True)]

colCount = 0
rowCount = 0
baseDF = pd.DataFrame()
for f in files:
    print(f)
    nextDF = pd.read_csv(f)
    colCount += len(nextDF.columns)
    rowCount += len(nextDF.index)
    baseDF = merge(baseDF, nextDF)

print(baseDF)
print(f"Column count = {colCount}")
print(f"Rows count = {rowCount}")

baseDF.to_csv('./Data/merger.csv')
