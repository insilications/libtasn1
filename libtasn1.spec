#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libtasn1
Version  : 4.8
Release  : 15
URL      : http://ftp.gnu.org/gnu/libtasn1/libtasn1-4.8.tar.gz
Source0  : http://ftp.gnu.org/gnu/libtasn1/libtasn1-4.8.tar.gz
Summary  : Library for ASN.1 and DER manipulation
Group    : Development/Tools
License  : GFDL-1.3 GPL-3.0 GPL-3.0+ LGPL-2.0+ LGPL-2.1
Requires: libtasn1-bin
Requires: libtasn1-lib
Requires: libtasn1-doc
BuildRequires : bison
BuildRequires : docbook-xml
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


%prep
cd ..
%setup -q -n libtasn1-4.8

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
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
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
