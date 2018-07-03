%define	modname	Text-CharWidth
%define	modver	0.04

Summary:	Text-CharWidth module for perl 
Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	16
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Text/%{modname}-%{modver}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:  perl(Test::Simple)

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

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorarch}/Text/CharWidth.pm
%{perl_vendorarch}/auto/Text/CharWidth/CharWidth.so
%{_mandir}/man3/*

