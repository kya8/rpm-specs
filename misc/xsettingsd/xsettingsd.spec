%global commit 1b2bccaa18fecd15749de92b05d8b3e99088111a
%global commit_date 20180626
%global shortcommit %(c=%{commit};echo ${c:0:7})

Name:		xsettingsd
Version:	1.0.0
Release:	2.%{commit_date}git%{shortcommit}%{?dist}
Summary:	a daemon that implements the XSETTINGS specification

License:	BSD
URL:		https://github.com/derat/xsettingsd

Source0:	%{url}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	scons
BuildRequires:	libstdc++-devel
BuildRequires:  pkgconfig(x11)


%description
xsettingsd is a daemon that implements the XSETTINGS specification.

It is intended to be small, fast, and minimally dependent on other libraries.
It can serve as an alternative to gnome-settings-daemon for users who are not
using the GNOME desktop environment but who still run GTK+ applications and
want to configure things such as themes, font anti-aliasing/hinting, and UI
sound effects.

%prep
%autosetup -n %{name}-%{commit}

%build
%set_build_flags
scons xsettingsd dump_xsettings

%install
%{__install} -Dm0755 xsettingsd dump_xsettings -t %{buildroot}%{_bindir}/
%{__install} -Dm0644 xsettingsd.1 dump_xsettings.1 -t %{buildroot}%{_mandir}/man1/

%files
%{_bindir}/*
%{_mandir}/man1/*.1*
%doc README COPYING

%changelog
