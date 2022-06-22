%global         debug_package %{nil}

Version:        1.8.0
Release:        1%{?dist}
URL:            https://github.com/belluzj/fantasque-sans
Source0:        %{url}/releases/download/v%{version}/FantasqueSansMono-LargeLineHeight-NoLoopK.tar.gz

%global fontlicense       OFL-1.1 license

%global fontlicenses      LICENSE.txt
%global fontdocs          *.md

%global fontfamily        Fantasque Sans Mono
%global fontsummary       A font family with a great monospaced variant for programmers

%global fonts             TTF/*.ttf
%global fontdescription   %{expand:
Fantasque Sans Mono is a programming font, designed with functionality in 
mind, and with some wibbly-wobbly handwriting-like fuzziness that makes it 
unassumingly cool.}

%fontpkg

%prep
%setup -c

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Wed Jun 22 12:15:06 EDT 2022 Peter Wu
- Release - v1.8.0
