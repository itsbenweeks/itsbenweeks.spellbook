Setting up an Odroid HC-2 for GlusterFS NAS
---

After telling myself that I should have a NAS on my home network, I finally
decided to do so. The community at reddit's r/homelab has several people posting
their various rigs and how they configure them, so I've been keeping a look out
over the several that get posted every week.

Enter this post,
https://www.reddit.com/r/DataHoarder/comments/8ocjxz/200tb_glusterfs_odroid_hc2_build/
(okay, it's r/DataHorder, guess it was actually cross-posted) and I realized
that something like this would be much easier to implement. So I bought some
parts and decided to set to task.

##Configuring your SD card.

This was one of the easiest parts. I needed to configure my SD card to run
ODroid's XU4 armbian image. Taking the 32GB card I purchased, I ran etcher and
flashed the card. This would mean that I needed to configure it separately.
Given that these single-use cards only had one purpose, I decided to give them
hostnames that match various radiolaria from one of [Ernst Haeckel's prints](https://commons.wikimedia.org/wiki/File:Haeckel_Discoidea.jpg "Haeckel's Discoidea print.").

Once the odroid image is flashed into the sd card, it's simply a matter of
putting the card into the hc-2 and powering it on. After doing that, I was able
to assign it an IP address and get started.

##Setting up the HDD
Gluster is funded by Red Hat, so all their documentation mentions XFS. As such,
I decided to go along with that in hopes that would minimize any potential
issues. It turns out that armbian doesn't have xfs in it's stock image for xu4,
but I changed the profile to a HC1 in armbian-config by going to System > DTB.

The following command seemed good enough:

```
mkfs.xfs -i size=512 /dev/sda1
echo '/dev/sda1 /data/brick1 xfs defaults 1 2' >> /etc/fstab
mount -a && mount
```


##Configuring GlusterFS Servers

In order to correctly configure GlusterFS, I needed to make sure that the
networking was configure such that the nodes in the gluster cluster would be
able to see each other. I took the relatively easy route of assigning static
DHCP addresed to the mac addresses for the HC-2s.

In order to allow gluster to commincate with the other nodes, I needed to add a
rule in iptables for each assigned ip address:

```
iptables -I INPUT -p all -s 192.168.2.3 -j ACCEPT
iptables -I INPUT -p all -s 192.168.2.4 -j ACCEPT
iptables -I INPUT -p all -s 192.168.2.5 -j ACCEPT
iptables -I INPUT -p all -s 192.168.2.6 -j ACCEPT
iptables -I INPUT -p all -s 192.168.2.7 -j ACCEPT
```

Once that was done, a good amount of deliberation was done to make sure that the
cluster would be able to recover a lost device. This required a thin-arbiter as
described in their documentation at the following link:

https://docs.gluster.org/en/main/Administrator-Guide/Thin-Arbiter-Volumes/

With that done, the gluster command to create the volume was as follows:

```
gluster volume create gvol0 transport tcp replica 2 thin-arbiter 1
boseanum:/data/brick1 quadratum:/data/brick1 furcatum:/data/brick1 
trispinosum:/data/brick1 amphirhopalum:/data/brick1 force
