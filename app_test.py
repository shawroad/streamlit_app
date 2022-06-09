
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import altair


def matplotlib_in_streamlit():
     # 可以将matplot画的图嵌入到页面内   下面三行就可实现  但是太丑了
     fig = plt.figure()
     plt.plot([1, 2, 3, 4], [21, 12, 32, 12])
     st.pyplot(fig)


if __name__ == '__main__':
     st.title('画图')
     st.text('折线图')
     chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
     st.line_chart(chart_data)

     st.text('柱状图')
     chart_data = pd.DataFrame(np.random.randn(50, 3), columns=["a", "b", "c"])
     st.bar_chart(chart_data)


