Summary:	Text-CharWidth module for perl 
Name:		perl-Text-CharWidth
Version:	0.04
Release:	%mkrel 5
License:	GPL or Artistic
Group:		Development/Perl
Source0:	Text-CharWidth-%{version}.tar.bz2
URL:		http://www.cpan.org
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%setup -q -n Text-CharWidth-%{version}

# perl path hack
find . -type f | xargs %{__perl} -p -i -e "s|^#!/usr/local/bin/perl|#!%{_bindir}/perl|g"

%build
perl Makefile.PL INSTALLDIRS=vendor </dev/null

%make

make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/Text/CharWidth.pm
%{perl_vendorarch}/auto/Text/CharWidth/CharWidth.so
%{_mandir}/man3/*
