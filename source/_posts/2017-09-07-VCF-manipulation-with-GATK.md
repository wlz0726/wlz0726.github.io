---
title: VCF manipulation with GATK
date: 2017-09-07
categories:
- bioinformatics
tags:
- GATK
- VCF
- 变异检测
- SNP
---

# VCF manipulation with GATK

**原文日期**: 2017-09-07
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## GATK VCF 操作

### 选择变异

```bash
# 选择 SNP
gatk SelectVariants \
  -V input.vcf \
  --select-type-to-include SNP \
  -O snps.vcf

# 选择 INDEL
gatk SelectVariants \
  -V input.vcf \
  --select-type-to-include INDEL \
  -O indels.vcf

# 选择特定样本
gatk SelectVariants \
  -V input.vcf \
  -sn sample1 \
  -O sample1.vcf
```

### 合并 VCF

```bash
gatk MergeVcfs \
  -I input1.vcf \
  -I input2.vcf \
  -O merged.vcf
```

### 拆分 VCF

```bash
# 按染色体拆分
for chr in {1..22} X Y; do
  gatk SelectVariants \
    -V input.vcf \
    -R reference.fasta \
    -L $chr \
    -O chr${chr}.vcf
done
```

---

*此文档为 GitHub 博客自动归档*
