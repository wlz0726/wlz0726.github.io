---
title: build blog with hexo
date: 2016-10-08
categories:
  - tools
---

# build blog with hexo on github

**原文日期**: 2016-10-08
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## Hexo 博客搭建指南

### 安装 Hexo

```bash
npm install -g hexo-cli
hexo init blog
cd blog
npm install
```

### 配置 GitHub Pages

1. 在 GitHub 创建仓库 `wlz0726.github.io`

2. 配置 `_config.yml` 中的 deploy 部分：

```
deploy:
  type: git
  repo: https://github.com/wlz0726/wlz0726.github.io.git
  branch: master
```

3. 部署：

```bash
hexo generate
hexo deploy
```

### 常用命令

### 主题推荐

- **NexT**: 简洁优雅

- **landscape**: 默认主题

- **yilia**: 响应式设计

### 文章格式

```
---
title: 文章标题
date: 2016-10-08 14:01:47
tags: [标签 1, 标签 2]
categories: 分类
---

文章正文...
```

---

*此文档为 GitHub 博客自动归档*
