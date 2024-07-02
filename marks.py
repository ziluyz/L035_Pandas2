import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Name": ["Вася", "Петя", "Маша", "Коля", "Витя", "Саша", "Миша", "Ваня", "Юля", "Катя"],
}

df = pd.DataFrame(data)
df['Math'] = np.random.randint(2, 5, 10)
df['Math'] = df['Math'].map({2: 3, 3: 3, 4: 4, 5: 5})
df['Physics'] = np.random.randint(2, 5, 10)
df['Physics'] = df['Physics'].map({2: 4, 3: 3, 4: 4, 5: 5})
df['English'] = np.random.randint(2, 6, 10)
df['English'] = df['English'].map({2: 3, 3: 3, 4: 4, 5: 5, 6: 5})
df['Chemistry'] = np.random.randint(2, 6, 10)
df['Chemistry'] = df['Chemistry'].map({2: 3, 3: 3, 4: 4, 5: 5, 6: 4})
df['Biology'] = np.random.randint(2, 6, 10)
df['Biology'] = df['Biology'].map({2: 3, 3: 3, 4: 4, 5: 5, 6: 3})
print(df.head())

for subject in df.columns[1:]:
    print(f'Средний балл по предмету {subject} = ', df[subject].mean())

for subject in df.columns[1:]:
    print(f'Медианный балл по предмету {subject} = ', df[subject].median())

Q1_math = df['Math'].quantile(0.25)
Q3_math = df['Math'].quantile(0.75)
print(f'Квартили по математике: Q1 = {Q1_math}, Q3 = {Q3_math}, IQR = {Q3_math - Q1_math}')

for subject in df.columns[1:]:
    print(f'Стандартное отклонение оценок по предмету {subject} = ', df[subject].std())