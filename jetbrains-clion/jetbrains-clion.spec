%global         debug_package %{nil}

%global         source_name clion

Name:           jetbrains-clion
Version:        2022.3.1
Release:        1%{?dist}
Summary:        JetBrains' C/C++ IDE.

License:        Custom. Refer to /opt/jetbrains/clion/license for details.
URL:            https://www.jetbrains.com/clion
Source0:        https://download.jetbrains.com/cpp/CLion-%{version}.tar.gz
Source1:        %{name}.desktop

Requires:       python3
Requires:       bash
Requires:       java
Requires:       glibc
Requires:       libgcc
Recommends:     cmake
Recommends:     gdb
Recommends:     lldb
Recommends:     ninja-build

%description
JetBrains' cross platform C/C++ IDE.

%prep
%autosetup -n %{source_name}-%{version}

%build
%{__rm} -rf jbr
%{__rm} -rf bin/cmake
%{__rm} -rf bin/gdb
%{__rm} -rf bin/lldb
%{__rm} -rf bin/ninja
%{__rm} -rf bin/rtos

%{__rm} -rf plugins/performanceTesting/bin/libyjpagent.so
%{__rm} -rf plugins/python-ce/helpers/pydev/pydevd_attach_to_process/attach_linux_x86.so

%{__rm} -rf plugins/gateway-plugin/lib/remote-dev-workers/remote-dev-worker-darwin-amd64
%{__rm} -rf plugins/gateway-plugin/lib/remote-dev-workers/remote-dev-worker-windows-amd64.exe
%{__rm} -rf plugins/gateway-plugin/lib/remote-dev-workers/remote-dev-worker-darwin-arm64
%{__rm} -rf plugins/gateway-plugin/lib/remote-dev-workers/remote-dev-worker-linux-arm64
%{__rm} -rf plugins/gateway-plugin/lib/remote-dev-workers/remote-dev-worker-windows-arm64.exe

find bin -type f -name '*.py' -exec sed -i '1 s/env python/python3/' {} \;

%install
%{__mkdir} -p %{buildroot}/opt/jetbrains/clion
%{__mkdir} -p %{buildroot}%{_bindir}
%{__mkdir} -p %{buildroot}%{_datadir}/applications

%{__ln_s} /opt/jetbrains/clion/bin/clion.sh %{buildroot}%{_bindir}/clion

%{__install} -D -m 0644 %{SOURCE1} -t %{buildroot}%{_datadir}/applications
%{__cp} -r * %{buildroot}/opt/jetbrains/clion

%files
%{_bindir}/clion
%{_datadir}/*
/opt/jetbrains/clion/*

%changelog
* Sun 25 Dec 2022 05:21:02 PM EST
- CLion-2022.3.1

* Sat 17 Sep 2022 02:38:33 PM EDT
- CLion-2022.2.3

* Sat 02 Jul 2022 05:10:29 PM EDT
- CLion-2022.1.3

* Wed Dec  2 17:44:16 EST 2020 Peter Wu <peterwu@hotmail.com>
- CLion-2020.3

* Fri Nov 27 09:43:05 EST 2020 Peter Wu <peterwu@hotmail.com>
- CLion-2020.2.5

* Mon Nov 23 09:42:31 AM EST 2020 Peter Wu <peterwu@hotmail.com>
- CLion-2020.2.4
