import pandas as pd
import numpy as np
# df2 = pd.DataFrame({'A': 1.,
#                    'B': pd.Timestamp('20130102'),
#                     'C': pd.Series(1, index=list(range(4)), dtype='float32'),
#                     'D': np.array([3] * 4, dtype='int32'),
#                    'E': pd.Categorical(["test", "train", "test", "train"]),
#                      'F': 'foo'})

# print(df2)
"""
output:
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
"""

#设置新列会自动根据索引对齐数据
# s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
# print(s1)
"""
output:
2013-01-02    1
2013-01-03    2
2013-01-04    3
2013-01-05    4
2013-01-06    5
2013-01-07    6
Freq: D, dtype: int64
"""

df = pd.DataFrame(np.random.randn(10, 4))
pieces = [df[:3], df[3:7], df[7:]]
# print(pieces)
"""
0  0.902651  0.150625 -0.291665  0.220751
1 -0.188521  0.130443 -0.008045  1.074823
2  0.594288 -2.246439  0.456267 -1.296706
3  0.963225  0.215242  0.206628 -0.526528
4 -0.506828  1.134883  0.549327  0.944430
5  0.184592  0.631535 -0.561415 -0.357763
6  1.406520 -0.026201 -0.661854 -0.830290
7  0.324380 -0.278888  0.753445 -0.590513
8 -1.121209  0.296216 -0.578055 -1.420044
9  0.601686  0.786369 -1.440058  1.064700

[Done] exited with code=0 in 0.643 seconds

[Running] set PYTHONIOENCODING=utf8 && python "d:\myownproject\python_module\pandas\ten_minute_to_pandas\ten_minute.py"
[          0         1         2         3
0 -0.373071 -0.530921 -1.538129  0.031943
1 -0.383470 -0.271856  0.177228  1.371854
2  1.221670  0.787364 -0.610222  0.870088,           0         1         2         3
3  0.044643 -0.527478 -0.467751  0.578333
4  1.938748 -0.253916 -1.447081  0.560759
5  1.685412 -0.177840  1.835068 -0.114197
6  0.495883  1.315437  0.032838 -2.241391,           0         1         2         3
7 -1.737737  1.084439  0.115656  0.506746
8 -0.357714 -0.871044 -0.537509  0.327687
9 -0.629513 -1.200397 -0.583734 -0.289744]

"""
# df = pd.concat(pieces)

# print(df)


#merge
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})

right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
# print(left)
# print(right)
"""
output:
   key  lval
0  foo     1
1  foo     2
   key  rval
0  foo     4
1  foo     5
"""
s= pd.merge(left, right, on='key')

print(s)

"""
   key  lval  rval
0  foo     1     4
1  foo     1     5
2  foo     2     4
3  foo     2     5
"""

df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])

s = df.iloc[3]
data = df.append(s,ignore_index=True)
# print(data)

"""
          A         B         C         D
0 -0.210018  0.080723  0.507755  1.138411
1 -0.201914  0.920912  1.420332  0.287999
2 -0.527455 -0.535411  0.252164  0.448502
3  2.183684 -0.119130  1.220929  0.631295
4  1.074264 -1.726736 -0.376312  2.743750
5 -0.414366  0.330916 -0.966685 -0.500967
6  0.829644 -2.367204  0.469080  0.707505
7 -0.427569  0.193741 -1.962748 -1.081152
8  2.183684 -0.119130  1.220929  0.631295
"""

#分组
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                        'foo', 'bar', 'foo', 'foo'],
                'B': ['one', 'one', 'two', 'three',
                        'two', 'two', 'one', 'three'],
                    'C': np.random.randn(8),
                'D': np.random.randn(8)})

sum = df.groupby('A').sum()
print(sum)
"""
A                      
bar -0.389725  1.162116
foo -5.919402 -1.048245
"""