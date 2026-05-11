---
title: Data management of plink format
date: 2017-06-28
categories:
- bioinformatics
tags:
- PLINK
- 数据管理
- GWAS
- 基因型
---

# Data management of plink format

**原文日期**: 2017-06-28
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## PLINK 数据管理

### 参考文档

PLINK 1.9 manual: https://www.cog-genomics.org/plink/1.9/

### 提取特定位点

```bash
plink --bfile input \
      --extract positions.in \
      --make-bed \
      --out output
```

### 合并文件

#### 方法 1: 转 VCF 合并

```bash
# 转 VCF
plink --bfile file1 --recode vcf --out file1
plink --bfile file2 --recode vcf --out file2

# 合并 VCF
bcftools merge file1.vcf file2.vcf -o merged.vcf

# 转回 PLINK
plink --vcf merged.vcf --make-bed --out merged
```

#### 方法 2: PLINK 直接合并

```bash
# 生成合并列表
echo "file1.bed file1.bim file1.fam" > merge.txt
echo "file2.bed file2.bim file2.fam" >> merge.txt

# 合并
plink --bfile file1 --merge-list merge.txt --make-bed --out merged
```

### 格式转换

```bash
# PLINK → VCF
plink --bfile input --recode vcf --out output

# VCF → PLINK
plink --vcf input.vcf --make-bed --out output

# PLINK → EIGENSTRAT
plink --bfile input --recode eigenstrat --out output
```

### 质量控制

```bash
# MAF 过滤
plink --bfile input --maf 0.05 --make-bed --out output

# 缺失率过滤
plink --bfile input --geno 0.1 --make-bed --out output

# HWE 过滤
plink --bfile input --hwe 1e-6 --make-bed --out output
```

---

*此文档为 GitHub 博客自动归档*
