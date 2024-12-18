# Flet - Getting Started

Marcus Zou

## Resource

- http://flet.dev/
- https://github.com/flet-dev/flet

## Setup

Very simple to setup a Flet env as below:

```shell
mkdir flet-proj
cd flet-proj

python -m venv venv
source venv/bin activate
pip install --upgrade pip

pip install flet
# pip install -r requirements.txt
```

## More Setups may be needed Sometimes

Test run a Flet counter app (as per the Flet templates):

```shell
flet create counter
flet run counter
```

Then you may encounter 2 types of complaints:

Complaint #1:

> error while loading shared libraries: libgstapp-1.0.so.0: cannot open shared object file: No such file or directory

Complaint #2:

> error while loading shared libraries: libmpv.so.1: cannot open shared object file: No such file or directory

- When running Flet app in Windows 11/10, there will be no issue!

- When running Flet project in WSL2/Ubuntu distros, you will encounter the 2 complaints above, then -

```shell
sudo apt install libgstreamer-plugins-base1.0-0

sudo apt install libmpv-dev libmpv2
sudo ln -s /usr/lib/x86_64-linux-gnu/libmpv.so /usr/lib/libmpv.so.1
```

- When running Flet app in Debian/Ubuntu-based Linux, you will encounter Complaint #2, then -

```shell
sudo apt install libmpv-dev libmpv2
sudo ln -s /usr/lib/x86_64-linux-gnu/libmpv.so /usr/lib/libmpv.so.1
```

- When running Flet project in Red Hat (Alma, Rocky, Fedora, Oracle) Linux, It normally present the Complaint #2 as described above, then -

```shell
## Run the command to install the packages:
sudo dnf install mpv-libs
sudo dnf install mpv-devel

## Searching the packages on directory
cd /usr/lib64

## Searching the mpv
find *mpv*

## The answer must be:
## libmpv.so 
## libmpv.so.2 
## libmpv.so.2.1.0 

## Creating a symbolic link
sudo ln -s /usr/lib64/libmpv.so /usr/lib64/libmpv.so.1
```

## Run the Demo Projects

There are only 2 template-based projects: `counter` and `minimal`. actually they are same.

```shell
# flet create counter
flet run counter
```

## The End
