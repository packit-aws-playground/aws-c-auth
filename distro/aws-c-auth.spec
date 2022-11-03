Name:           aws-c-auth
Version:        0.6.5 
Release:        6%{?dist}
Summary:        C99 library implementation of AWS client-side authentication

License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         aws-c-auth-cmake.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  aws-c-common-devel
BuildRequires:  aws-c-sdkutils-devel
BuildRequires:  aws-c-cal-devel
BuildRequires:  aws-c-io-devel
BuildRequires:  aws-c-compression-devel
BuildRequires:  aws-c-http-devel

Requires:       openssl
Requires:       aws-c-common-libs
Requires:       aws-c-sdkutils-libs
Requires:       aws-c-cal-libs
Requires:       aws-c-io-libs
Requires:       aws-c-compression-libs
Requires:       aws-c-http-libs

%description
C99 library implementation of AWS client-side authentication:
standard credentials providers and signing


%package libs
Summary:        C99 library implementation of AWS client-side authentication

%description libs
C99 library implementation of AWS client-side authentication:
standard credentials providers and signing


%package devel
Summary:        C99 library implementation of AWS client-side authentication
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
C99 library implementation of AWS client-side authentication:
standard credentials providers and signing


%prep
%autosetup -p1


%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install


%files libs
%license LICENSE
%doc README.md
%{_libdir}/libaws-c-auth.so.1.0.0

%files devel
%dir %{_includedir}/aws/auth
%{_includedir}/aws/auth/*.h
%{_libdir}/libaws-c-auth.so
%dir %{_libdir}/cmake/aws-c-auth
%dir %{_libdir}/cmake/aws-c-auth/shared
%{_libdir}/cmake/aws-c-auth/aws-c-auth-config.cmake
%{_libdir}/cmake/aws-c-auth/shared/aws-c-auth-targets-noconfig.cmake
%{_libdir}/cmake/aws-c-auth/shared/aws-c-auth-targets.cmake



%changelog
* Tue Feb 22 2022 David Duncan <davdunc@amazon.com> - 0.6.5-6
- Updated for package review

* Tue Feb 22 2022 Kyle Knapp <kyleknap@amazon.com> - 0.6.5-5
- Include missing devel directories

* Thu Feb 03 2022 Kyle Knapp <kyleknap@amazon.com> - 0.6.5-4
- Add patch to set CMake configs to correct path

* Thu Feb 03 2022 David Duncan <davdunc@amazon.com> - 0.6.5-3
- Fix CMake targets and move files to lib

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.6.5-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.6.5.1
- Initial package development
