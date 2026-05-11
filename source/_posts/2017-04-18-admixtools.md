---
title: admixtools
date: 2017-04-18
categories:
- bioinformatics
tags:
- ADMIXTOOLS
- 群体遗传学
- admixture
- f3/f4统计
---

# admixtools

**原文日期**: 2017-04-18
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## ADMIXTOOLS 使用指南

### 简介

ADMIXTOOLS 是哈佛大学 Reich 实验室开发的群体遗传学分析工具包，主要用于：

- 群体混合分析 (Admixture)

- f-statistics 计算 (f2, f3, f4)

- 系统发育关系推断

- 基因流检测

### 安装

#### 方法 1: 源码编译

```bash
# 克隆仓库
git clone https://github.com/DReichLab/AdmixTools.git
cd AdmixTools

# 编译
make

# 添加到 PATH
export PATH=$PATH:/path/to/AdmixTools/bin
```

#### 方法 2: conda 安装

```bash
conda install -c bioconda admixtools
```

### 数据格式

ADMIXTOOLS 使用 **EIGENSTRAT 格式**:

1. **.geno** - 基因型数据

2. **.snp** - SNP 信息

3. **.ind** - 个体信息

#### 从 PLINK 转换

```bash
# 使用 convertf
convertf -p parfile
```

**parfile 示例**:

```python
genotypename: input.bed
snpname: input.bim
indivname: input.fam
outputformat: EIGENSTRAT
genotypeoutname: output.geno
snpoutname: output.snp
indivoutname: output.ind
```

### 常用程序

#### 1. qpAdm - 混合比例估计

```bash
qpAdm -p parfile
```

**parfile 示例**:

```python
popleft: Target
popright: Source1 Source2 Source3
outpop: ALL
details: YES
```

#### 2. qpGraph - 构建系统发育图

```bash
qpGraph -p parfile -g graphfile
```

#### 3. f4 统计量

```bash
f4 -p parfile
```

**parfile 示例**:

```python
popfilename: pops.txt
f4mode: YES
```

### 结果解读

#### f3 统计量

- **负值**: 表明目标群体是源群体的混合后代

- **Z 分数**: |Z| > 3 认为显著

#### f4 统计量

- **显著非零**: 表明存在基因流

- **符号**: 指示基因流方向

### 应用场景

1. **古代 DNA 分析**: 检测古代群体与现代群体的关系

2. **人群历史**: 推断人群混合事件

3. **疾病研究**: 控制群体分层

### 注意事项

1. **数据质量**: 确保 SNP 质量和覆盖度

2. **样本选择**: 选择合适的参考群体

3. **多重检验**: 校正 p 值

4. **结果验证**: 使用多种方法交叉验证

---

*此文档为 GitHub 博客自动归档*
