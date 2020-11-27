%global         source_name idea-IC
%global         debug_package %{nil}
%global         build_version 202.8194.7

Name:           jetbrains-idea-ce
Version:        2020.2.4
Release:        1%{?dist}
Summary:        JetBrains IntelliJ IDEA Community Edition

License:        ASL2.0
URL:            https://www.jetbrains.com/idea
Source0:        https://download.jetbrains.com/idea/ideaIC-%{version}.tar.gz
Source1:        %{name}.desktop

Requires:       java

%description
JetBrains IntelliJ IDEA Community Edition

%prep
%autosetup -n %{source_name}-%{build_version}

%build
%{__rm} -rf %{_builddir}/%{source_name}-%{build_version}/jbr
%{__rm} -rf %{_builddir}/%{source_name}-%{build_version}/bin/fsnotifier

find %{_builddir}/%{source_name}-%{build_version}/bin -type f -name '*.sh' -exec sed -i '1 s/\/bin\/sh/\/usr\/bin\/sh/' {} \;
find %{_builddir}/%{source_name}-%{build_version}/bin -type f -name '*.py' -exec sed -i '1 s/env python/python3/' {} \;

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/opt/jetbrains/idea-ce
%{__mkdir} -p %{buildroot}%{_bindir}
%{__mkdir} -p %{buildroot}%{_datadir}/applications

%{__ln_s} /opt/jetbrains/idea-ce/bin/idea.sh %{buildroot}%{_bindir}/idea-ce

%{__install} -D -m 0644 %{SOURCE1} -t %{buildroot}%{_datadir}/applications
%{__cp} -r %{_builddir}/%{source_name}-%{build_version}/* %{buildroot}/opt/jetbrains/idea-ce

%files
%{_bindir}/idea-ce
%{_datadir}/*
/opt/jetbrains/idea-ce/*

%changelog
* Fri Nov 27 10:45:18 EST 2020 Peter Wu <peterwu@hotmail.com>
- IntelliJ IDEA 2020.2.4
