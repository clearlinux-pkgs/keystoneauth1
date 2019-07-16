#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : keystoneauth1
Version  : 3.15.0
Release  : 50
URL      : https://files.pythonhosted.org/packages/87/15/2be688ba92e1243f8942db04fd527454b95e892201b0ed05f04618548745/keystoneauth1-3.15.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/87/15/2be688ba92e1243f8942db04fd527454b95e892201b0ed05f04618548745/keystoneauth1-3.15.0.tar.gz
Summary  : Authentication Library for OpenStack Identity
Group    : Development/Tools
License  : Apache-2.0
Requires: keystoneauth1-license = %{version}-%{release}
Requires: keystoneauth1-python = %{version}-%{release}
Requires: keystoneauth1-python3 = %{version}-%{release}
Requires: fixtures
Requires: iso8601
Requires: lxml
Requires: oauthlib
Requires: os-service-types
Requires: pbr
Requires: python-mock
Requires: requests
Requires: requests-kerberos
Requires: six
Requires: stevedore
BuildRequires : buildreq-distutils3
BuildRequires : fixtures
BuildRequires : iso8601
BuildRequires : lxml
BuildRequires : oauthlib
BuildRequires : os-service-types
BuildRequires : pbr
BuildRequires : python-mock
BuildRequires : requests
BuildRequires : requests-kerberos
BuildRequires : six
BuildRequires : stevedore

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/keystoneauth.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package license
Summary: license components for the keystoneauth1 package.
Group: Default

%description license
license components for the keystoneauth1 package.


%package python
Summary: python components for the keystoneauth1 package.
Group: Default
Requires: keystoneauth1-python3 = %{version}-%{release}

%description python
python components for the keystoneauth1 package.


%package python3
Summary: python3 components for the keystoneauth1 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the keystoneauth1 package.


%prep
%setup -q -n keystoneauth1-3.15.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1563247452
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/keystoneauth1
cp LICENSE %{buildroot}/usr/share/package-licenses/keystoneauth1/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/keystoneauth1/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
