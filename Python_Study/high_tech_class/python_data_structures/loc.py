import pandas as pd
loc = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})
loc[0, 'A'] = 10  
loc.iloc[1, 1] = 20  
loc.loc[2, 'C'] = 30  

print(loc)

iloc = pd.DataFrame({
    'X': [10, 20, 30],
    'Y': [40, 50, 60],
    'Z': [70, 80, 90]
})
iloc.iloc[0, 0] = 100
iloc.iloc[1, 1] = 200
iloc.iloc[2, 2] = 300
print(iloc)