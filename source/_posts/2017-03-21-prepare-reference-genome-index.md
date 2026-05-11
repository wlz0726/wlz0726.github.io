---
title: prepare reference genome index
date: 2017-03-21
categories:
  - tools
---

# prepare reference genome index

**原文日期**: 2017-03-21
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## 参考基因组索引构建

### BWA 索引

```bash
# 下载参考基因组
wget ftp://ftp.ensembl.org/pub/release-84/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz

# 解压
gunzip Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz

# 创建索引
bwa index -a bwtsw Homo_sapiens.GRCh38.dna.primary_assembly.fa
```

**输出文件**:

- `.amb` - 模糊位点信息

- `.ann` - 序列注释

- `.bwt` - Burrows-Wheeler 转换

- `.pac` - 压缩序列

- `.sa` - 后缀数组

### Bowtie2 索引

```bash
bowtie2-build reference.fasta index_prefix
```

### HISAT2 索引

```bash
hisat2-build reference.fasta index_prefix
```

### STAR 索引

```bash
STAR --runMode genomeGenerate \
     --genomeDir /path/to/index \
     --genomeFastaFiles reference.fasta \
     --sjdbGTFfile annotation.gtf \
     --sjdbOverhang 100 \
     --runThreadN 8
```

**参数说明**:

- `--sjdbOverhang`: 读长 -1（如 101bp 读长设为 100）

- `--runThreadN`: 线程数

### 注意事项

1. **磁盘空间**: 人类基因组索引约需 30-50GB

2. **内存**: STAR 索引需要约 30GB 内存

3. **时间**: 完整索引约需 1-4 小时

4. **版本**: 记录参考基因组版本（GRCh37/GRCh38）

### 验证索引

```bash
# BWA
bwa mem -t 4 reference.fasta reads.fastq | samtools view -c

# 应该输出比对上的 reads 数
```

---

*此文档为 GitHub 博客自动归档*
