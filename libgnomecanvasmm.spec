Summary:	C++ wrappers for libgnomecanvas
Summary(pl):	Interfejsy C++ dla libgnomecanvas
Name:		libgnomecanvasmm
Version:	2.0.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.0/%{name}-%{version}.tar.bz2
# Source0-md5:	f6beefb0fe523e17c39435cb5775f300
URL:		http://www.gnome.org/
BuildRequires:	gtkmm-devel >= 2.2.7
BuildRequires:	libgnomecanvas-devel >= 2.3.6
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libgnomecanvas.

%description -l pl
Interfejsy C++ dla libgnomecanvas.

%package devel
Summary:	Devel files for libgnomecanvasmm
Summary(pl):	Pliki nag³ówkowe dla libgnomecanvasmm
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtkmm-devel >= 2.2.7
Requires:	libgnomecanvas-devel >= 2.3.6

%description devel
Devel files for libgnomecanvasmm.

%description devel -l pl
Pliki nag³ówkowe dla libgnomecancasmm.

%package static
Summary:	libgnomecanvasmm static library
Summary(pl):	Biblioteka statyczna libgnomecanvasmm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
libgnomecanvasmm static library.

%description static -l pl
Biblioteka statyczna libgnomecanvasmm.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub scripts
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
%attr(755,root,root) %{_libdir}/libgnomecanvasmm*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomecanvasmm*.so
%{_libdir}/libgnomecanvasmm*.la
%{_libdir}/%{name}-2.0
%{_includedir}/%{name}-2.0
%{_pkgconfigdir}/%{name}-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomecanvasmm*.a
