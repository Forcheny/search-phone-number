# -*- coding: utf-8 -*-
"""

        Version 1.2.0001  2010-11-16    YONC
        Get two parameters "team=lsd" and "phoneNumber=+4544448888" from the url
        # Version 1.1, conf load
        # Version 1.0, no conf load
        # phoneNumber = request.form['phoneNumber']   # 从html获取参数值
"""

import sys
sys.path.insert(1, "D:\Apache24\LSD_PhoneBook\www")
from flask import Flask,request,render_template
from search import pandas_search
from ConfigLoad import check_section
import numpy as np

app = Flask(__name__)

# 定义home页面
@app.route('/')
def index():
    return render_template('home.html')
# 定义search初始页面
@app.route('/search_lsd', methods=['GET'])
def search_form_lsd():
    return render_template('form_lsd.html')
# 定义search初始页面
@app.route('/search_pandoralsd', methods=['GET'])
def search_form_pandoralsd():
    return render_template('form_pandoralsd.html')


# 定义searchnumber?team=lsd&phoneNumber=+4544426000
@app.route('/searchnumber')
def search_number():
    team = request.args.get('team', '')
    phoneNumber = request.args.get('phoneNumber', '')
    recordResult = []
    destColumn = []
    if check_section(team):
        if phoneNumber:
            recordResult, destColumn = pandas_search(team, phoneNumber)
            if recordResult:
                target_data = np.array(recordResult)[:, destColumn]
                if len(recordResult) >= 5:
                    warning =  'More than 5 records are matched with the number, list top 5 records.'
                else:
                    warning = '%s record(s) are matched with the number.' %len(recordResult)
                return render_template('form_%s.html' %team, table_data=target_data, message=warning)
            else:
                return render_template('form_%s.html' %team, message='No record is found out !')
        else:
            return render_template('form_%s.html' %team, message='Missing phone number in url !')
    else:
        return render_template('form_default.html', message='Missing team or team is undefined in url !')


if __name__ == '__main__':
    app.run()
