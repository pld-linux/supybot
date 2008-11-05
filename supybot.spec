Summary:	A cross-platform IRC bot written in Python
Summary(pl.UTF-8):	Wieloplatformowy bot IRC-owy napisany w Pythonie
Name:		Supybot
Version:	0.83.3
Release:	2
License:	BSD
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/supybot/%{name}-%{version}.tar.bz2
# Source0-md5:	72f8f28f1d847b9070be1bc5f8b002a4
URL:		http://supybot.com/
BuildRequires:	python >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq  python
Requires:	python-sqlite
Requires:	python-TwistedCore
Requires:	pydoc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Supybot is a cross-platform IRC bot written in Python, known to run
anywhere Python runs.

* Supybot is actively developed.
* Supybot offers nested commands.
* Supybot has a powerful and flexible capability system for handling
  security.
* Supybot includes many plugins, and has many more ripe for the
  picking on this very website.
* Supybot supports multiple servers.
* Supybot supports multiple channels.
* Supybot is user-friendly.
* Supybot is developer-friendly.

%description -l pl.UTF-8
Supybot to wieloplatformowy bot IRC-owy napisany w Pythonie,
działający na wszystkich platformach obsługiwanych przez Pythona.

- Jest aktywnie rozwijany.
- Oferuje zagnieżdżone polecenia.
- Ma potężny i elastyczny system uprawnień do obsługi bezpieczeństwa.
- Zawiera wiele wtyczek i można ich pobrać jeszcze więcej ze strony.
- Obsługuje wiele serwerów.
- Obsługuje wiele kanałów.
- Jest przyjazny dla użytkowników.
- Jest przyjazny dla programistów.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

install docs/man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/[A-Z]* ACKS ChangeLog README RELNOTES
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/supybot
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/*.egg-info
%endif
%{_mandir}/man1/*
