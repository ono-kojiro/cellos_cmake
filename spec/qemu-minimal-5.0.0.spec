%global debug_package %{nil}

%define name qemu
%define version 5.0.0

Name: %{name}
Epoch: 1
Version: %{version}
Release: 1%{?dist}
Summary: qemu

Group: Development/Tools
License: GPL
URL: http://qemu.org/
Source0: http://wiki.qemu-project.org/download/qemu-%{version}.tar.xz

%global have_rbd 0


BuildRequires: gcc zlib-devel ncurses-devel glib2-devel libssh-devel curl-devel
BuildRequires: pixman-devel >= 0.21.8
Requires: zlib ncurses glib2 libssh

%description
QEMU

### common ###
%package common
Summary: QEMU common files needed by all QEMU targets
Group: Development/Tools

%description common
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the common files needed by all QEMU targets

%package guest-agent
Summary: QEMU guest agent
Group: System Environment/Daemons
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description guest-agent
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides an agent to run inside guests, which communicates
with the host over a virtio-serial channel named "org.qemu.guest_agent.0"

This package does not need to be installed on the host OS.

### img ###
%package img
Summary: QEMU command line tool for manipulating disk images
Group: Development/Tools

%description img
This package provides a command line tool for manipulating disk images

###
%package -n ivshmem-tools
Summary: Client and server for QEMU ivshmem device
Group: Development/Tools

%description -n ivshmem-tools
This package provides client and server tools for QEMU's ivshmem device.

###
%package system-x86
Summary: QEMU system emulator for x86
Group: Development/Tools

%description system-x86
qemu for x86

%package system-ppc
Summary: QEMU system emulator for PPC
Requires: %{name}-system-ppc-core = %{epoch}:%{version}-%{release}
#%{requires_all_block_modules}

%description system-ppc
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for PPC and PPC64 systems.

%package system-ppc-core
Summary: QEMU system emulator for PPC
Requires: %{name}-common = %{epoch}:%{version}-%{release}

%description system-ppc-core
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for PPC and PPC64 systems.

%prep
%setup -q -n %{name}-%{version}

%build
		
# --cross-prefix=x86_64-w64-mingw32-

run_configure() {
	sh ../configure \
		--prefix=%{_prefix} \
		--libdir=%{_libdir} \
		--sysconfdir=%{_sysconfdir} \
		--disable-user \
		--disable-linux-user \
		--disable-bsd-user \
		--disable-docs \
		--disable-sdl \
		--enable-curl \
		--enable-curses \
		--disable-smartcard \
		--python=/usr/bin/python3 \
		"$@"
}

mkdir -p build-qemu
pushd build-qemu
run_configure \
	--target-list="ppc-softmmu,ppc64-softmmu"

	#--target-list="i386-softmmu,arm-softmmu,ppceabi-softmmu"

make %{?_smp_mflags}
popd

%install
pushd build-qemu
make install DESTDIR=%{buildroot}

# Provided by package openbios
#rm -rf %{buildroot}%{_datadir}/%{name}/openbios-ppc
rm -rf %{buildroot}%{_datadir}/%{name}/openbios-sparc32
rm -rf %{buildroot}%{_datadir}/%{name}/openbios-sparc64
# Provided by package SLOF
rm -rf %{buildroot}%{_datadir}/%{name}/slof.bin
# Provided by package ipxe
rm -rf %{buildroot}%{_datadir}/%{name}/pxe*rom
rm -rf %{buildroot}%{_datadir}/%{name}/efi*rom
# Provided by package seavgabios
rm -rf %{buildroot}%{_datadir}/%{name}/vgabios*bin
# Provided by package s390
rm -rf %{buildroot}%{_datadir}/%{name}/s390*.img

# Provided by system-microblaze-core
rm -rf %{buildroot}%{_datadir}/%{name}/petalogix*.dtb

# Provided by system-alpha-core
rm -rf %{buildroot}%{_datadir}/%{name}/palcode-clipper

# Provided by system-ppc-core
#rm -rf %{buildroot}%{_datadir}/%{name}/ppc_rom.bin

rm -rf %{buildroot}%{_datadir}/%{name}/QEMU,cgthree.bin
rm -rf %{buildroot}%{_datadir}/%{name}/QEMU,tcx.bin
rm -rf %{buildroot}%{_datadir}/%{name}/trace-events-all

popd

%files
# Deliberately empty

%files common
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/keymaps/
%{_datadir}/applications/qemu.desktop
%{_datadir}/icons/hicolor/*
%attr(4755, root, root) %{_libexecdir}/qemu-bridge-helper

%files guest-agent
%{_bindir}/qemu-ga

%files img
%{_bindir}/qemu-img
%{_bindir}/qemu-io
%{_bindir}/qemu-nbd

%files -n ivshmem-tools
%{_bindir}/ivshmem-client
%{_bindir}/ivshmem-server

%files system-x86
%{_bindir}/*
%{_datadir}/%{name}/bios.bin
%{_datadir}/%{name}/bios-256k.bin
%{_datadir}/%{name}/sgabios.bin
%{_datadir}/%{name}/linuxboot.bin
%{_datadir}/%{name}/linuxboot_dma.bin
%{_datadir}/%{name}/multiboot.bin
%{_datadir}/%{name}/kvmvapic.bin

%files system-ppc
# Deliberately empty

%files system-ppc-core
%{_bindir}/qemu-system-ppc
%{_bindir}/qemu-system-ppc64
%{_datadir}/%{name}/bamboo.dtb
%{_datadir}/%{name}/bios-microvm.bin
%{_datadir}/%{name}/canyonlands.dtb
%{_datadir}/%{name}/hppa-firmware.img
%{_datadir}/%{name}/edk2-*
%{_datadir}/%{name}/firmware/*.json
%{_datadir}/%{name}/openbios-ppc
%{_datadir}/%{name}/opensbi-*.bin
%{_datadir}/%{name}/pvh.bin
%{_datadir}/%{name}/qemu-nsis.bmp
%{_datadir}/%{name}/qemu_vga.ndrv
%{_datadir}/%{name}/skiboot.lid
%{_datadir}/%{name}/u-boot.e500
%{_datadir}/%{name}/u-boot-sam460-20100605.bin
%ifarch %{power64}
%{_sysconfdir}/security/limits.d/95-kvm-ppc64-memlock.conf
%endif

