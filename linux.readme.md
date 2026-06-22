
## 🖥️ Essential Linux Commands & Usages

### 🔧 System Information & Monitoring
- `uname -a` → Show system info (kernel, OS).  
- `top` / `htop` → Monitor running processes and resource usage.  
- `df -h` → Disk space usage in human-readable format.  
- `du -sh <dir>` → Size of a directory.  
- `free -m` → Memory usage.  
- `uptime` → System load and uptime.  

---

### 📂 File & Directory Management
- `ls -l` → List files with details.  
- `cd <dir>` → Change directory.  
- `pwd` → Print current working directory.  
- `mkdir <dir>` → Create directory.  
- `rm -rf <dir>` → Remove directory and contents.  
- `find /path -name "*.log"` → Search for files.  

---

### 📜 File Viewing & Editing
- `cat file.txt` → View file contents.  
- `less file.txt` → Scroll through file.  
- `head -n 20 file.txt` → First 20 lines.  
- `tail -f logfile.log` → Live view of logs.  
- `nano file.txt` / `vim file.txt` → Edit files.  

---

### 🔐 User & Permission Management
- `whoami` → Current user.  
- `id` → Show user ID and groups.  
- `chmod 755 file.sh` → Change permissions.  
- `chown user:group file.txt` → Change ownership.  
- `sudo <command>` → Run command as root.  

---

### 🌐 Networking
- `ping google.com` → Test connectivity.  
- `curl http://example.com` → Fetch web content.  
- `wget http://example.com/file.zip` → Download files.  
- `ifconfig` / `ip addr` → Show network interfaces.  
- `netstat -tulnp` → Show active ports and processes.  
- `ssh user@host` → Secure remote login.  

---

### 📦 Package Management
- **Debian/Ubuntu:**  
  - `apt update && apt upgrade` → Update packages.  
  - `apt install <pkg>` → Install package.  
- **RedHat/CentOS:**  
  - `yum install <pkg>` / `dnf install <pkg>`.  

---

### ⚙️ Process & Job Control
- `ps aux` → List all processes.  
- `kill -9 <pid>` → Force kill process.  
- `jobs` → Show background jobs.  
- `fg %1` → Bring job to foreground.  
- `bg %1` → Resume job in background.  

---

### 🗂️ Archiving & Compression
- `tar -cvf archive.tar dir/` → Create tar archive.  
- `tar -xvf archive.tar` → Extract archive.  
- `gzip file.txt` → Compress file.  
- `gunzip file.txt.gz` → Decompress file.  

---

### 🛠️ Useful Scripts (Examples)
#### 1. Backup Script
```bash
#!/bin/bash
# Backup home directory
tar -czf backup.tar.gz /home/user
```

#### 2. Log Cleaner
```bash
#!/bin/bash
# Delete logs older than 7 days
find /var/log -type f -mtime +7 -exec rm -f {} \;
```

#### 3. Disk Usage Alert
```bash
#!/bin/bash
THRESHOLD=80
USAGE=$(df / | grep / | awk '{print $5}' | sed 's/%//')
if [ $USAGE -gt $THRESHOLD ]; then
  echo "Disk usage above $THRESHOLD%!" | mail -s "Alert" admin@example.com
fi
```

---

## 🎯 Interview-Level Insights
- *“How do you monitor system performance in Linux?”* → Mention `top`, `htop`, `free`, `df`.  
- *“How would you automate log cleanup?”* → Show `find` with `-mtime` in a script.  
- *“What’s the difference between `chmod` 755 and 644?”* → 755 gives execute permission, 644 is read/write only.  

---

