%global _enable_debug_package 0
%global debug_package %{nil}

Summary:            C port of High Dynamic Range (HDR) Histogram
Name:               hdr-histogram-c
Version:            0.9.6
Release:            1%{?dist}
License:            BSD or CC0
Group:              Development/Tools
Source:             hdr-histogram-c-%{version}.tar.gz
URL:                https://github.com/HdrHistogram/HdrHistogram_c
BuildRequires:      cmake
BuildRequires:      make
BuildRequires:      gcc
BuildRequires:      zlib-devel
Requires:           zlib


%description
This library is a C port of High Dynamic Range (HDR) Histogram


%package devel
Summary:            C port of High Dynamic Range (HDR) Histogram development kit
Requires:           hdr-histogram-c
Group:              Development/Libraries

%description devel
Development packages for the C port of High Dynamic Range (HDR) Histogram

%prep
%autosetup -n hdr-histogram-c-%{version}

%build
mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr ..
make all

%install
cd build
make install

%files
%doc README.md LICENSE.txt COPYING.txt
%{_libdir}/*
%{_bindir}/*


%files devel
%{_includedir}/*


%changelog
* Sun Jul 23 2017 Otavio R. Piske <angusyoung@gmail.com> - 20170723
- Initial packaging