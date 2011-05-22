%define		module dateutil
Summary:	Extensions to the standard datetime module
Summary(pl.UTF-8):	Rozszerzenia modułu datetime języka Python
Name:		python-dateutil
Version:	2.0
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	http://niemeyer.net/download/python-dateutil/python-%{module}-%{version}.tar.gz
# Source0-md5:	22297f7e891bcd79a80d9446d8b20542
URL:		http://niemeyer.net/python-dateutil
BuildRequires:	rpm-pythonprov
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

%build
%{__python3} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python3} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT \

# NOTE: Not sure but seems zoneinfo is needed under windows only
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/dateutil/zoneinfo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README
%{py3_sitescriptdir}/dateutil
%{py3_sitescriptdir}/python_dateutil-*.egg-info
