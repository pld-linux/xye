Summary:	Xye is a puzzle game
Summary(hu.UTF-8):	Xye egy kirakó játék
Summary(pl.UTF-8):	Gra logiczna Xye
Name:		xye
Version:	0.9.1
Release:	0.1
License:	PNG/ZLIB
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/xye/%{name}-%{version}.tar.gz
# Source0-md5:	ed03194c9e37c8bd805b9348a2caa7c3
Source1:	%{name}.desktop
URL:		http://xye.sourceforge.net/
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_ttf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xye is a puzzle game in which the objective is to help a character
that looks like a green circle to get all the gems in the room. This
is, of course, not as easy as it sounds, Xye must solve all sorts of
puzzles while at the same time avoiding all sorts of traps and beasts.

%description -l hu.UTF-8
Xye egy kirakó játék, amelynek a célja, hogy segíts a zöld
körben látható karakternek az összes gyémántot összegyűjteni a
szobában. Ez, természetesen, nem olyan egyszerű, ahogy első
hallásra tűnik, Xye-ben mindenféle kirakót kell megoldani,
miközben az idő és mindenféle csapdák és szörnyek ellened
dolgoznak.

%description -l pl.UTF-8
Xye to gra logiczna, w której celem jest pomaganie bohaterowi
wyglądającemu jak zielone kółko w zebraniu wszystkich kamieni w
pomieszczeniu. Nie jest to tak proste, jak się wydaje. Xye musi
rozwiązywać zagadki logiczne różnego typu, unikając
równocześnie pułapek oraz potworów.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}
install -d $RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install xye.ico $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README GAMEINTRO.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.ico
