Name:           python2-meliae
Version:        0.4.0
Release:        20%{?dist}
Summary:        Python memory usage statistics

Group:          Development/Languages
License:        GPLv3
URL:            https://launchpad.net/meliae
Source0:        https://files.pythonhosted.org/packages/98/c6/7fa12062ddfe1732d43b34b64a3fe99da958a88fa1d8b7550fe386a9ca01/meliae-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python2 python2-devel
BuildRequires:	python2-setuptools
BuildRequires:  python2-Cython
BuildRequires:  python2-simplejson
%{?python_provide:%python_provide python2-meliae}

%description 
"meliae" provides a way to dump python memory usage information to a JSON disk
format, which can then be parsed into useful things like graph representations.

The name is simply a fun word (means Ash-wood Nymph).


%prep
%setup -q -n meliae-%{version}

%build
%py2_build


%install
%py2_install

%check
# run_tests.py doesn't seem to work in the main directory: sys.path pulls in
# the dir of the script, which contains meliae/intset.pyx, but the built
# intset.so has been installed elsewhere in the tree, leading to:
#   ImportError: cannot import name _intset
# The meliae.tests directory isn't installed, so we do need to run from this
# directory.
# As a crude workaround, copy the .so files back into the source tree:
cp $RPM_BUILD_ROOT/%{python2_sitearch}/meliae/*.so meliae
%{__python2} run_tests.py --verbose

%files 
%doc CHANGES.txt COPYING.txt README.txt TODO.txt
%{_bindir}/strip_duplicates.py
%{python2_sitearch}/meliae
%{python2_sitearch}/meliae-*-py?.?.egg-info


%changelog

* Mon Feb 18 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.4.0-20
- Upstream

* Tue Jul 24 2018 Tadej Janež <tadej.j@nez.si> - 0.4.0-18
- Use macros for building and installation (%%py2_build and %%py_install)
- Remove buildroot removal in %%install as mandated in
  https://fedoraproject.org/wiki/Packaging:Guidelines#Tags_and_Sections
- Replace unversioned Python macros with with appropriate Python 2 versions
  as mandated in:
  https://fedoraproject.org/wiki/Packaging:Python#Macros
- Add gcc to BuildRequires to account for
  https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.0-16
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.0-14
- Python 2 binary package renamed to python2-meliae
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 13 2012 Luke Macken <lmacken@redhat.com> - 0.4.0-2
- Add python-simplejson to the BuildRequires to fix a couple of unit tests

* Tue Jan 24 2012 David Malcolm <dmalcolm@redhat.com> - 0.4.0-1
- 0.4.0
- drop upstream patch 1 (meliae-0.2.0-fix-builtintype-heap-assertion.patch)
- add a %%check section, running the upstream test suite

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Apr 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.2.0-3
- rewrite files stanza to ensure that egg-info was generated (Thomas Spura)

* Fri Mar 26 2010 David Malcolm <dmalcolm@redhat.com> - 0.2.0-2
- fix assertion failure seen with non-heap types

* Fri Mar 26 2010 David Malcolm <dmalcolm@redhat.com> - 0.2.0-1
- initial packaging

