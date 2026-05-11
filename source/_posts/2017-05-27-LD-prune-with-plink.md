---
title: LD-prune with plink
date: 2017-05-27
categories:
- bioinformatics
tags:
- PLINK
- LD pruning
- 连锁不平衡
- GWAS
---

# LD-prune with plink

**原文日期**: 2017-05-27
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## PLINK 连锁不平衡修剪

### 目的

去除高度相关的 SNP，用于：

- PCA 分析

- 群体结构分析

- 减少多重检验

- 提高计算效率

### 命令

```bash
# LD 修剪
plink --bfile input \
      --indep-pairwise 50 5 0.2 \
      --out pruned

# 提取修剪后的 SNP
plink --bfile input \
      --extract pruned.prune.in \
      --make-bed \
      --out input_pruned
```

### 参数说明

`--indep-pairwise <窗口大小> <步长> <r²阈值>`

### 参数调整

#### 更严格（保留更少 SNP）

```bash
plink --bfile input --indep-pairwise 50 5 0.1 --out pruned_strict
```

#### 更宽松（保留更多 SNP）

```bash
plink --bfile input --indep-pairwise 50 5 0.5 --out pruned_loose
```

### 结果文件

### 验证

```bash
# 检查保留的 SNP 数量
wc -l pruned.prune.in

# 检查 LD 结构
plink --bfile input_pruned --r2 --ld-window 99999 --ld-window-kb 1000 --ld-window-r2 0
```

### 应用场景

1. **PCA 分析**: 去除 LD 影响

2. **群体结构**: ADMIXTURE 分析前处理

3. **GWAS**: 减少多重检验负担

4. **系统发育**: 构建无偏树

---

*此文档为 GitHub 博客自动归档*
