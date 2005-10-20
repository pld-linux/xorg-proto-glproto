Summary:	GL protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u GL i pomocnicze
Name:		xorg-proto-glproto
Version:	1.4.1
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/proto/glproto-%{version}.tar.bz2
# Source0-md5:	dd439aa517177697d60d7ee6cdbc614f
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
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
%setup -q -n glproto-%{version}

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
%dir %{_includedir}/GL
%{_includedir}/GL/*.h
%{_includedir}/GL/internal
%{_pkgconfigdir}/glproto.pc
