%define		origname	Supybot
Summary:	A cross-platform IRC bot written in Python
Summary(pl.UTF-8):	Wieloplatformowy bot IRC-owy napisany w Pythonie
Name:		supybot
Version:	0.83.4.1
Release:	1
Group:		Applications/Networking
# The entire source code is BSD except for
# Supybot-0.83.4/plugins/Math/local/convertcore.py which is GPL v2
License:	BSD and GPL v2
URL:		http://supybot.com/
Source0:	http://downloads.sourceforge.net/supybot/%{origname}-%{version}.tar.bz2
# Source0-md5:	96ce90559c7d6fde5e3c93174c509408
# Fix a conflict between python-json and the built in json module
# in Python 2.6.  Already submitted and commited upstream.
Patch0:		json.patch
# fix karma plugin to actually work should go upstream
Patch1:		karma-plugin.patch
BuildRequires:	python-distribute
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-TwistedCore
Requires:	python-TwistedNames
Requires:	python-dateutil
Requires:	python-dictclient
Requires:	python-feedparser
Requires:	python-simplejson
Provides:	Supybot = %{version}-%{release}
Obsoletes:	Supybot < %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Supybot is a cross-platform IRC bot written in Python, known to run
anywhere Python runs.

- Supybot is actively developed.
- Supybot offers nested commands.
- Supybot has a powerful and flexible capability system for handling
  security.
- Supybot includes many plugins, and has many more ripe for the
  picking on this very website.
- Supybot supports multiple servers.
- Supybot supports multiple channels.
- Supybot is user-friendly.
- Supybot is developer-friendly.

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
%setup -q -n %{origname}-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp -a docs/man/supybot.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -a docs/man/supybot-adduser.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -a docs/man/supybot-botchk.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -a docs/man/supybot-plugin-create.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -a docs/man/supybot-plugin-doc.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -a docs/man/supybot-test.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -a docs/man/supybot-wizard.1 $RPM_BUILD_ROOT%{_mandir}/man1

# These are provided in python-feedparser, python-dateutil,
# python-dictclient, and python-simplejson
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/supybot/plugins/RSS/local
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/supybot/plugins/Time/local
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/supybot/plugins/Dict/local
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/supybot/plugins/Google/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKS ChangeLog LICENSE README RELNOTES
%doc docs/{ADVANCED_PLUGIN_CONFIG,ADVANCED_PLUGIN_TESTING,CAPABILITIES}
%doc docs/{CONFIGURATION,FAQ,GETTING_STARTED,PLUGIN_TUTORIAL,STYLE}
%doc docs/{USING_UTILS,USING_WRAP}
%attr(755,root,root) %{_bindir}/supybot
%attr(755,root,root) %{_bindir}/supybot-adduser
%attr(755,root,root) %{_bindir}/supybot-botchk
%attr(755,root,root) %{_bindir}/supybot-plugin-create
%attr(755,root,root) %{_bindir}/supybot-plugin-doc
%attr(755,root,root) %{_bindir}/supybot-plugin-package
%attr(755,root,root) %{_bindir}/supybot-test
%attr(755,root,root) %{_bindir}/supybot-wizard
%{py_sitescriptdir}/supybot
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/supybot-*.egg-info
%endif
%{_mandir}/man1/supybot.1*
%{_mandir}/man1/supybot-adduser.1*
%{_mandir}/man1/supybot-botchk.1*
%{_mandir}/man1/supybot-plugin-create.1*
%{_mandir}/man1/supybot-plugin-doc.1*
%{_mandir}/man1/supybot-test.1*
%{_mandir}/man1/supybot-wizard.1*
