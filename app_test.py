
import numpy as np
import pandas as pd
import streamlit as st


if __name__ == '__main__':
     st.title('画图')
     st.text('折线图')
     chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
     st.line_chart(chart_data)

     st.text('柱状图')
     chart_data = pd.DataFrame(np.random.randn(50, 3), columns=["a", "b", "c"])
     st.bar_chart(chart_data)


