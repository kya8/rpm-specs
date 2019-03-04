%global svn_rev 1112
%global svn_date 20181020

Name:           vlmcsd
Version:        0
Release:        0.1.%{svn_date}svn%{svn_rev}%{?dist}
Summary:        KMS Emulator in C

License:        Unknown
URL:            https://github.com/Wind4/vlmcsd
Source0:        %{url}/archive/svn%{svn_rev}.tar.gz#/%{name}-svn%{svn_rev}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  coreutils

# Requires:       

%description
A KMS Emulator in C.


%prep
%autosetup -n %{name}-svn%{svn_rev}


%build
%{set_build_flags}
%make_build STRIP=0 


%install

%{__install} -D -m 755 -t %{buildroot}/%{_bindir}/ bin/vlmcs*
%{__install} -D -m 644 -t %{buildroot}/%{_sysconfdir}/ etc/vlmcsd.*

%{__install} -D -m 644 -t %{buildroot}/%{_mandir}/man1/ man/vlmcs.1.gz
%{__install} -D -m 644 -t %{buildroot}/%{_mandir}/man7/ man/vlmcsd.7.gz
%{__install} -D -m 644 -t %{buildroot}/%{_mandir}/man8/ man/vlmcsd.8.gz
%{__install} -D -m 644 -t %{buildroot}/%{_mandir}/man5/ man/vlmcsd.ini.5.gz


%files
%{_bindir}/vlmcs*
%config(noreplace) %{_sysconfdir}/vlmcsd.*
%{_mandir}/man1/*.1.gz
%{_mandir}/man7/*.7.gz
%{_mandir}/man8/*.8.gz
%{_mandir}/man5/*.5.gz


%changelog
