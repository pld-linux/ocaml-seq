#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Compatibility package for OCaml's standard iterator type starting from 4.07
Summary(pl.UTF-8):	Pakiet zgodności ze typem standardowego iteratora z OCamla >= 4.07
Name:		ocaml-seq
Version:	0.2.2
Release:	1
License:	LGPL v2.1 with linking exception
Group:		Libraries
#Source0Download: https://github.com/c-cube/seq/releases
Source0:	https://github.com/c-cube/seq/archive/%{version}/seq-%{version}.tar.gz
# Source0-md5:	9033e02283aa3bde9f97f24e632902e3
URL:		https://github.com/c-cube/seq
BuildRequires:	ocaml >= 1:4.00
BuildRequires:	ocaml-dune >= 1.1.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Compatibility package for OCaml's standard iterator type starting from
4.07.

This package contains files needed to run bytecode executables using
OCaml seq library.

%description -l pl.UTF-8
Pakiet zgodności ze typem standardowego iteratora z OCamla >= 4.07.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki OCamla seq.

%package devel
Summary:	Compatibility package for OCaml's standard iterator type starting from 4.07 - development part
Summary(pl.UTF-8):	Pakiet zgodności ze typem standardowego iteratora z OCamla >= 4.07 - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using
seq library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
biblioteki seq.

%prep
%setup -q -n seq-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/seq/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/seq

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%dir %{_libdir}/ocaml/seq
%{_libdir}/ocaml/seq/META
%{_libdir}/ocaml/seq/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/seq/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/seq/*.cmi
%{_libdir}/ocaml/seq/*.cmt
%{_libdir}/ocaml/seq/*.cmti
%{_libdir}/ocaml/seq/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/seq/*.a
%{_libdir}/ocaml/seq/*.cmx
%{_libdir}/ocaml/seq/*.cmxa
%endif
%{_libdir}/ocaml/seq/dune-package
%{_libdir}/ocaml/seq/opam
