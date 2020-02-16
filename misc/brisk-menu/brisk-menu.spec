Name:           brisk-menu
Version:        0.6.1
Release:        1%{?dist}
Summary:        A modern and efficient menu for MATE Desktop

License:        GPLv2+
URL:            https://github.com/getsolus/brisk-menu
Source0:        %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.xz

BuildRequires:  meson, gcc
BuildRequires:	glib2-devel
BuildRequires:	gtk3-devel
BuildRequires:	pkgconfig(libmatepanelapplet-4.0)
BuildRequires:	pkgconfig(libmate-menu)
BuildRequires:	pkgconfig(libnotify)

Requires:       mate-panel

%description
A modern and efficient menu designed to improve the MATE Desktop Environment
with modern, first-class options.

%prep
%autosetup -n %{name}-v%{version}


%build
%meson
%meson_build


%install
%meson_install


%check
%meson_test


%find_lang %{name}


%files -f %{name}.lang
%license LICENSE LICENSE.CC-BY-SA-4.0 AUTHORS
%{_libexecdir}/brisk-menu
%{_datadir}/dbus-1/services/*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mate-panel/applets/*


%changelog
* Sat Feb 15 2020 taocris
- Initial packaging
