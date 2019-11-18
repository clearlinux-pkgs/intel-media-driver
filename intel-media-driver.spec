#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : intel-media-driver
Version  : 19.3.0
Release  : 18
URL      : https://github.com/intel/media-driver/archive/intel-media-19.2.0/media-driver-19.3.0.tar.gz
Source0  : https://github.com/intel/media-driver/archive/intel-media-19.2.0/media-driver-19.3.0.tar.gz
Summary  : Intel(R) C for Media Runtime
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: intel-media-driver-lib = %{version}-%{release}
Requires: intel-media-driver-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : libX11-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : libpciaccess-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(igdgmm)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(pciaccess)

%description
This directory contains a copy of the installed kernel headers
required by the iHD driver to communicate with the kernel.
Whenever driver needs new definitions for new kernel
APIs, these files should be updated.

%package dev
Summary: dev components for the intel-media-driver package.
Group: Development
Requires: intel-media-driver-lib = %{version}-%{release}
Provides: intel-media-driver-devel = %{version}-%{release}
Requires: intel-media-driver = %{version}-%{release}

%description dev
dev components for the intel-media-driver package.


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
%setup -q -n media-driver-intel-media-19.2.0
cd %{_builddir}/media-driver-intel-media-19.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1574097403
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DINSTALL_DRIVER_SYSCONF=OFF
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1574097403
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/intel-media-driver
cp %{_builddir}/media-driver-intel-media-19.2.0/LICENSE.md %{buildroot}/usr/share/package-licenses/intel-media-driver/0bf81514cc26fb24f29c2b53f3b972066f9cc758
cp %{_builddir}/media-driver-intel-media-19.2.0/media_driver/media_libvpx.LICENSE %{buildroot}/usr/share/package-licenses/intel-media-driver/4dbe7c1f3a1833a88333a7c282119323e9ef44fa
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}/usr/lib64/igfxcmrt64.so

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/igfxcmrt/cm_hw_vebox_cmd_g10.h
/usr/include/igfxcmrt/cm_rt.h
/usr/include/igfxcmrt/cm_rt_api_os.h
/usr/include/igfxcmrt/cm_rt_def_os.h
/usr/include/igfxcmrt/cm_rt_extension.h
/usr/include/igfxcmrt/cm_rt_g10.h
/usr/include/igfxcmrt/cm_rt_g8.h
/usr/include/igfxcmrt/cm_rt_g9.h
/usr/lib64/libigfxcmrt.so
/usr/lib64/pkgconfig/igfxcmrt.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/dri/iHD_drv_video.so
/usr/lib64/libigfxcmrt.so.7
/usr/lib64/libigfxcmrt.so.7.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/intel-media-driver/0bf81514cc26fb24f29c2b53f3b972066f9cc758
/usr/share/package-licenses/intel-media-driver/4dbe7c1f3a1833a88333a7c282119323e9ef44fa
