%define         module dateutil
Summary:	Extensions to the standard datetime module
Summary(pl):	Rozszerzenia modulu datetime jezyka Python
Name:		python-dateutil
Version:	1.1
Release:	1
License:	PSF
Group:		Libraries/Python
Source0:	http://labix.org/download/python-dateutil/python-%{module}-%{version}.tar.bz2
# Source0-md5:	f259496f4059dda806837503ee4235f3
URL:		http://labix.org/python-dateutil
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The dateutil module provides powerful extensions to the standard datetime module, available in Python 2.3+.
Allows
- computing of relative deltas (next month, next year, next monday, last week of month, etc),
- computing of dates based on very flexible recurrence rules, using a superset of the [WWW] iCalendar specification,
- parsing of RFC strings,
- peneric parsing of dates in almost any string format.

%description -l pl
Modul dateutil jest poteznym rozszerzeniem standardowego modulu datetime, dostepnego w Pythonie 2.3+.
Pozwala na
- obliczanie relatywnych roznic (nastepny miesiac, rok, Poniedzialek, ostatni tydzien itp.),
- obliczanie  dat bazujcych na bardzo elastycznych rekurencyjnych zasadach, uzywajac nadzbioru specyfikacji [WWW] iCalendar.
- parsowanie lancuchow znakowych RFC,
- parsowanie dat w prawie kazdym formacie.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
        --root=$RPM_BUILD_ROOT  --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
#NOTE: Not sure but seems zoneinfno is needed under windows only
#%%dir %{py_sitescriptdir}/%{module}/zoneinfo
#%%{py_sitescriptdir}/%{module}/zoneinfo/*.py[co]
