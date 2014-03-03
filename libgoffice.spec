#
# Conditional build:
%bcond_without	static_libs	# static library
#
%define		orgname	goffice
%define		api_version	0.10
#
Summary:	Glib/Gtk+ set of document centric objects and utilities
Summary(pl.UTF-8):	Zestaw zorientowanych dokumentowo obiektów i narzędzi Glib/Gtk+
Name:		libgoffice
Version:	0.10.11
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/goffice/0.10/%{orgname}-%{version}.tar.xz
# Source0-md5:	855d536b0b61004b3ffada6b62440588
URL:		http://www.gtk.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	gdk-pixbuf2-devel >= 2.22.0
BuildRequires:	gettext-devel
BuildRequires:	ghostscript-devel >= 9.06
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gobject-introspection-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.2.0
BuildRequires:	gtk-doc >= 1.12
BuildRequires:	intltool >= 0.35.0
BuildRequires:	lasem-devel >= 0.4.1
BuildRequires:	libgsf-devel >= 1.14.23
BuildRequires:	librsvg-devel >= 2.22.0
BuildRequires:	libspectre-devel >= 0.2.6
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pango-devel >= 1:1.24.0
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrender-devel
Requires:	cairo >= 1.10.0
Requires:	gdk-pixbuf2 >= 2.22.0
Requires:	glib2 >= 1:2.28.0
Requires:	gtk+3 >= 3.2.0
Requires:	lasem >= 0.4.1
Requires:	libgsf >= 1.14.23
Requires:	librsvg >= 2.22.0
Requires:	libspectre >= 0.2.6
Requires:	libxml2 >= 1:2.6.26
Requires:	pango >= 1:1.24.0
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GOffice - a Glib/Gtk+ set of document centric objects and utilities.

%description -l pl.UTF-8
GOffice - Zestaw zorientowanych dokumentowo obiektów i narzędzi
Glib/Gtk+.

%package devel
Summary:	Header files for GOffice library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GOffice
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.10.0
Requires:	glib2-devel >= 1:2.28.0
Requires:	gtk+3-devel >= 3.2.0
Requires:	lasem-devel >= 0.4.1
Requires:	libgsf-devel >= 1.14.23
Requires:	libspectre-devel >= 0.2.6
Requires:	libxml2-devel >= 1:2.6.26
Requires:	pango-devel >= 1:1.24.0

%description devel
This is the package containing the header files for GOffice.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe GOffice.

%package static
Summary:	Static GOffice library
Summary(pl.UTF-8):	Statyczna biblioteka GOffice
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GOffice library.

%description static -l pl.UTF-8
Statyczna biblioteka GOffice.

%package apidocs
Summary:	GOffice library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki GOffice
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GOffice library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki GOffice.

%prep
%setup -qn %{orgname}-%{version}

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-introspection \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/goffice/%{api_version}/plugins

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/goffice/%{version}/plugins/*/*.{a,la} \
	$RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{orgname}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{orgname}-%{version}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_libdir}/libgoffice-%{api_version}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoffice-%{api_version}.so.10
%dir %{_libdir}/goffice
%dir %{_libdir}/goffice/%{api_version}
%dir %{_libdir}/goffice/%{api_version}/plugins
%dir %{_libdir}/goffice/%{version}
%dir %{_libdir}/goffice/%{version}/plugins
%dir %{_libdir}/goffice/%{version}/plugins/*
%attr(755,root,root) %{_libdir}/goffice/%{version}/plugins/*/*.so
%{_libdir}/goffice/%{version}/plugins/*/*.xml
%{_libdir}/girepository-1.0/GOffice-%{api_version}.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgoffice-%{api_version}.so
%{_includedir}/libgoffice-%{api_version}
%{_pkgconfigdir}/libgoffice-%{api_version}.pc
%{_datadir}/gir-1.0/GOffice-%{api_version}.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgoffice-%{api_version}.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/goffice-%{api_version}
