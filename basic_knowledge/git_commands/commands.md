## 一、常用 Git 命令总结

### 本地仓库操作

```bash
git init                        # 初始化仓库
git status                      # 查看当前状态
git add <file>                  # 添加文件到暂存区
git add .                       # 添加所有更改
git commit -m "message"         # 提交更改
git log                         # 查看提交记录
git diff                        # 查看未提交的更改
```

---

### 远程仓库操作

```bash
git remote add origin <url>     # 添加远程仓库
git remote -v                   # 查看远程仓库地址
git push -u origin master       # 推送主分支并设置 upstream
git pull                        # 拉取并合并远程分支
git clone <url>                 # 克隆远程仓库
```

---

### 分支操作

```bash
git branch                      # 查看本地分支
git branch <name>               # 创建分支
git checkout <name>             # 切换分支
git checkout -b <name>          # 创建并切换分支
git merge <branch>              # 合并其他分支到当前分支
git branch -d <name>            # 删除本地分支
git push origin --delete <name> # 删除远程分支
```

---

### 同步/恢复操作

```bash
git fetch                       # 获取远程分支更新（不自动合并）
git pull origin main            # 拉取远程 main 并合并
git reset --hard HEAD~1         # 回退最近一次提交
git stash                       # 暂存当前修改
git stash pop                   # 恢复暂存修改
```

---

## 二、推送至远程仓库的完整流程（第一次）

1. 初始化仓库（或已有项目）：

```bash
git init
```

2. 添加远程仓库地址：

```bash
git remote add origin https://github.com/username/repo.git
```

3. 添加并提交文件：

```bash
git add .
git commit -m "initial commit"
```

4. 推送到远程主分支：

```bash
git push -u origin master       # 或 main，根据仓库主分支名
```

> `-u` 表示设置 upstream，之后你只需要用 `git push` 即可。

---

## 三、创建分支并推送到远程分支流程

1. 创建并切换分支：

```bash
git checkout -b feature/login
```

2. 编写代码并提交：

```bash
git add .
git commit -m "add login feature"
```

3. 推送到远程分支：

```bash
git push -u origin feature/login
```

4. 日后继续开发，只需：

```bash
git push                         # 推送更新
```

---

## 四、推荐 Git 管理流程（适合个人项目和小团队）

### Git Workflow（通用版）：

```plaintext
main / master 分支：发布用、稳定版本
develop 分支：测试版本，集成所有开发代码
feature/* 分支：开发新功能
hotfix/* 分支：紧急修复 bug
release/* 分支：准备发布
```

### 推荐开发流程（简化版）：

1. 从 `main` 创建 `develop` 分支
2. 每个功能从 `develop` 创建 `feature/xxx`
3. 功能完成后合并到 `develop`
4. 准备发布时创建 `release/x.y`
5. 测试后合并 `release` 到 `main`（生产）和 `develop`（保留记录）
6. 修 bug 时从 `main` 创建 `hotfix/xxx`

> 可使用 GitHub 的 Pull Request 进行代码评审合并。

---

## 五、版本协作建议（团队）

| 情况       | 建议操作                                          |
| -------- | --------------------------------------------- |
| 每次开始工作   | `git pull origin 分支名`                         |
| 修改后      | `git add . && git commit -m ""`               |
| 每天结束前    | `git push`                                    |
| 合并其他人的更新 | `git fetch + git merge` 或 `git pull --rebase` |
| 远程冲突     | 手动解决后重新 `commit + push`                       |

---
