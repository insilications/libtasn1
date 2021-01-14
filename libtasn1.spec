#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libtasn1
Version  : 4.16.0
Release  : 41
URL      : http://mirrors.kernel.org/gnu/libtasn1/libtasn1-4.16.0.tar.gz
Source0  : http://mirrors.kernel.org/gnu/libtasn1/libtasn1-4.16.0.tar.gz
Summary  : Library for ASN.1 and DER manipulation
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+ LGPL-2.0+ LGPL-2.1
Requires: libtasn1-bin = %{version}-%{release}
Requires: libtasn1-info = %{version}-%{release}
Requires: libtasn1-lib = %{version}-%{release}
Requires: libtasn1-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : docbook-xml
BuildRequires : findutils
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkg-config
BuildRequires : texinfo
BuildRequires : valgrind
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
|Branch|CI system|Status|
|:----:|:-------:|-----:|
|Master|Gitlab|[![build status](https://gitlab.com/gnutls/libtasn1/badges/master/pipeline.svg)](https://gitlab.com/gnutls/libtasn1/commits/master)[![coverage report](https://gitlab.com/gnutls/libtasn1/badges/master/coverage.svg)](https://gnutls.gitlab.io/libtasn1/coverage)|

%package bin
Summary: bin components for the libtasn1 package.
Group: Binaries

%description bin
bin components for the libtasn1 package.


%package dev
Summary: dev components for the libtasn1 package.
Group: Development
Requires: libtasn1-lib = %{version}-%{release}
Requires: libtasn1-bin = %{version}-%{release}
Provides: libtasn1-devel = %{version}-%{release}
Requires: libtasn1 = %{version}-%{release}
Requires: libtasn1-dev = %{version}-%{release}
Requires: libtasn1-dev32 = %{version}-%{release}

%description dev
dev components for the libtasn1 package.


%package dev32
Summary: dev32 components for the libtasn1 package.
Group: Default
Requires: libtasn1-lib32 = %{version}-%{release}
Requires: libtasn1-bin = %{version}-%{release}
Requires: libtasn1-dev = %{version}-%{release}
Requires: libtasn1-dev32 = %{version}-%{release}

%description dev32
dev32 components for the libtasn1 package.


%package info
Summary: info components for the libtasn1 package.
Group: Default

%description info
info components for the libtasn1 package.


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


%package man
Summary: man components for the libtasn1 package.
Group: Default

%description man
man components for the libtasn1 package.


%package staticdev
Summary: staticdev components for the libtasn1 package.
Group: Default
Requires: libtasn1-dev = %{version}-%{release}
Requires: libtasn1-dev32 = %{version}-%{release}

%description staticdev
staticdev components for the libtasn1 package.


%package staticdev32
Summary: staticdev32 components for the libtasn1 package.
Group: Default
Requires: libtasn1-dev32 = %{version}-%{release}

%description staticdev32
staticdev32 components for the libtasn1 package.


%prep
%setup -q -n libtasn1-4.16.0
cd %{_builddir}/libtasn1-4.16.0
pushd ..
cp -a libtasn1-4.16.0 build32
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610593824
export GCC_IGNORE_WERROR=1
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fuse-ld=bfd -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe  -fPIC -fipa-pta -flto=16 -fno-plt -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -Wl,-O2 -Wl,-z,now -Wl,-z,relro -ffat-lto-objects -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fuse-ld=bfd -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe  -fPIC -fipa-pta -flto=16 -fno-plt -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -Wl,-O2 -Wl,-z,now -Wl,-z,relro -ffat-lto-objects -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_GEN"
export FFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fuse-ld=bfd -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe  -fPIC -fipa-pta -flto=16 -fno-plt -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -Wl,-O2 -Wl,-z,now -Wl,-z,relro -ffat-lto-objects -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fuse-ld=bfd -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe  -fPIC -fipa-pta -flto=16 -fno-plt -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -Wl,-O2 -Wl,-z,now -Wl,-z,relro -ffat-lto-objects -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fuse-ld=bfd -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe  -fPIC -fipa-pta -flto=16 -fno-plt -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -Wl,-O2 -Wl,-z,now -Wl,-z,relro -ffat-lto-objects -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_GEN"
#
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -malign-data=cacheline -feliminate-unused-debug-types -fno-lto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -pipe  -fPIC -fipa-pta -flto=16 -fno-plt -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -Wl,-O2 -Wl,-z,now -Wl,-z,relro -ffat-lto-objects -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_USE"
export FCFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -malign-data=cacheline -feliminate-unused-debug-types -fno-lto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -pipe  -fPIC -fipa-pta -flto=16 -fno-plt -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -Wl,-O2 -Wl,-z,now -Wl,-z,relro -ffat-lto-objects -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_USE"
export FFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -malign-data=cacheline -feliminate-unused-debug-types -fno-lto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -pipe  -fPIC -fipa-pta -flto=16 -fno-plt -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -Wl,-O2 -Wl,-z,now -Wl,-z,relro -ffat-lto-objects -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_USE"
export CXXFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -malign-data=cacheline -feliminate-unused-debug-types -fno-lto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -fvisibility-inlines-hidden -pipe  -fPIC -fipa-pta -flto=16 -fno-plt -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -Wl,-O2 -Wl,-z,now -Wl,-z,relro -ffat-lto-objects -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_USE"
export LDFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -malign-data=cacheline -feliminate-unused-debug-types -fno-lto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -pipe  -fPIC -fipa-pta -flto=16 -fno-plt -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -Wl,-O2 -Wl,-z,now -Wl,-z,relro -ffat-lto-objects -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_USE"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#
%global _lto_cflags 1
## altflags_pgo end
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
 %configure --enable-shared --enable-static
make  %{?_smp_mflags}  VERBOSE=1 V=1

make VERBOSE=1 V=1 %{?_smp_mflags} check || :
make clean
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%configure --enable-shared --enable-static
make  %{?_smp_mflags}  VERBOSE=1 V=1

pushd ../build32/
export CFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export CXXFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export LDFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --enable-shared --enable-static  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}  VERBOSE=1 V=1
popd

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
make %{?_smp_mflags} check || :
cd ../build32;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1610593824
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
/usr/include/libtasn1.h
/usr/lib64/libtasn1.so
/usr/lib64/pkgconfig/libtasn1.pc
/usr/share/man/man3/asn1_array2tree.3
/usr/share/man/man3/asn1_bit_der.3
/usr/share/man/man3/asn1_check_version.3
/usr/share/man/man3/asn1_copy_node.3
/usr/share/man/man3/asn1_create_element.3
/usr/share/man/man3/asn1_decode_simple_ber.3
/usr/share/man/man3/asn1_decode_simple_der.3
/usr/share/man/man3/asn1_delete_element.3
/usr/share/man/man3/asn1_delete_structure.3
/usr/share/man/man3/asn1_delete_structure2.3
/usr/share/man/man3/asn1_der_coding.3
/usr/share/man/man3/asn1_der_decoding.3
/usr/share/man/man3/asn1_der_decoding2.3
/usr/share/man/man3/asn1_der_decoding_element.3
/usr/share/man/man3/asn1_der_decoding_startEnd.3
/usr/share/man/man3/asn1_dup_node.3
/usr/share/man/man3/asn1_encode_simple_der.3
/usr/share/man/man3/asn1_expand_any_defined_by.3
/usr/share/man/man3/asn1_expand_octet_string.3
/usr/share/man/man3/asn1_find_node.3
/usr/share/man/man3/asn1_find_structure_from_oid.3
/usr/share/man/man3/asn1_get_bit_der.3
/usr/share/man/man3/asn1_get_length_ber.3
/usr/share/man/man3/asn1_get_length_der.3
/usr/share/man/man3/asn1_get_object_id_der.3
/usr/share/man/man3/asn1_get_octet_der.3
/usr/share/man/man3/asn1_get_tag_der.3
/usr/share/man/man3/asn1_length_der.3
/usr/share/man/man3/asn1_number_of_elements.3
/usr/share/man/man3/asn1_object_id_der.3
/usr/share/man/man3/asn1_octet_der.3
/usr/share/man/man3/asn1_parser2array.3
/usr/share/man/man3/asn1_parser2tree.3
/usr/share/man/man3/asn1_perror.3
/usr/share/man/man3/asn1_print_structure.3
/usr/share/man/man3/asn1_read_node_value.3
/usr/share/man/man3/asn1_read_tag.3
/usr/share/man/man3/asn1_read_value.3
/usr/share/man/man3/asn1_read_value_type.3
/usr/share/man/man3/asn1_strerror.3
/usr/share/man/man3/asn1_write_value.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libtasn1.so
/usr/lib32/pkgconfig/32libtasn1.pc
/usr/lib32/pkgconfig/libtasn1.pc

%files info
%defattr(0644,root,root,0755)
/usr/share/info/libtasn1.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtasn1.so.6
/usr/lib64/libtasn1.so.6.6.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libtasn1.so.6
/usr/lib32/libtasn1.so.6.6.0

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/asn1Coding.1
/usr/share/man/man1/asn1Decoding.1
/usr/share/man/man1/asn1Parser.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libtasn1.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libtasn1.a
