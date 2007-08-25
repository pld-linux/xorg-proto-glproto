Summary:	GL protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu GL i pomocnicze
Name:		xorg-proto-glproto
Version:	1.4.8
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/glproto-%{version}.tar.bz2
# Source0-md5:	3dfbd17203c0c88b94b6f579f24c11cc
Patch0:		%{name}-shaders.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GL protocol and ancillary headers.

%description -l pl.UTF-8
Nagłówki protokołu GL i pomocnicze.

%package devel
Summary:	GL protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu GL i pomocnicze
Group:		X11/Development/Libraries
# <GL/glxint.h> needs <X11/X*.h> and <GL/gl.h>
Requires:	OpenGL-devel
Requires:	xorg-proto-xproto-devel

%description devel
GL protocol and ancillary headers.

%description devel -l pl.UTF-8
Nagłówki protokołu GL i pomocnicze.

%prep
%setup -q -n glproto-%{version}
%patch0 -p1

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
%{_includedir}/GL/glxint.h
%{_includedir}/GL/glxmd.h
%{_includedir}/GL/glxproto.h
%{_includedir}/GL/glxtokens.h
%dir %{_includedir}/GL/internal
%{_includedir}/GL/internal/glcore.h
%{_pkgconfigdir}/glproto.pc
