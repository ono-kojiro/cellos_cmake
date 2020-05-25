%global debug_package %{nil}

%define name qemu
%define version 4.2.0

Name: %{name}
Epoch: 1
Version: %{version}
Release: 1%{?dist}
Summary: qemu

Group: Development/Tools
License: GPL
URL: http://qemu.org/
Source0: http://wiki.qemu-project.org/download/qemu-%{version}.tar.xz

# guest agent service
Source10: qemu-guest-agent.service
Source17: qemu-ga.sysconfig
# guest agent udev rules
Source11: 99-qemu-guest-agent.rules
# /etc/qemu/bridge.conf
Source12: bridge.conf
# qemu-kvm back compat wrapper installed as /usr/bin/qemu-kvm
Source13: qemu-kvm.sh
# PR manager service
Source14: qemu-pr-helper.service
Source15: qemu-pr-helper.socket
# /etc/modprobe.d/kvm.conf, for x86
Source20: kvm-x86.modprobe.conf
# /etc/security/limits.d/95-kvm-ppc64-memlock.conf
Source21: 95-kvm-ppc64-memlock.conf

# Fix a test suite error
Patch0001: 0001-tests-fix-modules-test-duplicate-test-case-error.patch
# Miscellaneous fixes for RISC-V
Patch0002: 0002-riscv-sifive_u-fix-a-memory-leak-in-soc_realize.patch
Patch0003: 0003-riscv-Set-xPIE-to-1-after-xRET.patch
Patch0004: 0004-target-riscv-Fix-tb-flags-FS-status.patch
Patch0005: 0005-target-riscv-fsd-fsw-doesn-t-dirty-FP-state.patch
Patch0006: 0006-target-riscv-update-mstatus.SD-when-FS-is-set-dirty.patch
# virtio-fs support
Patch0007: 0007-virtio-fs-fix-MSI-X-nvectors-calculation.patch
Patch0008: 0008-vhost-user-fs-remove-vhostfd-property.patch
Patch0009: 0009-build-rename-CONFIG_LIBCAP-to-CONFIG_LIBCAP_NG.patch
Patch0010: 0010-virtiofsd-Pull-in-upstream-headers.patch
Patch0011: 0011-virtiofsd-Pull-in-kernel-s-fuse.h.patch
Patch0012: 0012-virtiofsd-Add-auxiliary-.c-s.patch
Patch0013: 0013-virtiofsd-Add-fuse_lowlevel.c.patch
Patch0014: 0014-virtiofsd-Add-passthrough_ll.patch
Patch0015: 0015-virtiofsd-Trim-down-imported-files.patch
Patch0016: 0016-virtiofsd-Format-imported-files-to-qemu-style.patch
Patch0017: 0017-virtiofsd-remove-mountpoint-dummy-argument.patch
Patch0018: 0018-virtiofsd-remove-unused-notify-reply-support.patch
Patch0019: 0019-virtiofsd-Remove-unused-enum-fuse_buf_copy_flags.patch
Patch0020: 0020-virtiofsd-Fix-fuse_daemonize-ignored-return-values.patch
Patch0021: 0021-virtiofsd-Fix-common-header-and-define-for-QEMU-buil.patch
Patch0022: 0022-virtiofsd-Trim-out-compatibility-code.patch
Patch0023: 0023-vitriofsd-passthrough_ll-fix-fallocate-ifdefs.patch
Patch0024: 0024-virtiofsd-Make-fsync-work-even-if-only-inode-is-pass.patch
Patch0025: 0025-virtiofsd-Add-options-for-virtio.patch
Patch0026: 0026-virtiofsd-add-o-source-PATH-to-help-output.patch
Patch0027: 0027-virtiofsd-Open-vhost-connection-instead-of-mounting.patch
Patch0028: 0028-virtiofsd-Start-wiring-up-vhost-user.patch
Patch0029: 0029-virtiofsd-Add-main-virtio-loop.patch
Patch0030: 0030-virtiofsd-get-set-features-callbacks.patch
Patch0031: 0031-virtiofsd-Start-queue-threads.patch
Patch0032: 0032-virtiofsd-Poll-kick_fd-for-queue.patch
Patch0033: 0033-virtiofsd-Start-reading-commands-from-queue.patch
Patch0034: 0034-virtiofsd-Send-replies-to-messages.patch
Patch0035: 0035-virtiofsd-Keep-track-of-replies.patch
Patch0036: 0036-virtiofsd-Add-Makefile-wiring-for-virtiofsd-contrib.patch
Patch0037: 0037-virtiofsd-Fast-path-for-virtio-read.patch
Patch0038: 0038-virtiofsd-add-fd-FDNUM-fd-passing-option.patch
Patch0039: 0039-virtiofsd-make-f-foreground-the-default.patch
Patch0040: 0040-virtiofsd-add-vhost-user.json-file.patch
Patch0041: 0041-virtiofsd-add-print-capabilities-option.patch
Patch0042: 0042-virtiofs-Add-maintainers-entry.patch
Patch0043: 0043-virtiofsd-passthrough_ll-create-new-files-in-caller-.patch
Patch0044: 0044-virtiofsd-passthrough_ll-add-lo_map-for-ino-fh-indir.patch
Patch0045: 0045-virtiofsd-passthrough_ll-add-ino_map-to-hide-lo_inod.patch
Patch0046: 0046-virtiofsd-passthrough_ll-add-dirp_map-to-hide-lo_dir.patch
Patch0047: 0047-virtiofsd-passthrough_ll-add-fd_map-to-hide-file-des.patch
Patch0048: 0048-virtiofsd-passthrough_ll-add-fallback-for-racy-ops.patch
Patch0049: 0049-virtiofsd-validate-path-components.patch
Patch0050: 0050-virtiofsd-Plumb-fuse_bufvec-through-to-do_write_buf.patch
Patch0051: 0051-virtiofsd-Pass-write-iov-s-all-the-way-through.patch
Patch0052: 0052-virtiofsd-add-fuse_mbuf_iter-API.patch
Patch0053: 0053-virtiofsd-validate-input-buffer-sizes-in-do_write_bu.patch
Patch0054: 0054-virtiofsd-check-input-buffer-size-in-fuse_lowlevel.c.patch
Patch0055: 0055-virtiofsd-prevent-.-escape-in-lo_do_lookup.patch
Patch0056: 0056-virtiofsd-prevent-.-escape-in-lo_do_readdir.patch
Patch0057: 0057-virtiofsd-use-proc-self-fd-O_PATH-file-descriptor.patch
Patch0058: 0058-virtiofsd-sandbox-mount-namespace.patch
Patch0059: 0059-virtiofsd-move-to-an-empty-network-namespace.patch
Patch0060: 0060-virtiofsd-move-to-a-new-pid-namespace.patch
Patch0061: 0061-virtiofsd-add-seccomp-whitelist.patch
Patch0062: 0062-virtiofsd-Parse-flag-FUSE_WRITE_KILL_PRIV.patch
Patch0063: 0063-virtiofsd-cap-ng-helpers.patch
Patch0064: 0064-virtiofsd-Drop-CAP_FSETID-if-client-asked-for-it.patch
Patch0065: 0065-virtiofsd-set-maximum-RLIMIT_NOFILE-limit.patch
Patch0066: 0066-virtiofsd-fix-libfuse-information-leaks.patch
Patch0067: 0067-virtiofsd-add-syslog-command-line-option.patch
Patch0068: 0068-virtiofsd-print-log-only-when-priority-is-high-enoug.patch
Patch0069: 0069-virtiofsd-Add-ID-to-the-log-with-FUSE_LOG_DEBUG-leve.patch
Patch0070: 0070-virtiofsd-Add-timestamp-to-the-log-with-FUSE_LOG_DEB.patch
Patch0071: 0071-virtiofsd-Handle-reinit.patch
Patch0072: 0072-virtiofsd-Handle-hard-reboot.patch
Patch0073: 0073-virtiofsd-Kill-threads-when-queues-are-stopped.patch
Patch0074: 0074-vhost-user-Print-unexpected-slave-message-types.patch
Patch0075: 0075-contrib-libvhost-user-Protect-slave-fd-with-mutex.patch
Patch0076: 0076-virtiofsd-passthrough_ll-add-renameat2-support.patch
Patch0077: 0077-virtiofsd-passthrough_ll-disable-readdirplus-on-cach.patch
Patch0078: 0078-virtiofsd-passthrough_ll-control-readdirplus.patch
Patch0079: 0079-virtiofsd-rename-unref_inode-to-unref_inode_lolocked.patch
Patch0080: 0080-virtiofsd-fail-when-parent-inode-isn-t-known-in-lo_d.patch
Patch0081: 0081-virtiofsd-extract-root-inode-init-into-setup_root.patch
Patch0082: 0082-virtiofsd-passthrough_ll-clean-up-cache-related-opti.patch
Patch0083: 0083-virtiofsd-passthrough_ll-use-hashtable.patch
Patch0084: 0084-virtiofsd-Clean-up-inodes-on-destroy.patch
Patch0085: 0085-virtiofsd-support-nanosecond-resolution-for-file-tim.patch
Patch0086: 0086-virtiofsd-fix-error-handling-in-main.patch
Patch0087: 0087-virtiofsd-cleanup-allocated-resource-in-se.patch
Patch0088: 0088-virtiofsd-fix-memory-leak-on-lo.source.patch
Patch0089: 0089-virtiofsd-add-helper-for-lo_data-cleanup.patch
Patch0090: 0090-virtiofsd-Prevent-multiply-running-with-same-vhost_u.patch
Patch0091: 0091-virtiofsd-enable-PARALLEL_DIROPS-during-INIT.patch
Patch0092: 0092-virtiofsd-fix-incorrect-error-handling-in-lo_do_look.patch
Patch0093: 0093-Virtiofsd-fix-memory-leak-on-fuse-queueinfo.patch
Patch0094: 0094-virtiofsd-Support-remote-posix-locks.patch
Patch0095: 0095-virtiofsd-use-fuse_lowlevel_is_virtio-in-fuse_sessio.patch
Patch0096: 0096-virtiofsd-prevent-fv_queue_thread-vs-virtio_loop-rac.patch
Patch0097: 0097-virtiofsd-make-lo_release-atomic.patch
Patch0098: 0098-virtiofsd-prevent-races-with-lo_dirp_put.patch
Patch0099: 0099-virtiofsd-rename-inode-refcount-to-inode-nlookup.patch
Patch0100: 0100-libvhost-user-Fix-some-memtable-remap-cases.patch
Patch0101: 0101-virtiofsd-passthrough_ll-fix-refcounting-on-remove-r.patch
Patch0102: 0102-virtiofsd-introduce-inode-refcount-to-prevent-use-af.patch
Patch0103: 0103-virtiofsd-do-not-always-set-FUSE_FLOCK_LOCKS.patch
Patch0104: 0104-virtiofsd-convert-more-fprintf-and-perror-to-use-fus.patch
Patch0105: 0105-virtiofsd-Reset-O_DIRECT-flag-during-file-open.patch
Patch0106: 0106-virtiofsd-Fix-data-corruption-with-O_APPEND-write-in.patch
Patch0107: 0107-virtiofsd-passthrough_ll-Use-cache_readdir-for-direc.patch
Patch0108: 0108-virtiofsd-add-definition-of-fuse_buf_writev.patch
Patch0109: 0109-virtiofsd-use-fuse_buf_writev-to-replace-fuse_buf_wr.patch
Patch0110: 0110-virtiofsd-process-requests-in-a-thread-pool.patch
Patch0111: 0111-virtiofsd-prevent-FUSE_INIT-FUSE_DESTROY-races.patch
Patch0112: 0112-virtiofsd-fix-lo_destroy-resource-leaks.patch
Patch0113: 0113-virtiofsd-add-thread-pool-size-NUM-option.patch
Patch0114: 0114-virtiofsd-Convert-lo_destroy-to-take-the-lo-mutex-lo.patch
Patch0115: 0115-virtiofsd-passthrough_ll-Pass-errno-to-fuse_reply_er.patch
Patch0116: 0116-virtiofsd-stop-all-queue-threads-on-exit-in-virtio_l.patch
Patch0117: 0117-virtiofsd-add-some-options-to-the-help-message.patch
# Fix segfault with SR-IOV hot-{plug,unplug}
Patch0118: 0118-vfio-pci-Don-t-remove-irqchip-notifier-if-not-regist.patch

# Fix ppc shutdown issue (bz #1784961)
Patch0201: 0201-spapr-Don-t-trigger-a-CAS-reboot-for-XICS-XIVE-mode-.patch

%global have_rbd 0


BuildRequires: gcc zlib-devel ncurses-devel glib2-devel libssh-devel curl-devel
BuildRequires: bzip2-devel libxml2-devel
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
%autopatch -p1

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
%{_datadir}/%{name}/ppc_rom.bin
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

