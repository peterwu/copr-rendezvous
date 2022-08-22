%global debug_package %{nil}
%global __strip /bin/true
%define _build_id_links none

%define stumpwm_contrib_git_revision 6d4584f01dec0143a169186df1608860d1aa1ef0
%define clx_truetype_git_revision    667afec17f4e0b911857b776ba65f8fd31d19240

Name:    stumpwm
Version: 22.05
Release: 2%{?dist}
License: GPLv2
Summary: A tiling, keyboard driven X11 Window Manager written entirely in Common Lisp
Source0: https://github.com/%{name}/%{name}/archive/%{version}.tar.gz
Source1: stumpwm.desktop
Source2: https://beta.quicklisp.org/quicklisp.lisp
Source3: sbclrc
Source4: https://github.com/stumpwm/stumpwm-contrib/archive/%{stumpwm_contrib_git_revision}.tar.gz
Source5: https://github.com/lihebi/clx-truetype/archive/%{clx_truetype_git_revision}.tar.gz

BuildRequires: autoconf
BuildRequires: coreutils
BuildRequires: make
BuildRequires: sbcl
BuildRequires: texinfo
BuildRequires: texinfo-tex

Requires: sbcl
# stumpish
Requires: rlwrap
Requires: xprop

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

rm -rf %{buildroot}/usr/share/info/dir

mkdir -p %{buildroot}%{_datadir}/xsessions
install -m 0644 %{SOURCE1} -t %{buildroot}%{_datadir}/xsessions

mkdir -p %{buildroot}/usr/share/common-lisp/source
cp -r ~/quicklisp/dists/quicklisp/software/alexandria-*  %{buildroot}/usr/share/common-lisp/source/alexandria
cp -r ~/quicklisp/dists/quicklisp/software/clx-*         %{buildroot}/usr/share/common-lisp/source/clx
cp -r ~/quicklisp/dists/quicklisp/software/cl-ppcre-*    %{buildroot}/usr/share/common-lisp/source/cl-ppcre
cp -r ~/quicklisp/dists/quicklisp/software/cl-unicode-*  %{buildroot}/usr/share/common-lisp/source/cl-unicode

# stumpwm-contrib modules
## ttf-fonts
tar zxvf %{SOURCE4} -C /tmp
mkdir -p %{buildroot}/usr/share/stumpwm/contrib/util
cp -r /tmp/stumpwm-contrib-%{stumpwm_contrib_git_revision}/util/ttf-fonts %{buildroot}/usr/share/stumpwm/contrib/util/ttf-fonts

## clx-truetype
tar zxvf %{SOURCE5} -C /tmp
cp -r /tmp/clx-truetype-%{clx_truetype_git_revision} %{buildroot}/usr/share/common-lisp/source/clx-truetype

## stumpish
install -m 0755 /tmp/stumpwm-contrib-%{stumpwm_contrib_git_revision}/util/stumpish/stumpish -t %{buildroot}%{_bindir}

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

# stumpwm-contrib modules
## ttf-fonts
%{_datadir}/stumpwm/contrib/util/ttf-fonts
%{_datadir}/common-lisp/source/clx-truetype

## stumpish
%{_bindir}/stumpish

%changelog
* Tue 16 Aug 2022 06:24:16 PM EDT - Peter Wu
- Release 22.05

* Mon Aug 22 16:23:39 EDT 2022 - Peter Wu
- Add stumpish & ttf-fonts from stumpwm-contrib
