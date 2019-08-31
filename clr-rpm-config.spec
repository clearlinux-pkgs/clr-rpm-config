#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-rpm-config
Version  : 210
Release  : 210
URL      : http://localhost/cgit/projects/clr-rpm-config/snapshot/clr-rpm-config-210.tar.xz
Source0  : http://localhost/cgit/projects/clr-rpm-config/snapshot/clr-rpm-config-210.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: clr-rpm-config-license = %{version}-%{release}
Requires: clr-avx-tools
Requires: clr-python-timestamp
BuildRequires : clr-avx-tools
BuildRequires : clr-python-timestamp

%description
No detailed description available

%package license
Summary: license components for the clr-rpm-config package.
Group: Default

%description license
license components for the clr-rpm-config package.


%prep
%setup -q -n clr-rpm-config-210

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567279127
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1567279127
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-rpm-config
cp LICENSE %{buildroot}/usr/share/package-licenses/clr-rpm-config/LICENSE
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
/usr/lib/rpm/clr/brp-sparc64-linux
/usr/lib/rpm/clr/brp-strip
/usr/lib/rpm/clr/brp-strip-comment-note
/usr/lib/rpm/clr/brp-strip-shared
/usr/lib/rpm/clr/brp-strip-static-archive
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
/usr/lib/rpm/clr/symset-table
/usr/lib/rpm/fileattrs/cmake.attr
/usr/lib/rpm/fileattrs/mvn.attr
/usr/lib/rpm/fileattrs/perl.attr
/usr/lib/rpm/generic
/usr/lib/rpm/koji
/usr/lib/rpm/pc
/usr/lib/rpm/redhat
/usr/lib/rpm/unknown

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-rpm-config/LICENSE
