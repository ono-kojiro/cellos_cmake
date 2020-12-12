# FORCE NOARCH
# This package is noarch intentionally, although it supplies binaries,
# as they're not intended for the build platform, but for ARM.
# The related discussion can be found here:
# https://www.redhat.com/archives/fedora-devel-list/2009-February/msg02261.html
%global _binaries_in_noarch_packages_terminate_build 0

%global __os_install_post /usr/lib/rpm/brp-compress

%global target powerpc-none-eabi
%global pkg_version 3.1.0

%global build_nano 1

Name:           %{target}-newlib
Version:        3.1.0
Release:        5%{?dist}
Summary:        C library intended for use on %{target} embedded systems
# For a breakdown of the licensing, see NEWLIB-LICENSING
License:        BSD and MIT and LGPLv2+ and ISC
URL:            http://sourceware.org/newlib/
Source0:        ftp://sourceware.org/pub/newlib/newlib-%{pkg_version}.tar.gz
Source1:        README.fedora
Source2:        NEWLIB-LICENSING

BuildRequires:  gcc
BuildRequires:  %{target}-binutils %{target}-gcc %{target}-gcc-c++ texinfo texinfo-tex
BuildArch:      noarch

%description
Newlib is a C library intended for use on embedded systems. It is a
conglomeration of several library parts, all under free software licenses
that make them easily usable on embedded products.

%prep
%setup -q -n newlib-%{pkg_version}

%build
rm -rf build-{newlib,nano}
mkdir build-{newlib,nano}

pushd build-newlib

export CFLAGS_FOR_TARGET="-mbig-endian"
export AR_FOR_TARGET="%{target}-gcc-ar"
export RANLIB_FOR_TARGET="%{target}-gcc-ranlib"

../configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --htmldir=%{_docdir}/html \
    --pdfdir=%{_docdir}/pdf \
    --target=%{target} \
    --disable-multilib \
	--disable-newlib-io-float \
	--disable-newlib-io-long-double \
	--enable-newlib-supplied-syscalls \
	--disable-newlib-io-pos-args \
	--disable-newlib-io-c99-formats \
	--disable-newlib-io-long-long \
	--disable-newlib-register-fini \
	--disable-newlib-nano-malloc \
	--disable-newlib-nano-formatted-io \
	--enable-newlib-atexit-dynamic-alloc \
	--disable-newlib-global-atexit \
	--disable-lite-exit \
	--disable-newlib-reent-small \
	--enable-newlib-multithread \
	--enable-newlib-wide-orient \
	--enable-newlib-unbuf-stream-opt \
	--enable-target-optspace \
    --disable-nls 
    
make %{?_smp_mflags}

%if %{build_nano}
popd
pushd build-nano
export CFLAGS_FOR_TARGET="-g -Os -ffunction-sections -fdata-sections"
../configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --target=%{target} \
    --disable-newlib-supplied-syscalls    \
    --enable-newlib-reent-small           \
    --disable-newlib-fvwrite-in-streamio  \
    --disable-newlib-fseek-optimization   \
    --disable-newlib-wide-orient          \
    --enable-newlib-nano-malloc           \
    --disable-newlib-unbuf-stream-opt     \
    --enable-lite-exit                    \
    --enable-newlib-global-atexit         \
    --enable-newlib-nano-formatted-io     \
    --disable-nls

make %{?_smp_mflags}

popd
%endif

%install
pushd build-newlib
make install DESTDIR=%{buildroot}
popd

%if %{build_nano}
pushd build-nano
NANO_ROOT=%{buildroot}/nano
make install DESTDIR=$NANO_ROOT

for i in $(find $NANO_ROOT -regex ".*/lib\(c\|g\|rdimon\)\.a"); do
    echo INFO : file is $i
	echo INFO : `file $i`
    file=$(basename $i | sed "s|\.a|_nano\.a|")
    target_path=$(dirname $i | sed "s|$NANO_ROOT||")
    cp $i "%{buildroot}$target_path/$file"
done
mkdir -p %{buildroot}/usr/powerpc-none-eabi/include/newlib-nano/
cp -p $NANO_ROOT/usr/powerpc-none-eabi/include/newlib.h %{buildroot}/usr/powerpc-none-eabi/include/newlib-nano/newlib.h
popd
%endif

cp %{SOURCE1} .
cp %{SOURCE2} .

# we don't want these as we are a cross version
rm -rf %{buildroot}%{_infodir}

rm -rf $NANO_ROOT
%if 0
# despite us being noarch redhat-rpm-config insists on stripping our files
%if %{fedora}0 > 200
%global __os_install_post /usr/lib/rpm/brp-compress
%else
%global __os_install_post /usr/lib/rpm/redhat/brp-compress
%endif
%endif

%files
%doc README.fedora
%license NEWLIB-LICENSING COPYING*
%dir %{_prefix}/%{target}
%dir %{_prefix}/%{target}/include/
%{_prefix}/%{target}/include/*
%dir %{_prefix}/%{target}/lib
%{_prefix}/%{target}/lib/*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 02 2019 Michal Hlavinka <mhlavink@redhat.com> - 3.1.0-3
- rebuild with gcc 9.2.0

* Mon Mar 11 2019 Michal Hlavinka <mhlavink@redhat.com> - 3.1.0-2
- add nano version of newlib.h

* Fri Mar 08 2019 Michal Hlavinka <mhlavink@redhat.com> - 3.1.0-0
- updated to 3.1.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 06 2018 Michal Hlavinka <mhlavink@redhat.com> - 3.0.0-2
- updated to 3.0.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Michal Hlavinka <mhlavink@redhat.com> - 2.5.0-2
- make sure -Os flags are used for nano version (#1443512)

* Fri Jun 23 2017 Michal Hlavinka <mhlavink@redhat.com> - 2.5.0-1
- updated to 2.5.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 13 2016 Michal Hlavinka <mhlavink@redhat.com> - 2.4.0-8
- bump release and rebuild

* Thu Jun 30 2016 Michal Hlavinka <mhlavink@redhat.com> - 2.4.0-7
- updated to 2.4.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0_1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 02 2015 Michal Hlavinka <mhlavink@redhat.com> - 2.2.0_1-6
- bump release and rebuild

* Wed Sep 02 2015 Michal Hlavinka <mhlavink@redhat.com> - 2.2.0_1-5
- add --enable-newlib-io-long-long configure option

* Mon Aug 31 2015 Michal Hlavinka <mhlavink@redhat.com> - 2.2.0_1-4
- added nano versions of libraries
- cleaned up spec file
- credits: Johnny Robeson

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0_1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 01 2015 Michal Hlavinka <mhlavink@redhat.com> - 2.2.0_1-2
- rebuild for gcc 5.1

* Tue Apr 14 2015 Michal Hlavinka <mhlavink@redhat.com> - 2.2.0_1-1
- newlib updated to 2.2.0_1

* Mon Jun 09 2014 Michal Hlavinka <mhlavink@redhat.com> - 2.1.0-5
- fix FTBFS (#1105970)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 25 2014 Michal Hlavinka <mhlavink@redhat.com> - 2.1.0-3
- enable libnosys (#1060567,#1058722)

* Tue Jan 14 2014 Michal Hlavinka <mhlavink@redhat.com> - 2.1.0-2
- rebuild with newer arm-none-eabi-gcc

* Wed Jan 08 2014 Michal Hlavinka <mhlavink@redhat.com> - 2.1.0-1
- initial import
