#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : intel-media-driver
Version  : 18.3.0
Release  : 4
URL      : https://github.com/intel/media-driver/archive/intel-media-18.3.0.tar.gz
Source0  : https://github.com/intel/media-driver/archive/intel-media-18.3.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: intel-media-driver-lib = %{version}-%{release}
Requires: intel-media-driver-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : libX11-dev
BuildRequires : libpciaccess-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(igdgmm)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(pciaccess)
Patch1: 0001-cmrtlib-remove-cmrtlib-from-compilation.patch

%description
# Intel(R) Media Driver for VAAPI
## Introduction
The Intel(R) Media Driver for VAAPI is a new VA-API (Video Acceleration API)
user mode driver supporting hardware accelerated decoding, encoding, and
video post processing for GEN based graphics hardware.

%package lib
Summary: lib components for the intel-media-driver package.
Group: Libraries
Requires: intel-media-driver-license = %{version}-%{release}

%description lib
lib components for the intel-media-driver package.


%package license
Summary: license components for the intel-media-driver package.
Group: Default

%description license
license components for the intel-media-driver package.


%prep
%setup -q -n media-driver-intel-media-18.3.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539370571
mkdir -p clr-build
pushd clr-build
%cmake .. -DINSTALL_DRIVER_SYSCONF=OFF
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1539370571
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/intel-media-driver
cp LICENSE.md %{buildroot}/usr/share/package-licenses/intel-media-driver/LICENSE.md
cp media_driver/media_libvpx.LICENSE %{buildroot}/usr/share/package-licenses/intel-media-driver/media_driver_media_libvpx.LICENSE
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/dri/iHD_drv_video.so

%files license
%defattr(-,root,root,-)
/usr/share/package-licenses/intel-media-driver/LICENSE.md
/usr/share/package-licenses/intel-media-driver/media_driver_media_libvpx.LICENSE
