Name:           compton-next
Version:        6.2
Release:        1%{?dist}
Summary:        A compositor for X11

License:        MIT
URL:            https://www.github.com/yshui/compton
Source0:        %{url}/archive/v%{version}.tar.gz#/compton-%{version}.tar.gz


BuildRequires: meson
BuildRequires: gcc
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(x11-xcb)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(libconfig) >= 1.4
BuildRequires: pkgconfig(libpcre)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(pixman-1)

BuildRequires: libev-devel
BuildRequires: pkgconfig(libxdg-basedir)
BuildRequires: pkgconfig(xpresent)

BuildRequires: asciidoc
BuildRequires: desktop-file-utils

Requires:   xorg-x11-utils

Conflicts:  compton

%description
Compton-next is an active fork of the original compton, a compositor for X11.

%prep
%autosetup -n compton-%{version}

%build
%meson -D build_docs=true
%meson_build

%install
%meson_install

%check
%meson_test

desktop-file-validate %{buildroot}/%{_datadir}/applications/compton.desktop

%files
%license LICENSES/* COPYING CONTRIBUTORS
%doc README_orig.md README.md compton.sample.conf
%{_bindir}/compton
%{_bindir}/compton-convgen.py
%{_bindir}/compton-trans
%{_mandir}/man1/compton.1*
%{_mandir}/man1/compton-trans.1*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/compton.*

%changelog
