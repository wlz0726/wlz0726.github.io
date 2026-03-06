#!/usr/bin/env python3
import os
from datetime import datetime

deploy_dir = '/Users/wlz/.openclaw/workspace/wlz0726.github.io'

posts = [
    ('2026-03-06', '龙虾日记 #5 - PDF 处理与 PPT 自动化', '2026/03/06/2026-03-06-龙虾日记 -5/'),
    ('2026-03-05', '龙虾日记 #4 - 多 Agent 协作', '2026/03/05/2026-03-05-龙虾日记 -4/'),
    ('2026-03-04', '龙虾日记 #3 - 安全规则确立', '2026/03/04/2026-03-04-龙虾日记 -3/'),
    ('2026-03-03', '龙虾日记 #2 - 语音功能探索', '2026/03/03/2026-03-03-龙虾日记 -2/'),
    ('2026-03-02', '龙虾日记 #1 - OpenClaw 初体验', '2026/03/02/2026-03-02-龙虾日记 -1/'),
]

post_items = ''
for date, title, link in posts:
    post_items += f'''
  <article class="post" itemscope itemtype="http://schema.org/Article">
    <header class="post-header">
      <h2 class="post-title" itemprop="name headline">
        <a href="/{link}" class="post-title-link" itemprop="url">{title}</a>
      </h2>
      <div class="post-meta">
        <span class="post-date">
          <time datetime="{date}" itemprop="datePublished">{date}</time>
        </span>
      </div>
    </header>
  </article>
'''

index_html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width">
  <title>lizhong's notes</title>
  <link rel="stylesheet" href="/css/main.css">
</head>
<body>
  <div class="main-content">
    <header>
      <h1>lizhong's notes</h1>
    </header>
    <div class="post-list">
{post_items}
    </div>
  </div>
</body>
</html>
'''

with open(os.path.join(deploy_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(index_html)

print('✅ index.html updated!')
