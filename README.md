# group commonality analyzer  群组共同性分析器


分析你与所有群组成员的共同群，主要是指在多个QQ群中相同的群友或交集的部分。

# Before
本项目使用了NapCatQQ作为数据APi源,请你按照 https://napneko.com/guide/start-install，配置好NapCatQQ并启动HTTP服务使用默认3000端口即可.

确保您安装了rye. https://rye.astral.sh/guide/installation/ 本项目的环境使用rye进行管理

# start up

clone 此项目

在项目目录下执行`rye sync` , rye会根据pyproject.toml文件下载依赖

执行`rye run python get_data.py` 来获取您的原始数据

执行`rye run python wash_data.py` 对数据进行过滤

执行 `rye run python analyzer.py` 分析数据 其生成的merged_user_group_with_count.csv展示了所有群的群友与您共同的群以及数量

执行` rye run python merge_count.py `将merged_user_group_with_count.csv中的数据进行合并，您可以用来分析拥有共同群组的群友的数量分布(去除了group_count==1的数据)
