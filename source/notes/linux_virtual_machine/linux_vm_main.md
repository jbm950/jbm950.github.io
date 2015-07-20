# Linux Virtual Machines

## Table of Contents

> ### Ubuntu Desktop VM

> - [Virtualbox Steps](#virtualbox_steps)
>       - [Additional Options](#vb_additional_options)
> - [Install Ubuntu](#install_ubuntu)
> - [Set up Vim](#set_up_vim)
> - [Set up Python](#set_up_python)
> - [Other Libraries](#other_libraries)

## Setting up an Ubuntu desktop for use

> - I will be using [virtualbox](https://www.virtualbox.org/wiki/Downloads) for
    my virtual machines  
> - I will be going through the steps to setup a ubuntu desktop in this portion
    of the notes. The download for Ubuntu Desktop can be found
    [here](http://www.ubuntu.com/download/desktop)

> ### VirtualBox steps {#virtualbox_steps}

>> Begin by clicking on the button in the upper left hand corner to create a new
   virtual machine

<div align="center">
<table class="image">
<caption align="bottom">Create a New Virtual Machine</caption>
<tr><td><img src="./img/new_vmachine.jpg"
alt="New Virtual Machine" title="New Virtual Machine"
height="400" width="500"/>
</td></tr>
</table>
</div>

>> Now you're going to be asked what opperating system to use for the new
   virtual machine. You will also need to name your machine in this step to
   differentiate it from your other virtual machines. In this set of the notes
   I'm going to go over the creation of a Ubuntu desktop virtual machine and for
   the sake of the notes I'm going to name it test.

<div align="center">
<table class="image">
<caption align="bottom">Name and Choose System</caption>
<tr><td><img src="./img/choose_system.jpg"
alt="Name Virtual Machine" title="Name Virtual Machine"
height="400" width="500"/>
</td></tr>
</table>
</div>

>> The next step will be to determine the amount of ram you want the virtual
   machine to be able to access. Of my 8 gb of ram I have decided to allow the
   vm to use 2 gb in case I still want to use the main operating system at the
   same time.

<div align="center">
<table class="image">
<caption align="bottom">Name and Choose System</caption>
<tr><td><img src="./img/vm_memory.jpg"
alt="Name Virtual Machine" title="Name Virtual Machine"
height="400" width="500"/>
</td></tr>
</table>
</div>

>> Virtualbox will then ask if we want to create a new virtual disk or use an
   existing one. Most often a new disk will be made the only exception being if
   trying to used the same virtual machine on different computers and you want
   the same harddrive to be used.

<div align="center">
<table class="image">
<caption align="bottom">Create New Virtual Harddrive</caption>
<tr><td><img src="./img/harddrivecreate.jpg"
alt="Create Virtual Harddrive" title="Create Virtual Harddrive"
height="400" width="500"/>
</td></tr>
</table>
</div>

>> The filetype for the disk needs to be determined next. Since I don't use
   vmware or any other virtual machine software, I'm just going to leave the
   file type as vdi.

<div align="center">
<table class="image">
<caption align="bottom">Choose Virtualdisk Filetype</caption>
<tr><td><img src="./img/diskfiletype.jpg"
alt="Choose Virtualdisk Filetype" title="Choose Virtualdisk Filetype"
height="400" width="500"/>
</td></tr>
</table>
</div>

>> Virtualbox now needs to know if you want the new virtualdisk to expand as
>> needed or if you want to leave it at a fixed value. I chose dynamically
>> sized as I've had trouble with fixed size in the past and dynamically sized
>> ones are easier to expand later if necessary.

<div align="center">
<table class="image">
<caption align="bottom">Choose Virtualdisk Storage Type</caption>
<tr><td><img src="./img/type_of_storage.jpg"
alt="Choose Virtualdisk Storage Type" title="Choose Virtualdisk Storage Type"
height="400" width="500"/>
</td></tr>
</table>
</div>

>> Now the size and location of the virtualdisk is decided. I have marked the
   button for relocating the new virtualdisk. Also I changed the harddrive size
   to 10 gb.

<div align="center">
<table class="image">
<caption align="bottom">Choose Virtualdisk Storage Size</caption>
<tr><td><img src="./img/size_of_storage.jpg"
alt="Choose Virtualdisk Storage Size" title="Choose Virtualdisk Storage Size"
height="400" width="500"/>
</td></tr>
</table>
</div>

>> The virtual machine should now be made and you're ready to run the install
   of the operating system.

>> #### Additional Options {#vb_additional_options}

>>> __Use a different ip address__

>>> __Access USB ports__

> ### Install Ubuntu {#install_ubuntu}

>> To begin the install of Ubuntu on the new virtual machine, start up the new
   virtual machine.

<div align="center">
<table class="image">
<caption align="bottom">Start the New Virtual Machine</caption>
<tr><td><img src="./img/start_vm.jpg"
alt="Start Virtual Machine" title="Start Virtual Machine"
height="400" width="500"/>
</td></tr>
</table>
</div>

>> The next step is to click the icon to browse your files for the Ubuntu
   desktop iso file. This will allow the virtual machine to boot up using
   Ubuntu. Once you've selected the iso file click start.

<div align="center">
<table class="image">
<caption align="bottom">Select the ISO File</caption>
<tr><td><img src="./img/select_iso.jpg"
alt="Find iso File" title="Find iso File"
height="400" width="500"/>
</td></tr>
</table>
</div>

>> Now comes the time to actaully install Ubuntu on the new virtaul machine.
   We'll be selecting install ubuntu instead of try Ubuntu.

<div align="center">
<table class="image">
<caption align="bottom">Install Ubuntu</caption>
<tr><td><img src="./img/ubuntu_install.jpg"
alt="Install Ubuntu" title="Install Ubuntu"
height="400" width="500"/>
</td></tr>
</table>
</div>

>> I'm going to make it go ahead and download updates while installing to
   possibly save time later. Other than that go ahead and click continue.

<div align="center">
<table class="image">
<caption align="bottom">Install Ubuntu Step 1</caption>
<tr><td><img src="./img/uinstall_step1.jpg"
alt="Install Ubuntu Step 1" title="Install Ubuntu Step 1"
height="400" width="500"/>
</td></tr>
</table>
</div>

>> Now we're going to go ahead and install ubuntu. Don't worry about it's
   warning about erasing the disk because it will be contained with the newly
   created virtual harddrive which has nothing on it yet anyways.

<div align="center">
<table class="image">
<caption align="bottom">Install Ubuntu Final Step</caption>
<tr><td><img src="./img/inst_ubuntu_finalstep.jpg"
alt="Install Ubuntu Final Step" title="Install Ubuntu Final Step"
height="400" width="500"/>
</td></tr>
</table>
</div>

>> Simply click continue and let the install begin.

<div align="center">
<table class="image">
<caption align="bottom">Change Disk Warning</caption>
<tr><td><img src="./img/disk_change_warning.jpg"
alt="Change Disk Warning" title="Change Disk Warning"
height="400" width="500"/>
</td></tr>
</table>
</div>

>> This step is self explanitory. Go ahead and select your time zone and then
   continue on.

<div align="center">
<table class="image">
<caption align="bottom">Time Zone Selection</caption>
<tr><td><img src="./img/time_zone_select.jpg"
alt="Time Zone Selection" title="Time Zone Selection"
height="400" width="500"/>
</td></tr>
</table>
</div>

>> Select the keyboard language setup for your use. Being in the US I don't
   have to change the defaults and can simply continue on to the next step.

<div align="center">
<table class="image">
<caption align="bottom">Keyboard Language Selection</caption>
<tr><td><img src="./img/keyboard_lang.jpg"
alt="Keyboard Language Selection" title="Keyboard Language Selection"
height="400" width="500"/>
</td></tr>
</table>
</div>

>> The last step will be to set up the user account you will be using for the
   Ubuntu system. Putting in your name will automatically fill in the next two
   text boxes. Set your password and decided whether or not you want your
   system to automatically log in when started or if you want it to prompt you
   for your password. After hitting continue the install should begin.

<div align="center">
<table class="image">
<caption align="bottom">User Setup</caption>
<tr><td><img src="./img/ubuntu_usersetup.jpg"
alt="User Setup" title="User Setup"
height="400" width="500"/>
</td></tr>
</table>
</div>

>> #### Fullscreen

> ### Setting up vim {#set_up_vim}

> ### Setting up Python {#set_up_python}

>> #### pip

>> #### virtualenv

>> #### kivy

>>> __Cython__

>>> __Pygame__

> ### Other Important Libraries {#other_libraries}

>> #### Git
