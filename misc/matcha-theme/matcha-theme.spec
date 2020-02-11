Name:           matcha-theme
Version:        20200206
%global upstream_version 2020-02-06
Release:        1%{?dist}
Summary:	A flat Design theme for GTK 3, GTK 2 and Gnome-Shell 

License:	GPLv3
URL:		https://github.com/vinceliuice/matcha 
Source0:	%{url}/archive/%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       gtk-murrine-engine, gtk2-engines

%description
Matcha is a flat Design theme for GTK 3, GTK 2 and Gnome-Shell which supports
GTK 3 and GTK 2 based desktop environments like Gnome, Unity, Budgie, Pantheon,
XFCE, Mate, etc.

%prep
%autosetup -n matcha-%{upstream_version}

%build

%install
%{__mkdir} -p %{buildroot}/%{_datadir}/themes
./Install -d %{buildroot}/%{_datadir}/themes

%files
%license LICENSE AUTHORS
%doc HACKING
%{_datadir}/themes/*


%changelog
