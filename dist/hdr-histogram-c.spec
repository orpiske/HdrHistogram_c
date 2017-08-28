Summary:            C port of High Dynamic Range (HDR) Histogram
Name:               hdr-histogram-c
Version:            0.9.6
Release:            6%{?dist}
License:            BSD or CC0
# To be used only when submitting the package
# Source:             https://github.com/HdrHistogram/HdrHistogram_c/archive/%{version}.tar.gz
Source:             hdr-histogram-c-%{version}.tar.gz
URL:                https://github.com/HdrHistogram/HdrHistogram_c
BuildRequires:      cmake
BuildRequires:      make
BuildRequires:      gcc >= 4.8.0
BuildRequires:      zlib-devel

%description
This library is a C port of High Dynamic Range (HDR) Histogram


%package devel
Summary:            C port of High Dynamic Range (HDR) Histogram development kit
Requires:           %{name}%{?_isa} = %{version}-%{release}

%description devel
Development packages for the C port of High Dynamic Range (HDR) Histogram

%prep
%autosetup -n hdr-histogram-c-%{version}

%build
mkdir build && cd build
%cmake -DCMAKE_USER_C_FLAGS="-fPIC" ..
%make_build all


%install
cd build
%make_install

%files
%doc README.md
%license LICENSE.txt COPYING.txt
%{_libdir}/*.so.*
%{_libdir}/*.a
%{_bindir}/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files devel
%{_includedir}/*
%{_libdir}/*.so


%post devel -p /sbin/ldconfig

%postun devel -p /sbin/ldconfig

%changelog
* Mon Aug 28 2017 Otavio R. Piske <angusyoung@gmail.com> - 0.9.6-6
- Fedora packaging guidelines: only package so in devel package
- Fedora packaging guidelines: adjust BuildRequires, otherwise fails on older platforms

* Sun Aug 06 2017 Otavio R. Piske <angusyoung@gmail.com> - 0.9.6-5
- Adjusted to use the correct license macro
- Prevent the devel package from being used with incompatible versions
- Remove groups

* Sun Aug 06 2017 Otavio R. Piske <angusyoung@gmail.com> - 0.9.6-4
- Added support for passing additional compiler flags

* Sun Aug 06 2017 Otavio R. Piske <angusyoung@gmail.com> - 0.9.6-3
- Added a patch for the invalid header initialization (upstream issue #44)

* Fri Jul 28 2017 Otavio R. Piske <angusyoung@gmail.com> - 0.9.6-2
- Adjust to comply with fedora packaging guidelines

* Sun Jul 23 2017 Otavio R. Piske <angusyoung@gmail.com> - 0.9.6-1
- Initial packaging