---
title: install emacs
date: 2018-06-12
categories:
  - bioinformatics
---

# install emacs

**原文日期**: 2018-06-12
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## Emacs 安装与配置

### 安装

#### macOS

```bash
brew install emacs
```

#### Ubuntu/Debian

```bash
sudo apt-get install emacs
```

### 基础配置 ~/.emacs.d/init.el

```python
;; 基本设置
(setq inhibit-startup-message t)
(show-paren-mode t)
(column-number-mode t)
(line-number-mode t)

;; 主题
(load-theme 'tango-dark t)

;; 包管理
(require 'package)
(add-to-list 'package-archives
             '("melpa" . "https://melpa.org/packages/") t)
(package-initialize)

;; 自动安装 use-package
(unless (package-installed-p 'use-package)
  (package-install 'use-package))

(require 'use-package)
```

### 推荐包

- **magit**: Git 集成

- **company**: 代码补全

- **flycheck**: 语法检查

- **org-mode**: 笔记/计划

---

*此文档为 GitHub 博客自动归档*
