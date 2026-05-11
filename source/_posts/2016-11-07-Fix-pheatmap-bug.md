---
title: Fix pheatmap bug
date: 2016-11-07
categories:
- tools
tags:
- R
- pheatmap
- debug
- 热图
---

# Fix pheatmap bug

**原文日期**: 2016-11-07
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## pheatmap 包问题修复

### 问题描述

pheatmap 在 R 中绘制热图时可能出现的错误：

- 颜色显示异常

- 聚类失败

- 中文乱码

### 解决方案

#### 1. 更新 pheatmap 包

```
# 卸载旧版本
remove.packages("pheatmap")

# 重新安装
install.packages("pheatmap")
```

#### 2. 检查数据格式

```
# 确保是数值矩阵
data_matrix <- as.matrix(data)

# 检查是否有 NA
sum(is.na(data_matrix))

# 处理 NA
data_matrix[is.na(data_matrix)] <- 0
```

#### 3. 解决中文乱码

```
# 设置图形参数
par(family = "STKaiti")  # 或 "SimHei"

# 或使用 showtext 包
library(showtext)
showtext_auto()
```

### 代码示例

```
library(pheatmap)

# 基本热图
pheatmap(data_matrix)

# 带聚类
pheatmap(data_matrix, 
         scale = "row",
         clustering_distance_rows = "correlation",
         clustering_distance_cols = "correlation")

# 自定义颜色
pheatmap(data_matrix,
         color = colorRampPalette(c("blue", "white", "red"))(100))

# 添加注释
pheatmap(data_matrix,
         annotation_row = row_annotation,
         annotation_col = col_annotation)
```

### 常见参数

---

*此文档为 GitHub 博客自动归档*
