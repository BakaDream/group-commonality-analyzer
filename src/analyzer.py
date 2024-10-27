import pandas as pd
import os

data_folder = os.path.join("data", "group")


# 获取一个index为群号 value为群名的dataframe()
def get_groups_name():
    df = pd.read_csv("qq_group_list.csv")
    df = df[["group_id", "group_name"]]
    df.set_index("group_id", inplace=True)
    df.to_csv("1.csv")


if __name__ == "__main__":
    # 创建一个空的DataFrame来存储结果
    all_data = pd.DataFrame()

    # 遍历文件夹中的所有CSV文件
    for file in os.listdir(data_folder):
        if file.endswith(".csv"):
            file_path = os.path.join(data_folder, file)
            # 读取CSV文件
            df = pd.read_csv(file_path)
            # 提取所需的列
            df_filtered = df[["user_id", "group_id"]]
            # 将提取的数据添加到总的DataFrame中
            all_data = pd.concat([all_data, df_filtered], ignore_index=True)

    # 使用user_id进行合并，并将重复的group_id存储为列表
    merged_data = (
        all_data.groupby("user_id")["group_id"].agg(lambda x: list(x)).reset_index()
    )

    # 添加一列，统计每个user_id对应的group_id数量
    merged_data["group_count"] = merged_data["group_id"].apply(len)

    # 显示合并后的数据
    print(merged_data)

    # 可选择保存为新的CSV文件
    merged_data.to_csv("merged_user_group_with_count.csv", index=False)
