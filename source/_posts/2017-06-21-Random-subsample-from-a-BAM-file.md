---
title: Random subsample from a BAM file
date: 2017-06-21
categories:
- tools
tags:
- BAM
- samtools
- NGS
- bash
---

# Random subsample from a BAM file

**原文日期**: 2017-06-21
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## BAM 文件随机抽样

### 使用 samtools

```bash
# 抽样 10%
samtools view -s 0.1 -b input.bam > subsample.bam

# 抽样 50%
samtools view -s 0.5 -b input.bam > subsample.bam

# 指定种子（可重复）
samtools view -s 42.1 -b input.bam > subsample.bam
```

### 参数格式

`-s seed.fraction`

- `seed`: 随机种子（整数）

- `fraction`: 抽样比例（0-1）

### 使用 seqtk

```bash
# 抽样 100 万条 reads
samtools fastq input.bam | \
  seqtk sample -s100 - 1000000 | \
  bwa mem -p reference.fasta - | \
  samtools sort -o subsample.bam
```

### 注意事项

1. **双端数据**: 保持配对关系

2. **种子**: 相同种子产生相同结果

3. **比例**: 根据需求选择

---

*此文档为 GitHub 博客自动归档*
