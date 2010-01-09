Summary:	GL extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia GL
Name:		xorg-proto-glproto
Version:	1.4.11
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/glproto-%{version}.tar.bz2
# Source0-md5:	78e7c4dc7dcb74b1869fee7897e00f59
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig
BuildRequires:	xorg-util-util-macros >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GL extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia GL.

%package devel
Summary:	GL extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia GL
Group:		X11/Development/Libraries
# <GL/glxint.h> needs <X11/X*.h> and <GL/gl.h>
Requires:	OpenGL-devel
Requires:	xorg-proto-xproto-devel

%description devel
GL extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia GL.

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
%doc COPYING ChangeLog
%{_includedir}/GL/glxint.h
%{_includedir}/GL/glxmd.h
%{_includedir}/GL/glxproto.h
%{_includedir}/GL/glxtokens.h
%dir %{_includedir}/GL/internal
%{_includedir}/GL/internal/glcore.h
%{_pkgconfigdir}/glproto.pc
