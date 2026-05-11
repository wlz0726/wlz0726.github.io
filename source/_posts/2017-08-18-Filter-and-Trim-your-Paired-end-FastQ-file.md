---
title: Filter and Trim your Paired-end FastQ file
date: 2017-08-18
categories:
- bioinformatics
tags:
- FASTQ
- 质量控制
- trimming
- NGS
---

# Filter and Trim your Paired-end FastQ file

**原文日期**: 2017-08-18
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## FastQ 文件过滤和修剪

### 使用 Trimmomatic

```bash
java -jar trimmomatic.jar PE \
  input_R1.fastq input_R2.fastq \
  output_R1_paired.fastq output_R1_unpaired.fastq \
  output_R2_paired.fastq output_R2_unpaired.fastq \
  ILLUMINACLIP:adapters.fa:2:30:10 \
  LEADING:3 \
  TRAILING:3 \
  SLIDINGWINDOW:4:15 \
  MINLEN:36
```

### 参数说明

### 使用 fastp（推荐）

```bash
fastp -i input_R1.fastq -I input_R2.fastq \
      -o output_R1.fastq -O output_R2.fastq \
      -h report.html \
      -j report.json \
      -q 20 \
      -l 50 \
      -w 4
```

### 质量评估

```bash
# FastQC
fastqc input.fastq

# MultiQC 汇总
multiqc ./
```

---

*此文档为 GitHub 博客自动归档*
