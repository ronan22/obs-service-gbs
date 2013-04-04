%define do_unittests 0

Name:           obs-service-gbs
License:        GPL-2.0+
Group:          Development/Tools/Building
Summary:        Get sources from a repository managed with GBS
Version:        0.0
Release:        0
URL:            http://www.tizen.org
Source:         %{name}-%{version}.tar.bz2
Requires:       gbs
Requires:       obs-service-git-buildpackage >= 0.1
BuildRequires:  python
BuildRequires:  python-setuptools
%if 0%{?do_unittests}
BuildRequires:  python-coverage
BuildRequires:  python-nose
BuildRequires:  obs-service-git-buildpackage >= 0.1
%endif
BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

This source service supports getting packaging files from a git repository that
is being maintained with the GBS tool.


%prep
%setup


%build
%{__python} setup.py build


%if 0%{?do_unittests}
%check
%{__python} setup.py nosetests
%endif


%install
%{__python} setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}
rm -rf %{buildroot}%{python_sitelib}/*info


%files
%defattr(-,root,root,-)
%doc COPYING
%dir /usr/lib/obs
%dir /usr/lib/obs/service
/usr/lib/obs/service/*
%{python_sitelib}/obs_service_gbs