"""
@file   : main.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2022-06-10
"""
import json
import requests
import streamlit as st
#from pyecharts.globals import ThemeType
# from pyecharts import options as opts
# from pyecharts.charts import Bar, Pie
# from streamlit_echarts import st_echarts, st_pyecharts


class MultiApp:
    def __init__(self):
        self.apps = []
        self.app_dict = {}

    def add_app(self, title, func):
        if title not in self.apps:
            self.apps.append(title)
            self.app_dict[title] = func

    def run(self):
        title = st.sidebar.radio(
            '功能',
            self.apps,
            format_func=lambda title: str(title))
        self.app_dict[title]()


def run_docker_notebook():
    with open('./data/docker笔记.md', 'r', encoding='utf8') as f:
        text = f.read()
    st.write(text)


def run_sql_notebook():
    with open('./data/sql语句联系.md', 'r', encoding='utf8') as f:
        text = f.read()
    st.write(text)


def run_plot():
    # 这里借助pyecharts

    # 首先是柱状图  瞎编一组数据
    x = ['10->15k', '15-20k', '20-25k', '25-30k', '30-35k', '35-40k', '40k+']
    y = [213, 421, 131, 321, 145, 123, 73]

    b = (
        Bar({"theme": ThemeType.DARK})  # 设置主题
            .set_global_opts(
            title_opts=opts.TitleOpts(title="程序员收入(自己瞎编的)"),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-45))  # 名字倾斜15度
        )
        .add_xaxis(x)
        .add_yaxis('人数', y)

    )
    st_pyecharts(b, height='400px', width='100%')

    # 同样用上述的数据画个饼状图
    pie = (
        Pie()
            .set_global_opts(title_opts=opts.TitleOpts(title="程序员收入"),
                             legend_opts=opts.LegendOpts(orient="vertical", pos_top="0%",
                                                         pos_right="0%", is_show=True,
                                                         item_gap=2, item_width=8,
                                                         item_height=4
                                                         ),
                             )
            .add("", [list(z) for z in zip(x, y)])
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}", font_size=10, is_show=True))  # 标签显示的样子

    )
    st_pyecharts(pie, height='600px', width='100%')


if __name__ == '__main__':
    app = MultiApp()
    app.add_app('SQL语句练习', run_sql_notebook)
    app.add_app('docker笔记', run_docker_notebook)
    # app.add_app('随机画画图', run_plot)
    app.run()
