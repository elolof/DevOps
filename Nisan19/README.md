## Case1

### Case1.1

Centos makine kurulumu yapıldıktan sonra yüklü olan paketlerin güncellemesi yapılır. Centos paket manager olan yum ile bu işlem yapılabilir. `-y` parametresini vererek komutu çalıştırdığımızda yapacağı işlemleri kontrol edemeyebiliriz, update işleminin öneminden dolayı `-y` parametresi göndermeden işlem yapılmıştır.

   `yum update `

### Case1.2

Update işleminden sonra makinede bir user oluşturalım.

`adduser user.name && passwd user.name`


### Case1.3

`su user.name`

`fdisk -l` komutu ile makinedeki diskleri ve partion larını görüntüleyebiliriz. `/dev/sdb` makineye eklediğim 10G disktir. 

```
[root@frtest ansible]# fdisk -l

Disk /dev/sda: 32.2 GB, 32212254720 bytes, 62914560 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0x000a6833

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048     2099199     1048576   83  Linux
/dev/sda2         2099200    62914559    30407680   8e  Linux LVM

Disk /dev/mapper/centos-root: 27.9 GB, 27913093120 bytes, 54517760 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/mapper/centos-swap: 3221 MB, 3221225472 bytes, 6291456 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/sdb: 10.7 GB, 10737418240 bytes, 20971520 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
```

`fdisk /dev/sdb` komutu ile disk partition oluşturabiliriz.

```
[root@frtest ansible]# fdisk /dev/sdb

Welcome to fdisk (util-linux 2.23.2).

Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table
Building a new DOS disklabel with disk identifier 0x76d6139d.

Command (m for help): n
Partition type:
   p   primary (0 primary, 0 extended, 4 free)
   e   extended
Select (default p): p
Partition number (1-4, default 1): 1
First sector (2048-20971519, default 2048):
Using default value 2048
Last sector, +sectors or +size{K,M,G} (2048-20971519, default 20971519): +2G
Partition 1 of type Linux and of size 9 GiB is set

Command (m for help): w
The partition table has been altered!

Calling ioctl() to re-read partition table.
Syncing disks.
```

Aşağıda `/dev/sdb1` partition oluştuğunu görebiliriz.

```
[root@frtest ansible]# fdisk -l

Disk /dev/sda: 32.2 GB, 32212254720 bytes, 62914560 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0x000a6833

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048     2099199     1048576   83  Linux
/dev/sda2         2099200    62914559    30407680   8e  Linux LVM

Disk /dev/mapper/centos-root: 27.9 GB, 27913093120 bytes, 54517760 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/mapper/centos-swap: 3221 MB, 3221225472 bytes, 6291456 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/sdb: 10.7 GB, 10737418240 bytes, 20971520 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0x76d6139d

   Device Boot      Start         End      Blocks   Id  System
/dev/sdb1            2048    18876415     9437184   83  Linux
```

Partition oluştuktan sonra bu diski mount etmeliyiz. Mount edeceğimiz dizini oluşturduktan sonra `mkfs.ext4 /dev/sdb1 <mount_directory>` komutu ile ilgili yere mount edilmelidir. Burada hangi file system ile mount edileceği kullanıcının seçimidir. xfs, ext3, ext4 etc. 

### Case1.4

```
 mkdir /opt/bootcamp
 touch /opt/bootcamp/bootcamp.txt && echo "merhaba trendyol" > /opt/bootcamp/bootcamp.txt
 cd /home/user.name/
 ```
 
### Case1.5

`elolof=$(find / -name bootcamp.txt) &&  mv $elolof /root/bootcamp/`


## Case2

