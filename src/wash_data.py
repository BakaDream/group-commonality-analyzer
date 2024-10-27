""" "
用来清洗数据
剔除qq群成员里的自己，机器人
"""

import pandas as pd
from static import DATA_PATH, GROUP_PATH, BASE_URL
import os
from qq_api import QQApi

if __name__ == "__main__":
    qq_api = QQApi(base_url=BASE_URL)
    my_user_id = qq_api.get_login_info()["user_id"]
    uin_ranges = qq_api.get_robot_uin_range()
    # 遍历文件夹中的所有CSV文件
    for file in os.listdir(GROUP_PATH):
        if file.endswith(".csv"):
            file_path = os.path.join(GROUP_PATH, file)
            df = pd.read_csv(file_path)
            # 删除自己那一行
            df = df.query("user_id != @my_user_id")
            # 删除机器人的数据
            # 使用query删除user_id在范围内
            query_conditions = " & ".join(
                f"not ({min_uin} <= user_id <= {max_uin})"
                for min_uin, max_uin in [
                    (int(range_data["minUin"]), int(range_data["maxUin"]))
                    for range_data in uin_ranges
                ]
            )

            df = df.query(query_conditions)
            df.to_csv(file_path, index=False)
