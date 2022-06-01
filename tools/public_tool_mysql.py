# coding: utf-8
import pymysql
from pymysql import cursors


class toolMyDB:
    def __init__(self, host: str, user: str, port: int, passwd: str, db: str, charset: str):
        """
        :param host:
        :param user:
        :param port:
        :param passwd:
        :param db:
        :param charset:
        """
        self.cnn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=passwd,
            database=db,
            charset=charset
        )
        self.cursor = self.cnn.cursor(cursor=cursors.DictCursor)  # 结果使用dict返回

    def __del__(self):
        """
        :return:
        """
        try:
            self.cnn.close()
        except Exception as e:
            raise e

        try:
            self.cursor.close()
        except Exception as e:
            raise e

    def insert(self, table, insert_data):
        """
        :param table:
        :param insert_data: type:[{},{}]:
        :return:effect_row 1 影响的行数
        """
        try:
            for data in insert_data:
                key = ','.join(data.keys())
                values = map(self._deal_values, data.values())
                insert_data = ', '.join(values)
                sql = "insert into {table}({key}) values ({val})".format(table=table, key=key, val=insert_data)
                effect_row = self.cursor.execute(sql)
                self.cnn.commit()
                return effect_row
        except Exception as e:
            raise e
        finally:
            # self.close_db()
            pass

    def delete(self, table, condition):
        """
        :param table:
        :param condition type{"":""}:
        :return effect_row 1 影响的行数:
        """
        condition_list = self._deal_values(condition)
        condition_data = ' and '.join(condition_list)
        sql = "delete from {table} where {condition}".format(table=table, condition=condition_data)
        effect_row = self.cursor.execute(sql)
        self.cnn.commit()
        # self.close_db()
        return effect_row

    def update(self, table, data, condition=None):
        """
        :param table:
        :param data type 字典 {}:
        :param condition tpye 字典 {}:
        :return:
        """
        update_list = self._deal_values(data)
        update_data = ",".join(update_list)
        if condition is not None:
            condition_list = self._deal_values(condition)
            condition_data = ' and '.join(condition_list)
            sql = "update {table} set {values} where {condition}".format(table=table, values=update_data,
                                                                         condition=condition_data)
        else:
            sql = "update {table} set {values}".format(table=table, values=update_data)
        effect_row = self.cursor.execute(sql)
        self.cnn.commit()
        # self.close_db()
        return effect_row

    def select_id(self, table, id):
        """
        :param table:
        :param show_list type 列表 （字段）:
        :param condition type 字典:
        :param get_one bool:
        :return:
        """
        sql = "select * from {table} where id = {id}".format(table=table, id=id)
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        # self.close_db()
        if result:
            return result
        else:
            return None

    def select_some(self, table, filed, value):
        """
        :param table:
        :param show_list type 列表 （字段）:
        :param condition type 字典:
        :return:
        """
        sql = "select * from {table} where {filed} = '{value}'".format(table=table, filed=filed, value=value)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        # self.close_db()
        if result:
            return result
        else:
            return None

    def select_all(self, table):
        """
        :param table:
        :param show_list type 列表 （字段）:
        :param condition type 字典:
        :return:
        """
        sql = "select * from {table}".format(table=table)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        # self.close_db()
        if result:
            return result
        else:
            return None

    def query_sql(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if result:
            return result
        else:
            return None

    def _deal_values(self, value):
        """
        self._deal_values(value) -> str or list
            处理传进来的参数
        """
        # 如果是字符串则加上''
        if isinstance(value, str):
            value = ("'{value}'".format(value=value))
        # 如果是字典则变成key=value形式
        elif isinstance(value, dict):
            result = []
            for key, value in value.items():
                value = self._deal_values(value)
                res = "{key}={value}".format(key=key, value=value)
                result.append(res)
            return result
        else:
            value = (str(value))
        return value

    # 执行sql脚本文件
    def run_sql_file(self, sql_file):
        """
        执行操作
        """
        try:
            with open(sql_file, encoding='utf-8', mode='r') as f:
                # 读取整个sql文件，以分号切割。[:-1]删除最后一个元素，也就是空字符串
                sql_list = f.read().split(';')[:-1]
                for x in sql_list:
                    # 判断包含空行的
                    if '\n' in x:
                        # 替换空行为1个空格
                        x = x.replace('\n', '')
                    # 判断多个空格时
                    if '    ' in x:
                        # 替换为空
                        x = x.replace('    ', '')
                    # sql语句添加分号结尾
                    sql_item = x + ';'
                    # print(sql_item)
                    run_sql_result = self.fetch_all(sql_item)
                    print("执行成功sql: %s" % sql_item)
                    print(run_sql_result)
        except Exception:
            self.cnn.rollback()
            print('执行失败sql: %s' % sql_item)
            return False
        return True


# if __name__ == '__main__':
#     host = "127.0.0.1"
#     user = "root"
#     port = 3306
#     passwd = "123456"
#     db = "pytest_auto_uitest_apitest"
#     charset = "utf8"
#     mydb = toolMyDB(host, user, port, passwd, db, charset)
#     rs = mydb.query_sql("select * from ui")
#     print(rs)
