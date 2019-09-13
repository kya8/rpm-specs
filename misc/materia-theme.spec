Name:           materia-theme
Version:        20190912
Release:        1%{?dist}
Summary:        A Material Design-like theme for GNOME/GTK+ based desktop environments

License:        GPLv2
URL:            https://github.com/nana-4/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  bash
BuildRequires:  bc

Requires:       %{_datadir}/gtk-engines/murrine.xml
Requires:       gnome-themes-extra


%description
Materia is a Material Design-like theme for GNOME/GTK+ based desktop
environments. It supports GTK3, GTK2, Metacity, GNOME Shell, Unity, MATE,
LightDM, GDM, Chrome theme, etc.


%prep
%autosetup


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/themes
cd $RPM_BUILD_DIR/%{name}-%{version}
./install.sh --dest $RPM_BUILD_ROOT/%{_datadir}/themes


%files
%license COPYING
%doc README.md
%{_datadir}/themes/*


%changelog
* Fri Sep 13 2019 taocris - 20190912-1
- New upstream release

* Tue Sep 03 2019 kas7 - 20190831-1
- New upstream release.


