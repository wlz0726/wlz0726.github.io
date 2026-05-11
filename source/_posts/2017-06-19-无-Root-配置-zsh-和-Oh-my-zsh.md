---
title: 无 Root 配置 zsh 和 Oh-my-zsh
date: 2017-06-19
categories:
- tools
tags:
- zsh
- oh-my-zsh
- Linux
- Shell
- 服务器
---

# 无 Root 配置 zsh 和 Oh-my-zsh

**原文日期**: 2017-06-19
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## 无 Root 权限安装 zsh

### 1. 下载源码

```bash
wget https://sourceforge.net/projects/zsh/files/zsh/5.8/zsh-5.8.tar.xz
tar xf zsh-5.8.tar.xz
cd zsh-5.8
```

### 2. 编译安装到用户目录

```bash
./configure --prefix=$HOME/.local
make
make install
```

### 3. 添加到 PATH

```bash
echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

## 安装 Oh-my-zsh

```bash
# 设置 zsh 路径
export ZSH=$HOME/.oh-my-zsh

# 克隆 Oh-my-zsh
git clone https://github.com/ohmyzsh/ohmyzsh.git $ZSH

# 复制模板配置
cp $ZSH/templates/zshrc.zsh-template $HOME/.zshrc
```

### 编辑 ~/.zshrc

```bash
# 设置主题
ZSH_THEME="robbyrussell"

# 设置插件
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)

# 设置 zsh 路径
export ZSH=$HOME/.oh-my-zsh

# 启动 Oh-my-zsh
source $ZSH/oh-my-zsh.sh
```

## 安装插件

### zsh-autosuggestions

```bash
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

### zsh-syntax-highlighting

```bash
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

## 设置默认 shell

如果有 sudo 权限：

```bash
# 查看可用 shell
cat /etc/shells

# 设置默认 shell
chsh -s $HOME/.local/bin/zsh
```

如果没有 sudo 权限，每次手动启动：

```bash
$HOME/.local/bin/zsh
```

## 推荐主题

- **robbyrussell**: 默认主题，简洁

- **agnoster**: 美观，需要 Powerline 字体

- **powerlevel10k**: 功能强大，高度可定制

---

*此文档为 GitHub 博客自动归档*
