%define		orgname	goffice
Summary:	Glib/Gtk+ set of document centric objects and utilities
Summary(pl):	Zestaw zorientowanych dokumentowo obiektów i narzêdzi Glib/Gtk+
Name:		libgoffice
Version:	0.0.2
Release:	1
Epoch:		0
License:	GPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/goffice/0.0/%{orgname}-%{version}.tar.bz2
# Source0-md5:	48c1a8c79e062cfa8a24d99a98d3d0f8
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2 >= 2:2.6.0
BuildRequires:	intltool >= 0.27.2
BuildRequires:	libart_lgpl >= 2.3.11
BuildRequires:	libgnomeprint-devel >= 2.8.2
BuildRequires:	libgnomeui-devel
BuildRequires:	libgsf-gnome-devel >= 1.12.1
BuildRequires:	libtool 
BuildRequires:	libxml2-devel >= 2.4.12
BuildRequires:	pkgconfig
Requires:	libgsf-gnome >= 1.12.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GOffice - a Glib/Gtk+ set of document centric objects and utilities.

%description -l pl
GOffice - Zestaw zorientowanych dokumentowo obiektów i narzêdzi
Glib/Gtk+.

%package devel
Summary:	Header files for GOffice library
Summary(pl):	Pliki nag³ówkowe biblioteki GOffice
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgsf-gnome-devel >= 1.12.1

%description devel
This is the package containing the header files for GOffice.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe GOffice.

%package static
Summary:	Static GOffice library
Summary(pl):	Statyczna biblioteka GOffice
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GOffice library.

%description static -l pl
Statyczna biblioteka GOffice.

%prep
%setup -qn %{orgname}-%{version}

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	--with-gnome
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/goffice/%{version}/plugins/*/*.{a,la}

%find_lang %{orgname}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/goffice
%dir %{_libdir}/goffice/%{version}
%dir %{_libdir}/goffice/%{version}/plugins
%dir %{_libdir}/goffice/%{version}/plugins/*
%attr(755,root,root) %{_libdir}/goffice/%{version}/plugins/*/*.so
%{_libdir}/goffice/%{version}/plugins/*/*.glade
%{_libdir}/goffice/%{version}/plugins/*/*.xml
%{_datadir}/%{orgname}
%{_pixmapsdir}/goffice

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libgoffice-1
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
