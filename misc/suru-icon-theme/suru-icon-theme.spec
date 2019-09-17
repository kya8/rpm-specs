%global commit 2d8102084eaf194f04076ec6949feacb0eb4a1ba
%global commit_date 20180928
%global shortcommit %(c=%{commit};echo ${c:0:7})


Name:           suru-icon-theme
Version:        0
Release:        1.%{commit_date}git%{shortcommit}%{?dist}
Summary:        An open source FreeDesktop icon project by Sam Hewitt

License:        CC-BY-SA
URL:            https://github.com/snwh/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz

BuildArch:      noarch

BuildRequires:  meson
Recommends:     suru-cursor-theme

%description
Suru is a revitalization of the icon set that was developed for the Ubuntu 
mobile platform. The principles and styles created for Suru now serve as the 
basis for a new FreeDesktop icon theme. It has also been extended with a desktop 
cursor theme.

%package -n suru-cursor-theme
Summary:        Cursor theme supplementary to the Suru icon theme.

%description -n suru-cursor-theme
%{summary}.


%prep
%autosetup -n %{name}-%{commit}


%build
%meson
%meson_build

%install
%meson_install

/bin/touch %{buildroot}%{_datadir}/icons/Suru/icon-theme.cache

%check
%meson_test


%files
%license COPYING LICENSE_CCBYSA AUTHORS
%doc README.md
%{_datadir}/icons/Suru
# listed twice...
%ghost %{_datadir}/icons/Suru/icon-theme.cache
%exclude %{_datadir}/icons/Suru/cursors
%exclude %{_datadir}/icons/Suru/cursor.theme

%files -n suru-cursor-theme
%dir %{_datadir}/icons/Suru
%{_datadir}/icons/Suru/cursors
%{_datadir}/icons/Suru/cursor.theme

%changelog
