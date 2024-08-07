#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
Name     : intel-media-driver
Version  : 24.3.1
Release  : 89
URL      : https://github.com/intel/media-driver/archive/intel-media-24.3.1/media-driver-24.3.1.tar.gz
Source0  : https://github.com/intel/media-driver/archive/intel-media-24.3.1/media-driver-24.3.1.tar.gz
Summary  : Intel(R) C for Media Runtime
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: intel-media-driver-lib = %{version}-%{release}
Requires: intel-media-driver-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : libX11-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libpciaccess-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(igdgmm)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(libva-x11)

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
%setup -q -n media-driver-intel-media-24.3.1
cd %{_builddir}/media-driver-intel-media-24.3.1
pushd ..
cp -a media-driver-intel-media-24.3.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1723041661
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fno-lto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DINSTALL_DRIVER_SYSCONF=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fno-lto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DINSTALL_DRIVER_SYSCONF=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fno-lto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1723041661
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/intel-media-driver
cp %{_builddir}/media-driver-intel-media-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/intel-media-driver/0bf81514cc26fb24f29c2b53f3b972066f9cc758 || :
cp %{_builddir}/media-driver-intel-media-%{version}/media_driver/media_libvpx.LICENSE %{buildroot}/usr/share/package-licenses/intel-media-driver/4dbe7c1f3a1833a88333a7c282119323e9ef44fa || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib64/igfxcmrt64.so
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/include/igfxcmrt/cm_rt_g11.h
/usr/include/igfxcmrt/cm_rt_g12_dg1.h
/usr/include/igfxcmrt/cm_rt_g12_tgl.h
/usr/include/igfxcmrt/cm_rt_g8.h
/usr/include/igfxcmrt/cm_rt_g9.h
/usr/lib64/libigfxcmrt.so
/usr/lib64/pkgconfig/igfxcmrt.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/dri/iHD_drv_video.so
/V3/usr/lib64/libigfxcmrt.so.7.2.0
/usr/lib64/dri/iHD_drv_video.so
/usr/lib64/libigfxcmrt.so.7
/usr/lib64/libigfxcmrt.so.7.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/intel-media-driver/0bf81514cc26fb24f29c2b53f3b972066f9cc758
/usr/share/package-licenses/intel-media-driver/4dbe7c1f3a1833a88333a7c282119323e9ef44fa
