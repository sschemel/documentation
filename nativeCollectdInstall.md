**We HIGHLY recommend that you install our latest package of collectd.
You can find
instructions **[**here**](https://support.signalfx.com/hc/en-us/articles/205147119)**. **

If you are already familiar with collectd and just need to know how to
configure collectd to point to SignalFx please see
these [instructions](https://support.signalfx.com/hc/en-us/articles/201094025-Use-collectd). 

**What is collectd?**

Collectd is collects system performance statistics periodically and
provides the ability to store the values in a variety of ways. It is the
most popular and widely used monitoring agent. Due to that it is written
in C it is incredibly fast, lightweight, and available on the majority
of Linux distributions. If you want more information you can
visit [collectd's home page](https://collectd.org/). 

***Step One: Download & Install collectd* **

**For Debian-based versions of linux: Debian, Ubuntu, etc**

1\. Confirm you are running a Debian-based system:

```which dpkg```

*\*If this command returns something like: ‘/bin/dpkg’ it’s a safe bet
you are on a debian based version of linux*

2\. Update local repository

```sudo apt-get update```

3\. Install collectd 

```sudo apt-get install collectd```

4\. Check that collectd has installed

```collectd -h```

*\*If you get a message like the following collectd hasn’t
installed: -bash: collectd: command not found*

**For RPM-based Linux distributions: RedHat, CentOS, etc**

1\. Confirm you are running a RPM-based system:

```which rpm```

*\*If this command returns something like: ‘/bin/rpm’ it’s a safe bet
you are on a RPM based version of linux*

2\. If you are using RedHat/CentOS 7.x you need to enable the epel
repository by running:

```sudo yum install epel-release```

If you are using an older version of RedHat/CentOS/Fedora that is 6.x or
earlier you need to enable the epel (Extra Packages for Enterprise
Linux) repository to install collectd. &lt;link to other doc&gt;\
*All other versions of RPM-based linux distributions will also need the
epel repository enabled before you can install collectd.*

2\. Update local repository 

```sudo yum update```

3\. Install collectd 

```sudo yum install collectd```

*\*If a version of collectd earlier than 5.2 got installed you
will **NOT** be able to aggregate CPU metrics. The Aggregation plugin is
only supported on 5.2 and later. For the best experience we recommend
you use our latest collectd 5.5.x package. Instruction can be
found *[*here*](https://support.signalfx.com/hc/en-us/articles/205147119)

4\. Install baseline collectd plugins

```sudo yum install collectd-disk collectd-write_http```

5\. Check that collectd has installed

```collectd -h```

*If you get a message like the following collectd hasn’t
installed: -bash: collectd: command not found*

***Step Two: Configure collectd to send metrics to SignalFx***

Now that collectd is installed we need to configure it to collect
and send metrics to SignalFx. To automatically configure collectd with a
base configuration and to send metrics to SignalFx follow the
instructions below. To manually configure collectd please see these
instructions

1\. To do this you need to run the following curl command:

```curl -sSL https://dl.signalfx.com/collectd-simple | bash -s -- -t
API_TOKEN```

*\*to find your org API Token go
to *[*https://app.signalfx.com/\#/myprofile*](https://app.signalfx.com/#/myprofile) 

or

```curl -sSL https://dl.signalfx.com/collectd-simple | sudo bash -s --```

example:

```curl -sSL https://dl.signalfx.com/collectd-simple | bash -s --
-t abc_123_efg```

or

```curl -sSL https://dl.signalfx.com/collectd-simple | sudo bash -s --```

2\. You will be asked how you want to configure your hostname.** \
**Type 'input' and press enter\
*\*options 'dns' and 'aws' are not relevant in this tutorial *

3\. Next you will be asked to input the hostname value. \
Type the 'hostname' and press enter

***Step Three: View Metrics in SignalFx***

We have pre-built a handful of discovery dashboards for you to explore
and discover your metrics. Our recommended place to start is in the
Catalog which you can get to
here <https://app.signalfx.com/#/catalog/?selectedKeyValue=sf_key:host>
