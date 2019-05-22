#!//usr/local/bin python
# -*- coding:utf-8 -*-

"""
Created on 2019/1/16 14:19
@author: liangchen
Project: SelfTestPro
"""
import pymysql
# db_name = ['presell']
# db_presell = "host='common101.my.2dfire-daily.com', user='twodfire', passwd='123456',db='presell',port=3306, charset='utf8'"
sql = "select * from `presell_stock_order` where order_id = '99928869683679f60168374e089b005f'"
sql1 = "select banner_title,banner_desc,img,content_json from presell_album_banner where banner_id = '372388439246602241' AND is_valid = 1"
db_name = "presell"

def select_daily(sql, db_name, *args):
    """
    查询方法，支持返回多行多个字段，接收一个或三个参数，参数2-3都填或都不填，如查询返回第一条记录中的id的值，传入（sql，'presell', 0，'id'）
    :param sql，必填，要执行的sql语句，返回多行多字段
    :param 2，第几条记录
    :param 3，要查询的字段名
    :return: result，查询结果
    """
    db = pymysql.connect(host='common101.my.2dfire-daily.com', user='twodfire', passwd='123456',db=db_name,port=3306, charset='utf8')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        if args:
            row, id = args[0], args[1]
            result = get_result(data, row, id)
        else:
            result = data
        print(result)
        return  str(result)
    except ZeroDivisionError as e:
        print(e)
        db.rollback()
    cursor.close()
    db.commit()
    db.close()

def get_result(data, row, id):
    """
    取字典列表类型具体值
    :param data: 字典列表
    :param row: 列表中的第几个值，从1开始
    :param id: 字典的key
    :return: value 字典的value
    """
    result = datavalue(data)
    row = int(row)
    print(type(result[0]))
    print(result[0].keys())
    if row < len(result) + 1 and id in result[0].keys():
        return result[row-1][id]
    else:
        return '参数错误'
    print("---------result----------:"+result)



def datavalue(data):
    """
    查询结果类型转换
    """
    result = []
    if data:
        for i in data:
            result.append(i)
        return result
    else:
        return ''

# data_sql = select_daily(sql, db_name)
# print(data_sql)

data_sql = ({'presell_stock_order_id': 400717459369328640, 'presell_stock_id': 398324690738839552, 'customer_id': '10c34bce7bc345448013cd21f06b9197', 'order_id': '99928869683679f60168374e089b005f', 'discount': 50, 'entity_id': '99928869', 'time_frame_id': 660, 'time_frame_name': '11:00-11:10', 'seat_type_id': 1, 'seat_type_name': '小桌||1-2人', 'week_id': 5, 'meal_time': 1547175600000, 'stock_time': 1547136000000, 'start_time': 1547175600000, 'end_time': 1547176200000, 'order_status': 3, 'source': 1, 'ext_field': '{"refundRatio":70,"serviceFeePlan":{"fee":100,"ratio":5,"type":1}}', 'create_time': 1547116087289, 'op_time': 1547236082900, 'last_ver': 3, 'is_valid': 1, 'effective_time': 1547121487289},)
# data_test = ({'number': 1, 'user': '张三'},)
# resultTest = datavalue(data_sql)
# print(resultTest)
# print(resultTest[0].keys())
# print(get_result(data_sql, 1, 'discount'))
data_list = [{'banner_title': '接口测试用', 'banner_desc': '接口测试用-专题描述', 'img': 'https://download.2dfire.com/advertisingplatform/41c1c1f2cfd342d29a56d59a4acdf9d2.jpg', 'content_json': '[{"content":"接口测试用-专题详情1","index":0,"type":1},{"content":"https://download.2dfire.com/advertisingplatform/5f1419d429894a7990cea033a58a4de7.jpg","index":1,"type":2},{"type":3,"content":"9918007967f2dce60167f4435d1100eb","dishImg":"http://ifiletest.2dfire.com/99180079/menu/0d94f75455ed45e68bb5c487681b1106.png","entityName":"橄榄内网测试店_0002","menuName":"接口测试用普通商品","index":2}]'}]
data_sql1 = select_daily(sql1, 'presell')

# print(select_daily(sql1, 'presell'))
print(get_result(data_list, 1, 'banner_title'))