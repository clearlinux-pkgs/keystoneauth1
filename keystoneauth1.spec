#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : keystoneauth1
Version  : 4.2.1
Release  : 63
URL      : https://files.pythonhosted.org/packages/58/46/a679eacd89f493be20766585a8b7040ea12357cbd724ac3f0fa6867d4e0c/keystoneauth1-4.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/58/46/a679eacd89f493be20766585a8b7040ea12357cbd724ac3f0fa6867d4e0c/keystoneauth1-4.2.1.tar.gz
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
Team and repository tags
        ========================

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
Provides: pypi(keystoneauth1)
Requires: pypi(iso8601)
Requires: pypi(os_service_types)
Requires: pypi(pbr)
Requires: pypi(requests)
Requires: pypi(six)
Requires: pypi(stevedore)

%description python3
python3 components for the keystoneauth1 package.


%prep
%setup -q -n keystoneauth1-4.2.1
cd %{_builddir}/keystoneauth1-4.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1596553094
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/keystoneauth1
cp %{_builddir}/keystoneauth1-4.2.1/LICENSE %{buildroot}/usr/share/package-licenses/keystoneauth1/3bc2515d38cf15fbffb99283a4b24e7bc6403351
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/keystoneauth1/3bc2515d38cf15fbffb99283a4b24e7bc6403351

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
