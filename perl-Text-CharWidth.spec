%define	modname	Text-CharWidth
%define	modver	0.04

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	5

Summary:	Text-CharWidth module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Text/%{modname}-%{modver}.tar.bz2

BuildRequires:	perl-devel

%description
Text::CharWidth - Get number of occupied columns of a string on
terminal

This module supplies features similar as wcwidth(3) and wcswidth(3) in
C language.

Characters have its own width on terminal depending on locale. For
example, ASCII characters occupy one column per character, east Asian
fullwidth characters (like Hiragana or Han Ideograph) occupy two
columns per character, and combining characters (apperaring in
ISO-8859-11 Thai, Unicode, and so on) occupy zero columns per
character. mbwidth() gives the width of the first character of the
given string and mbswidth() gives the width of the whole given string.

The names of mbwidth and mbswidth came from ``multibyte'' versions of
wcwidth and wcswidth which are ``wide character'' versions.

mblen(string) returns number of bytes of the first character of the
string. Please note that a character may consist of multiple bytes in
multibyte encodings such as UTF-8, EUC-JP, EUC-KR, GB2312, or Big5.

mbwidth(string) returns the width of the first character of the
string. mbswidth(string) returns the width of the whole string.

Parameters are to be given in locale encodings, not always in UTF-8.

%prep
%setup -q -n %{modname}-%{modver}

# perl path hack
find . -type f | xargs %{__perl} -p -i -e "s|^#!/usr/local/bin/perl|#!%{_bindir}/perl|g"

%build
perl Makefile.PL INSTALLDIRS=vendor </dev/null
%make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorarch}/Text/CharWidth.pm
%{perl_vendorarch}/auto/Text/CharWidth/CharWidth.so
%{_mandir}/man3/*

%changelog
* Wed Feb 13 2013 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.40.0-4
- cleanups

* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.40.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 555237
- rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 405663
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.04-6mdv2009.0
+ Revision: 258614
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.04-5mdv2009.0
+ Revision: 246628
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.04-3mdv2008.1
+ Revision: 151405
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Oden Eriksson <oeriksson@mandriva.com> 0.04-2mdv2008.0
+ Revision: 76892
- rebuild


* Fri Jul 14 2006 Oden Eriksson <oeriksson@mandriva.com> 0.04-1mdv2007.0
- initial Mandriva package

