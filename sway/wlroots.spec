%global commit 522ddd93f145533055ab889ef3a540c550c18008
%global shortcommit %(c=%{commit};echo ${c:0:7})
%global commit_date 20190515

# soname version
%global abi_ver 3

Name:           wlroots
Version:        0.6.0
Release:        100.%{commit_date}git%{shortcommit}%{?dist}
Summary:        A modular Wayland compositor library

License:        MIT
URL:            https://github.com/swaywm/%{name}
Source0:        %{url}/archive/%{commit}.zip#/%{name}-%{commit}.zip

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  meson

BuildRequires:  pkgconfig(libinput)
#BuildRequires:  libpng
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  wayland-devel >= 0.17.0
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libcap)

#xwayland support
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xinput)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-icccm)


%description
%{summary}.


%package        devel
Summary:        Development files for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.


%prep
%autosetup -n %{name}-%{commit}


%build
# fedora sets this to 'enabled', which may cause dependency failures
%global __meson_auto_features auto
%meson
%meson_build


%install
%meson_install


%check
%meson_test


%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.%{abi_ver}*


%files  devel
%doc examples
%{_includedir}/wlr
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
