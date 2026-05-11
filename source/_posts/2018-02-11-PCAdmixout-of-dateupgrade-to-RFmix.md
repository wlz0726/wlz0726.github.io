---
title: PCAdmix(out-of-date;upgrade to RFmix)
date: 2018-02-11
categories:
- bioinformatics
tags:
- PCA
- admixture
- 群体结构
- RFmix
---

# PCAdmix (out-of-date; upgrade to RFmix)

**原文日期**: 2018-02-11
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## PCAdmix - 局部祖先推断

### ⚠️ 注意

**PCAdmix 已过时，建议升级到 RFmix**

### RFmix 优势

- 更高的准确性

- 更快的速度

- 更好的文档支持

- 持续维护更新

### RFmix 安装

```bash
# 下载
wget https://drive.google.com/file/d/xxx/view

# 运行
python rfmix.py --reference=ref.vcf --query=query.vcf
```

### 局部祖先推断流程

1. 准备参考面板（已知祖先的样本）

2. 准备查询样本

3. 运行 RFmix

4. 解析输出结果

### 输出解读

- 每个 SNP 位置的祖先来源概率

- 染色体级别的祖先片段

- 混合时间估计

---

*此文档为 GitHub 博客自动归档*
