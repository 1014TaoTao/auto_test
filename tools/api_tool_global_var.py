# coding:utf-8
# ==============================
#         EXCEL列封装
# ==============================
class global_var:
    def __init__(self):
        self.test_id = 0
        self.test_module = 1
        self.test_function = 2
        self.test_run = 3
        self.base_url = 4
        self.test_url = 5
        self.test_data = 6
        self.test_method = 7
        self.type_data = 8
        self.test_header = 9
        self.test_token = 10
        self.upload_path = 11
        self.test_case_depend = 12
        self.test_filed_depend = 13
        self.test_status_code = 14
        self.test_expect_msg = 15
        self.test_expect_data = 16
        self.test_result = 17
        self.test_response = 18
        self.test_check_sql = 19


    def get_id(self):
        """
        :return:
        """
        return self.test_id

    def get_module(self):
        """
        :return:
        """
        return self.test_module

    def get_fuction(self):
        """
        :return:
        """
        return self.test_function

    def get_url(self):
        """
        :return:
        """
        return self.test_url

    def get_run(self):
        """
        :return:
        """
        return self.test_run

    def get_run_way(self):
        """
        :return:
        """
        return self.test_method

    def get_header(self):
        """
        :return:
        """
        return self.test_header

    def get_filed_depend(self):
        """
        :return:
        """
        return self.test_filed_depend

    def get_data(self):
        """
        :return:
        """
        return self.test_data

    def get_expect_msg(self):
        """
        :return:
        """
        return self.test_expect_msg

    def get_expect_data(self):
        """
        :return:
        """
        return self.test_expect_data

    def get_result(self):
        """
        :return:
        """
        return self.test_result

    def get_response(self):
        """
        :return:
        """
        return self.test_response

    def get_status_code(self):
        """
        :return:
        """
        return self.test_status_code

    def get_check_sql(self):
        """
        :return:
        """
        return self.test_check_sql

    def get_token(self):
        """
        :return:
        """
        return self.test_token

    def get_case_depend(self):
        """
        :return:
        """
        return self.test_case_depend

    def get_base_url(self):
        """
        :return:
        """
        return self.base_url

    def get_type_data(self):
        """
        :return:
        """
        return self.type_data

    def get_upload_path(self):
        """
        :return:
        """
        return self.upload_path
# if __name__ == '__main__':
#     print(global_var.get_data)
