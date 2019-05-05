#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : commonmark
Version  : 0.9.0
Release  : 5
URL      : https://files.pythonhosted.org/packages/ac/9d/a9ff7efaf06fb2b6fcc7a035760ba0971250832e37f0c554c335d86c160b/commonmark-0.9.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ac/9d/a9ff7efaf06fb2b6fcc7a035760ba0971250832e37f0c554c335d86c160b/commonmark-0.9.0.tar.gz
Summary  : Python parser for the CommonMark Markdown spec
Group    : Development/Tools
License  : BSD-3-Clause
Requires: commonmark-bin = %{version}-%{release}
Requires: commonmark-license = %{version}-%{release}
Requires: commonmark-python = %{version}-%{release}
Requires: commonmark-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
commonmark.py
=============
commonmark.py is a pure Python port of `jgm <https://github.com/jgm>`__'s
`commonmark.js <https://github.com/jgm/commonmark.js>`__, a
Markdown parser and renderer for the
`CommonMark <http://commonmark.org>`__ specification, using only native
modules. Once both this project and the CommonMark specification are
stable we will release the first ``1.0`` version and attempt to keep up
to date with changes in ``commonmark.js``.

%package bin
Summary: bin components for the commonmark package.
Group: Binaries
Requires: commonmark-license = %{version}-%{release}

%description bin
bin components for the commonmark package.


%package license
Summary: license components for the commonmark package.
Group: Default

%description license
license components for the commonmark package.


%package python
Summary: python components for the commonmark package.
Group: Default
Requires: commonmark-python3 = %{version}-%{release}

%description python
python components for the commonmark package.


%package python3
Summary: python3 components for the commonmark package.
Group: Default
Requires: python3-core

%description python3
python3 components for the commonmark package.


%prep
%setup -q -n commonmark-0.9.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557016048
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/commonmark
cp LICENSE %{buildroot}/usr/share/package-licenses/commonmark/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cmark

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/commonmark/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
