---
title: Calculate IBD using beagle and germline
date: 2018-02-26
categories:
  - bioinformatics
---

# Calculate IBD using beagle and germline

**原文日期**: 2018-02-26
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## IBD 检测 - Beagle + GERMLINE

### 简介

IBD (Identity by Descent) 检测用于找出样本间共享的祖先片段。

### 流程

#### 1. 使用 Beagle 定相

```bash
java -jar beagle.jar \
  gt=input.vcf \
  out=phased \
  nthreads=8
```

#### 2. 使用 GERMLINE 检测 IBD

```bash
perl runGermline.pl \
  -input phased.vcf \
  -min_m 1.0 \
  -min_s 0.5 \
  -output ibd_results
```

### 参数说明

### 结果解读

输出包含：

- 样本对

- IBD 片段位置

- 片段长度

- 共享等位基因数量

### 过滤建议

- 最小长度：≥ 1 cM

- 最小 SNP 数：≥ 50

- 错误率：≤ 0.01

---

*此文档为 GitHub 博客自动归档*
