"""
用来获取qq群列表，
以及qq群成员的原始数据
有时候可能因为速率限制get_group_member_list可能会失效
"""

from qq_api import QQApi
import pandas as pd
import time
from tqdm import tqdm
import os
from static import DATA_PATH, BASE_URL,GROUP_PATH


"""
程序开始前准备过程，用来创建数据目录
"""


def start_up():
    if not os.path.exists(DATA_PATH):
        os.mkdir(DATA_PATH)
    if not os.path.exists(GROUP_PATH):
        os.mkdir(GROUP_PATH)


if __name__ == "__main__":
    print("程序开始执行")
    start_up()
    qq_api = QQApi(base_url=BASE_URL)
    no_cache = True
    # 获取并保存群列表数据
    group_list_data = qq_api.get_group_list(no_cache=no_cache)
    group_list_df = pd.DataFrame(group_list_data)
    group_list_df.set_index("group_id", inplace=True)
    group_list_df.to_csv(os.path.join(DATA_PATH, "qq_group_list.csv"))
    print(f"获取群列表完成! 共获取到{group_list_df.shape[0]}个群。")
    print("接下来获取每个群的群成员信息")

    pbar = tqdm(group_list_df.index)
    # 获取并保存群成员数据
    for group_id in pbar:
        pbar.set_description(f"正在获取群{group_id}的成员列表")
        group_member_data = qq_api.get_group_member_list(
            group_id=group_id, no_cache=no_cache
        )
        group_member_df = pd.DataFrame(group_member_data)
        group_member_df.set_index("user_id", inplace=True)
        group_member_df.to_csv(os.path.join(GROUP_PATH, f"{group_id}.csv"))
        time.sleep(1)
    print("数据获取完毕")
