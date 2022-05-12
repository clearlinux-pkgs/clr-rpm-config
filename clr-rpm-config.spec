#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-rpm-config
Version  : 248
Release  : 247
URL      : http://localhost/cgit/projects/clr-rpm-config/snapshot/clr-rpm-config-248.tar.xz
Source0  : http://localhost/cgit/projects/clr-rpm-config/snapshot/clr-rpm-config-248.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: clr-rpm-config-license = %{version}-%{release}
Requires: clr-avx-tools
Requires: clr-python-timestamp

%description
No detailed description available

%package license
Summary: license components for the clr-rpm-config package.
Group: Default

%description license
license components for the clr-rpm-config package.


%prep
%setup -q -n clr-rpm-config-248
cd %{_builddir}/clr-rpm-config-248

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1652368571
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1652368571
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-rpm-config
cp %{_builddir}/clr-rpm-config-248/LICENSE %{buildroot}/usr/share/package-licenses/clr-rpm-config/4cc77b90af91e615a64ae04893fdffa7939db84c
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
