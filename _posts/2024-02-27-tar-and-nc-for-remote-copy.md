---
layout: post
title: use tar and nc to remote copy files
category: computer
---
Having a copy of the root file system (rootfs) from a target system is important in vulnerability research.

When investigating embedded systems, some factors can make this process more difficult:

- the target system lacks typical programs used for copying files to remotes systems (eg. `scp`)
- the target system is not physically accessible
- the target system has very little storage

I have noticed that netcat, or `nc`, is one utility that’s fairly common on embedded systems. In the past, I’ve used this for copying a single file at a time by setting up a listener on the target:

`# cat file.txt | nc -lp 1234` 

and then connecting to it from my host:

`$ nc <TARGET_IP_ADDR> 1234 > file.txt`

But it wasn’t till recently that I realized I could use `nc` in conjunction with `tar` (which is also fairly common to find on embedded systems) to easily copy an entire file system from target to host. You can do this with two commands.

First run `$ tar -cz / | nc -lp 1234` on the target.

- `-c` tells tar to create an archive
- `-z` tells tar to compress the archive before sending it to netcat
- `/` specifies you want tar to create an archive from the root directory
- `-lp` means “listen on port…”

Next run `$ nc <TARGET_IP_ADDR> 1234 | pv > rootfs` on your host system.

- `pv` this functionally behaves exactly like `cat` but will display progress

Since tar creates the archive on the fly, it doesn’t matter if out target doesn’t have much storage to spare - as soon as tar packages and zips a small portion of the root directory, it sends it to netcat.
