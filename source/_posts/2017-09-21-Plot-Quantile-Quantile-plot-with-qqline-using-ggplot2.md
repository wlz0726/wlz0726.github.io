---
title: Plot Quantile-Quantile plot with qqline using ggplot2
date: 2017-09-21
categories:
  - bioinformatics
---

# Plot Quantile-Quantile plot with qqline using ggplot2

**原文日期**: 2017-09-21
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## QQ 图绘制

### 使用 ggplot2

```
library(ggplot2)

# 示例数据
data <- rnorm(100)

# 创建 QQ 图
ggplot(data.frame(sample = sort(data), 
                  theoretical = qnorm(ppoints(100))),
       aes(x = theoretical, y = sample)) +
  geom_point() +
  geom_abline(slope = 1, intercept = 0, color = "red") +
  labs(title = "Q-Q Plot",
       x = "Theoretical Quantiles",
       y = "Sample Quantiles") +
  theme_minimal()
```

### 使用基础 R

```
# 生成数据
data <- rnorm(100)

# QQ 图
qqnorm(data)
qqline(data, col = "red")
```

### GWAS 中的 QQ 图

```
# 读取 p 值
gwas <- read.table("gwas.assoc", header = TRUE)

# 计算 -log10(p)
gwas$neg_log_p <- -log10(gwas$P)

# 期望值
gwas$expected <- -log10(ppoints(nrow(gwas)))

# 绘图
ggplot(gwas, aes(x = expected, y = neg_log_p)) +
  geom_point(alpha = 0.5) +
  geom_abline(slope = 1, intercept = 0, color = "red") +
  theme_minimal()
```

---

*此文档为 GitHub 博客自动归档*
