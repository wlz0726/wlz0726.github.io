#!/usr/bin/env node
const Hexo = require('hexo');
const hexo = new Hexo(process.cwd(), { silent: false });

hexo.init().then(() => {
  return hexo.call('generate', {});
}).then(() => {
  console.log('Build complete!');
  return hexo.exit();
}).catch(err => {
  console.error('Build failed:', err);
  process.exit(1);
});
