import requests


class QQApi:
    def __init__(self, base_url):
        self.session = requests.Session()
        self.base_url = base_url

    def _call_api(self, path, method, data=None):
        """
        调用API
        :param method: GET, POST, PUT, DELETE
        :param path: 请求路径
        :param data: 发送的数据
        :return:
        """
        url = self.base_url + path

        if method == "GET":
            response = self.session.get(url, params=data)
        elif method == "POST":
            response = self.session.post(url, json=data)
        elif method == "PUT":
            response = self.session.put(url, json=data)
        elif method == "DELETE":
            response = self.session.delete(url)
        else:
            raise Exception("Method not supported")
        try:
            data = response.json()
            if data["retcode"] != 0:
                raise Exception(data["message"])
        except Exception as e:
            raise Exception(f"网络错误！！！请求失败: {e}")
        return data["data"]

    def get_group_list(self, no_cache=True):
        data = {"no_cache": no_cache}
        resp = self._call_api(path=r"/get_group_list", method="POST", data=data)
        return resp

    def get_group_member_list(self, group_id, no_cache=True):
        data = {"group_id": group_id, "no_cache": no_cache}
        resp = self._call_api(path="/get_group_member_list", method="POST", data=data)
        return resp

    def get_login_info(self):
        resp = self._call_api(path="/get_login_info", method="GET")
        return resp

    def get_robot_uin_range(self):
        resp = self._call_api(path="/get_robot_uin_range", method="GET")
        return resp
