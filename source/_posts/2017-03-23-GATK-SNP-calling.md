---
title: GATK SNP calling
date: 2017-03-23
categories:
  - tools
---

# GATK SNP calling

**原文日期**: 2017-03-23
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## GATK SNP 检测流程

### 环境准备

```bash
# 下载 GATK
wget https://github.com/broadinstitute/gatk/releases/download/4.2.0.0/gatk-4.2.0.0.zip
unzip gatk-4.2.0.0.zip
cd gatk-4.2.0.0
```

### 预处理流程

#### 1. 比对

```bash
bwa mem -t 8 -M reference.fasta reads_R1.fastq reads_R2.fastq | \
  samtools sort -o sorted.bam
```

#### 2. 标记重复

```bash
gatk MarkDuplicates \
  -I sorted.bam \
  -O dedup.bam \
  -M metrics.txt
```

#### 3. 基础质量重校准 (BQSR)

```bash
# 第一步：构建重校准表
gatk BaseRecalibrator \
  -R reference.fasta \
  -I dedup.bam \
  --known-sites dbSNP.vcf \
  --known-sites Mills_and_1000G_gold_standard.vcf \
  -O recal.table

# 第二步：应用重校准
gatk ApplyBQSR \
  -R reference.fasta \
  -I dedup.bam \
  --bqsr-recal-file recal.table \
  -O recal.bam
```

### 变异检测

#### HaplotypeCaller

```bash
# 单样本
gatk HaplotypeCaller \
  -R reference.fasta \
  -I recal.bam \
  -O output.vcf \
  --dont-use-soft-clipped-bases \
  --standard-min-confidence-threshold-for-calling 30

# 多样本（GVCF 模式）
gatk HaplotypeCaller \
  -R reference.fasta \
  -I sample1.bam \
  -O sample1.g.vcf \
  -ERC GVCF
```

#### 联合基因分型

```bash
# 合并 GVCF
gatk CombineGVCFs \
  -R reference.fasta \
  --variant sample1.g.vcf \
  --variant sample2.g.vcf \
  -O combined.g.vcf

# 联合基因分型
gatk GenotypeGVCFs \
  -R reference.fasta \
  -V combined.g.vcf \
  -O output.vcf
```

### 变异过滤

```bash
gatk VariantFiltration \
  -R reference.fasta \
  -V output.vcf \
  --filter-expression "QD < 2.0" \
  --filter-name "QD2" \
  --filter-expression "FS > 60.0" \
  --filter-name "FS60" \
  --filter-expression "MQ < 40.0" \
  --filter-name "MQ40" \
  -O filtered.vcf
```

### 常用过滤阈值

---

*此文档为 GitHub 博客自动归档*
