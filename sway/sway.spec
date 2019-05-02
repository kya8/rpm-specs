Name:           sway
Version:        1.0
Release:        3%{?dist}
Summary:        i3-compatible window manager for Wayland
License:        MIT
URL:            https://github.com/swaywm/sway
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wlroots) >= 0.5.0
BuildRequires:  wayland-devel
BuildRequires:  libevdev-devel
BuildRequires:  git
BuildRequires:  scdoc
# Dmenu is the default launcher in sway
Recommends:     dmenu
# By default the Fedora background is used
Recommends:     f%{fedora}-backgrounds-base
# dmenu (as well as rxvt any many others) requires XWayland on Sway
Requires:       xorg-x11-server-Xwayland
# Sway binds the terminal shortcut to one specific terminal. In our case urxvtc-ml
Recommends:     rxvt-unicode-256color-ml
# TODO: needs packaging
# grim is the recommended way to take screenshots on sway 1.0+
# Recommends:     grim

%description
Sway is a tiling window manager supporting Wayland compositor protocol and
i3-compatible configuration.

%prep
%autosetup -p 1

%build
%meson
%meson_build

%install
%meson_install
# Set default terminal to urxvt256c-ml
sed -i 's/^set $term urxvt$/set \$term urxvt256c-ml/' %{buildroot}%{_sysconfdir}/sway/config
# Set Fedora background as default background
sed -i "s|^output \* bg .*|output * bg /usr/share/backgrounds/f%{fedora}/default/normalish/f%{fedora}.png fill|" %{buildroot}%{_sysconfdir}/sway/config

%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/sway
%config(noreplace) %{_sysconfdir}/sway/config
%dir %{_sysconfdir}/sway/security.d
%config(noreplace) %{_sysconfdir}/sway/security.d/00-defaults
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man7/*
%{_bindir}/sway
%{_bindir}/swaybar
%{_bindir}/swaybg
%{_bindir}/swaymsg
%{_bindir}/swaynag
%{_datadir}/wayland-sessions/sway.desktop
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_sway*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/sway*
%dir %{_datadir}/fish
%dir %{_datadir}/fish/completions
%{_datadir}/fish/completions/sway*
%{_datadir}/backgrounds/sway

%changelog
