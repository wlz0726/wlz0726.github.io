---
title: Map with BWA and do Indel realignment with GATK
date: 2017-08-18
categories:
- bioinformatics
tags:
- BWA
- GATK
- Indel realignment
- NGS
- 变异检测
---

# Map with BWA and do Indel realignment with GATK

**原文日期**: 2017-08-18
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## BWA 比对 + GATK Indel 重比对

### 完整流程

#### 1. BWA 比对

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

#### 3. Indel 重比对（GATK3）

```bash
# 创建目标区间
gatk RealignerTargetCreator \
  -R reference.fasta \
  -I dedup.bam \
  -known dbSNP.vcf \
  -o intervals.list

# 执行重比对
gatk IndelRealigner \
  -R reference.fasta \
  -I dedup.bam \
  -targetIntervals intervals.list \
  -known dbSNP.vcf \
  -O realigned.bam
```

### 注意

**GATK4 已移除 IndelRealigner**，因为 HaplotypeCaller 内置了局部重比对功能。

---

*此文档为 GitHub 博客自动归档*
