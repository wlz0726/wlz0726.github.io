# 王理中的个人博客

> 生物信息学、科研笔记、技术分享

**网站地址**: https://wlz0726.github.io

---

## 🚀 快速开始

### 1. 安装依赖

```bash
# 确保已安装 Node.js (v14+)
node --version

# 安装 Hexo CLI
npm install -g hexo-cli

# 安装项目依赖
cd wlz0726.github.io
npm install
```

### 2. 本地预览

```bash
# 启动本地服务器
hexo server

# 访问 http://localhost:4000
```

### 3. 发布新文章

```bash
# 创建新文章（会自动生成 markdown 文件）
hexo new "文章标题"

# 编辑文章
# 文件位置：source/_posts/文章标题.md

# 再次预览
hexo server

# 生成静态文件
hexo generate

# 提交到 GitHub
git add .
git commit -m "添加新文章：文章标题"
git push origin master
```

---

## 📝 文章格式

```markdown
---
title: 文章标题
date: 2026-03-04 23:30:00
tags: [标签 1, 标签 2]
categories: [分类名]
---

文章正文内容...
```

### 常用 Front-matter 字段

| 字段 | 说明 | 示例 |
|------|------|------|
| `title` | 文章标题 | `title: 我的第一篇文章` |
| `date` | 发布日期 | `date: 2026-03-04 23:30:00` |
| `tags` | 标签（数组） | `tags: [生物信息学，科研]` |
| `categories` | 分类（数组） | `categories: [科研笔记]` |
| `updated` | 更新日期 | `updated: 2026-03-05` |

---

## 📁 目录结构

```
wlz0726.github.io/
├── source/           # 源文件目录
│   ├── _posts/      # 文章（markdown 格式）
│   ├── about/       # 页面
│   └── images/      # 图片
├── themes/          # 主题
├── _config.yml      # 站点配置
├── package.json     # 依赖配置
└── public/          # 生成的静态文件（git 推送的）
```

---

## 🎨 主题

使用 **Next 主题** (Muse 风格)

主题文档：https://theme-next.js.org/

### 自定义主题

```bash
# 编辑主题配置
vim themes/next/_config.yml
```

---

## 📦 部署

网站通过 **GitHub Pages** 自动部署：

1. 推送到 `master` 分支
2. GitHub Actions 自动构建
3. 访问 https://wlz0726.github.io

---

## 📊 内容分类

### 现有分类

- **科研笔记** - 群体基因组学、生物信息学研究
- **技术文档** - Shell/R/Python cheatsheets
- **生活记录** - 日常思考、心得体会

### 标签体系

现有 61 个标签，包括：
- 生物信息学
- 群体基因组学
- 数据分析
- 编程技巧
- 科研工具

---

## 🛠️ 维护记录

### 2026-03-04

- ✅ 恢复 Hexo 项目结构
- ✅ 创建发布流程文档
- ✅ 添加新文章《龙虾日记》
- ✅ 配置自动部署

---

## 📞 联系方式

**作者**: 王理中  
**GitHub**: [@wlz0726](https://github.com/wlz0726)  
**Email**: (待添加)

---

**© 2016-2026 王理中 | Powered by Hexo & NexT**
