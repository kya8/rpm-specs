#TODO: handle unrar alternatives

# do not strip and make debug packages
%global         __strip /bin/true
%global         debug_package %{nil}

%bcond_with unrar

Name:           rar
Summary:        Command line tools to create and manage RAR archives
Version:        5.7.0
Release:        1%{?dist}
License:        Proprietary
URL:            https://www.rarlab.com

Source0:        %{url}/rar/rarlinux-%{version}.tar.gz
Source1:        %{url}/rar/rarlinux-x64-%{version}.tar.gz
ExclusiveArch:  %{ix86} x86_64

%if %{with unrar}
Provides:       unrar%{?_isa} = %{?epoch}:%{version}-%{release}
Conflicts:      unrar
%endif

%description
RAR is a powerful tool allowing you to manage and control archive files.
Console RAR supports archives only in RAR format, which names usually have a
".rar" extension. ZIP and other formats are not supported.

%prep
%ifarch %{ix86}
%setup -q -n %{name}
%endif

%ifarch x86_64
%setup -q -T -b 1 -n %{name}
%endif

%build

%install
%{__install} -D -p -m0755 rar %{buildroot}%{_bindir}/rar
%if %{with unrar}
%{__install} -D -p -m0755 unrar %{buildroot}%{_bindir}/unrar
%endif
%{__install} -D -p -m0644 rarfiles.lst %{buildroot}%{_sysconfdir}/rarfiles.lst
%{__install} -D -p -m0755 default.sfx %{buildroot}%{_libdir}/default.sfx

%files
%license license.txt
%doc acknow.txt order.htm rar.txt readme.txt whatsnew.txt
%config(noreplace) %{_sysconfdir}/rarfiles.lst
%{_bindir}/rar
%if %{with unrar}
%{_bindir}/unrar
%endif
%{_libdir}/default.sfx

%changelog
