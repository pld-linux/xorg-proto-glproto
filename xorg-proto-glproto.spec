Summary:	GL protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u GL i pomocnicze
Name:		xorg-proto-glproto
Version:	1.4.3
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/proto/glproto-X11R7.0-%{version}.tar.bz2
# Source0-md5:	0ecb98487d7457f0592298fe9b8688f0
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GL protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u GL i pomocnicze.

%package devel
Summary:	GL protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u GL i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
GL protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u GL i pomocnicze.

%prep
%setup -q -n glproto-X11R7.0-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%dir %{_includedir}/GL
%{_includedir}/GL/*.h
%{_includedir}/GL/internal
%{_pkgconfigdir}/glproto.pc
