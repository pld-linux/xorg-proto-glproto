Summary:	GL protocol and ancillary headers
Summary(pl):	Nag��wki protoko�u GL i pomocnicze
Name:		xorg-proto-glproto
Version:	1.4.4
Release:	1
License:	MIT
Group:		X11/Development/Libraries
#Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/proto/glproto-X11R7.0-%{version}.tar.bz2
Source0:	http://xorg.freedesktop.org/current/src/proto/glproto-1.4.4.tar.bz2
# Source0-md5:	151a7df5535157bcdd92e47dbddd13aa
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GL protocol and ancillary headers.

%description -l pl
Nag��wki protoko�u GL i pomocnicze.

%package devel
Summary:	GL protocol and ancillary headers
Summary(pl):	Nag��wki protoko�u GL i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
GL protocol and ancillary headers.

%description devel -l pl
Nag��wki protoko�u GL i pomocnicze.

%prep
#%setup -q -n glproto-X11R7.0-%{version}
%setup -qn glproto-%{version}

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
