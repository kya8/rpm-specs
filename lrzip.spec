%global commit 79f505165be5524a52fcaaada7aee8a62978fbf9
%global commit_date 20190224
%global shortcommit %(c=%{commit};echo ${c:0:7})

%ifarch %{ix86}
%bcond_without assembler
%else
%bcond_with assembler
%endif

# JIT in bundled libzpaq is supported on x86 and x86_64 only
%ifarch %{ix86} x86_64
%bcond_without jit
%else
%bcond_with jit
%endif


Name:           lrzip
Version:        0.631
Release:        5.%{commit_date}git%{shortcommit}%{?dist}
Summary:        Compression program optimized for large files
Group:          Applications/File
# libzpaq:      MIT
# lzma:         Public Domain
# md5.{c,h}:    GPLv3+
# other files:  GPLv2+
License:        GPLv2+ and GPLv3+ and MIT and Public Domain
URL:            https://github.com/ckolivas/%{name}
Source0:        %{url}/archive/%{commit}.zip#/%{name}-%{commit}.zip

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-common

BuildRequires:  findutils

BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  lzo-devel

BuildRequires:  %{_bindir}/pod2man

%if %{with assembler}
BuildRequires:  nasm
%endif


# Bundles zpaq. lrzip does not work with newer zpaq versions.
Provides:       bundled(zpaq) = 5.01

%description
Long Range ZIP or Lzma RZIP

This is a compression program optimized for large files. The larger the file
and the more memory you have, the better the compression advantage this will
provide, especially once the files are larger than 100 MB. The advantage can
be chosen to be either size (much smaller than bzip2) or speed (much faster
than bzip2). Decompression is always much faster than bzip2.


%package libs
Summary:        Long Range ZIP library
Group:          System Environment/Libraries
Provides:       bundled(zpaq) = 5.01

%description libs
Dynamic library implementing Long Range ZIP or Lzma RZIP algorithm and archive
format.


%package devel
Summary:        Development files for Long Range ZIP library
Group:          Development/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Files needed to develop application using Long Range ZIP library.


%package static
Summary:        Static Long Range ZIP library
Group:          Development/Libraries
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Provides:       bundled(zpaq) = 5.01

%description static
Static library implementing Long Range ZIP or Lzma RZIP algorithm and archive
format.


%prep
%autosetup -n %{name}-%{commit}


%build
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-shared --enable-static --disable-static-bin \
    --%{?with_assembler:enable}%{!?with_assembler:disable}-asm \
    --enable-largefile %{!?with_jit:CPPFLAGS="${CPPFLAGS} -DNOJIT"}
%make_build


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm {} +


%ldconfig_scriptlets libs


%files
%doc %{_pkgdocdir}/*
%{_bindir}/*
%{_mandir}/man1/*.1.gz
%{_mandir}/man5/*.5.gz

%files libs
%license COPYING
%{_libdir}/lib%{name}.so.*

%files devel
%doc decompress_demo.c liblrzip_demo.c
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*

%files static
%{_libdir}/lib%{name}.a

%changelog
