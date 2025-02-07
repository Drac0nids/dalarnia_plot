from flask import Flask, render_template, request,jsonify
import sqlite3
import json

app = Flask(__name__)

# 数据库路径
DB_PATH = 'plotstate.db'


# 查询PL值的数据，排除rent为None的数据，按rent从小到大排序
def get_pl_data(pl_value):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 查询语句：根据PL值获取数据，并按rent从小到大排序
    query = '''
        SELECT * FROM plot
        WHERE PL = ? AND rent IS NOT NULL AND left != 0
        ORDER BY rent ASC
    '''
    cursor.execute(query, (pl_value,))
    rows = cursor.fetchall()
    conn.close()

    return rows


@app.route('/')
def index():
    # 获取请求中的PL参数，默认PL为1
    pl_value = request.args.get('pl', '1')

    # 获取对应PL值的数据
    data = get_pl_data(pl_value)

    # 将数据和PL值传递到HTML模板中
    return render_template('index.html', data=data, selected_pl=pl_value)

# 读取价格数据从 JSON 文件
def load_prices_from_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

@app.route('/prices')
def get_price():
    prices_data = load_prices_from_json('prices.json')
    return render_template('prices.html', prices=prices_data)

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=5000)
