# memscanner

Scan the memory of a process to find pointers which point from one memory region to another.

## Example

```sh
$ /bin/sleep 42 &
[1] 352410

$ sudo python memscanner.py $!
[0x0000559c938e61d0 -> 0x00007f7d9ebaf850]  (+0x000001d0 -> +0x00078850)  /bin/sleep (r--p) -> /lib/x86_64-linux-gnu/libc-2.31.so (r-xp)
[0x0000559c938e7010 -> 0x00007ffdbe594760]  (+0x00000010 -> +0x00020760)  /bin/sleep (rw-p) -> [stack] (rw-p)
[0x0000559c938e7011 -> 0x00007f7d9ecfe6a0]  (+0x00000011 -> +0x000016a0)  /bin/sleep (rw-p) -> /lib/x86_64-linux-gnu/libc-2.31.so (rw-p)
[0x0000559c938e701a -> 0x00007f7d9ecfc960]  (+0x0000001a -> +0x00002960)  /bin/sleep (rw-p) -> /lib/x86_64-linux-gnu/libc-2.31.so (r--p)
[0x0000559c941d4069 -> 0x00007f7d9e5bb5c0]  (+0x00000069 -> +0x000195c0)  [heap] (rw-p) -> /usr/lib/locale/locale-archive (r--p)
[0x0000559c941d427f -> 0x00007f7d9ecd1010]  (+0x0000027f -> +0x00022010)  [heap] (rw-p) -> /lib/x86_64-linux-gnu/libc-2.31.so (r--p)
[0x00007f7d9ecfa5b6 -> 0x0000559c938e70c0]  (+0x000005b6 -> +0x000000c0)  /lib/x86_64-linux-gnu/libc-2.31.so (r--p) -> /bin/sleep (rw-p)
[0x00007f7d9ecfa5be -> 0x00007f7d9ed4e060]  (+0x000005be -> +0x00000060)  /lib/x86_64-linux-gnu/libc-2.31.so (r--p) -> /lib/x86_64-linux-gnu/ld-2.31.so (rw-p)
[0x00007f7d9ecfa5c4 -> 0x00007f7d9ed4de60]  (+0x000005c4 -> +0x00000e60)  /lib/x86_64-linux-gnu/libc-2.31.so (r--p) -> /lib/x86_64-linux-gnu/ld-2.31.so (r--p)
[0x00007f7d9ecfd002 -> 0x00007f7d9ed38bb0]  (+0x00000002 -> +0x00017bb0)  /lib/x86_64-linux-gnu/libc-2.31.so (rw-p) -> /lib/x86_64-linux-gnu/ld-2.31.so (r-xp)
[0x00007f7d9ecfd0dc -> 0x00007f7d9e5c6294]  (+0x000000dc -> +0x00024294)  /lib/x86_64-linux-gnu/libc-2.31.so (rw-p) -> /usr/lib/locale/locale-archive (r--p)
[0x00007f7d9ecfd0e2 -> 0x0000559c941d5420]  (+0x000000e2 -> +0x00001420)  /lib/x86_64-linux-gnu/libc-2.31.so (rw-p) -> [heap] (rw-p)
[0x00007f7d9ecfd539 -> 0x0000559c938e7008]  (+0x00000539 -> +0x00000008)  /lib/x86_64-linux-gnu/libc-2.31.so (rw-p) -> /bin/sleep (rw-p)
[0x00007f7d9ed4d0ad -> 0x00007ffdbe5fb120]  (+0x000000ad -> +0x00000120)  /lib/x86_64-linux-gnu/ld-2.31.so (r--p) -> [vdso] (r-xp)
[0x00007f7d9ed4d0c0 -> 0x00007ffdbe593228]  (+0x000000c0 -> +0x0001f228)  /lib/x86_64-linux-gnu/ld-2.31.so (r--p) -> [stack] (rw-p)
[0x00007f7d9ed4d1fc -> 0x00007f7d9ebaf850]  (+0x000001fc -> +0x00078850)  /lib/x86_64-linux-gnu/ld-2.31.so (r--p) -> /lib/x86_64-linux-gnu/libc-2.31.so (r-xp)
[0x00007f7d9ed4e003 -> 0x00007f7d9ec75830]  (+0x00000003 -> +0x0013e830)  /lib/x86_64-linux-gnu/ld-2.31.so (rw-p) -> /lib/x86_64-linux-gnu/libc-2.31.so (r-xp)
[0x00007f7d9ed4e13e -> 0x0000559c938dd318]  (+0x0000013e -> +0x00000318)  /lib/x86_64-linux-gnu/ld-2.31.so (rw-p) -> /bin/sleep (r--p)
[0x00007f7d9ed4e1c1 -> 0x00007f7d9eb1a790]  (+0x000001c1 -> +0x00008790)  /lib/x86_64-linux-gnu/ld-2.31.so (rw-p) -> /lib/x86_64-linux-gnu/libc-2.31.so (r--p)
[0x00007ffdbe577b95 -> 0x00007f7d9ed26bab]  (+0x00003b95 -> +0x00005bab)  [stack] (rw-p) -> /lib/x86_64-linux-gnu/ld-2.31.so (r-xp)
[0x00007ffdbe577ba5 -> 0x00007f7d9ed444a0]  (+0x00003ba5 -> +0x000004a0)  [stack] (rw-p) -> /lib/x86_64-linux-gnu/ld-2.31.so (r--p)
[0x00007ffdbe577c6b -> 0x0000559c938dda49]  (+0x00003c6b -> +0x00000a49)  [stack] (rw-p) -> /bin/sleep (r--p)
[0x00007ffdbe577c8a -> 0x00007f7d9ed4e060]  (+0x00003c8a -> +0x00000060)  [stack] (rw-p) -> /lib/x86_64-linux-gnu/ld-2.31.so (rw-p)
[0x00007ffdbe577cd6 -> 0x00007f7d9eb19608]  (+0x00003cd6 -> +0x00007608)  [stack] (rw-p) -> /lib/x86_64-linux-gnu/libc-2.31.so (r--p)
[0x00007ffdbe577cd8 -> 0x00007f7d9ed20474]  (+0x00003cd8 -> +0x00000474)  [stack] (rw-p) -> /lib/x86_64-linux-gnu/ld-2.31.so (r--p)
[0x00007ffdbe577d1b -> 0x00007f7d9ecfd0a0]  (+0x00003d1b -> +0x000000a0)  [stack] (rw-p) -> /lib/x86_64-linux-gnu/libc-2.31.so (rw-p)
[0x00007ffdbe577d24 -> 0x00007f7d9ebae3d0]  (+0x00003d24 -> +0x000773d0)  [stack] (rw-p) -> /lib/x86_64-linux-gnu/libc-2.31.so (r-xp)
[0x00007ffdbe577d7e -> 0x00007f7d9eccae26]  (+0x00003d7e -> +0x0001be26)  [stack] (rw-p) -> /lib/x86_64-linux-gnu/libc-2.31.so (r--p)
[0x00007ffdbe577da2 -> 0x00007f7d9eb0e1c0]  (+0x00003da2 -> +0x0056c1c0)  [stack] (rw-p) -> /usr/lib/locale/locale-archive (r--p)
[0x00007ffdbe577de1 -> 0x0000559c938e6bc0]  (+0x00003de1 -> +0x00000bc0)  [stack] (rw-p) -> /bin/sleep (r--p)
[0x00007ffdbe577de7 -> 0x0000559c938e7090]  (+0x00003de7 -> +0x00000090)  [stack] (rw-p) -> /bin/sleep (rw-p)
[0x00007ffdbe577de8 -> 0x0000559c938e3004]  (+0x00003de8 -> +0x00000004)  [stack] (rw-p) -> /bin/sleep (r--p)
[0x00007ffdbe577deb -> 0x0000559c938df940]  (+0x00003deb -> +0x00000940)  [stack] (rw-p) -> /bin/sleep (r-xp)
```