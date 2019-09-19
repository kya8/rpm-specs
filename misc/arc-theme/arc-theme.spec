%global common_configure --disable-unity --srcdir=..

# build from git snapshot
%global git_build 0

%if 0%{?git_build}
%global commit ec6db845a1f1745444366492787c4846385c9543
%global short_commit %(c=%{commit};echo ${c:0:7})
%endif

Name:		arc-theme
Version:	20190917
Release:	1%{?git_build:.git%{short_commit}}%{?dist}
Summary:	Flat Gtk theme with transparent elements

License:	GPLv3+
URL:		https://github.com/arc-design/%{name}

%if 0%{?git_build}
Source0:	%{url}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
%else
Source0:	%{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif

BuildArch:	noarch

BuildRequires:	autoconf, automake
BuildRequires:  pkg-config
BuildRequires:	fdupes
BuildRequires:	gtk3-devel
BuildRequires:	gtk-murrine-engine
BuildRequires:	inkscape
BuildRequires:	optipng
BuildRequires:	sassc
# Allow detecting gnome-shell version. Otherwise use --with-gnome-shell=<version>
BuildRequires:	gnome-shell

Requires:	filesystem
Requires:	gnome-themes-standard
Requires:	gnome-themes-extra
Requires:	gtk-murrine-engine


%description
Arc is a flat theme with transparent elements for GTK 3, GTK 2 and GNOME Shell 
which supports GTK 3 and GTK 2 based desktop environments like GNOME, Unity, 
Pantheon, Xfce, MATE, Cinnamon (>=3.4), Budgie Desktop (10.4 for GTK+3.22) etc.


%prep
%if 0%{?git_build}
%autosetup -n %{name}-%{commit}
%else
%autosetup
%endif
%{_bindir}/autoreconf -fiv


%build
%{__mkdir} -p regular solid
pushd regular
%{__ln_s} -f ../configure configure
%configure %{common_configure}
popd
pushd solid
%{__ln_s} -f ../configure configure
%configure --disable-transparency %{common_configure}
popd
%make_build -C regular
%make_build -C solid


%install
%make_install -C regular
%make_install -C solid

# symlink duplicate files
%fdupes -s %{buildroot}%{_datadir}


%files
%license AUTHORS COPYING
%doc README.md
%{_datadir}/themes/*


%changelog
