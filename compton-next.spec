Name:           compton-next
Version:        5
Release:        0.2.RC4%{?dist}
Summary:        A compositor for X11.

License:        MIT
URL:            https://www.github.com/yshui/compton
Source0:        %{url}/archive/v%{version}-rc4.tar.gz#/compton-%{version}-rc4.tar.gz


BuildRequires:  meson

BuildRequires : gcc
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xcomposite)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xdamage)
BuildRequires : pkgconfig(xrender)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(libconfig) >= 1.4
BuildRequires : pcre-devel
BuildRequires : pkgconfig(libdrm)
BuildRequires : mesa-libGL-devel
BuildRequires : pkgconfig(dbus-1)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires : asciidoc
BuildRequires : desktop-file-utils

BuildRequires:  libev-devel
BuildRequires:  pkgconfig(libxdg-basedir)
BuildRequires:  pkgconfig(xpresent)

Requires:   xorg-x11-utils

Conflicts:  compton
       

%description
Fork of the original compton, a compositor for X11.

%prep
%autosetup -n compton-%{version}-rc4


%build
%meson -D build_docs=true
%meson_build


%install
%meson_install


%check
%meson_test

desktop-file-validate %{buildroot}/%{_datadir}/applications/compton.desktop

%files
%license LICENSES COPYING
%doc README.md
%{_bindir}/compton
%{_bindir}/compton-convgen.py
%{_bindir}/compton-trans
%{_mandir}/man1/compton.1*
%{_mandir}/man1/compton-trans.1*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/compton.*


%changelog
