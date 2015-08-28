**Who should follow this documentation?**

If you are new to SignalFx, new to collectd, or new to reporting infrastructure metrics follow this guide.

**What is the end goal?**

1. Downloaded and installed SingalFx's build of collectd
2. Configured collectd to send a baseline of infrastructure metrics to
SignalFx.
3. Viewed the metrics being sent to SignalFx in your organization's Host
page.

**Which Operating Systems are supported?**

  * Ubuntu 12.04, 14.04 & 15.04
  * RHEL/Centos 5.x, 6.x & 7.x
  * Amazon Linux 2014.09 & 2015.03

**Ubuntu 12.04, 14.04 & 15.04**

1. Update apt-get

 ```sudo apt-get update```

2. Install required package for obtaining SignalFx collectd Packages

  **For ubuntu versions &gt; 13.10** - install software-properties-common source package to get SignalFx collectd package

 ```sudo apt-get install software-properties-common```

  **For unbuntu versions &lt; 13.10** - install python-software-properties source package to get SignalFxÂ collectd package

 ```sudo apt-get install python-software-properties```

3. Get the SignalFx collectd package

 ```sudo add-apt-repository ppa:signalfx/collectd-release```

4. Update apt-get to reference new SignalFx package

 ```sudo apt-get update```

5. Install collectd and additional plugins

 ```sudo apt-get install collectd```

6. Configure collectd to send metrics to SignalFx

  With a known API_Token (API token can be found here: https://app.signalfx.com/#/myprofile)

  ```curl -sSL https://dl.signalfx.com/collectd-simple | sudo bash -s -- -t api_token```
 Example:
  ```curl -sSL https://dl.signalfx.com/collectd-simple | sudo bash -s -- -t ABC1234DEF321``` 

  or with user credentials. (You will be promoted for username and password.)

  ```curl -sSL https://dl.signalfx.com/collectd-simple | sudo bash -s --```
 Example:
  ```curl -sSL https://dl.signalfx.com/collectd-simple | sudo bash -s --```  

7. You will be asked how you want to configure your hostname. Type 'input' and press enter

     *options 'dns' and 'aws' are not applicable to this tutorial and you should only use 'input'

8. Next you will be asked to input the hostname value. Type the 'hostname' and press enter

9. You can now view your metrics in SignalFx. We recommend you start with viewing them here under your host page:
 <https://app.signalfx.com/#/catalog/?selectedKeyValue=sf_key:host>


**RHEL/CentOS 6 & 7, Amazon Linux 2014.09, Amazon Linux 2015.03**
 
1. Update wget

 ```sudo yum install wget```

2. Download SignalFx RPM
 Link to list of current
 RPMs <https://support.signalfx.com/hc/en-us/articles/205066479>

 ```wget ~Link to SignalFX RPMs~```

 Example:

 ```wget https://dl.signalfx.com/rpms/SignalFx-rpms/release/SignalFx-RPMs-centos-7-release-1.0-0.noarch.rpm```

3. Install SignalFx RPM

 ```sudo yum install RPM_Name```

 Example:

 ```sudo yum install SignalFx-RPMs-centos-7-release-1.0-0.noarch.rpm```

4. Install collectd and needed base plugins

 ```sudo yum install collectd collectd-disk collectd-write_http```

5. Configure collectd to send metrics to SignalFx

  With a known api token (API token can be found here: https://app.signalfx.com/#/myprofile)

 ```curl -sSL https://dl.signalfx.com/collectd-simple | sudo bash -s -- -t api_token```

  or with user credentials. (You will be promoted for username and password)

 ```curl -sSL https://dl.signalfx.com/collectd-simple | sudo bash -s --```

6. You will be asked how you want to configure your hostname. Type 'input' and press enter

     *options 'dns' and 'aws' are not applicable to this tutorial

7. Next you will be asked to input the hostname value. Type the 'hostname' and press enter

8. You can now view your metrics in SignalFx. We recommend you start with viewing them here under your host page:
 <https://app.signalfx.com/#/catalog/?selectedKeyValue=sf_key:host>


**RHEL/CentOS 5**

1. Install python-simplejson

 ```sudo yum install python-simplejson```

2. Update openssl

 ```sudo yum update openssl```

3. Install wget

 ```sudo yum install wget```

4. Download SignalFx RPM
 Link to list of current
 RPMs <https://support.signalfx.com/hc/en-us/articles/205066479>

 ```wget SignalFx_Centos_5_RPM_Location```

 Example:

 ```wget https://s3.amazonaws.com/public-downloads--signalfuse-com/rpms/SignalFx-rpms/release/SignalFx-RPMs-centos-5-release-1.0-0.noarch.rpm```

5. Install SignalFx RPM

 ```sudo yum install --nogpgcheck SignalFx_Centos_5_RPM_Filename```

 Example:

 ```sudo yum install --nogpgcheck SignalFx-RPMs-centos-5-release-1.0-0.noarch.rpm```

6. Install collectd and baseplugins

 ```sudo yum install collectd collectd-disk collectd-write_http```

7. Configure collectd with a known api token (API token can be found here: https://app.signalfx.com/#/myprofile)

 ```curl https://s3.amazonaws.com/public-downloads--signalfuse-com/collectd-simple | sudo bash -s -- -t $api_token```

8. You will be asked how you want to configure your hostname. Type 'input' and press enter

     *options 'dns' and 'aws' are not applicable to this tutorial and you should only use 'input'

9. Next you will be asked to input the hostname value. Type the 'hostname' and press enter

10. You can now view your metrics in SignalFx. We recommend you start with viewing them here under your host page:
<https://app.signalfx.com/#/catalog/?selectedKeyValue=sf_key:host>
