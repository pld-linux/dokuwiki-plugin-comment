%define		plugin		comment
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	DokuWiki plugin to add Add comments/notes to your wiki source
Name:		dokuwiki-plugin-%{plugin}
Version:	20090206
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/dokufreaks/plugin-comment/tarball/2009-02-06/%{plugin}-%{version}.tgz
# Source0-md5:	aded94aa800d880bf48a0f135ccc34a6
URL:		http://www.dokuwiki.org/plugin:comment
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki >= 20061106
Requires:	php-common >= 4:%{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
This tiny plugin allows you to leave notes to yourself (and other
authors of your wiki) in the wiki source code that won't be shown on
the wiki page. The syntax is like C and PHP.

%prep
%setup -qc
mv *-%{plugin}-*/* .

version=$(cat VERSION)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
%{__rm} $RPM_BUILD_ROOT%{plugindir}/{COPYING,README,VERSION}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{plugindir}
%{plugindir}/*.php
