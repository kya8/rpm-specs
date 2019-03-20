Name:           plata-theme
Version:        0.6.3.1
Release:        1%{?dist}
Summary:        A Gtk+ theme based on Material Design Refresh

License:        GPLv2 and CC-BY-SA
URL:            https://gitlab.com/tista500/plata-theme
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  autoconf, automake
BuildRequires:  pkg-config
BuildRequires:  gdk-pixbuf2-devel >= 2.32.2
BuildRequires:  glib2-devel >= 2.48.0
BuildRequires:  inkscape >= 0.91
BuildRequires:  sassc >= 3.3
BuildRequires:  libxml2

# BuildRequires:  fdupes

Requires:       gtk-murrine-engine >= 0.98.1
Recommends:     google-roboto-fonts

%description
A Gtk+ theme based on Material Design Refresh.

%prep
%autosetup


%build
NOCONFIGURE=1 ./autogen.sh

%configure \
--enable-plank \
--enable-telegram 

%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install

# symlink duplicate files

%files
%license COPYING LICENSE_CC_BY_SA4
%doc README.md
%{_datadir}/themes/*

%changelog
