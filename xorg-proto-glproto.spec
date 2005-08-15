# $Rev: 3333 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	GL protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u GL i pomocnicze
Name:		xorg-proto-glproto
Version:	1.4
Release:	0.01
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/proto/glproto-%{version}.tar.bz2
# Source0-md5:	9cda6fbdcc75f6d7d9cd1d3839264609
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/glproto-%{version}-root-%(id -u -n)

%description
GL protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u GL i pomocnicze.


%package devel
Summary:	GL protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u GL i pomocnicze
Group:		X11/Development/Libraries

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
%{_includedir}/GL/*.h
%{_includedir}/GL/internal
%{_pkgconfigdir}/glproto.pc
