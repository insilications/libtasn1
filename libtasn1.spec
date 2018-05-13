#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9D5EAAF69013B842 (nmav@gnutls.org)
#
Name     : libtasn1
Version  : 4.13
Release  : 30
URL      : https://ftp.gnu.org/gnu/libtasn1/libtasn1-4.13.tar.gz
Source0  : https://ftp.gnu.org/gnu/libtasn1/libtasn1-4.13.tar.gz
Source99 : https://ftp.gnu.org/gnu/libtasn1/libtasn1-4.13.tar.gz.sig
Summary  : Library for ASN.1 and DER manipulation
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+ LGPL-2.0+ LGPL-2.1
Requires: libtasn1-bin
Requires: libtasn1-lib
Requires: libtasn1-doc
BuildRequires : bison
BuildRequires : docbook-xml
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : valgrind

%description
This is GNU Libtasn1, a small ASN.1 library.
The C library (libtasn1.*) is licensed under the GNU Lesser General
Public License version 2.1 or later.  See the file COPYING.LIB.

%package bin
Summary: bin components for the libtasn1 package.
Group: Binaries

%description bin
bin components for the libtasn1 package.


%package dev
Summary: dev components for the libtasn1 package.
Group: Development
Requires: libtasn1-lib
Requires: libtasn1-bin
Provides: libtasn1-devel

%description dev
dev components for the libtasn1 package.


%package dev32
Summary: dev32 components for the libtasn1 package.
Group: Default
Requires: libtasn1-lib32
Requires: libtasn1-bin
Requires: libtasn1-dev

%description dev32
dev32 components for the libtasn1 package.


%package doc
Summary: doc components for the libtasn1 package.
Group: Documentation

%description doc
doc components for the libtasn1 package.


%package lib
Summary: lib components for the libtasn1 package.
Group: Libraries

%description lib
lib components for the libtasn1 package.


%package lib32
Summary: lib32 components for the libtasn1 package.
Group: Default

%description lib32
lib32 components for the libtasn1 package.


%prep
%setup -q -n libtasn1-4.13
pushd ..
cp -a libtasn1-4.13 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526171539
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1526171539
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/asn1Coding
/usr/bin/asn1Decoding
/usr/bin/asn1Parser

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libtasn1.so
/usr/lib64/pkgconfig/libtasn1.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libtasn1.so
/usr/lib32/pkgconfig/32libtasn1.pc
/usr/lib32/pkgconfig/libtasn1.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtasn1.so.6
/usr/lib64/libtasn1.so.6.5.5

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libtasn1.so.6
/usr/lib32/libtasn1.so.6.5.5
