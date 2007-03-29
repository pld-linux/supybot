Summary:	Bazaar-NG - a changeset oriented revision control system
Summary(pl.UTF-8):	Bazaar-NG - system kontroli wersji zorientowany na zestawy zmian
Name:		Supybot
Version:	0.83.2
Release:	1
License:	BSD
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/sourceforge/supybot/Supybot-0.83.2.tar.bz2
# Source0-md5:	514c23a3388b65da81b9b6f1990a1912
URL:		http://supybot.com
BuildRequires:	python >= 1:2.5
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq  python
Requires:	python-sqlite
Requires:	python-TwistedCore
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Supybot is a cross-platform IRC bot written in Python, known to run anywhere Python runs.

* Supybot is actively developed.
* Supybot offers nested commands.
* Supybot has a powerful and flexible capability system for handling security.
* Supybot includes many plugins , and has many more ripe for the picking on this very website.
* Supybot supports multiple servers.
* Supybot supports multiple channels.
* Supybot is user-friendly.
* Supybot is developer-friendly.

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
%{py_sitescriptdir}/*.egg-info
%{py_sitescriptdir}/supybot
%{_mandir}/man1/*
