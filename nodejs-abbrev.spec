%{?scl:%scl_package nodejs-abbrev}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       %{?scl_prefix}nodejs-abbrev
Version:    1.0.9
Release:    2%{?dist}
Summary:    Abbreviation calculator for Node.js
License:    ISC
URL:        https://github.com/isaacs/abbrev-js
Source0:    http://registry.npmjs.org/abbrev/-/abbrev-%{version}.tgz
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Calculate the set of unique abbreviations for a given set of strings.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/abbrev
cp -pr abbrev.js package.json %{buildroot}%{nodejs_sitelib}/abbrev

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
tap test.js --cov
%endif

%files
%{nodejs_sitelib}/abbrev
%doc README.md LICENSE

%changelog
* Mon Jul 03 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.9-2
- rh-nodejs8 rebuild

* Tue Sep 06 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.9-1
- Update

* Thu Jun 09 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.7-2
- Resolves: rhbz#1334856 , fixes wrong license

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.7-1
- Update

* Wed Jan 07 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.5-1
- New upstream release 1.0.5

* Tue Oct 22 2013 Tomas Hrcka <thrcka@redhat.com> - 1.0.4-7
- enable collection when running tests 

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.4-6
- restrict to compatible arches

* Fri May 03 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0.4-5
- Run unit tests as part of build

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.4-4
- add macro for EPEL6 dependency generation

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0.4-4
- Add support for software collections

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.4-2
- fix missing dist macro in Release

* Thu Jan 10 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.4-1
- new upstream release 1.0.4
- include newly added LICENSE file

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.3-5
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.3-4
- clean up for submission

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.3-3
- guard Requires for F17 automatic depedency generation

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.3-2
- missing Group field for EL5

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.3-1
- new upstream release 1.0.3

* Mon Aug 22 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.2-1
- initial package
