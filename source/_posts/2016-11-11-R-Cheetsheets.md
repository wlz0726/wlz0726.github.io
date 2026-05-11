---
title: R Cheetsheets
date: 2016-11-11
categories:
  - tools
---

# R Cheetsheets

**原文日期**: 2016-11-11
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## R 语言快速参考

### 安装包

```
# 安装 CRAN 包
install.packages("ggplot2")

# 安装 GitHub 包
install.packages("devtools")
devtools::install_github("author/package")

# 加载包
library(ggplot2)
```

### 数据导入

```
# CSV
df <- read.csv("file.csv", stringsAsFactors = FALSE)

# Excel
library(readxl)
df <- read_excel("file.xlsx")

# RDS
df <- readRDS("file.rds")

# 保存
write.csv(df, "output.csv", row.names = FALSE)
saveRDS(df, "output.rds")
```

### 数据探索

```
str(df)          # 结构
summary(df)      # 摘要
head(df, 10)     # 前 10 行
dim(df)          # 维度
names(df)        # 列名
table(df$col)    # 频数表
```

### 数据选择

```
# dplyr 方式
library(dplyr)

# 选择列
df %>% select(col1, col2)

# 过滤行
df %>% filter(col1 > 5)

# 排序
df %>% arrange(desc(col1))

# 添加列
df %>% mutate(new_col = col1 * 2)
```

### 数据聚合

```
# 分组汇总
df %>%
  group_by(category) %>%
  summarise(
    mean_val = mean(value),
    sd_val = sd(value),
    n = n()
  )
```

### 常用绘图

```
# 散点图
ggplot(df, aes(x, y)) + geom_point()

# 柱状图
ggplot(df, aes(x)) + geom_bar()

# 箱线图
ggplot(df, aes(group, value)) + geom_boxplot()

# 折线图
ggplot(df, aes(x, y)) + geom_line()
```

---

*此文档为 GitHub 博客自动归档*
