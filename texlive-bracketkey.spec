Name:		texlive-bracketkey
Version:	17129
Release:	2
Summary:	Produce bracketed identification keys
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bracketkey
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bracketkey.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bracketkey.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an environment bracketkey for use when
producing lists of species.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bracketkey/bracketkey.sty
%doc %{_texmfdistdir}/doc/latex/bracketkey/Malva.pdf
%doc %{_texmfdistdir}/doc/latex/bracketkey/Malva.tex
%doc %{_texmfdistdir}/doc/latex/bracketkey/README
%doc %{_texmfdistdir}/doc/latex/bracketkey/bracketkey.pdf
%doc %{_texmfdistdir}/doc/latex/bracketkey/bracketkey.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
