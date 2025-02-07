import sqlite3

def create_table():
    conn = sqlite3.connect('plotstate.db')
    cur = conn.cursor()
    sql_text_1 = '''CREATE TABLE plot (plotId NUMBER,planet TEXT,X TEXT,Y TEXT, PL TEXT, rent NUMBER, left NUMBER);'''
    cur.execute(sql_text_1)
    conn.commit()
    conn.close()
def select_data():
    conn = sqlite3.connect('plotstate.db')
    cur = conn.cursor()
    sql_text_3 = "SELECT * FROM plot"
    cursor = cur.execute(sql_text_3)
    for row in cursor:
        print(row)
def isPlotExist(plotId):
    sql_text = "SELECT plotId FROM plot WHERE plotId ="+str(plotId)
    conn = sqlite3.connect('plotstate.db')
    cur = conn.cursor()
    cursor = cur.execute(sql_text)
    result = cursor.fetchone()
    return result
def parsePlotId(plotId):
    if(str(plotId)[:3] == "101"):
        planet = "prime"
    elif(str(plotId)[:3] == "102"):
        planet = "simia"
    else:
        planet = "caldera"
    x = str(plotId)[7:9]
    y = str(plotId)[10:12]
    return planet,x,y

def insert_plot(plotId,planet,x,y):
    conn = sqlite3.connect('plotstate.db')
    cur = conn.cursor()
    insert_sql = "INSERT INTO plot (plotId,planet,X,Y) \
          VALUES (?,?,?,? )"
    data = (plotId,planet,x,y)
    cur.execute(insert_sql, data)
    conn.commit()
def update_digleft(plotId,digleft):
    conn = sqlite3.connect('plotstate.db')
    cur = conn.cursor()
    cur.execute('''
        UPDATE plot
        SET left = ?
        WHERE plotId = ?
        ''', (digleft, plotId))
    conn.commit()
def update_rent(plotId,rent):
    conn = sqlite3.connect('plotstate.db')
    cur = conn.cursor()
    cur.execute('''
            UPDATE plot
            SET rent = ?
            WHERE plotId = ?
            ''', (rent, plotId))
    conn.commit()
def update_PL(plotId,PL):
    conn = sqlite3.connect('plotstate.db')
    cur = conn.cursor()
    cur.execute('''
                UPDATE plot
                SET PL = ?
                WHERE plotId = ?
                ''', (PL, plotId))
    conn.commit()
#create_table()
def recipeIdToPL(recipeId):
    if recipeId == 1:
        PL = 1
        return PL
    elif recipeId == 2 or recipeId == 3:
        PL = 3
        return PL
    elif recipeId == 4 or recipeId == 5:
        PL = 7
        return PL
    elif recipeId == 7:
        PL = 12
        return PL
    elif recipeId == 8 or recipeId ==9 or recipeId ==10 or recipeId==11:
        PL = 15
        return PL



def get_lowest_rent_pl_1(limit=100):
    # 查询 PL 为 1 且 rent 最低的 100 条记录
    conn = sqlite3.connect('plotstate.db')
    cur = conn.cursor()
    cur.execute('''
    SELECT * FROM plot
    WHERE PL = '1'
    ORDER BY rent ASC
    LIMIT ?
    ''', (limit,))

    # 获取查询结果
    results = cur.fetchall()
    conn.close()
    print(results)
if __name__ == '__main__':
    #update_digleft(103003028001,10)
    #update_rent(103003028001,0.2)
    #update_PL(103003028001,100)
    select_data()



