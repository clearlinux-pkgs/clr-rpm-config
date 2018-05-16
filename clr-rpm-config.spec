Name:       clr-rpm-config
Summary:    Clear Linux specific rpm configuration files
Version:    80
Release:    82
Group:      Development/System
License:    GPL-2.0+
URL:        http://www.clearlinux.org
Source0:    http://localhost/cgit/projects/clr-rpm-config/snapshot/clr-rpm-config-80.tar.gz
AutoReqProv: No
Requires: clr-python-timestamp

%description
Clear Linux specific rpm configuration files.

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
make DESTDIR=${RPM_BUILD_ROOT} install
mkdir -p  $RPM_BUILD_ROOT/usr/lib/rpm
ln -s clr $RPM_BUILD_ROOT/usr/lib/rpm/unknown
ln -s clr $RPM_BUILD_ROOT/usr/lib/rpm/generic
ln -s clr $RPM_BUILD_ROOT/usr/lib/rpm/redhat
ln -s clr $RPM_BUILD_ROOT/usr/lib/rpm/koji
ln -s clr $RPM_BUILD_ROOT/usr/lib/rpm/pc
rm -f %{buildroot}/usr/lib/rpm/clr/perl.prov
ln -s /usr/lib/rpm/perl.prov %{buildroot}/usr/lib/rpm/clr/perl.prov

%files
%defattr(-,root,root,-)
/usr/lib/rpm/*
