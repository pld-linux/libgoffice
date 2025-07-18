#
# Conditional build:
%bcond_without	static_libs	# static library
#
%define		orgname	goffice
%define		api_version	0.10
Summary:	Glib/Gtk+ set of document centric objects and utilities
Summary(pl.UTF-8):	Zestaw zorientowanych dokumentowo obiektów i narzędzi Glib/Gtk+
Name:		libgoffice
Version:	0.10.59
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	https://download.gnome.org/sources/goffice/0.10/%{orgname}-%{version}.tar.xz
# Source0-md5:	db013c15c5f6280c46a395647db759a4
URL:		https://gitlab.gnome.org/GNOME/goffice
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7.2
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	gdk-pixbuf2-devel >= 2.22.0
BuildRequires:	gettext-tools
BuildRequires:	ghostscript-devel >= 9.06
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gobject-introspection-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.8.7
BuildRequires:	gtk-doc >= 1.12
BuildRequires:	intltool >= 0.35.0
BuildRequires:	lasem-devel >= 0.4.1
BuildRequires:	libgsf-devel >= 1.14.24
BuildRequires:	librsvg-devel >= 2.22.0
BuildRequires:	libspectre-devel >= 0.2.6
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	libxslt-devel
BuildRequires:	pango-devel >= 1:1.24.0
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(cairo-pdf) >= 1.10.0
BuildRequires:	pkgconfig(cairo-ps) >= 1.10.0
BuildRequires:	pkgconfig(cairo-svg) >= 1.10.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrender-devel
Requires:	cairo >= 1.10.0
Requires:	gdk-pixbuf2 >= 2.22.0
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.8.7
Requires:	lasem >= 0.4.1
Requires:	libgsf >= 1.14.24
Requires:	librsvg >= 2.22.0
Requires:	libspectre >= 0.2.6
Requires:	libxml2 >= 1:2.6.26
Requires:	pango >= 1:1.24.0
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
Requires:	glib2-devel >= 1:2.40.0
Requires:	gtk+3-devel >= 3.8.7
Requires:	lasem-devel >= 0.4.1
Requires:	libgsf-devel >= 1.14.24
Requires:	libspectre-devel >= 0.2.6
Requires:	libxml2-devel >= 1:2.6.26
Requires:	libxslt-devel
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
BuildArch:	noarch

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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/goffice/%{version}/plugins/*/*.la \
	$RPM_BUILD_ROOT%{_libdir}/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/goffice/%{version}/plugins/*/*.a
%endif

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
%{_libdir}/girepository-1.0/GOffice-%{api_version}.typelib
%dir %{_libdir}/goffice
%dir %{_libdir}/goffice/%{api_version}
%dir %{_libdir}/goffice/%{api_version}/plugins
%dir %{_libdir}/goffice/%{version}
%dir %{_libdir}/goffice/%{version}/plugins
%dir %{_libdir}/goffice/%{version}/plugins/*
%attr(755,root,root) %{_libdir}/goffice/%{version}/plugins/*/*.so
%{_libdir}/goffice/%{version}/plugins/*/*.xml
%{_datadir}/goffice

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
