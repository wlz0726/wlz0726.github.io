---
title: libgd GD problem installing Circos
date: 2016-11-15
categories:
  - tools
---

# libgd and GD problem (installing Circos)

**原文日期**: 2016-11-15
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## Circos 安装问题 - libgd

### 问题描述

安装 Circos 时遇到的 libgd 依赖问题：

```python
GD library not found
```

### 解决方案

#### macOS

```bash
# 使用 Homebrew 安装 gd
brew install gd

# 安装 Perl GD 模块
cpan GD
# 或
cpanm GD
```

#### Ubuntu/Debian

```bash
# 安装 gd 库
sudo apt-get install libgd-dev

# 安装 Perl GD 模块
sudo cpan GD
```

#### CentOS/RHEL

```bash
sudo yum install gd-devel
cpan GD
```

### 验证安装

```
#!/usr/bin/perl
use GD;

print "GD module installed successfully\n";

# 创建简单图像
my $img = GD::Image->new(100, 100);
my $white = $img->colorAllocate(255, 255, 255);
my $black = $img->colorAllocate(0, 0, 0);

$img->rectangle(0, 0, 99, 99, $black);
```

### Circos 完整安装

```bash
# 克隆 Circos
git clone https://github.com/krishah/circos.git
cd circos

# 安装依赖
cpan Config::General
cpan Math::VecStat
cpan Math::Bezier
cpan Math::Round
cpan Math::CDF
cpan SVG
cpan Clone
cpan Font::TTF

# 测试
bin/circos --conf etc/test.conf
```

### 常见问题

#### 1. GD 安装失败

```bash
# 确保 gd-config 在 PATH 中
which gd-config

# 如果不在，添加路径
export PATH=/usr/local/bin:$PATH
```

#### 2. 字体问题

```bash
# 安装字体
brew install fontconfig
```

---

*此文档为 GitHub 博客自动归档*
