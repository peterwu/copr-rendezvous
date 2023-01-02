%global debug_package %{nil}

Name:           fzy
Version:        1.0
Release:        1%{?dist}
Summary:        A simple, fast fuzzy finder for the terminal

License:        MIT
URL:            https://github.com/jhawthorn/fzy
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
fzy is a fast, simple fuzzy text selector for the terminal with an advanced scoring algorithm.

%check
make check

%prep
%setup

%build
%make_build

%install
rm -rf %{buildroot}
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc ALGORITHM.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
* Mon 02 Jan 2023 11:06:04 AM EST - Peter Wu
- Release v1.0
