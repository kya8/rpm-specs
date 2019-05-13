%global commit 0a8f00c74dffc93900e7aae545c56a4eaa023f4b
%global commit_date 20190512
%global shortcommit %(c=%{commit};echo ${c:0:7})

Name:           xfwm4
Version:        4.13.1
Release:        16.%{commit_date}git%{shortcommit}%{?dist}
Summary:        Next generation window manager for Xfce

Group:          User Interface/Desktops
License:        GPLv2+
URL:            http://www.xfce.org/
#VCS git:git://git.xfce.org/xfce/xfwm4
Source0:        https://github.com/xfce-mirror/%{name}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz

BuildRequires:  gcc, gcc-c++
BuildRequires:  libxfce4ui-devel
BuildRequires:  libXext-devel
BuildRequires:  gettext 
BuildRequires:  intltool
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  startup-notification-devel >= 0.5
BuildRequires:  libglade2-devel
BuildRequires:  libwnck3-devel >= 3.14
BuildRequires:  xfconf-devel
BuildRequires:  desktop-file-utils
BuildRequires:	exo-devel
BuildRequires:	xfce4-dev-tools
BuildRequires:	libXpresent-devel
BuildRequires:	libepoxy-devel
BuildRequires:	libtool
BuildRequires:	librsvg2

Provides:       firstboot(windowmanager) = xfwm4

%description
xfwm4 is a window manager compatible with GNOME, GNOME2, KDE2, KDE3 and Xfce.

%prep
%autosetup -n %{name}-%{commit}
NOCONFIGURE=1 ./autogen.sh


%build
# "--enable-maintainer-mode" is required for git builds.
%configure \
  --disable-static \
  --enable-maintainer-mode \
  --enable-epoxy \
  --enable-startup-notification \
  --enable-xsync \
  --enable-render \
  --enable-randr \
  --enable-xpresent \
  --enable-compositor \

%make_build

%install
%make_install

%find_lang %{name}

for file in %{buildroot}/%{_datadir}/applications/*.desktop; do
    desktop-file-validate $file
done


%files -f %{name}.lang
%license COPYING AUTHORS
%doc README TODO COMPOSITOR NEWS
%{_bindir}/xfwm4
%{_bindir}/xfwm4-settings
%{_bindir}/xfwm4-tweaks-settings
%{_bindir}/xfwm4-workspace-settings
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/xfwm4
%{_datadir}/themes/*
%dir %{_libdir}/xfce4/xfwm4/
%{_libdir}/xfce4/xfwm4/helper-dialog


%changelog
