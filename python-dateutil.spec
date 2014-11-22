#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module dateutil
Summary:	Extensions to the standard Python datetime module
Summary(pl.UTF-8):	Rozszerzenia modułu datetime języka Python
Name:		python-dateutil
Version:	2.2
Release:	2
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/p/python-dateutil/python-%{module}-%{version}.tar.gz
# Source0-md5:	c1f654d0ff7e33999380a8ba9783fd5c
Patch0:		system-zoneinfo.patch
URL:		http://labix.org/python-dateutil
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 0.219
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
Requires:	python-six
Requires:	tzdata >= 2013h
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

%package -n python3-dateutil
Summary:	Extensions to the standard Python datetime module
Summary(pl.UTF-8):	Rozszerzenia modułu datetime języka Python
Group:		Libraries/Python
Requires:	python3-six
Requires:	tzdata >= 2013h

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

%prep
%setup -q
%patch0 -p1

%build
%if %{with python2}
%{__python} setup.py build --build-base build-2
%endif

%if %{with python3}
%{__python3} setup.py build --build-base build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 \
	install \
		--skip-build \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT

%py_postclean

# NOTE: Not sure but seems zoneinfo is needed under windows only
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/dateutil/zoneinfo
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	install \
		--skip-build \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT

# NOTE: Not sure but seems zoneinfo is needed under windows only
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/dateutil/zoneinfo
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README
%{py_sitescriptdir}/dateutil
%{py_sitescriptdir}/python_dateutil-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-dateutil
%defattr(644,root,root,755)
%doc LICENSE NEWS README
%{py3_sitescriptdir}/dateutil
%{py3_sitescriptdir}/python_dateutil-%{version}-py*.egg-info
%endif
