#!/usr/bin/env python3
import os
import re
from datetime import datetime

posts_dir = '/Users/wlz/.openclaw/workspace/wlz0726.github.io/source/_posts'
deploy_dir = '/Users/wlz/.openclaw/workspace/wlz0726.github.io/.deploy_git'

def parse_frontmatter(content):
    match = re.match(r'---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not match:
        return {}, content
    meta = {}
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            meta[key.strip()] = val.strip()
    return meta, match.group(2)

def md_to_html(md):
    html = md
    html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    html = re.sub(r'^- (.*?)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'^```(\w*)\n(.*?)\n```$', r'<pre><code>\2</code></pre>', html, flags=re.DOTALL|re.MULTILINE)
    html = html.replace('\n\n', '</p><p>')
    return f'<p>{html}</p>'

for filename in sorted(os.listdir(posts_dir)):
    if not filename.endswith('.md'):
        continue
    
    filepath = os.path.join(posts_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    meta, body = parse_frontmatter(content)
    title = meta.get('title', 'Untitled')
    date = meta.get('date', '').split()[0]
    tags = meta.get('tags', [])
    
    if date:
        date_parts = date.split('-')
        year, month, day = date_parts[0], date_parts[1], date_parts[2]
    else:
        year, month, day = '2026', '01', '01'
    
    html_content = md_to_html(body)
    
    html_template = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width">
  <title>{title}</title>
  <link rel="stylesheet" href="/css/main.css">
</head>
<body>
  <header><h1>{title}</h1><p>发表于 {date}</p></header>
  <article>{html_content}</article>
  <footer><a href="/">返回首页</a></footer>
</body>
</html>'''
    
    output_dir = os.path.join(deploy_dir, year, month, day, filename.replace('.md', ''))
    os.makedirs(output_dir, exist_ok=True)
    
    with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    print(f'✅ Generated: {year}/{month}/{day}/{filename.replace(".md", "")}/index.html')

print('\n✅ All posts generated!')
