%global debug_package %{nil}

Name: flm
Version: 0.9.45
Release: 1%{?dist}
Summary: FastFlowLM for Ryzen AI NPU
License: MIT and Proprietary
URL: https://github.com/FastFlowLM/FastFlowLM

Source: %{name}-%{version}.tar.gz

ExclusiveArch: x86_64

BuildRequires: git
BuildRequires: ninja-build
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: chrpath
BuildRequires: doxygen
BuildRequires: rust
BuildRequires: cargo
BuildRequires: boost-devel
BuildRequires: curlpp-devel
BuildRequires: fftw-devel
BuildRequires: libavformat-free-devel
BuildRequires: libavutil-free-devel
BuildRequires: libavcodec-free-devel
BuildRequires: libswresample-free-devel
BuildRequires: libswscale-free-devel
BuildRequires: uuid-devel
BuildRequires: libdrm-devel
BuildRequires: xrt-base-devel

Requires: boost
Requires: curlpp
Requires: fftw
Requires: libavformat-free
Requires: libavutil-free
Requires: libavcodec-free
Requires: libswresample-free
Requires: libswscale-free
Requires: uuid
Requires: libdrm
Requires: xrt-plugin-amdxdna

%description
FastFlowLM (FLM) runs large language models on AMD Ryzen AI XDNA2 NPUs
with a simple Ollama-like CLI interface. Purpose-built for NPU inference:
faster and over 10x more power-efficient than GPU-based runtimes.

Supports all Ryzen AI chips with XDNA2 NPUs (Strix, Strix Halo, Kraken,
Gorgon Point).

%prep
%autosetup -n %{name}-%{version}

%build
cd src
cmake --preset linux-default \
    -Wno-dev

cmake --build build -j $(nproc)

%install
cd src
mkdir -p %{buildroot}%{bindir}
DESTDIR=%{buildroot} cmake --install build
mkdir -p %{buildroot}%{_bindir}
ln -s /opt/fastflowlm/bin/flm %{buildroot}%{_bindir}/flm

%files
%license LICENSE_RUNTIME.txt
%doc README.md
/opt/fastflowlm
%{_bindir}/flm

%changelog
* Sat Jul 12 2026 Darren Cocco<linux.fedora.packaging@darren.cocco.id.au> 0.9.45-1
- Updated to 0.9.45

* Wed Jul 08 2026 Darren Cocco <linux.fedora.packaging@darren.cocco.id.au> 0.9.44-1
- Updated to 0.9.44

* Mon Jun 01 2026 Darren Cocco <linux.fedora.packaging@darren.cocco.id.au> 0.9.43-1
- Initial release

