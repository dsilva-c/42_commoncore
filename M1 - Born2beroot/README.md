<img width="2000" height="1000" alt="cover-born2beroot-bonus" src="https://raw.githubusercontent.com/ayogun/42-project-badges/refs/heads/main/covers/cover-born2beroot-bonus.png" />

<div align="center">

# 📚 M1 – Born2beRoot

![42 Born2beRoot](https://img.shields.io/badge/42-Born2beRoot-00babc?style=for-the-badge&logo=42)
![VirtualBox](https://img.shields.io/badge/VirtualBox-21416b?style=for-the-badge&logo=virtualbox&logoColor=white)
![Debian](https://img.shields.io/badge/Debian-A81D33?style=for-the-badge&logo=debian&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)

<p align="center">
  <img src="https://github.com/leogaudin/42_project_badges/raw/main/badges/born2beroot_bonus_max.webp" alt="born2beroot_bonus_max.webp">
</p>

This project is part of the **42cursus** at 42 Porto.  
The goal is to create a secure, minimal server environment using a Virtual Machine. This project introduces system administration, virtualization, partitioning, LVM, SSH, password policies, monitoring, and firewall configuration.

</div>

> **⚠️ Disclaimer:** This repository documents the step-by-step guide I followed for the project. It is intended for reference and does not contain the final VM files.

---

## 🎯 Objectives

- Install and configure a Virtual Machine (VirtualBox).
- Implement strict partitioning using **LVM** (Logical Volume Manager) .
- Configure a secure **SSH** service and firewall (**UFW**).
- Enforce strong password policies and sudo configurations.
- Create a bash script for system monitoring.
- **Bonus:** Setup a web server (**Lighttpd**), database (**MariaDB**), and strict network defense (**Fail2Ban**).

---

## 📑 Table of Contents

1.  [🎓 Chapter I: Theoretical Concepts (Defense Prep)](#-chapter-i-theoretical-concepts-defense-prep)
2.  [💿 Chapter II: VM Creation & Installation](#-chapter-ii-vm-creation--installation)
    * [Step 1: VirtualBox Configuration (sgoinfre & Dynamic Storage)](#step-1-virtualbox-configuration-sgoinfre--dynamic-storage)
    * [Step 2: Operating System Installation](#step-2-operating-system-installation)
    * [Step 3: Manual Partitioning (Encrypted LVM Bonus Structure)](#step-3-manual-partitioning-encrypted-lvm-bonus-structure)
3.  [⚙️ Chapter III: Mandatory Configuration](#-chapter-iii-mandatory-configuration)
    * [Step 1: Security Hardening (Sudo, User, SSH, UFW)](#step-1-security-hardening-sudo-user-ssh-ufw)
    * [Step 2: Password Policy & Aging (With Explanations)](#step-2-password-policy--aging-with-explanations)
    * [Step 3: System Monitoring Script](#step-3-system-monitoring-script)
4.  [🌟 Chapter IV: Bonus Configuration](#-chapter-iv-bonus-configuration)
    * [Bonus 1: Full Stack Web Server (Lighttpd, MariaDB, PHP, WordPress)](#bonus-1-full-stack-web-server)
    * [Bonus 2: Intrusion Defense (Fail2Ban)](#bonus-2-intrusion-defense-fail2ban)
5.  [🛡️ Chapter V: Defense & Submission](#-chapter-v-defense--submission)

---

## 🎓 Chapter I: Theoretical Concepts (Defense Prep)

*During your defense, you must explain the "Why" and "How" of your setup in detail.*

### 1. Virtualization & Hypervisors
**Virtualization** is the technology that allows you to create a software-based (virtual) representation of something, such as a computer.
* **Virtual Machine (VM):** An emulated computer system running inside your physical computer. It is isolated from the host, making it a safe sandbox to test server configurations without risking your main system.
* **Hypervisor:** The software layer that creates and runs VMs.
    * **Type 1 (Bare Metal):** Runs directly on the physical hardware without an underlying OS (e.g., Xen, ESXi). Common in data centers.
    * **Type 2 (Hosted):** Runs as an application on an existing Operating System (e.g., **VirtualBox**, VMware Workstation). We use this type for the project.

### 2. LVM (Logical Volume Manager)
**LVM** is a storage abstraction layer that allows for flexible disk management, separating the physical hardware from the file system.
* **Structure:**
    1.  **Physical Volumes (PV):** The actual raw disk or partition.
    2.  **Volume Groups (VG):** A storage pool combining multiple PVs.
    3.  **Logical Volumes (LV):** The virtual partitions carved from the VG.
* **Key Benefit:** **Dynamic Resizing.** Unlike standard partitions, which are fixed, you can expand a Logical Volume (e.g., if `/home` fills up) while the system is running using free space from the Volume Group, without reformatting the disk.

### 3. AppArmor vs SELinux
Both are **Mandatory Access Control (MAC)** systems that restrict what programs can do.
* **AppArmor (Debian):** Uses **file-path profiles**. It restricts programs by defining which specific files they are allowed to read, write, or execute. It is generally considered easier to configure and maintain.
* **SELinux (Rocky/RedHat):** Uses **inode labeling**. Every file and process has a security tag, and complex policies define how these tags interact. It is more granular but complex.

### 4. SSH (Secure Shell)
**SSH** is a cryptographic network protocol for operating network services securely over an unsecured network. It replaces insecure legacy tools like Telnet by encrypting the connection.
* **Port 4242:** We change the default port from **22** to **4242**. This is a technique called "Security by Obscurity"—it reduces log noise from automated bots scanning for default ports, though it does not stop targeted attacks.

### 5. UFW (Uncomplicated Firewall)
**UFW** is a user-friendly interface for `iptables` (the underlying Linux packet filtering system).
* **Strategy:** We follow the principle of "Least Privilege". We block **all** incoming connections by default and only explicitly "Allow" the specific ports we need (4242 for SSH, 80 for Web).

### 6. Sudo & TTY
**Sudo** allows a permitted user to execute a command as the superuser (`root`).
* **`requiretty`:** This security rule ensures that sudo commands can *only* be run from a real, interactive terminal session. This prevents background cron jobs or malicious scripts from silently hijacking root privileges.

---

## 💿 Chapter II: VM Creation & Installation

### Step 1: VirtualBox Configuration (sgoinfre & Dynamic Storage)
**⚠️ CAMPUS WARNING:** Saving a 30GB VM in your home folder will crash your account quota. You must use `sgoinfre`.

1.  Open VirtualBox -> **New**.
2.  **Name:** `Born2beRoot`.
3.  **Folder:** Select **Other...** -> Navigate to `/sgoinfre/students/<your_login>/`. Create a folder named `Born2beRoot` and select it.
4.  **Type:** Linux | **Version:** Debian (64-bit).
5.  **Memory:** **1024 MB** (minimum) or **2048 MB** (recommended for bonus).
6.  **Hard Disk:**
    * Select "Create a Virtual Hard Disk Now".
    * File Type: **VDI** (VirtualBox Disk Image).
    * Storage on Physical Hard Disk: **Dynamically Allocated**.
    * **⚠️ IMPORTANT:** Ensure "Pre-allocate Full Size" is **UNCHECKED**. This ensures the file starts small (only occupying space actually used) and grows only as needed.
    * **Size:** **30.8 GB** (Strictly required to accommodate the 7 bonus partitions).

### Step 2: Operating System Installation
1.  Start the VM with the **Debian Stable Netinst ISO**.
2.  Select **Install** (text mode) to minimize resource usage.
3.  **Hostname:** `<your_login>42` (e.g., `dsilva-c42`).
4.  **Root Password:** Set a strong password (you will enforce policy later).
5.  **User:** Create your primary user `<your_login>` (e.g., `dsilva-c`).

### Step 3: Manual Partitioning (Encrypted LVM Bonus Structure)
**Do not use Guided.** You must configure this manually to match the bonus requirements.

1.  Select **Manual**.
2.  **Boot Partition (`/boot`):**
    * Select Free Space -> Create New -> **500 MB** -> Primary -> Beginning.
    * Use as: **Ext4**. Mount point: **/boot**. Select "Done".
3.  **Encrypted Volume:**
    * Select remaining Free Space -> Create New -> **Max Size** -> Primary.
    * Use as: **Physical volume for encryption**. Select "Done".
4.  **Configure Encryption:**
    * Select "Configure encrypted volumes" -> Write changes? **Yes**.
    * Select partition (`/dev/sda2`). Finish.
    * **Passphrase:** Set a secure password. **Do not lose this.**
5.  **LVM Configuration:**
    * Select "Configure the Logical Volume Manager" -> Write changes? **Yes**.
    * **Create Volume Group:** Name: `LVMGroup`. Select the encrypted space (`/dev/mapper/sda2_crypt`).
    * **Create Logical Volumes:** Create these 7 volumes in this order (approximate sizes):
        1.  `root` -> **10 GB**
        2.  `swap` -> **1 GB** (or match RAM)
        3.  `home` -> **5 GB**
        4.  `var` -> **3 GB**
        5.  `srv` -> **3 GB**
        6.  `tmp` -> **3 GB**
        7.  `var-log` -> **Max remaining** (Enter max available size)
6.  **Format Partitions:**
    * Go back to the main list. Select each Logical Volume under `LVMGroup`.
    * Assign "Use as: **Ext4**" (except swap) and Mount Points:
        * `root` -> `/`
        * `swap` -> `swap area`
        * `home` -> `/home`
        * `var` -> `/var`
        * `srv` -> `/srv`
        * `tmp` -> `/tmp`
        * `var-log` -> **Enter manually:** `/var/log`
7.  **Finalize:** Finish partitioning and write changes to disk.
8.  **Software:** **UNCHECK** Desktop environment/GNOME. **CHECK** SSH server & Standard system utilities.

---

## ⚙️ Chapter III: Mandatory Configuration

*(Run all commands as root).*

### Step 1: Security Hardening (Sudo, User, SSH, UFW)
1.  **Sudo Config:**
    ```bash
    apt install sudo
    mkdir -p /var/log/sudo
    visudo
    ```
    *Insert exactly the following lines:*
    ```bash
    Defaults    passwd_tries=3
    Defaults    badpass_message="Incorrect password. Please try again."
    Defaults    logfile="/var/log/sudo/sudo.log"
    Defaults    log_input, log_output
    Defaults    requiretty
    Defaults    secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"
    ```
2.  **User & Groups:**
    ```bash
    groupadd user42
    adduser <your_login> sudo
    adduser <your_login> user42
    ```
3.  **SSH:**
    * Edit `/etc/ssh/sshd_config`: Change `Port 22` to `4242` and `PermitRootLogin` to `no`.
    * Restart: `systemctl restart ssh`.
4.  **Firewall:**
    ```bash
    apt install ufw
    ufw allow 4242
    ufw deny incoming
    ufw enable
    ```
    *(Confirm with `y`)*.

### Step 2: Password Policy & Aging (With Explanations)
1.  **Complexity (`/etc/security/pwquality.conf`):**
    ```ini
    minlen = 10        # Minimum password length must be 10 characters
    dcredit = -1       # Must contain at least 1 digit (-1 enforces credit)
    ucredit = -1       # Must contain at least 1 uppercase letter
    lcredit = -1       # Must contain at least 1 lowercase letter
    maxrepeat = 3      # Maximum of 3 consecutive identical characters allowed
    usercheck = 1      # Reject the password if it contains the username
    difok = 7          # New password must differ from old by at least 7 characters
    enforce_for_root   # Enforce these policies for the root user as well
    ```
2.  **Aging (`/etc/login.defs`):**
    ```bash
    PASS_MAX_DAYS   30  # Password expires every 30 days
    PASS_MIN_DAYS   2   # Minimum 2 days before password change is allowed
    PASS_WARN_AGE   7   # User receives warning 7 days before expiration
    ```
    * **Apply Manually:** The file edits only affect *new* users. You must run:
        `chage -M 30 -m 2 -W 7 <your_login>` (Repeat for `root`).

### Step 3: System Monitoring Script
The script must run every 10 minutes **relative to boot time** (e.g., if boot is 10:04, it runs at 10:14, 10:24).

1.  **Sleep Script (`/usr/local/bin/sleep.sh`):**
    ```bash
    #!/bin/bash
    # Calculates minutes since boot and sleeps the remainder of modulo 10
    sleep $(who -b | awk '{split($4, time, ":"); print time[2]%10}')m
    ```
2.  **Monitoring Script (`/usr/local/bin/monitoring.sh`):**
    *(Paste your full bash script here gathering uname, nproc, free, df, wall, etc. to match subject requirements).*
3.  **Cron Job:** `crontab -u root -e`
    `*/10 * * * * sh /usr/local/bin/sleep.sh; /usr/local/bin/monitoring.sh`

---

## 🌟 Chapter IV: Bonus Configuration

### Bonus 1: Full Stack Web Server
**Goal:** Functional WordPress site.

1.  **Install:** `apt install lighttpd mariadb-server php-cgi php-mysql wget`
2.  **Firewall:** `ufw allow 80`.
3.  **Database:**
    * Run `mysql_secure_installation` (Answer Y to all security questions).
    * Enter SQL: `mariadb -u root -p`
        * `CREATE DATABASE wordpress_db;`
        * `GRANT ALL ON wordpress_db.* TO 'wp_user'@'localhost' IDENTIFIED BY 'wp_pass';`
        * `FLUSH PRIVILEGES;` `EXIT;`
4.  **Lighttpd PHP:** Enable FastCGI modules.
    `lighty-enable-mod fastcgi fastcgi-php` -> `systemctl force-reload lighttpd`
5.  **WordPress Deployment:**
    * Download and extract latest WordPress to `/var/www/html`.
    * Set permissions: `chown -R www-data:www-data wordpress`
    * Rename config: `mv wp-config-sample.php wp-config.php`.
    * Edit `wp-config.php`: Update `DB_NAME`, `DB_USER`, and `DB_PASSWORD` with values from step 3.
6.  **Verify:** Visit `http://<VM_IP>/wordpress` (Use `hostname -I` to find your IP).

### Bonus 2: Intrusion Defense (Fail2Ban)
**Goal:** Protect SSH from brute force attacks.

1.  **Install:** `apt install fail2ban`
2.  **Config:** Copy the default config: `cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local`.
3.  **Edit `jail.local`:** Add/Edit the `[sshd]` section:
    ```ini
    [sshd]
    enabled = true
    port = 4242
    maxretry = 3
    bantime = 10m   # Bans the IP for 10 minutes (600 seconds)
    ```
4.  **Restart:** `systemctl restart fail2ban`.
5.  **Verify:** `fail2ban-client status sshd`.

---

## 🛡️ Chapter V: Defense & Submission

### Verification Checklist
* **Identity:** `hostnamectl` (Debian).
* **Partitions:** `lsblk` (7 LVM partitions + boot).
* **Network:** `ss -tunlp` (Ports 4242, 80).
* **Security:** `chage -l <user>` (30 days max).
* **Bonus:** Web browser loads WordPress. Fail2Ban jail is active.

### Submission Steps
1.  **Clean Up:** Remove any temporary scripts (like `verify.sh`).
2.  **Power Off:** `sudo shutdown now`.
3.  **Generate Signature (Host):**
    * Navigate to your storage: `cd /sgoinfre/students/<login>/Born2beRoot/`
    * Run Hash: `shasum Born2beRoot.vdi`
4.  **Submit:** Paste the hash output into `signature.txt`, commit, and push.

**⚠️ FINAL WARNING:** Do NOT start the VM after hashing. If you turn it on, the file changes, the hash changes, and you will receive a grade of 0.

---

## 🛠️ Tech stack

<div align="center">

<table width="100%">
    <thead>
        <tr>
            <th width="20%">Category</th>
            <th width="80%">Technologies</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center"><b>Virtualization & OS</b></td>
            <td>
                <img src="https://img.shields.io/badge/VirtualBox-21416b?logo=virtualbox&logoColor=white" alt="VirtualBox">
                <img src="https://img.shields.io/badge/Debian-A81D33?logo=debian&logoColor=white" alt="Debian">
            </td>
        </tr>
        <tr>
            <td align="center"><b>System & Security</b></td>
            <td>
                <img src="https://img.shields.io/badge/LVM-F7931E?logo=linux&logoColor=white" alt="LVM">
                <img src="https://img.shields.io/badge/SSH-000000?logo=openssh&logoColor=white" alt="SSH">
                <img src="https://img.shields.io/badge/UFW-FF4500?logo=ubuntu&logoColor=white" alt="UFW">
                <img src="https://img.shields.io/badge/Sudo-004088?logo=linux&logoColor=white" alt="Sudo">
                <img src="https://img.shields.io/badge/AppArmor-1B2252?logo=linux&logoColor=white" alt="AppArmor">
            </td>
        </tr>
        <tr>
            <td align="center"><b>Scripting</b></td>
            <td>
                <img src="https://img.shields.io/badge/Bash-4EAA25?logo=gnu-bash&logoColor=white" alt="Bash">
            </td>
        </tr>
        <tr>
            <td align="center"><b>Bonus Services</b></td>
            <td>
                <img src="https://img.shields.io/badge/Lighttpd-000000?logo=lighttpd&logoColor=white" alt="Lighttpd">
                <img src="https://img.shields.io/badge/MariaDB-003545?logo=mariadb&logoColor=white" alt="MariaDB">
                <img src="https://img.shields.io/badge/PHP-777BB4?logo=php&logoColor=white" alt="PHP">
                <img src="https://img.shields.io/badge/WordPress-21759B?logo=wordpress&logoColor=white" alt="WordPress">
                <img src="https://img.shields.io/badge/Fail2Ban-282c34?logo=security&logoColor=white" alt="Fail2Ban">
            </td>
        </tr>
    </tbody>
</table>

</div>

---

## 📝 License & credits

* **Curriculum:** [42 Porto](https://www.42network.org/campus/42-porto/)

> *This project is part of the 42 Student Network curriculum.*

---

## 📈 Final grade

<img width="1101" height="117" alt="Born2beRoot_grade" src="https://github.com/user-attachments/assets/2d7f2ba2-8c02-40fb-bc6c-e0508dd4c8d4" />
