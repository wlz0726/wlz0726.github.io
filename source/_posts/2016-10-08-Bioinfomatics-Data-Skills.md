---
title: Bioinfomatics Data Skills
date: 2016-10-08
categories:
  - tools
---

# Bioinfomatics Data Skills Cheatsheets

**原文日期**: 2016-10-08
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## 代码规范

代码应该是：

- **可读的** (readable)

- **模块化的** (modular)

- **可复用的** (reusable)

## 测试代码策略

问自己三个问题：

1. 这段代码被其他代码调用多少次？

2. 如果这段代码出错，对最终结果的影响有多大？

3. 如果发生错误，有多容易发现？

## 数据质量

**永远不要假设数据是高质量的！**

应该通过**探索性数据分析 (EDA)** 来证明数据质量。EDA 不复杂也不耗时，但能让你的研究更稳健。

## 最佳实践

### 1. 图表和统计应该是脚本的结果

不要手动处理数据，所有操作都应该是可重复的。

### 2. 使用相对路径

```bash
# ✅ 好
../data/stats/qual.txt

# ❌ 坏
/home/vinceb/projects/zmays-snps/data/stats/qual.txt
```

### 3. 项目文档

在每个项目的主目录中包含：

- 方法和工作流程（命令行）

- 所有数据的来源

- 数据下载时间/版本/方式

- 软件版本

## Shell 技巧

### 花括号扩展

```bash
echo dog-{gone,bowl,bark}
# 输出：dog-gone dog-bowl dog-bark

mkdir -p zmays-snps/{data/seqs,scripts,analysis}

touch seqs/zmays{A,B,C}_R{1,2}.fastq
```

### 通配符

**最佳实践**：尽可能限制通配符范围

```bash
# ✅ 好
zmaysB_R?.fastq

# ❌ 坏
zmaysB*
```

### 前导零和排序

```bash
# ✅ 好：file-0021.txt
# ❌ 坏：file-21.txt
```

## Tmux 快速参考

## 管道使用

```bash
program1 input.txt | tee intermediate-file.txt | program2 > results.txt
```

这里，program1 的输出既写入 intermediate-file.txt，又直接传递给 program2。

---

*此文档为 GitHub 博客自动归档*
