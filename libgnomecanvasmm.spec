Summary:	C++ wrappers for libgnomecanvas
Summary(pl):	Interfejsy C++ dla libgnomecanvas
Name:		libgnomecanvasmm
Version:	2.10.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgnomecanvasmm/2.10/%{name}-%{version}.tar.bz2
# Source0-md5:	09010717524f990915a6923d685ca5c1
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtkmm-devel >= 2.6.0
BuildRequires:	libgnomecanvas-devel >= 2.10.0
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libgnomecanvas.

%description -l pl
Interfejsy C++ dla libgnomecanvas.

%package devel
Summary:	Devel files for libgnomecanvasmm
Summary(pl):	Pliki nagłówkowe dla libgnomecanvasmm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtkmm-devel >= 2.6.0
Requires:	libart_lgpl-devel >= 2.3.16
Requires:	libgnomecanvas-devel >= 2.10.0

%description devel
Devel files for libgnomecanvasmm.

%description devel -l pl
Pliki nagłówkowe dla libgnomecancasmm.

%package static
Summary:	libgnomecanvasmm static library
Summary(pl):	Biblioteka statyczna libgnomecanvasmm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libgnomecanvasmm static library.

%description static -l pl
Biblioteka statyczna libgnomecanvasmm.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libgnomecanvasmm*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomecanvasmm*.so
%{_libdir}/libgnomecanvasmm*.la
%{_libdir}/%{name}-2.6
%{_includedir}/%{name}-2.6
%{_pkgconfigdir}/%{name}-2.6.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomecanvasmm*.a
