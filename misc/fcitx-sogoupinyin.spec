# disable debug packages
%global         __strip /bin/true
%global         debug_package %{nil}

# filter deps/reqs
# exclude everything for now...
%global __requires_exclude_from .*
%global __provides_exclude_from .*

Name:           fcitx-sogoupinyin
Version:        2.4.0.2905
Release:        1
Summary:        Sogou Pinyin for Linux
License:        Proprietary
URL:            https://pinyin.sogou.com/linux/
Source0:        sogoupinyin_%{version}_amd64.deb

ExclusiveArch:  x86_64

BuildRequires:  dpkg
Requires:       fcitx

%description
Sogou Pinyin for Linux

%prep
dpkg-deb -x %{SOURCE0} %{_builddir}/sogoupinyin

%build
cd %{_builddir}/sogoupinyin
rm -rf etc/

%install
cd %{_builddir}/sogoupinyin
mkdir -p %{buildroot}%{_libdir}
mv usr/lib/x86_64-linux-gnu/fcitx/ %{buildroot}%{_libdir}
mv usr/share %{buildroot}%{_prefix}
mv opt %{buildroot}

%files
/opt/*
%{_libdir}/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/doc/*
%{_datadir}/fcitx/*/*

%changelog
