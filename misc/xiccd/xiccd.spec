Name    : xiccd
Version : 0.3.0
Release : 1%{?dist}
Summary : X color profile daemon
License : GPLv3+
URL     : https://github.com/agalakhov/%{name}
Source0 : %{url}/archive/v%{version}.tar.gz
BuildRequires : gcc
BuildRequires : autoconf
BuildRequires : automake
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xrandr) >= 1.3
BuildRequires : pkgconfig(glib-2.0) => 2.36
BuildRequires : pkgconfig(colord) => 1.0.2
BuildRequires : desktop-file-utils
Requires : colord

%description
xiccd is a simple bridge between colord and X. It enumerates displays and
registers them in colord, creates default ICC profiles based on EDID data,
applies ICC profiles provided by colord and maintains the user's private ICC
storage directory. The primary goal of xiccd is providing color profile support
for desktop environments that do not support native color management yet.

%prep
%autosetup

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install

# move desktop file to autostart (where it belongs according to manpage) 
desktop-file-validate %{buildroot}/%{_sysconfdir}/xdg/autostart/%{name}.desktop 

%files
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}.desktop
%license COPYING
%doc AUTHORS README ChangeLog NEWS

%changelog

