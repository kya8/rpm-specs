Name:		xsettingsd
Version:	1.0.0
Release:	1%{?dist}
Summary:	Provides settings to X11 clients via the XSETTINGS specification

Group:		System Environment/Daemons
License:	BSD
URL:		https://github.com/derat/xsettingsd

Source0:	%{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	scons
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig(x11)


%description
xsettingsd is a daemon that implements the XSETTINGS specification.

It is intended to be small, fast, and minimally dependent on other libraries.
It can serve as an alternative to gnome-settings-daemon for users who are not
using the GNOME desktop environment but who still run GTK+ applications and
want to configure things such as themes, font anti-aliasing/hinting, and UI
sound effects.

%prep
%autosetup

%build
%set_build_flags
scons xsettingsd dump_xsettings

%install
%{__instal} -Dm0755 xsettingsd		%{buildroot}%{_bindir}/xsettingsd
%{__instal} -Dm0755 dump_xsettings		%{buildroot}%{_bindir}/dump_xsettings
%{__instal} -Dm0644 xsettingsd.1		%{buildroot}%{_mandir}/man1/xsettingsd.1
%{__instal} -Dm0644 dump_xsettings.1	%{buildroot}%{_mandir}/man1/dump_xsettings.1

%files
%{_bindir}/*
%{_mandir}/man1/*.1.*
%doc README COPYING

%changelog
