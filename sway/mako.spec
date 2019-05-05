Name:       mako
Version:    1.3
Release:    1%{?dist}
Summary:    Lightweight Wayland notification daemon
#Provides:   desktop-notification-daemon

License:    MIT
URL:        https://github.com/emersion/%{name}
Source0:    %{url}/archive/v%{version}.tar.gz

#TODO: Add dbus-activated systemd unit as required by the packaging guidelines.

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(cairo)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  scdoc
Requires:       dbus

%description
mako is a lightweight notification daemon for Wayland compositors that support
the layer-shell protocol.


%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_bindir}/mako
%{_bindir}/makoctl
%{_mandir}/man1/mako.1*
%{_mandir}/man1/makoctl.1*

%changelog

