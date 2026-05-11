---
title: Do Phasing with SHAPEIT
date: 2017-06-06
categories:
- bioinformatics
tags:
- SHAPEIT
- phasing
- 基因型推断
- 单倍型
---

# Do Phasing with SHAPEIT

**原文日期**: 2017-06-06
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## SHAPEIT 单倍型定相

### 简介

SHAPEIT 用于将基因型数据转换为单倍型数据（Phasing），确定等位基因的染色体来源。

### 安装

#### 方法 1: 源码编译

```bash
git clone https://github.com/Delaneau/shapeit4.git
cd shapeit4
make
```

#### 方法 2: conda 安装

```bash
conda install -c bioconda shapeit4
```

### 基本用法

```bash
shapeit4 --input input.vcf.gz \
         --map genetic_map.txt \
         --region 1 \
         --output output.bcf \
         --thread 4 \
         --seed 12345
```

### 参数说明

### 遗传图谱文件

从以下来源获取：

- **1000 Genomes**: ftp://ftp.1000genomes.ebi.ac.uk/

- **HapMap**: https://www.hapmap.org/

### 输出

- 定相后的 VCF/BCF 文件

- 单倍型概率信息

- 定相质量评估

### 质量评估

```bash
# 计算 switch error rate
shapeit4 --input output.bcf \
         --check \
         --true-haps reference.vcf.gz
```

### 应用场景

1. **单倍型分析**: Haplotype-based 分析

2. **IBD 检测**: 基于单倍型的 IBD 检测

3. **Imputation**: 提高基因型填补准确性

4. **选择信号**: 检测自然选择信号

---

*此文档为 GitHub 博客自动归档*
