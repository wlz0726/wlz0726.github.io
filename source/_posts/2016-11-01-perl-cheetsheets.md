---
title: perl cheetsheets
date: 2016-11-01
categories:
  - tools
---

# perl cheetsheets

**原文日期**: 2016-11-01
**来源**: https://github.com/wlz0726/wlz0726.github.io

---

## Perl 快速参考

### 变量类型

```
my $scalar = "hello";      # 标量
my @array = (1, 2, 3);     # 数组
my %hash = (a => 1);       # 哈希
```

### 控制结构

```
# if
if ($x > 0) {
    print "positive";
} elsif ($x < 0) {
    print "negative";
} else {
    print "zero";
}

# for
for my $i (0..10) {
    print $i;
}

# while
while ($condition) {
    # code
}
```

### 字符串

```
my $str = "hello";
print length($str);        # 5
print substr($str, 0, 2);  # he
$str =~ s/hello/world/;    # 替换
```

### 文件操作

```
open(my $fh, '<', 'file.txt') or die $!;
while (<$fh>) {
    print;
}
close($fh);
```

---

*此文档为 GitHub 博客自动归档*
