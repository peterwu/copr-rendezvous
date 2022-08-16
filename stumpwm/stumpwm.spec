%global debug_package %{nil}
%global __strip /bin/true
%define _build_id_links none

Name:    stumpwm
Version: 22.05
Release: 1%{?dist}
License: GPLv2
Summary: A tiling, keyboard driven X11 Window Manager written entirely in Common Lisp
Source0: https://github.com/%{name}/%{name}/archive/%{version}.tar.gz
Source1: stumpwm.desktop
Source2: https://beta.quicklisp.org/quicklisp.lisp
Source3: sbclrc

BuildRequires: autoconf
BuildRequires: coreutils
BuildRequires: make
BuildRequires: sbcl
BuildRequires: texinfo
BuildRequires: texinfo-tex

Requires: sbcl

%description
StumpWM is a window manager written entirely in Common Lisp. It attempts to be
highly customizable while relying entirely on the keyboard for input. You will
not find buttons, icons, title bars, tool bars, or any of the other conventional
GUI widgets.

%prep
sbcl --load %{SOURCE2} --eval "(quicklisp-quickstart:install)" --quit

# simulate (ql:add-to-init-file)
cp %{SOURCE3} ~/.sbclrc

sbcl --load %{SOURCE2} --eval "(ql:quickload \"clx\")" --quit
sbcl --load %{SOURCE2} --eval "(ql:quickload \"cl-ppcre\")" --quit
sbcl --load %{SOURCE2} --eval "(ql:quickload \"alexandria\")" --quit
sbcl --load %{SOURCE2} --eval "(ql:quickload \"cl-unicode\")" --quit

%autosetup -n %{name}-%{version}

./autogen.sh
./configure               \
--enable-compression      \
--prefix=%{buildroot}/usr \
--with-module-dir=/usr/share/stumpwm/contrib

%build
%make_build

# generate html/pdf documentation
makeinfo --pdf stumpwm.texi
makeinfo --html stumpwm.texi

%install
%make_install

mkdir -p %{buildroot}%{_datadir}/xsessions
install -m 0644 %{SOURCE1} -t %{buildroot}%{_datadir}/xsessions

mkdir -p %{buildroot}/usr/share/common-lisp/source
cp -r ~/quicklisp/dists/quicklisp/software/alexandria-*  %{buildroot}/usr/share/common-lisp/source/alexandria
cp -r ~/quicklisp/dists/quicklisp/software/clx-*         %{buildroot}/usr/share/common-lisp/source/clx
cp -r ~/quicklisp/dists/quicklisp/software/cl-ppcre-*    %{buildroot}/usr/share/common-lisp/source/cl-ppcre
cp -r ~/quicklisp/dists/quicklisp/software/cl-unicode-*  %{buildroot}/usr/share/common-lisp/source/cl-unicode

rm -rf %{buildroot}/usr/share/info/dir

%files
%license COPYING
%doc AUTHORS NEWS README.md
%doc stumpwm.pdf stumpwm.html
%doc sample-stumpwmrc.lisp

%{_bindir}/stumpwm
%{_infodir}/stumpwm.info.gz

%{_datadir}/xsessions/%{name}.desktop

%{_datadir}/common-lisp/source/alexandria
%{_datadir}/common-lisp/source/clx
%{_datadir}/common-lisp/source/cl-ppcre
%{_datadir}/common-lisp/source/cl-unicode

%changelog
* Tue 16 Aug 2022 06:24:16 PM EDT - Peter Wu
- Release 22.05
