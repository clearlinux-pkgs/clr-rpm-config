#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v10
# autospec commit: 5905be9
#
Name     : clr-rpm-config
Version  : 273
Release  : 271
URL      : http://localhost/cgit/projects/clr-rpm-config/snapshot/clr-rpm-config-273.tar.xz
Source0  : http://localhost/cgit/projects/clr-rpm-config/snapshot/clr-rpm-config-273.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: clr-rpm-config-license = %{version}-%{release}
Requires: clr-avx-tools
Requires: clr-python-timestamp
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package license
Summary: license components for the clr-rpm-config package.
Group: Default

%description license
license components for the clr-rpm-config package.


%prep
%setup -q -n clr-rpm-config-273
cd %{_builddir}/clr-rpm-config-273
pushd ..
cp -a clr-rpm-config-273 buildavx2
popd
pushd ..
cp -a clr-rpm-config-273 buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713543458
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make  %{?_smp_mflags}

pushd ../buildavx2
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
make  %{?_smp_mflags}
popd
pushd ../buildapx
GOAMD64=v3
CC=gcc-14
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -mapxf -mavx10.1 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1713543458
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-rpm-config
cp %{_builddir}/clr-rpm-config-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/clr-rpm-config/4cc77b90af91e615a64ae04893fdffa7939db84c || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v3
pushd ../buildapx/
%make_install_va
popd
GOAMD64=v2
%make_install
## install_append content
mkdir -p %{buildroot}/usr/lib/rpm
ln -s clr %{buildroot}/usr/lib/rpm/unknown
ln -s clr %{buildroot}/usr/lib/rpm/generic
ln -s clr %{buildroot}/usr/lib/rpm/redhat
ln -s clr %{buildroot}/usr/lib/rpm/koji
ln -s clr %{buildroot}/usr/lib/rpm/pc
rm -f %{buildroot}/usr/lib/rpm/clr/perl.prov
ln -s /usr/lib/rpm/perl.prov %{buildroot}/usr/lib/rpm/clr/perl.prov
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib/rpm/clr/LICENSE
/usr/lib/rpm/clr/VERSION
/usr/lib/rpm/clr/brp-compress
/usr/lib/rpm/clr/brp-create-abi
/usr/lib/rpm/clr/brp-implant-ident-static
/usr/lib/rpm/clr/brp-java-repack-jars
/usr/lib/rpm/clr/brp-python-bytecompile
/usr/lib/rpm/clr/brp-python-hardlink
/usr/lib/rpm/clr/brp-redhat
/usr/lib/rpm/clr/brp-remove-python-pyo
/usr/lib/rpm/clr/brp-set-epoch-timestamp
/usr/lib/rpm/clr/brp-sparc64-linux
/usr/lib/rpm/clr/brp-strip
/usr/lib/rpm/clr/brp-strip-comment-note
/usr/lib/rpm/clr/brp-strip-static-archive
/usr/lib/rpm/clr/brp-strip-static-lto
/usr/lib/rpm/clr/cmake.prov
/usr/lib/rpm/clr/config.guess
/usr/lib/rpm/clr/config.sub
/usr/lib/rpm/clr/dist.sh
/usr/lib/rpm/clr/find-provides
/usr/lib/rpm/clr/find-provides.d/firmware.prov
/usr/lib/rpm/clr/find-provides.d/modalias.prov
/usr/lib/rpm/clr/find-provides.debuginfo
/usr/lib/rpm/clr/find-provides.ksyms
/usr/lib/rpm/clr/find-provides.libtool
/usr/lib/rpm/clr/find-provides.pkgconfig
/usr/lib/rpm/clr/find-requires
/usr/lib/rpm/clr/find-requires.ksyms
/usr/lib/rpm/clr/find-requires.libtool
/usr/lib/rpm/clr/find-requires.pkgconfig
/usr/lib/rpm/clr/macros
/usr/lib/rpm/clr/mvn.prov
/usr/lib/rpm/clr/perl.prov
/usr/lib/rpm/clr/perl.req
/usr/lib/rpm/clr/rpmrc
/usr/lib/rpm/clr/rpmsort
/usr/lib/rpm/clr/so_symlink.req
/usr/lib/rpm/clr/symset-table
/usr/lib/rpm/fileattrs/cmake.attr
/usr/lib/rpm/fileattrs/elfoptimized.attr
/usr/lib/rpm/fileattrs/mingw.attr
/usr/lib/rpm/fileattrs/mvn.attr
/usr/lib/rpm/fileattrs/openmpi.attr
/usr/lib/rpm/fileattrs/perl.attr
/usr/lib/rpm/fileattrs/so_symlink.attr
/usr/lib/rpm/generic
/usr/lib/rpm/koji
/usr/lib/rpm/pc
/usr/lib/rpm/redhat
/usr/lib/rpm/unknown

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-rpm-config/4cc77b90af91e615a64ae04893fdffa7939db84c
