#!/usr/bin/env bash
echo "# pizza-shop-async" >> README.md
git init
git add README.md
git commit -m "init commit"
git branch -M main
git git remote add origin https://github.com/GoncharenkoDI/pizza-shop-async.git
git push -u origin main