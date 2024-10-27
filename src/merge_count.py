"""
用来显示有共同群组的群友的数量分布
"""

import pandas as pd


if __name__ == "__main__":
    # 读取数据
    df = pd.read_csv("merged_user_group_with_count.csv")
    # 过滤掉 group_count 为 1 的数据
    df = df.query("group_count > 1")

    # 统计每个 group_count 的数量
    count_distribution = df["group_count"].value_counts().reset_index()
    count_distribution.columns = ["group_count", "count"]

    # 按 group_count 升序排列
    count_distribution = count_distribution.sort_values(by="group_count").reset_index(
        drop=True
    )
    count_distribution.set_index("group_count",inplace=True)
    # 显示结果
    print(count_distribution)
