%global		upstream_name    scram
%global		upstream_version 1.0.0-beta.2

Name:		ongres-%upstream_name
Version:	%(echo %upstream_version | sed 's/-/~/g')
Release:	5%{?dist}
Summary:	Salted Challenge Response Authentication Mechanism (SCRAM) - Java Implementation
License:	BSD
URL:		https://github.com/ongres/%upstream_name
Source0:	https://github.com/ongres/%upstream_name/archive/%upstream_version/%upstream_name-%upstream_version.tar.gz
BuildRequires:	maven-local
BuildArch:	noarch

%description
This is a Java implementation of SCRAM (Salted Challenge Response
Authentication Mechanism) which is part of the family of Simple
Authentication and Security Layer (SASL, RFC 4422) authentication
mechanisms. It is described as part of RFC 5802 and RFC7677.

%package client
Summary:	Client for %{name}

%description client
This package contains the client for %{name}

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}

%package parent
Summary:	Parent POM of %{name}

%description parent
This package contains the %{name} parent POM.

%prep
%autosetup -p1 -n "%upstream_name-%upstream_version"
find \( -name '*.jar' -o -name '*.class' \) -delete
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-dependency-plugin client
%pom_remove_plugin -r :maven-javadoc-plugin

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-common
%license LICENSE

%files client -f .mfiles-client
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%files parent -f .mfiles-parent
%license LICENSE

%changelog
* Wed May 30 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.0~beta.2-5
- Remove explicit invocation of maven-javadoc-plugin

* Tue May 22 2018 Pavel Raiskup <praiskup@redhat.com> - 1.0.0~beta.2-4
- BR javadoc maven plugin explicitly
- use nicer Source0 format

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~beta.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 27 2017 Pavel Raiskup <praiskup@redhat.com> - 1.0.0~beta.2-2
- drop potential pre-compiled files from release tarball

* Fri Nov 24 2017 Augusto Caringi <acaringi@redhat.com> 1.0.0~beta.2-1
- initial rpm
