#
# Database On Demand (DBOD) API server SPEC file
#

%define version 0.5.0

# Trying to avoid Koji post-generation issues
%define __arch_install_post %{nil} # /usr/lib/rpm/check-buildroot
%define debug_package %{nil} # Disables building debug RPM

Summary: DB On Demand API
Name: cerndb-sw-dbod-api
Version: %{version}
Release: 0 
License: GPL
Group: Applications
ExclusiveArch: x86_64
Source: dbod-api-%{version}.tar.gz
URL: https://github.com/cerndb/dbod-api
Distribution: DBOD
Vendor: CERN
Packager: Ignacio Coterillo Coz <icotl@cern.ch>

# Build requirements
BuildRequires: python
BuildRequires: python-pip
BuildRequires: python-virtualenv
BuildRequires: postgresql-devel
BuildRequires: gcc
BuildRequires: openldap-devel
BuildRequires: cyrus-sasl-devel

# Requirements
# Requirements for the package are not specified here
# As they will be managed in the virtual environment

%description
DB On Demand API server

%prep
%setup -c dbod-api-%{version}
exit 0

%build
exit 0

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/dbod-venv/dbod-api
virtualenv $RPM_BUILD_ROOT/usr/local/dbod-venv/dbod-api
source $RPM_BUILD_ROOT/usr/local/dbod-venv/dbod-api/bin/activate
pip install -r requirements.pip
python setup.py install
mkdir -p $RPM_BUILD_ROOT/var/log/dbod
exit 0

%clean
rm -rf $RPM_BUILD_ROOT
exit 0

%files
/usr/local/dbod-venv/dbod-api/
%attr (-, dbod, dbod) /var/log/dbod

%changelog
* Tue Aug 4 2015 Ignacio Coterillo <icoteril@cern.ch> 0.5.0
- Initial packaging

