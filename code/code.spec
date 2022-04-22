%global         debug_package %{nil}

%global         build_id 1649664637 

Name:           code
Version:        1.66.2
Release:        1%{?dist}
Summary:        Code editing. Redefined.
License:        Multiple, see https://code.visualstudio.com/license
URL:            https://code.visualstudio.com
Source0:        https://packages.microsoft.com/yumrepos/vscode/%{name}-%{version}-%{build_id}.el7.x86_64.rpm
Source1:        %{name}.desktop
Source2:        %{name}-url-handler.desktop
Source3:        %{name}-workspace.xml

Requires:       gcc
Requires:       glibc
Requires:       gnupg
Requires:       gtk3
Requires:       libnotify
Requires:       libsecret
Requires:       libxkbfile
Requires:       lsof
Requires:       nss
Requires:       shared-mime-info
Requires:       xdg-utils

%description
Visual Studio Code is a new choice of tool that combines the simplicity of a
code editor with what developers need for the core edit-build-debug
cycle. See https://code.visualstudio.com/docs/setup/linux for installation
instructions and FAQ.

%prep
rm -rf %{buildroot}/%{name}-%{version}
mkdir -p %{name}-%{version}
rpm2cpio %{_sourcedir}/%{name}-%{version}-%{build_id}.el7.x86_64.rpm|cpio -idmv -D %{name}-%{version}

%install
%{__install} -d %{buildroot}/opt/microsoft/%{name}
%{__install} -d %{buildroot}/usr/bin
%{__install} -d %{buildroot}/usr/share/applications
%{__install} -d %{buildroot}/usr/share/pixmaps
%{__install} -d %{buildroot}/usr/share/mime/packages

%{__install} -p -m 0644 %{name}-%{version}/usr/share/pixmaps/com.visualstudio.code.png %{buildroot}/usr/share/pixmaps/com.visualstudio.code.png

%{__install} -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
%{__install} -p -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}-url-handler.desktop
%{__install} -p -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/mime/packages/%{name}-workspace.xml
%{__install} -D -p -m 0644 %{name}-%{version}%{_datadir}/%{name}/resources/app/LICENSE.rtf .
%{__install} -D -p -m 0644 %{name}-%{version}%{_datadir}/bash-completion/completions/%{name} %{buildroot}%{_datadir}/bash-completion/completions/%{name}
%{__install} -D -p -m 0644 %{name}-%{version}%{_datadir}/zsh/site-functions/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%{__cp} -r %{name}-%{version}%{_datadir}/%{name} %{buildroot}/opt/microsoft/

%{__ln_s} /opt/microsoft/%{name}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE.rtf
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/*.xml
%{_datadir}/pixmaps/*.png
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
/opt/microsoft/%{name}/*

%changelog
* Wed 23 Mar 2022 09:24:32 PM EDT Peter Wu
- Release v1.65.2

* Wed Mar 30 14:59:04 EDT 2022 Peter Wu
- Release v1.66.0

* Thu 07 Apr 2022 05:57:07 PM EDT Peter Wu
- Release v1.66.1
