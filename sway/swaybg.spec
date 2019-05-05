Name:           swaybg
Version:        1.0
Release:        1%{?dist}
Summary:        A wallpaper utility for Wayland compositors
License:        MIT
URL:            https://github.com/swaywm/swaybg
Source0:        %{url}/archive/%{version}.zip

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:	git

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  wayland-devel
BuildRequires:  scdoc


%description
swaybg is a wallpaper utility for Wayland compositors. It is compatible with
any Wayland compositor which implements the following Wayland protocols:
* wlr-layer-shell
* xdg-output
* xdg-shell

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
%{_mandir}/man1/*
%{_bindir}/swaybg

%changelog
