import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''


# First, split the string on the (hidden characters that indicate) newlines
data = data.splitlines() # we could also do data.split('\n')

# Then, split each item in this list on the commas
# the bracketed expression is a list comprehension
data = [i.split(', ') for i in data] 

# Now, convert create a pandas dataframe
column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

print "****"
x = stats.mode(df['Alcohol'])
print x[0]
print "****"

# Convert Alcohol and Tobacco columns to float
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)


#  mean, median, mode, range, variance, and standard deviation for the Alcohol and Tobacco dataset 
#  with full text (ex. "The range for the Alcohol and Tobacco dataset is ..."). 

print "The mean for Alcohol dataset is %f" % df['Alcohol'].mean()
print "The mean for Tobacco dataset is %f" % df['Tobacco'].mean()

print "The median for Alcohol dataset is %f" % df['Alcohol'].median() 
print "The median for Tobacco dataset is %f" % df['Tobacco'].median() 
print "The mode for Alcohol dataset is ", stats.mode(df['Alcohol']) 
print "The mode for Tobacco dataset is ", stats.mode(df['Tobacco']) 

print "The range of Alcohol dataset is ", max(df['Alcohol']) - min(df['Alcohol'])
print "The range of Tobacco dataset is ", max(df['Tobacco']) - min(df['Tobacco'])

print "the variance of Alcohol dataset is %f" % df['Alcohol'].var() 
print "the variance of Tobacco dataset is %f" % df['Tobacco'].var() 

print "The standard variation for Alcohol dataset is %s" % df['Alcohol'].std() 
print "The standard variation for Tobacco dataset is %s" % df['Tobacco'].std() 

