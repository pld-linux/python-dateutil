#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module
%bcond_without	tests	# unit tests

%define		module dateutil
%define		tzdata_ver	2016i
Summary:	Extensions to the standard Python datetime module
Summary(pl.UTF-8):	Rozszerzenia modułu datetime języka Python
Name:		python-dateutil
Version:	2.6.0
Release:	2
License:	BSD
Group:		Libraries/Python
# Source0Download: https://pypi.python.org/simple/python-dateutil/
Source0:	https://pypi.python.org/packages/51/fc/39a3fbde6864942e8bb24c93663734b74e281b984d1b8c4f95d64b0c21f6/%{name}-%{version}.tar.gz
# Source0-md5:	6e38f91e8c94c15a79ce22768dfeca87
URL:		https://dateutil.readthedocs.org/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-six >= 1.5
%if "%{py_ver}" < "2.7"
BuildRequires:	python-unittest2
%endif
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-six >= 1.5
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	tzdata >= %{tzdata_ver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The dateutil module provides powerful extensions to the standard
datetime module, available in Python 2.3+. Allows:
- computing of relative deltas (next month, next year, next monday,
  last week of month, etc),
- computing of dates based on very flexible recurrence rules, using a
  superset of the [WWW] iCalendar specification,
- parsing of RFC strings,
- peneric parsing of dates in almost any string format.

This package contains Python 2.x module.

%description -l pl.UTF-8
Moduł dateutil jest potężnym rozszerzeniem standardowego modułu
datetime, dostępnego w Pythonie 2.3+. Pozwala na:
- obliczanie relatywnych różnic (następny miesiąc, rok, poniedziałek,
  ostatni tydzień miesiąca itp.),
- obliczanie dat w oparciu o bardzo elastyczne rekurencyjne zasady, z
  użyciem nadzbioru specyfikacji [WWW] iCalendar,
- analizę łańcuchow znakowych RFC,
- analizę dat w prawie każdym formacie.

Ten pakiet zawiera moduł Pythona 2.x.

%package zoneinfo
Summary:	Internal zoneinfo implementation for Python 2 dateutil module
Summary(pl.UTF-8):	Wewnętrzna implementacja zoneinfo dla modułu Pythona 2 dateutil
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description zoneinfo
Internal zoneinfo implementation for Python 2 dateutil module.

Note: it contains own timezone database, which might not be up to date
with system zoneinfo data.

%description zoneinfo -l pl.UTF-8
Wewnętrzna implementacja zoneinfo dla modułu Pythona 2 dateutil.

Uwaga: zawiera własną bazę danych stref czasowych, która nie musi być
aktualna w stosunku do systemowych danych zoneinfo.

%package -n python3-dateutil
Summary:	Extensions to the standard Python datetime module
Summary(pl.UTF-8):	Rozszerzenia modułu datetime języka Python
Group:		Libraries/Python
Requires:	tzdata >= %{tzdata_ver}

%description -n python3-dateutil
The dateutil module provides powerful extensions to the standard
datetime module, available in Python 2.3+. Allows:
- computing of relative deltas (next month, next year, next monday,
  last week of month, etc),
- computing of dates based on very flexible recurrence rules, using a
  superset of the [WWW] iCalendar specification,
- parsing of RFC strings,
- peneric parsing of dates in almost any string format.

This package contains Python 3.x module.

%description -n python3-dateutil -l pl.UTF-8
Moduł dateutil jest potężnym rozszerzeniem standardowego modułu
datetime, dostępnego w Pythonie 2.3+. Pozwala na:
- obliczanie relatywnych różnic (następny miesiąc, rok, poniedziałek,
  ostatni tydzień miesiąca itp.),
- obliczanie dat w oparciu o bardzo elastyczne rekurencyjne zasady, z
  użyciem nadzbioru specyfikacji [WWW] iCalendar,
- analizę łańcuchow znakowych RFC,
- analizę dat w prawie każdym formacie.

Ten pakiet zawiera moduł Pythona 3.x.

%package -n python3-dateutil-zoneinfo
Summary:	Internal zoneinfo implementation for Python 3 dateutil module
Summary(pl.UTF-8):	Wewnętrzna implementacja zoneinfo dla modułu Pythona 3 dateutil
Group:		Libraries/Python
Requires:	python3-dateutil = %{version}-%{release}

%description -n python3-dateutil-zoneinfo
Internal zoneinfo implementation for Python 3 dateutil module.

Note: it contains own timezone database, which might not be up to date
with system zoneinfo data.

%description -n python3-dateutil-zoneinfo -l pl.UTF-8
Wewnętrzna implementacja zoneinfo dla modułu Pythona 3 dateutil.

Uwaga: zawiera własną bazę danych stref czasowych, która nie musi być
aktualna w stosunku do systemowych danych zoneinfo.

%prep
%setup -q

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README.rst
%dir %{py_sitescriptdir}/dateutil
%{py_sitescriptdir}/dateutil/*.py[co]
%{py_sitescriptdir}/dateutil/tz
%{py_sitescriptdir}/python_dateutil-%{version}-py*.egg-info

%files zoneinfo
%defattr(644,root,root,755)
%{py_sitescriptdir}/dateutil/zoneinfo
%endif

%if %{with python3}
%files -n python3-dateutil
%defattr(644,root,root,755)
%doc LICENSE NEWS README.rst
%dir %{py3_sitescriptdir}/dateutil
%{py3_sitescriptdir}/dateutil/*.py
%{py3_sitescriptdir}/dateutil/__pycache__
%{py3_sitescriptdir}/dateutil/tz
%{py3_sitescriptdir}/python_dateutil-%{version}-py*.egg-info

%files -n python3-dateutil-zoneinfo
%defattr(644,root,root,755)
%{py3_sitescriptdir}/dateutil/zoneinfo
%endif
