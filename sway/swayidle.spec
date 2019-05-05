Name: swayidle
Version: 1.3
Release: 1%{?dist}
Summary: An idle management daemon for Wayland

License: MIT
URL: https://github.com/swaywm/swayidle
Source0: %{url}/archive/%{version}.tar.gz

BuildRequires: meson
BuildRequires: gcc
BuildRequires: pkgconfig(wayland-protocols) >= 1.14
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: scdoc

%description
Swayidle is an idle management daemon for Wayland compositors.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/fish/completions/swayidle.fish
%dir %{_datadir}/fish
%dir %{_datadir}/fish/completions
%{_datadir}/zsh/site-functions/_%{name}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_mandir}/man1/%{name}.1.gz

%changelog

