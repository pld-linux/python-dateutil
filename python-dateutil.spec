%define		module dateutil
Summary:	Extensions to the standard datetime module
Summary(pl.UTF-8):	Rozszerzenia modułu datetime języka Python
Name:		python-dateutil
Version:	1.5
Release:	4
License:	BSD
Group:		Libraries/Python
Source0:	http://niemeyer.net/download/python-dateutil/python-%{module}-%{version}.tar.gz
# Source0-md5:	35f3732db3f2cc4afdc68a8533b60a52
Patch0:		system-zoneinfo.patch
URL:		http://niemeyer.net/python-dateutil
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 0.219
Requires:	tzdata
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

%description -l pl.UTF-8
Moduł dateutil jest potężnym rozszerzeniem standardowego modułu
datetime, dostępnego w Pythonie 2.3+. Pozwala na:
- obliczanie relatywnych różnic (następny miesiąc, rok, poniedziałek,
  ostatni tydzień miesiąca itp.),
- obliczanie dat w oparciu o bardzo elastyczne rekurencyjne zasady, z
  użyciem nadzbioru specyfikacji [WWW] iCalendar,
- analizę łańcuchow znakowych RFC,
- analizę dat w prawie każdym formacie.

%prep
%setup -q
%patch0 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT \

%py_postclean

# NOTE: Not sure but seems zoneinfo is needed under windows only
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/dateutil/zoneinfo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README
%{py_sitescriptdir}/dateutil
%{py_sitescriptdir}/python_dateutil-*.egg-info
