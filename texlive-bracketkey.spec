# revision 17129
# category Package
# catalog-ctan /macros/latex/contrib/bracketkey
# catalog-date 2010-02-19 21:33:30 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-bracketkey
Version:	1.0
Release:	1
Summary:	Produce bracketed identification keys
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bracketkey
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bracketkey.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bracketkey.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides an environment bracketkey for use when
producing lists of species.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bracketkey/bracketkey.sty
%doc %{_texmfdistdir}/doc/latex/bracketkey/Malva.pdf
%doc %{_texmfdistdir}/doc/latex/bracketkey/Malva.tex
%doc %{_texmfdistdir}/doc/latex/bracketkey/README
%doc %{_texmfdistdir}/doc/latex/bracketkey/bracketkey.pdf
%doc %{_texmfdistdir}/doc/latex/bracketkey/bracketkey.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
