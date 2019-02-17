%global commit e30ee407a42311ff67878921a95161e1bc58bbb5
%global commit_date 20190130
%global shortcommit %(c=%{commit};echo ${c:0:7})

Name:           xarchiver
Version:        0.5.4.14
Release:        1.%{commit_date}git%{shortcommit}%{?dist}
Summary:        Archive manager for Xfce

License:        GPLv2+
URL:            https://github.com/ib/xarchiver
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz

BuildRequires:  gtk3-devel, libxml2-devel, gettext
BuildRequires:  xfce4-dev-tools >= 4.3.90.2
BuildRequires:  autoconf >= 2.69
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  intltool
BuildRequires:	xmlto, docbook-style-xsl
BuildRequires:  desktop-file-utils

# could add more archivers here
Requires:       xdg-utils, tar, unzip, zip
Recommends:     xz, bzip2, gzip, arj, binutils, cpio, p7zip

%description
Xarchiver is a lightweight GTK2 only frontend for manipulating 7z, arj, bzip2,
gzip, iso, rar, lha, tar, zip, RPM and deb files. It allows you to create
archives and add, extract, and delete files from them. Password protected
archives in the arj, 7z, rar, and zip formats are supported.


%prep
%autosetup -n %{name}-%{commit}
# fix spurious executable permissions of some debug files
chmod -x src/mime.*


%build
%configure
%make_build


%install
%make_install

%find_lang %{name}

for file in %{buildroot}/%{_datadir}/applications/*.desktop; do
    desktop-file-validate $file
done


%files -f %{name}.lang
%doc %{_pkgdocdir}/*
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/pixmaps/%{name}/
%{_libexecdir}/thunar-archive-plugin/*.tap
%{_mandir}/man1/%{name}.*


%changelog
