import streamlit as st
import numpy as np
import pandas as pd
import time

from PIL import Image

st.title("Streamlit 超入門")

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目':[10, 20, 30, 40]
})

#動的な表にはデータフレーム
st.dataframe(df.style.highlight_max(axis=0))
#静的な表にはテーブル
st.table(df.style.highlight_max(axis=0))

#マークダウン
"""
# 章
## 節
### 項

#バッククオーテーション shift + @
```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

#折れ線グラフ
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(df)

#マップ
df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df)

 #イメージ
st.write("Display Image")

#チェックボックス(boolian型で返すため、if文で表示可否をできる)
if st.checkbox('Show Image'):
    img = Image.open('sample.png')
    st.image(img, caption='sample image', use_column_width=True)

#セレクトボックス
option = st.selectbox(
'あなたが好きな数字を教えてください',
list(range(1, 11))
)
'あなたの好きな数字は', option, 'です。'

#テキスト入力
option2 = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味：', option2

#スライダー
condition = st.slider('あなたの今の調子は?', 0, 100, 50)
'コンディション；', condition

#siderbar
option3 = st.sidebar.text_input('あなたの特技を教えてください。')
'あなたの特技：', option3

#スライダー
condition2 = st.sidebar.slider('あなたの今の調子は?', 0, 200, 50)
'コンディション；', condition2

#２カラムにする場合
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

#expander
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

#プレグレスバーの表示
st.title('プレグレスバー')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'