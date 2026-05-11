---
title: CNVnator Based Analysis
date: 2017-04-27
categories:
- bioinformatics
tags:
- CNV
- CNVnator
- 拷贝数变异
- 结构变异
---

# CNVnator Based Analysis

**原文日期**: 2017-04-27
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## CNVnator 拷贝数变异分析

### 简介

CNVnator 是基于读取深度 (Read Depth) 的 CNV 检测工具，适用于：

- 全基因组 CNV 检测

- 大片段拷贝数变异

- 群体水平 CNV 分析

### 安装

```bash
# 克隆仓库
git clone https://github.com/abyzovlab/CNVnator.git
cd CNVnator/src

# 编译（需要 ROOT 库）
make
```

### 分析流程

#### 1. 生成 ROOT 文件

```bash
cnvnator -root output.root -tree input.bam
```

#### 2. 生成直方图

```bash
cnvnator -root output.root -his 100
```

**bin 大小选择**:

- 100bp - 高分辨率，适合小 CNV

- 500bp - 中等分辨率

- 1kb - 适合大 CNV

#### 3. 分区

```bash
cnvnator -root output.root -part 100
```

#### 4. CNV 调用

```bash
cnvnator -root output.root -call 100
```

### 结果解读

输出格式：

```python
CNV_type chr start end size RD pval q0 annotation
```

#### 过滤建议

```bash
# 保留高质量 CNV
- pval < 0.05
- q0 < 0.5
- size > 1kb
```

### 可视化

```bash
# 生成覆盖率图
cnvnator -root output.root -chrom chr1 -png 100
```

### 注意事项

1. **GC 校正**: CNVnator 会自动进行 GC 校正

2. **bin 大小**: 根据研究目的选择

3. **对照样本**: 建议使用对照提高准确性

4. **验证**: 重要 CNV 建议用其他方法验证

---

*此文档为 GitHub 博客自动归档*
