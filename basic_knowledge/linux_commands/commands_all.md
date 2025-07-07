---

## 🖥️ 系统信息和资源查看

| 命令             | 功能                          |
| -------------- | --------------------------- |
| `uname -a`     | 查看系统内核及平台信息                 |
| `hostname`     | 查看主机名                       |
| `top` / `htop` | 实时查看进程和资源占用（`htop` 更友好，需安装） |
| `free -h`      | 查看内存使用情况（加 `-h` 显示人类可读格式）   |
| `df -h`        | 查看磁盘空间使用情况                  |
| `du -sh *`     | 查看当前目录下每个文件夹的大小             |
| `uptime`       | 查看系统运行时间和负载                 |
| `whoami`       | 显示当前用户名                     |

---

## 📂 文件与目录操作

| 命令                                | 功能                  |
| --------------------------------- | ------------------- |
| `ls -al`                          | 列出当前目录下所有文件（包括隐藏文件） |
| `cd`                              | 切换目录                |
| `pwd`                             | 显示当前工作目录            |
| `mkdir dirname`                   | 创建目录                |
| `rm filename`                     | 删除文件                |
| `rm -r dirname`                   | 删除目录及其内容            |
| `cp file1 file2`                  | 复制文件                |
| `mv file1 file2`                  | 移动/重命名文件            |
| `touch filename`                  | 创建空文件               |
| `cat filename`                    | 查看文件内容              |
| `less filename` / `more filename` | 分页查看文件内容            |
| `find /path -name "*.txt"`        | 查找文件                |

---

## 🛠️ 文件权限与所有权

| 命令                      | 功能       |
| ----------------------- | -------- |
| `chmod +x file`         | 赋予执行权限   |
| `chmod 755 file`        | 设置具体权限   |
| `chown user:group file` | 更改文件所有者  |
| `ls -l`                 | 查看权限和所有者 |

---

## 📦 软件包管理（APT）

| 命令                                  | 功能         |
| ----------------------------------- | ---------- |
| `sudo apt update`                   | 更新软件源列表    |
| `sudo apt upgrade`                  | 升级所有已安装的软件 |
| `sudo apt install package`          | 安装软件包      |
| `sudo apt remove package`           | 卸载软件包      |
| `sudo apt autoremove`               | 自动移除无用依赖   |
| `dpkg -l`                           | 查看已安装软件    |
| `which command` / `whereis command` | 查找命令位置     |

---

## 🔒 用户与权限管理

| 命令                       | 功能          |
| ------------------------ | ----------- |
| `adduser username`       | 添加新用户       |
| `sudo passwd username`   | 修改用户密码      |
| `usermod -aG group user` | 将用户添加到组中    |
| `groups`                 | 查看当前用户所属的组  |
| `sudo`                   | 以超级用户权限运行命令 |
| `su`                     | 切换用户        |

---

## 🔧 网络相关

| 命令                             | 功能                 |
| ------------------------------ | ------------------ |
| `ping example.com`             | 测试网络连通性            |
| `ifconfig` / `ip a`            | 查看网络配置（`ip a` 更推荐） |
| `netstat -tulnp` / `ss -tulnp` | 查看端口占用             |
| `curl http://example.com`      | 获取网页内容             |
| `wget URL`                     | 下载文件               |
| `scp file user@host:/path`     | 远程拷贝文件             |
| `ssh user@host`                | 远程登录服务器            |

---

## 🧪 进程与服务管理

| 命令                                     | 功能            |
| -------------------------------------- | ------------- |
| `ps aux`                               | 查看当前所有进程      |
| `kill PID`                             | 杀死指定进程        |
| `kill -9 PID`                          | 强制杀死进程        |
| `systemctl status service`             | 查看服务状态        |
| `systemctl start/stop/restart service` | 控制服务启停        |
| `journalctl -xe`                       | 查看系统日志（含错误信息） |

---

## 📜 文本处理（常用于脚本中）

| 命令                           | 功能        |
| ---------------------------- | --------- |
| `grep "keyword" filename`    | 查找关键词     |
| `sed 's/old/new/g' file`     | 文本替换      |
| `awk '{print $1}' file`      | 提取列       |
| `cut -d ':' -f1 /etc/passwd` | 用分隔符提取字段  |
| `sort`                       | 排序        |
| `uniq`                       | 去重        |
| `wc -l`                      | 行数统计      |
| `head -n 10` / `tail -n 10`  | 显示开头/结尾几行 |

---

## 🗃️ 压缩与解压

| 命令                           | 功能       |
| ---------------------------- | -------- |
| `tar -czvf file.tar.gz dir/` | 打包并压缩    |
| `tar -xzvf file.tar.gz`      | 解压       |
| `zip -r file.zip dir/`       | 创建 zip 包 |
| `unzip file.zip`             | 解压 zip   |

---

## ⛓️ 常用快捷键（命令行）

| 快捷键        | 功能         |
| ---------- | ---------- |
| `Ctrl + C` | 终止当前命令     |
| `Ctrl + Z` | 挂起当前任务     |
| `Ctrl + D` | 退出 shell   |
| `Tab`      | 自动补全命令或文件名 |
| `Ctrl + A` | 光标移到行首     |
| `Ctrl + E` | 光标移到行尾     |
| `Ctrl + R` | 搜索历史命令     |

---

