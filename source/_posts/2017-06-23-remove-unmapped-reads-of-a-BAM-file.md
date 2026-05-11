---
title: remove unmapped reads of a BAM file
date: 2017-06-23
categories:
  - bioinformatics
---

# remove unmapped reads of a BAM file

**原文日期**: 2017-06-23
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## 移除 BAM 文件中未比对的 reads

### 使用 samtools

#### 保留比对的 reads

```bash
samtools view -bF 4 input.bam > output.mapped.bam
```

#### 保留未比对的 reads

```bash
samtools view -bf 4 input.bam > output.unmapped.bam
```

### FLAG 说明

### 双端数据

```bash
# 保留正确配对的 reads
samtools view -bF 260 input.bam > output.paired.bam

# 保留至少一端比对的 reads
samtools view -bF 12 input.bam > output.at_least_one.bam
```

### 排序和索引

```bash
# 排序
samtools sort output.mapped.bam -o output.mapped.sorted.bam

# 索引
samtools index output.mapped.sorted.bam
```

### 统计

```bash
# 比对统计
samtools flagstat input.bam
```

---

*此文档为 GitHub 博客自动归档*
